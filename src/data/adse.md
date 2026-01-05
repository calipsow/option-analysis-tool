# ADSE Option Analysis From: 05.01.2026 02:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $12.609999656677246

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1752 [-0.4356, 0.4661]**

- Stock Volatility: **0.4988 [0.4316, 0.5718]**

- Based on **1185** observations


- Garch Volatility forecast: **0.5090**

### 2. Validate Stock Option Contracts

- Analyze **1** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 10.000000 |       2.200000 |         -0.000236 |         -0.391198 |          0.061393 |   0.993945 |      0.459675 | 0.994602 | 0.013135 | -0.002878 | 0.000389 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$2.20**

Expected profit (USD): **-0.00** [lowest: -0.39, highest: 0.06]

Delta: 0.9946 (price sensitivity)

Gamma: 0.0131 (delta sensitivity)

Theta: $-0.0029 (negative decay per trading-day)

Vega: $0.0004 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.39%**

Profit probability: **45.97%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $10 | $2.20 | $2.63 | 3.09 | 0.4988 | -0.43 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1186** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1226**

- Modal profit prediction correlation: **0.4121**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **7.69%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1752 [-0.4356, 0.4661]**

- Stock Volatility: **0.4988 [0.4316, 0.5718]**

- Based on **1185** observations


- Garch Volatility forecast: **0.5090**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       7.600000 |          2.410828 |          0.856517 |          2.894799 |   1.000000 |      0.759522 | 1.000000 | 0.000000 | -0.000492 | 0.000000 |
|  7.500000 |       5.000000 |          0.015779 |         -1.490160 |          0.543893 |   0.990622 |      0.417828 | 0.993322 | 0.006626 | -0.002043 | 0.000996 |
| 10.000000 |       2.800000 |         -0.139548 |         -1.441018 |          0.448744 |   0.856452 |      0.378499 | 0.882641 | 0.069798 | -0.007810 | 0.010493 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$7.60**

Expected profit (USD): **2.41** [lowest: 0.86, highest: 2.89]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **75.95%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $7.60 | $10.13 | 5.28 | 0.4988 | -2.53 |
| $8 | $5.00 | $5.18 | 2.92 | 0.4988 | -0.18 |
| $10 | $2.80 | $2.85 | 0.62 | 0.4988 | -0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1186** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1226**

- Modal profit prediction correlation: **0.4121**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **7.69%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1752 [-0.4356, 0.4661]**

- Stock Volatility: **0.4988 [0.4316, 0.5718]**

- Based on **1185** observations


- Garch Volatility forecast: **0.5090**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 10.000000 |       2.600000 |          1.273593 |         -1.880972 |          3.041773 |   0.720656 |      0.407651 | 0.798242 | 0.054732 | -0.006896 | 0.025392 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$2.60**

Expected profit (USD): **1.27** [lowest: -1.88, highest: 3.04]

Delta: 0.7982 (price sensitivity)

Gamma: 0.0547 (delta sensitivity)

Theta: $-0.0069 (negative decay per trading-day)

Vega: $0.0254 (volatility sensitivity per 1%)

ITM (In The Money) probability: **72.07%**

Profit probability: **40.77%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $10 | $2.60 | $3.40 | 1.23 | 0.4988 | -0.80 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1186** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1226**

- Modal profit prediction correlation: **0.4121**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **7.69%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1752 [-0.4356, 0.4661]**

- Stock Volatility: **0.4988 [0.4316, 0.5718]**

- Based on **1185** observations


- Garch Volatility forecast: **0.5090**

### 2. Validate Stock Option Contracts

- Analyze **1** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

