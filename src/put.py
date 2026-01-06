
# Enhanced Python script for options analysis using Black-Scholes Model
# Includes improved parameter estimation, risk management, and backtesting capabilities
import argparse

import datetime
import pathlib
import numpy as np
import numpy.typing as npt
import pandas as pd
from scipy.stats import norm
# from scipy.optimize import minimize_scalar
import math
import warnings
from typing import Dict, List, Optional
from dataclasses import dataclass
import matplotlib.pyplot as plt

from typing import Optional, Dict, List
# from datetime import datetime, timedelta

from utils import StockTicker, get_log_print, get_future_date

log_print = get_log_print

TRADING_DAYS = 252
HORIZON_DAYS = 29

# sigma: VOLATILITY
# mu: expected price drift

@dataclass
class OptionGreeks:
    """Container for option Greeks"""
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float

@dataclass
class ParameterEstimates:
    """Container for parameter estimates with confidence intervals"""
    mu_log: float          # E[log return] annualized
    mu_gbm: float          # Drift of S_t    
    sigma: float
    mu_ci_lower: float
    mu_ci_upper: float
    sigma_ci_lower: float
    sigma_ci_upper: float
    n_observations: int

class InputValidationError(ValueError):
    """Custom exception for input validation errors"""
    pass

def validate_inputs(S0: float, K: float, T: float, r: float, sigma: float) -> None:
    """
    Validate input parameters for option pricing functions.
    
    Args:
        S0: Current stock price
        K: Strike price
        T: Time to expiry (years)
        r: Risk-free rate
        sigma: Volatility
        
    Raises:
        InputValidationError: If any parameter is invalid
    """
    if S0 <= 0:
        raise InputValidationError("Stock price must be positive")
    if K <= 0:
        raise InputValidationError("Strike price must be positive")
    if T < 0:
        raise InputValidationError("Time to expiry cannot be negative")
    if sigma < 0:
        raise InputValidationError("Volatility cannot be negative")
    if abs(r) > 1:
        warnings.warn("Risk-free rate seems unusually high/low")

def estimate_mu_sigma_enhanced(
    prices: np.ndarray, 
    trading_days: int = TRADING_DAYS,
    confidence_level: float = 0.95,
    min_observations: int = HORIZON_DAYS,
    risk_free_rate: float = 0.0
) -> ParameterEstimates:
    """
    Enhanced parameter estimation with robustness improvements.
    """
    prices = np.asarray(prices, dtype=float)
    
    if len(prices) < max(2, min_observations):
        raise InputValidationError(f"Need at least {max(2, min_observations)} prices")
    
    if np.any(prices <= 0):
        raise InputValidationError("All prices must be positive")
    
    # ------------------------------------------------------------------
    # Log returns (trading-day based)
    # ------------------------------------------------------------------
    log_returns = np.diff(np.log(prices))
    n_obs = len(log_returns)
    dt = 1.0 / trading_days

    # ------------------------------------------------------------------
    # Robust volatility estimation
    # ------------------------------------------------------------------
    sigma_std_daily = np.std(log_returns, ddof=1)  # classical estimator
    
    # MAD-based volatility to reduce outlier influence
    sigma_mad_daily = 1.4826 * np.median(
        np.abs(log_returns - np.median(log_returns))
    )  # robust estimator
    
    # Blend standard + MAD volatility for stability
    sigma_daily = 0.7 * sigma_std_daily + 0.3 * sigma_mad_daily  # robustness blend
    
    sigma_annual = sigma_daily / math.sqrt(dt)

    # ------------------------------------------------------------------
    # Drift estimation with shrinkage toward risk-free rate
    # ------------------------------------------------------------------
    mu_daily = np.mean(log_returns)
    mu_annual_raw = mu_daily / dt  # noisy raw drift estimate

    # log-drift estimator
    mu_log_daily = np.mean(log_returns)
    mu_log_annual = mu_log_daily * trading_days

    # GBM drift (used only where appropriate)
    mu_gbm = mu_log_annual + 0.5 * sigma_annual**2
    
    # Shrink drift to reduce estimation error impact
    shrink_weight = 0.3  # limits overfitting of μ
    mu_annual = shrink_weight * mu_annual_raw + (1 - shrink_weight) * risk_free_rate

    # ------------------------------------------------------------------
    # Confidence intervals
    # ------------------------------------------------------------------
    alpha = 1 - confidence_level
    z = norm.ppf(1 - alpha / 2)

    # Correct annualized standard error of μ
    mu_se = sigma_annual / math.sqrt(n_obs * dt)  # fixes underestimation of μ uncertainty
    mu_ci_lower = mu_annual - z * mu_se
    mu_ci_upper = mu_annual + z * mu_se

    # Sigma CI (chi-squared), widened defensively for non-IID returns
    from scipy.stats import chi2
    chi2_lower = chi2.ppf(alpha / 2, n_obs - 1)
    chi2_upper = chi2.ppf(1 - alpha / 2, n_obs - 1)
    
    sigma_ci_lower = sigma_annual * math.sqrt((n_obs - 1) / chi2_upper)
    sigma_ci_upper = sigma_annual * math.sqrt((n_obs - 1) / chi2_lower)
    
    # Inflate CI slightly to account for volatility clustering
    sigma_ci_lower *= 0.9  # conservative widening
    sigma_ci_upper *= 1.1  # conservative widening

    return ParameterEstimates(
        mu_gbm=float(mu_gbm),
        mu_log=float(mu_log_annual),
        sigma=float(sigma_annual),
        mu_ci_lower=float(mu_ci_lower),
        mu_ci_upper=float(mu_ci_upper),
        sigma_ci_lower=float(sigma_ci_lower),
        sigma_ci_upper=float(sigma_ci_upper),
        n_observations=n_obs
    )

