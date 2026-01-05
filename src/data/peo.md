# PEO Option Analysis From: 05.01.2026 01:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $22.040000915527344

[SKIPPED]: Empty options data found

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0954 [-0.0697, 0.1105]**

- Stock Volatility: **0.2338 [0.2069, 0.2617]**

- Based on **6515** observations


- Garch Volatility forecast: **0.2019**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 20.000000 |       1.740000 |          0.262359 |         -0.354089 |          0.325727 |   0.896096 |      0.496725 | 0.895203 | 0.094066 | -0.007349 | 0.016912 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$20**

Market price: **$1.74**

Expected profit (USD): **0.26** [lowest: -0.35, highest: 0.33]

Delta: 0.8952 (price sensitivity)

Gamma: 0.0941 (delta sensitivity)

Theta: $-0.0073 (negative decay per trading-day)

Vega: $0.0169 (volatility sensitivity per 1%)

ITM (In The Money) probability: **89.61%**

Profit probability: **49.67%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $20 | $1.74 | $2.37 | 1.31 | 0.2338 | -0.63 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6516** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0622**

- Modal profit prediction correlation: **-0.0658**

- Backtests total: **90**

- Profitable Trades (profitable trades / total trades): **53.33%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0954 [-0.0697, 0.1105]**

- Stock Volatility: **0.2338 [0.2069, 0.2617]**

- Based on **6515** observations


- Garch Volatility forecast: **0.2019**

### 2. Validate Stock Option Contracts

- Analyze **1** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

