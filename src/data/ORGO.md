# ORGO Option Analysis From: 05.01.2026 02:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $4.635000228881836

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3765 [-0.7145, 0.6568]**

- Stock Volatility: **0.9724 [0.8485, 1.1043]**

- Based on **1947** observations


- Garch Volatility forecast: **1.0844**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       2.950000 |         -1.245017 |         -1.602167 |         -1.350062 |   0.998451 |      0.091606 | 0.999038 | 0.003394 | -0.000650 | 0.000030 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.95**

Expected profit (USD): **-1.25** [lowest: -1.60, highest: -1.35]

Delta: 0.9990 (price sensitivity)

Gamma: 0.0034 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.85%**

Profit probability: **9.16%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.95 | $2.14 | 5.48 | 0.9724 | 0.81 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1948** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2456**

- Modal profit prediction correlation: **0.0587**

- Backtests total: **24**

- Profitable Trades (profitable trades / total trades): **29.17%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3765 [-0.7145, 0.6568]**

- Stock Volatility: **0.9724 [0.8485, 1.1043]**

- Based on **1947** observations


- Garch Volatility forecast: **1.0844**

### 2. Validate Stock Option Contracts

- Analyze **1** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3765 [-0.7145, 0.6568]**

- Stock Volatility: **0.9724 [0.8485, 1.1043]**

- Based on **1947** observations


- Garch Volatility forecast: **1.0844**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       2.700000 |         -0.117669 |         -2.126432 |          0.247276 |   0.754831 |      0.241613 | 0.892325 | 0.054819 | -0.003434 | 0.005433 |
| 5.000000 |       1.050000 |          0.130044 |         -1.252135 |          0.386817 |   0.396912 |      0.186235 | 0.613277 | 0.113312 | -0.006721 | 0.011231 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.70**

Expected profit (USD): **-0.12** [lowest: -2.13, highest: 0.25]

Delta: 0.8923 (price sensitivity)

Gamma: 0.0548 (delta sensitivity)

Theta: $-0.0034 (negative decay per trading-day)

Vega: $0.0054 (volatility sensitivity per 1%)

ITM (In The Money) probability: **75.48%**

Profit probability: **24.16%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.70 | $2.34 | 3.57 | 0.9724 | 0.36 |
| $5 | $1.05 | $1.02 | 1.20 | 0.9724 | 0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1948** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2456**

- Modal profit prediction correlation: **0.0587**

- Backtests total: **24**

- Profitable Trades (profitable trades / total trades): **29.17%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3765 [-0.7145, 0.6568]**

- Stock Volatility: **0.9724 [0.8485, 1.1043]**

- Based on **1947** observations


- Garch Volatility forecast: **1.0844**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       2.450000 |          1.108637 |         -2.248207 |          2.211681 |   0.645331 |      0.229212 | 0.875389 | 0.043332 | -0.002799 | 0.008310 |
|  7.500000 |       1.000000 |          0.554089 |         -1.516826 |          1.082296 |   0.241507 |      0.108991 | 0.531099 | 0.083904 | -0.005157 | 0.016091 |
| 10.000000 |       0.500000 |          0.557195 |         -0.961001 |          1.027221 |   0.162864 |      0.076628 | 0.419466 | 0.082439 | -0.005034 | 0.015810 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.45**

Expected profit (USD): **1.11** [lowest: -2.25, highest: 2.21]

Delta: 0.8754 (price sensitivity)

Gamma: 0.0433 (delta sensitivity)

Theta: $-0.0028 (negative decay per trading-day)

Vega: $0.0083 (volatility sensitivity per 1%)

ITM (In The Money) probability: **64.53%**

Profit probability: **22.92%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.45 | $2.57 | 0.84 | 0.9724 | -0.12 |
| $8 | $1.00 | $0.90 | 2.08 | 0.9724 | 0.10 |
| $10 | $0.50 | $0.58 | 0.99 | 0.9724 | -0.08 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1948** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2456**

- Modal profit prediction correlation: **0.0587**

- Backtests total: **24**

- Profitable Trades (profitable trades / total trades): **29.17%**

--------------------------------------------------

