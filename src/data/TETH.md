# TETH Option Analysis From: 05.01.2026 01:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $15.569999694824219

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2011 [-1.2303, 1.1867]**

- Stock Volatility: **0.7400 [0.6208, 0.8780]**

- Based on **363** observations


- Garch Volatility forecast: **0.6718**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.000000 |       2.300000 |          0.905624 |          0.000032 |          1.477184 |   0.979750 |      0.622800 | 0.983353 | 0.020928 | -0.006419 | 0.001284 |
| 15.000000 |       0.940000 |         -0.266309 |         -0.779190 |          0.328316 |   0.615132 |      0.303592 | 0.645288 | 0.188097 | -0.038595 | 0.011544 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$2.30**

Expected profit (USD): **0.91** [lowest: 0.00, highest: 1.48]

Delta: 0.9834 (price sensitivity)

Gamma: 0.0209 (delta sensitivity)

Theta: $-0.0064 (negative decay per trading-day)

Vega: $0.0013 (volatility sensitivity per 1%)

ITM (In The Money) probability: **97.97%**

Profit probability: **62.28%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $12 | $2.30 | $3.62 | 1.79 | 0.7400 | -1.32 |
| $15 | $0.94 | $1.23 | 0.54 | 0.7400 | -0.29 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **364** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2053**

- Modal profit prediction correlation: **-1.0000**

- Backtests total: **2**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2011 [-1.2303, 1.1867]**

- Stock Volatility: **0.7400 [0.6208, 0.8780]**

- Based on **363** observations


- Garch Volatility forecast: **0.6718**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  9.000000 |       5.200000 |          1.912907 |         -3.291921 |          7.152533 |   0.919184 |      0.462110 | 0.952156 | 0.016771 | -0.005634 | 0.008344 |
| 16.000000 |       2.300000 |         -0.082730 |         -2.548486 |          4.204414 |   0.456467 |      0.229559 | 0.562453 | 0.066372 | -0.017310 | 0.033021 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$9**

Market price: **$5.20**

Expected profit (USD): **1.91** [lowest: -3.29, highest: 7.15]

Delta: 0.9522 (price sensitivity)

Gamma: 0.0168 (delta sensitivity)

Theta: $-0.0056 (negative decay per trading-day)

Vega: $0.0083 (volatility sensitivity per 1%)

ITM (In The Money) probability: **91.92%**

Profit probability: **46.21%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $9 | $5.20 | $6.86 | 0.61 | 0.7400 | -1.66 |
| $16 | $2.30 | $2.37 | 0.65 | 0.7400 | -0.07 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **364** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2053**

- Modal profit prediction correlation: **-1.0000**

- Backtests total: **2**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2011 [-1.2303, 1.1867]**

- Stock Volatility: **0.7400 [0.6208, 0.8780]**

- Based on **363** observations


- Garch Volatility forecast: **0.6718**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |       3.300000 |          1.495750 |         -3.745941 |         15.390237 |   0.496432 |      0.243623 | 0.659939 | 0.040055 | -0.011523 | 0.045886 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$15**

Market price: **$3.30**

Expected profit (USD): **1.50** [lowest: -3.75, highest: 15.39]

Delta: 0.6599 (price sensitivity)

Gamma: 0.0401 (delta sensitivity)

Theta: $-0.0115 (negative decay per trading-day)

Vega: $0.0459 (volatility sensitivity per 1%)

ITM (In The Money) probability: **49.64%**

Profit probability: **24.36%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $15 | $3.30 | $4.07 | 0.68 | 0.7400 | -0.77 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **364** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2053**

- Modal profit prediction correlation: **-1.0000**

- Backtests total: **2**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