def garch_volatility_forecast(
    returns: np.ndarray,
    horizon: int = 30,
    trading_days: int = TRADING_DAYS,
    vol_floor: float = 0.05,
    vol_cap: float = 1.50
) -> float:
    """
    Improved GARCH(1,1) volatility forecast with stabilization.
    """
    returns = np.asarray(returns, dtype=float)
    if len(returns) < 50:
        raise InputValidationError("Insufficient returns for GARCH forecast")

    # ------------------------------------------------------------------
    # Mean-adjust returns to avoid drift bias
    # ------------------------------------------------------------------
    mu = np.mean(returns)
    centered_returns = returns - mu  # removes drift contamination

    # ------------------------------------------------------------------
    # Robust initial variance estimate
    # ------------------------------------------------------------------
    init_var = np.var(centered_returns[-252:], ddof=1)  # recent regime focus

    # ------------------------------------------------------------------
    # Adaptive GARCH parameters (mild calibration)
    # ------------------------------------------------------------------
    # Typical equity constraint: alpha + beta < 1
    alpha = 0.08
    beta = 0.88
    if alpha + beta >= 0.98:
        beta = 0.98 - alpha  # enforce stationarity

    omega = (1 - alpha - beta) * init_var  # consistent long-run variance

    # ------------------------------------------------------------------
    # Recursive variance estimation (filtered variance)
    # ------------------------------------------------------------------
    sigma2 = init_var
    for r in centered_returns[-252:]:
        sigma2 = omega + alpha * r**2 + beta * sigma2  # standard GARCH update

    # ------------------------------------------------------------------
    # Multi-step variance forecast with mean reversion
    # ------------------------------------------------------------------
    persistence = alpha + beta
    long_run_var = omega / max(1e-6, (1 - persistence))  # numerical safety

    # Expected average variance over forecast horizon
    forecast_var = long_run_var + (sigma2 - long_run_var) * (
        (1 - persistence ** horizon) / (horizon * (1 - persistence))
    )  # smooths multi-step forecast

    # ------------------------------------------------------------------
    # Annualize and clamp volatility
    # ------------------------------------------------------------------
    forecast_vol = math.sqrt(forecast_var * trading_days)
    forecast_vol = float(np.clip(forecast_vol, vol_floor, vol_cap))  # stability bounds

    return forecast_vol

def expected_call_payoff_gbm(
    S0: float,
    K: float,
    T: float,
    mu: float,
    sigma: float,
    *,
    risk_neutral: bool = False,   # Explicitly control pricing vs forecasting measure
    r: float = 0.0,               # Risk-free rate (used only if risk_neutral=True)
    trading_days: int = TRADING_DAYS
) -> float:
    """
    Expected call payoff under GBM with improved numerical stability
    and explicit measure handling.
    """
    validate_inputs(S0, K, T, r, sigma)

    # Handle expiry explicitly to avoid numerical noise
    if T <= 0:
        return max(S0 - K, 0.0)

    # Enforce a minimum time step to avoid instability for very small T
    T_eff = max(T, 1.0 / trading_days)  # Stabilizes near-expiry calculations

    # Select correct drift depending on measure
    # Risk-neutral is required for pricing; physical is for forecasting
    mu_eff = r if risk_neutral else mu  # Ensures measure consistency

    # Deterministic edge case: zero volatility
    if sigma == 0.0:
        ST = S0 * math.exp(mu_eff * T_eff)
        payoff = max(ST - K, 0.0)
        return float(payoff)

    sqrt_T = math.sqrt(T_eff)
    ln_S0_K = math.log(S0 / K)

    # Use numerically stable d1/d2 formulation aligned with Black–Scholes structure
    d1_star = (
        ln_S0_K + (mu_eff + 0.5 * sigma * sigma) * T_eff
    ) / (sigma * sqrt_T)  # Closed-form expectation under GBM

    d2_star = d1_star - sigma * sqrt_T  # Prevents redundant recomputation

    # Closed-form expected payoff under GBM (no Monte Carlo variance)
    expected_payoff = (
        S0 * math.exp(mu_eff * T_eff) * norm.cdf(d1_star)
        - K * norm.cdf(d2_star)
    )

    # Enforce payoff non-negativity to guard against floating-point artifacts
    return max(float(expected_payoff), 0.0)

def expected_put_payoff_gbm(
    S0: float,
    K: float,
    T: float,
    mu: float,
    sigma: float,
    *,
    risk_neutral: bool = False,
    r: float = 0.0,
    trading_days: int = TRADING_DAYS
) -> float:
    """
    Expected put payoff under GBM.
    Mathematical dual of the call payoff; same GBM assumptions.
    """
    validate_inputs(S0, K, T, r, sigma)

    if T <= 0:
        return max(K - S0, 0.0)

    T_eff = max(T, 1.0 / trading_days)
    mu_eff = r if risk_neutral else mu

    if sigma == 0.0:
        ST = S0 * math.exp(mu_eff * T_eff)
        return float(max(K - ST, 0.0))

    sqrt_T = math.sqrt(T_eff)
    ln_K_S0 = math.log(K / S0)

    d1_star = (
        ln_K_S0 - (mu_eff - 0.5 * sigma * sigma) * T_eff
    ) / (sigma * sqrt_T)

    d2_star = d1_star - sigma * sqrt_T

    expected_payoff = (
        K * norm.cdf(d1_star)
        - S0 * math.exp(mu_eff * T_eff) * norm.cdf(d2_star)
    )

    return max(float(expected_payoff), 0.0)

def black_scholes_call(S0: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Enhanced Black-Scholes call price with input validation.
    """
    validate_inputs(S0, K, T, r, sigma)
    
    if T <= 0: return max(S0 - K, 0.0)
    
    if sigma == 0:
        # Zero volatility case
        discount_factor = math.exp(-r * T)
        forward_price = S0 / discount_factor
        return max(forward_price - K, 0.0) * discount_factor
    
    sqrt_T = math.sqrt(T)
    d1 = (math.log(S0 / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrt_T)
    d2 = d1 - sigma * sqrt_T
    
    price = S0 * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return max(price.item(), 0.0)

def black_scholes_put(S0, K, T, r, sigma):
    validate_inputs(S0, K, T, r, sigma)

    if T <= 0:
        return max(K - S0, 0.0)

    sqrt_T = math.sqrt(T)
    d1 = (math.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt_T)
    d2 = d1 - sigma * sqrt_T

    return max(
        K * math.exp(-r * T) * norm.cdf(-d2)
        - S0 * norm.cdf(-d1),
        0.0
    )

def calculate_greeks(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    q: float = 0.0,                  # dividend yield (BSM extension)
    trading_days: int = TRADING_DAYS # keep time units consistent
) -> OptionGreeks:
    """
    Calculate Black–Scholes–Merton option Greeks (local, risk-neutral).
    """
    validate_inputs(S0, K, T, r, sigma)

    # ------------------------------------------------------------------
    # Handle expiry with smooth ATM behavior
    # ------------------------------------------------------------------
    if T <= 0:
        eps = 1e-6  # avoids discontinuity at-the-money
        if abs(S0 - K) < eps:
            delta = 0.5  # ATM call delta at expiry
        else:
            delta = 1.0 if S0 > K else 0.0

        return OptionGreeks(
            delta=delta,
            gamma=0.0,
            theta=0.0,
            vega=0.0,
            rho=0.0
        )

    # ------------------------------------------------------------------
    # Numerical stabilization near expiry
    # ------------------------------------------------------------------
    T_eff = max(T, 1.0 / trading_days)  # prevents gamma blow-ups
    sqrt_T = math.sqrt(T_eff)

    # ------------------------------------------------------------------
    # Black–Scholes–Merton d1 / d2 (dividend-adjusted)
    # ------------------------------------------------------------------
    d1 = (
        math.log(S0 / K)
        + (r - q + 0.5 * sigma * sigma) * T_eff
    ) / (sigma * sqrt_T)

    d2 = d1 - sigma * sqrt_T

    pdf_d1 = norm.pdf(d1)
    cdf_d1 = norm.cdf(d1)
    cdf_d2 = norm.cdf(d2)

    # ------------------------------------------------------------------
    # Delta: dividend-adjusted spot sensitivity
    # ------------------------------------------------------------------
    delta = math.exp(-q * T_eff) * cdf_d1  # more accurate for dividend stocks

    # ------------------------------------------------------------------
    # Gamma: curvature (kept risk-neutral and local)
    # ------------------------------------------------------------------
    gamma = (
        math.exp(-q * T_eff) * pdf_d1
        / (S0 * sigma * sqrt_T)
    )

    # ------------------------------------------------------------------
    # Theta: trading-day decay (not calendar-day)
    # ------------------------------------------------------------------
    theta = (
        - (S0 * math.exp(-q * T_eff) * pdf_d1 * sigma) / (2 * sqrt_T)
        - r * K * math.exp(-r * T_eff) * cdf_d2
        + q * S0 * math.exp(-q * T_eff) * cdf_d1
    )
    theta /= trading_days  # aligns theta with 252-day convention

    # ------------------------------------------------------------------
    # Vega: sensitivity per 1% absolute volatility move
    # ------------------------------------------------------------------
    vega_raw = S0 * math.exp(-q * T_eff) * pdf_d1 * sqrt_T  # unscaled vega
    vega = vega_raw / 100.0  # per +1% vol change

    # ------------------------------------------------------------------
    # Rho: sensitivity per 1% interest-rate move
    # ------------------------------------------------------------------
    rho = K * T_eff * math.exp(-r * T_eff) * cdf_d2 / 100.0

    return OptionGreeks(
        delta=float(delta),
        gamma=float(gamma),
        theta=float(theta),
        vega=float(vega),
        rho=float(rho)
    )

def calculate_bid_ask_spread(volatility: float, liquidity_factor: float = 1.0) -> float:
    """
    Estimate bid-ask spread based on volatility and liquidity.
    Simple model for demonstration.
    """
    base_spread = 0.01  # 1% base spread
    vol_adjustment = volatility * 0.05  # Higher vol = wider spread
    return (base_spread + vol_adjustment) * liquidity_factor

def probability_profitable_expiry(
    S0: float,
    K: float,
    total_cost: float,
    T: float,
    mu_log: float,
    sigma: float
) -> float:
    if T <= 0 or sigma <= 0:
        return 1.0 if S0 > (K + total_cost) else 0.0

    threshold = K + total_cost
    d = (
        math.log(S0 / threshold)
        + (mu_log - 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    return float(norm.cdf(d))

def probability_profitable_expiry_put(
    S0: float,
    K: float,
    total_cost: float,
    T: float,
    mu_log: float,
    sigma: float
) -> float:
    threshold = K - total_cost

    # --- CRITICAL GUARD -----------------------------------------
    # Put can never be profitable if breakeven <= 0
    if threshold <= 0:
        return 0.0
    # ------------------------------------------------------------

    if T <= 0 or sigma <= 0:
        return 1.0 if S0 < threshold else 0.0

    d = (
        math.log(S0 / threshold)
        + (mu_log - 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    return float(norm.cdf(-d))

def compute_expected_profits_enhanced(
    S0: float,
    strike_grid: np.ndarray,
    T: float,
    params: ParameterEstimates,
    market_premiums: Optional[Dict[float, float]] = None,
    transaction_costs: float = 0.5,
    r: float = 0.0,
    liquidity_factors: Optional[Dict[float, float]] = None,
    use_garch: bool = False,
    returns_data: Optional[np.ndarray] = None,
    trading_days: int = TRADING_DAYS
) -> pd.DataFrame:
    """
    Enhanced profit computation with consistent measures, volatility roles,
    and time conventions.
    """
    rows = []

    # --- Volatility selection -------------------------------------------------
    if use_garch and returns_data is not None:
        # Use trading-day horizon, not calendar days, for GARCH consistency
        horizon_days = max(1, int(T * trading_days))  # Fixes earlier 365 mismatch
        sigma_forecast = garch_volatility_forecast(returns_data, horizon=horizon_days)
    else:
        sigma_forecast = params.sigma  # Historical / fallback volatility

    mu_physical = params.mu_gbm  # Explicit naming: physical drift for expectations

    # Precompute sqrt(T) once for numerical stability
    sqrt_T = math.sqrt(T) if T > 0 else 0.0

    for K in strike_grid:
        try:
            # --- Expected payoff (physical measure, no discounting) -------------
            E_payoff = expected_put_payoff_gbm(
                S0,
                K,
                T,
                mu_physical,
                sigma_forecast,
                risk_neutral=False  # Explicit: forecasting, not pricing
            )

            # --- Probability ITM (physical measure, corrected drift) ------------
            if T > 0 and sigma_forecast > 0:
                d_itm = (
                    math.log(S0 / K)
                    + (mu_physical - 0.5 * sigma_forecast**2) * T
                ) / (sigma_forecast * sqrt_T)  # Correct physical-measure ITM prob
                prob_ITM = float(norm.cdf(-d_itm))
            else:
                prob_ITM = 1.0 if S0 > K else 0.0

            # --- Market price (risk-neutral) ------------------------------------
            if market_premiums is not None and K in market_premiums:
                market_price = float(market_premiums[K])
            else:
                market_price = black_scholes_put(
                    S0,
                    K,
                    T,
                    r,
                    sigma_forecast  # Still acceptable as proxy if IV missing
                )

            # --- Liquidity & transaction adjustment -----------------------------
            liquidity_factor = liquidity_factors.get(K, 1.0) if liquidity_factors else 1.0
            bid_ask_spread = calculate_bid_ask_spread(
                sigma_forecast,
                liquidity_factor
            )

            # Apply half-spread pessimistically (buy-side realism)
            effective_price = market_price * (1 + bid_ask_spread / 2)

            # --- Expected profit (real monetary expectation, no discounting) -----
            exp_profit = E_payoff - effective_price - transaction_costs

            # --- Greeks (risk-neutral by definition) ----------------------------
            greeks = calculate_greeks(
                S0,
                K,
                T,
                r,
                sigma_forecast
            )

            # --- Profit confidence intervals (parameter uncertainty) -------------
            profit_scenarios = []
            for mu_scenario in (params.mu_ci_lower, params.mu_gbm, params.mu_ci_upper):
                for sigma_scenario in (
                    params.sigma_ci_lower,
                    params.sigma,
                    params.sigma_ci_upper
                ):
                    payoff_scenario = expected_put_payoff_gbm(
                        S0,
                        K,
                        T,
                        mu_scenario,
                        sigma_scenario,
                        risk_neutral=False  # Keep measure consistent
                    )
                    profit_scenarios.append(
                        payoff_scenario - effective_price - transaction_costs
                    )

            profit_ci_lower = float(np.percentile(profit_scenarios, 5))
            profit_ci_upper = float(np.percentile(profit_scenarios, 95))

            total_cost = market_price + transaction_costs

            prob_profit = probability_profitable_expiry_put(
                K=K, mu_log=params.mu_log, S0=S0, total_cost=total_cost, T=T, sigma=sigma_forecast
            )

            expected_payoff = expected_put_payoff_gbm(
                S0, K, T,
                mu=params.mu_gbm,
                sigma=sigma_forecast
            )

            expected_profit = expected_payoff - total_cost

            rows.append({
                "strike": K,
                "market_price": market_price,
                "effective_price": effective_price,
                "bid_ask_spread": bid_ask_spread,
                "E_payoff": E_payoff,
                "expected_profit": expected_profit,
                "profit_ci_lower": profit_ci_lower,
                "profit_ci_upper": profit_ci_upper,
                "prob_ITM": prob_ITM,
                "prob_profit": prob_profit,
                "delta": greeks.delta,
                "gamma": greeks.gamma,
                "theta": greeks.theta,
                "vega": greeks.vega,
                "rho": greeks.rho,
                "liquidity_factor": liquidity_factor,
                "sigma_forecast": sigma_forecast  # Added for transparency/debugging
            })

        except Exception as e:
            warnings.warn(f"Error processing strike {K}: {str(e)}")
            continue

    df = pd.DataFrame(rows)

    if not df.empty:
        # Sorting by raw expected profit is acceptable here,
        # but downstream ranking can use risk-adjusted metrics
        df = df.sort_values(["prob_profit", "expected_profit"],
    ascending=[False, False]).reset_index(drop=True)

    return df

def backtest_strategy(
        historical_prices: np.ndarray,        
        look_back_days: int = TRADING_DAYS,
        rebalance_freq: int = HORIZON_DAYS
    ) -> pd.DataFrame:
    """
    Backtest the options trading strategy.
    
    Args:
        historical_prices: Long time series of historical prices
        look_back_days: Days to use for parameter estimation
        rebalance_freq: Days between strategy rebalancing
        
    Returns:
        DataFrame with backtest results
    """    
    if len(historical_prices) < look_back_days + 100:
        raise InputValidationError("Insufficient historical data for back testing")
    
    results = []
    
    for i in range(look_back_days, len(historical_prices) - HORIZON_DAYS, rebalance_freq):
        try:
            # Current price and look_back window
            current_price = historical_prices[i]
            look_back_prices = historical_prices[i-look_back_days:i]
            
            # Parameter estimation
            params = estimate_mu_sigma_enhanced(look_back_prices, trading_days=TRADING_DAYS)
            
            # Future realized return (for validation)
            future_price = historical_prices[i + HORIZON_DAYS]  # 30 days ahead
            actual_return = (future_price - current_price) / current_price
            
            # Strategy prediction
            T = HORIZON_DAYS / TRADING_DAYS
            strike = current_price  # ATM for simplicity
            expected_payoff = expected_put_payoff_gbm(
                current_price, strike, T, params.mu_gbm, params.sigma
            )

            predicted_return = math.exp(params.mu_gbm * T) - 1
            prediction_error = actual_return - predicted_return

            results.append({
                'date_index': i,
                'current_price': current_price,
                'future_price': future_price,
                'actual_return': actual_return,
                'predicted_mu': params.mu_gbm,
                'predicted_sigma': params.sigma,
                'expected_payoff': expected_payoff,
                'prediction_error': prediction_error
            })
            
        except Exception as e:
            warnings.warn(f"Backtest error at index {i}: {str(e)}")
            continue
    
    return pd.DataFrame(results)

def plot_parameter_stability(
        params_history: List[ParameterEstimates], 
        title: str = "Parameter Stability Over Time"
    ) -> None:
    """
    Plot the stability of parameter estimates over time.
    """
    if not params_history:
        return
    
    mus = [p.mu_gbm for p in params_history]
    sigmas = [p.sigma for p in params_history]
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    ax1.plot(mus, label='Estimated μ', color='blue')
    ax1.fill_between(range(len(mus)), 
                     [p.mu_ci_lower for p in params_history],
                     [p.mu_ci_upper for p in params_history],
                     alpha=0.3, color='blue', label='95% CI')
    ax1.set_ylabel('Drift (μ)')
    ax1.legend()
    ax1.grid(True)
    
    ax2.plot(sigmas, label='Estimated σ', color='red')
    ax2.fill_between(range(len(sigmas)),
                     [p.sigma_ci_lower for p in params_history],
                     [p.sigma_ci_upper for p in params_history],
                     alpha=0.3, color='red', label='95% CI')
    ax2.set_ylabel('Volatility (σ)')
    ax2.set_xlabel('Time Period')
    ax2.legend()
    ax2.grid(True)
    
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()



# -------------------------------------------------------------
# CLI parsing
# -------------------------------------------------------------
def parse_args():
    parser = argparse.ArgumentParser(description="Calculate best stock options")

    parser.add_argument(
        "--ticker",
        required=True,
        help="Stock Ticker Symbol"
    )

    parser.add_argument(
        "--outfile",
        required=False,
        help="Filename in which the report gets saved in."
    )

    return parser.parse_args()


# ------------------- Enhanced Example Usage -------------------

def main(price_history: pd.DataFrame, stock_option: pd.DataFrame, days_to_expiration: float, ticker: str):
    """Main function demonstrating the enhanced functionality with real options data."""
    current_S0 = float(price_history['Close'].iloc[-1]) # stock close price is first col
    
    log_print(f"Expires At: **{get_future_date(days_to_expiration).strftime('%d.%m.%Y')}**")

    log_print("### 1. Black-School Analysis")        
    
    # ###########################################################################
    # GENERATE ESTIMATION BASED OF PAST STOCK PRICE DEVELOPMENTS
    # ###########################################################################
    
    try:
        closing_prices: npt.NDArray[np.floating] = np.asarray(price_history['Close'].values.astype(float), dtype=float)
        params = estimate_mu_sigma_enhanced(closing_prices, trading_days=TRADING_DAYS)

        log_print(f"- Stock Price Drift: **{params.mu_gbm:.4f} [{params.mu_ci_lower:.4f}, {params.mu_ci_upper:.4f}]**")
        log_print(f"- Stock Volatility: **{params.sigma:.4f} [{params.sigma_ci_lower:.4f}, {params.sigma_ci_upper:.4f}]**")
        log_print(f"- Based on **{params.n_observations}** observations")
        
        # GARCH forecast
        returns = np.diff(np.log(closing_prices))
        garch_vol = garch_volatility_forecast(returns, horizon=HORIZON_DAYS)
        log_print(f"\n- Garch Volatility forecast: **{garch_vol:.4f}**")
        
    except InputValidationError as e:
        log_print(f"[INPUT VALIDATION ERROR]: Parameter estimation error: {e}")
        return
    
    # ###########################################################################
    # ANALYSE STOCK OPTION CONTRACTS: based of past stock prices
    # ###########################################################################
    log_print(f"### 2. Validate Stock Option Contracts")
    
    # Use the passed stock_option DataFrame directly
    nearest_expiry_options = stock_option
    log_print(f"- Analyze **{len(nearest_expiry_options)}** strikes prices..")
    
    # Check if required columns exist
    required_columns = ['strike', 'lastPrice', 'impliedVolatility', 'bid', 'ask']
    missing_columns = [col for col in required_columns if col not in nearest_expiry_options.columns]
    
    if missing_columns:
        log_print(f"[MISSING COLS DETECTED]: Missing required columns: {missing_columns}")
        return
    
    # Filter using pandas first (type-checker friendly)
    valid_options = nearest_expiry_options[
        (nearest_expiry_options['lastPrice'] > 0) & 
        (nearest_expiry_options['impliedVolatility'] > 0) & 
        (nearest_expiry_options['bid'] > 0) & 
        (nearest_expiry_options['ask'] > 0)
    ].copy()

    if len(valid_options) == 0:
        log_print("**No valuable option strikes found**")
        return
    
    # Extract arrays from filtered data
    strikes = valid_options['strike'].values
    market_prices = valid_options['lastPrice'].values
    implied_vols = valid_options['impliedVolatility'].values
    bids = valid_options['bid'].values
    asks = valid_options['ask'].values
    
    log_print(f"Total of valuable options: {len(valid_options)}")
    
    T = int(days_to_expiration) / TRADING_DAYS
    r = 0.05  # Current risk-free rate        
    market_premiums = dict(zip(strikes, market_prices))
    
    # Create liquidity factors based on bid-ask spread
    liquidity_factors = {}
    for i, strike in enumerate(strikes):
        bid_ask_spread = (asks[i] - bids[i]) / market_prices[i] if market_prices[i] > 0 else 1.0
        liquidity_factors[strike] = 1.0 + bid_ask_spread  # Higher spread = lower liquidity
    
    # Enhanced profit analysis with real data
    log_print(f"### 3. Stock Option Contract Analysis")
    
    try:
        df_results = compute_expected_profits_enhanced(
            S0=current_S0,
            strike_grid=strikes, # type: ignore
            T=T,
            params=params,
            market_premiums=market_premiums,
            transaction_costs=0.5,
            r=r,
            liquidity_factors=liquidity_factors,
            use_garch=True,
            returns_data=returns
        )
        
        if len(df_results) == 0:
            log_print("**No valid results generated**")
            return
        
        # Display results
        log_print("- **Top 20 Valuable Option Strikes**")

        display_columns = ['strike', 'market_price', 'expected_profit', 'profit_ci_lower', 
                          'profit_ci_upper', 'prob_ITM', 'prob_profit', 'delta', 'gamma', 'theta', 'vega']
        
        log_print(f"{df_results[display_columns].head(20).to_markdown(index=False, floatfmt='.6f')}")
        
        # Risk analysis
        log_print(f"### 4. Option Call (Sell): Risk Assessment")
        
        best = df_results.iloc[0]
        log_print(f"Best strike price: **${best['strike']:.0f}**")
        log_print(f"Market price: **${best['market_price']:.2f}**")

        log_print(f"Expected profit (USD): **{best['expected_profit']:.2f}** [lowest: {best['profit_ci_lower']:.2f}, highest: {best['profit_ci_upper']:.2f}]")
        
        log_print(f"Delta: {best['delta']:.4f} (price sensitivity)")
        log_print(f"Gamma: {best['gamma']:.4f} (delta sensitivity)")
        log_print(f"Theta: ${best['theta']:.4f} (negative decay per trading-day)")
        log_print(f"Vega: ${best['vega']:.4f} (volatility sensitivity per 1%)")
        
        log_print(f"ITM (In The Money) probability: **{best['prob_ITM']:.2%}**")
        log_print(f"Profit probability: **{best['prob_profit']:.2%}**")
        
        # Compare with Black-Scholes theoretical prices
        log_print(f"### 5. Model VS Market Comparison")        
        
        table = "| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |\n|--------|--------|----------|----|-----------|----- |"

        for i, strike in enumerate(strikes[:20]):  # Show first 20
            try:
                bs_price = black_scholes_call(current_S0, strike, T, r, params.sigma)
                market_price = market_prices[i]
                iv = implied_vols[i]
                diff = market_price - bs_price
                row = f"\n| ${strike:.0f} | ${market_price:.2f} | ${bs_price:.2f} | {iv:.2f} | {params.sigma:.4f} | {diff:.2f} |"
                table += row
            except Exception as e:
                log_print(f"**[ERROR IN BLACK SCHOLES CALL]** Error comparing strike {strike}: {e}")

        log_print(table)
    except Exception as e:
        log_print(f"**[ERROR IN OPTION ANALYSIS]** Error in options analysis: {e}")
        return
    
    # ###########################################################################
    # BACKTESTING STRATEGY: tests stock option estimates
    # ###########################################################################
    log_print(f"### 6. Backtest Stock Option Strategies")
    
    try:
        backtest_results = backtest_strategy(            
            historical_prices=closing_prices,            
            look_back_days=TRADING_DAYS,
            rebalance_freq=70
        )
        
        if len(backtest_results) > 0:
            avg_error = np.mean(np.abs(backtest_results['prediction_error']))
            correlation = np.corrcoef(
                backtest_results['actual_return'], 
                backtest_results['predicted_mu'] * (HORIZON_DAYS) / (TRADING_DAYS)
            )[0,1]
            
            log_print(f"- Config: Look Back Interval **{TRADING_DAYS} Days**. **{len(closing_prices)}** Historical Prices **Last 5 Years**")
            
            log_print(f"- Average modal profit prediction error (actual price - predicted price): **{avg_error:.4f}**")
            log_print(f"- Modal profit prediction correlation: **{correlation:.4f}**")
            log_print(f"- Backtests total: **{len(backtest_results)}**")
            
            # Calculate strategy performance metrics
            profitable_trades = (backtest_results['prediction_error'] > 0).sum()
            total_trades = len(backtest_results)
            win_rate = profitable_trades / total_trades
            
            log_print(f"- Profitable Trades (profitable trades / total trades): **{win_rate:.2%}**")
        else:
            log_print("**Insufficient data for back testing**")
            
    except Exception as e: log_print(f"**[BACKTESTING ERROR]** {e}")
    
    # ###########################################################################
    # SAVE RESULTS TO FILE
    # ###########################################################################
    try:
        # Create unique filenames for each expiry
        expiry_date = "unknown"
        if not valid_options.empty and 'contractSymbol' in valid_options.columns:
            # Try to extract date from first contract symbol
            try:
                symbol = str(valid_options['contractSymbol'].iloc[0])
                expiry_date = symbol[4:10] if len(symbol) > 10 else "unknown"
            except:
                pass
        
        out_dir = pathlib.Path(__file__).parent / 'data'
        if out_dir.exists() is False or out_dir.is_dir() is False: out_dir.mkdir()
        
        out_dir_tables = out_dir / "put"
        if out_dir_tables.exists() is False or out_dir_tables.is_dir() is False: out_dir_tables.mkdir()

        out_dir_tables = out_dir_tables / ticker.upper()
        if out_dir_tables.exists() is False or out_dir_tables.is_dir() is False: out_dir_tables.mkdir()
        
        csv_path = f"enhanced_option_analysis_{expiry_date}.csv"        
        df_results.to_csv(out_dir_tables / csv_path, index=False)
        # log_print(f"\nResults saved to: {csv_path}")
        
        # Save real options data for reference
        options_path = f"real_options_data_{expiry_date}.csv"
        valid_options.to_csv(out_dir_tables / options_path, index=False)
        # log_print(f"Real options data saved to: {options_path}")
        
        # Save backtest results if available
        if 'backtest_results' in locals() and len(backtest_results) > 0:
            backtest_path = f"backtest_results_{expiry_date}.csv"
            backtest_results.to_csv(out_dir_tables / backtest_path, index=False)
            
            # log_print(f"Backtest results saved to: {backtest_path}")
            
    except Exception as e: 
        log_print(f"[FILE EXCEPTION]: Error while saving result in files: {e}")
    

# Fixed main execution
if __name__ == "__main__":
    args = parse_args()
    stock = StockTicker(args.ticker)
    log_print = get_log_print(args.outfile or "REPORT.md")
    
    log_print(f'# Put Option. {stock.get_ticker().ticker} Option Analysis From: {datetime.datetime.now().strftime('%d.%m.%Y %H:%m UTC')}')
    
    log_print(f"> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**")
    
    price_history = stock.get_price_history(start="2000-01-01")
    if price_history is None: raise ValueError('yfinance failed to load price history')
    print('price history loaded')

    stock_options = stock.get_stock_options()
    if not stock_options: raise ValueError('No options data available')
    print('current stock options loaded')

    current_stock_price = float(price_history['Close'].iloc[-1]) # stock close price is first col
    log_print(f"## Current Stock Price: ${current_stock_price}")
    
    # Process each expiration separately
    for i, stock_option in enumerate(stock_options):  # Limit to first 3 expirations
        # log_print(f'START CALCULATING OPTION PROFITABILITY NR: {i+1}/{len(stock_options)}')
        (contract, days_to_expiration) = stock_option
        
        if len(contract.index) == 0:
            log_print("[SKIPPED]: Empty options data found")
            continue

        if (days_to_expiration > 0) is False:
            log_print('[SKIPPED]: stock option contract already expired')
            continue

        try:
            
            log_print(f'### Calculate Stock Option Nr. {i + 1}')
            main(price_history=price_history, stock_option=contract, days_to_expiration=days_to_expiration, ticker=args.ticker)
            log_print(f"-"*50)
            # log_print(f'\nExpiration {i+1} analysis completed successfully')
        except Exception as e:
            log_print(f'[EXCEPTION]: Error analyzing expiration {i+1}: {str(e)}')
            log_print(stock_option)
            continue
            