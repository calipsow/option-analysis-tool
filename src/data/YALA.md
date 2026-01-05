# YALA Option Analysis From: 05.01.2026 00:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $7.059999942779541

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1994 [-0.5381, 0.5391]**

- Stock Volatility: **0.6290 [0.5453, 0.7193]**

- Based on **1320** observations


- Garch Volatility forecast: **0.3792**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       2.050000 |         -0.433905 |         -0.676666 |         -0.374427 |   1.000000 |      0.155909 | 1.000000 | 0.000002 | -0.000990 | 0.000000 |
| 2.500000 |       6.450000 |         -2.333905 |         -2.659619 |         -2.357783 |   1.000000 |      0.000009 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.05**

Expected profit (USD): **-0.43** [lowest: -0.68, highest: -0.37]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **15.59%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $6.45 | $4.56 | 9.91 | 0.6290 | 1.89 |
| $5 | $2.05 | $2.07 | 1.00 | 0.6290 | -0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1321** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1281**

- Modal profit prediction correlation: **0.0338**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1994 [-0.5381, 0.5391]**

- Stock Volatility: **0.6290 [0.5453, 0.7193]**

- Based on **1320** observations


- Garch Volatility forecast: **0.3792**

### 2. Validate Stock Option Contracts

- Analyze **1** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.500000 |       0.600000 |         -0.691529 |         -0.849846 |         -0.097230 |   0.408272 |      0.104085 | 0.411619 | 0.328620 | -0.005632 | 0.011609 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$0.60**

Expected profit (USD): **-0.69** [lowest: -0.85, highest: -0.10]

Delta: 0.4116 (price sensitivity)

Gamma: 0.3286 (delta sensitivity)

Theta: $-0.0056 (negative decay per trading-day)

Vega: $0.0116 (volatility sensitivity per 1%)

ITM (In The Money) probability: **40.83%**

Profit probability: **10.41%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $0.60 | $0.59 | 0.54 | 0.6290 | 0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1321** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1281**

- Modal profit prediction correlation: **0.0338**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1994 [-0.5381, 0.5391]**

- Stock Volatility: **0.6290 [0.5453, 0.7193]**

- Based on **1320** observations


- Garch Volatility forecast: **0.3792**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       2.500000 |         -0.312006 |         -1.875014 |          0.848984 |   0.925515 |      0.275468 | 0.931903 | 0.069132 | -0.002102 | 0.005875 |
|  2.500000 |       5.200000 |         -0.552506 |         -2.629951 |          0.437496 |   0.999971 |      0.245713 | 0.999976 | 0.000054 | -0.000487 | 0.000005 |
|  7.500000 |       0.910000 |         -0.522862 |         -1.141695 |          0.659839 |   0.475143 |      0.159533 | 0.493849 | 0.209792 | -0.004321 | 0.017829 |
| 10.000000 |       0.300000 |         -0.603366 |         -0.733474 |          0.252227 |   0.129125 |      0.043571 | 0.139269 | 0.116645 | -0.002259 | 0.009913 |
| 12.500000 |       0.200000 |         -0.664905 |         -0.687587 |         -0.187737 |   0.025051 |      0.007029 | 0.027928 | 0.033719 | -0.000639 | 0.002866 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.50**

Expected profit (USD): **-0.31** [lowest: -1.88, highest: 0.85]

Delta: 0.9319 (price sensitivity)

Gamma: 0.0691 (delta sensitivity)

Theta: $-0.0021 (negative decay per trading-day)

Vega: $0.0059 (volatility sensitivity per 1%)

ITM (In The Money) probability: **92.55%**

Profit probability: **27.55%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $5.20 | $4.61 | 1.33 | 0.6290 | 0.59 |
| $5 | $2.50 | $2.38 | 0.71 | 0.6290 | 0.12 |
| $8 | $0.91 | $1.00 | 0.83 | 0.6290 | -0.09 |
| $10 | $0.30 | $0.38 | 0.59 | 0.6290 | -0.08 |
| $12 | $0.20 | $0.14 | 0.78 | 0.6290 | 0.06 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1321** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1281**

- Modal profit prediction correlation: **0.0338**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1994 [-0.5381, 0.5391]**

- Stock Volatility: **0.6290 [0.5453, 0.7193]**

- Based on **1320** observations


- Garch Volatility forecast: **0.3792**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       4.580000 |          0.639017 |         -2.899169 |          2.981993 |   0.998210 |      0.354268 | 0.998647 | 0.001641 | -0.000507 | 0.000274 |
| 7.500000 |       1.050000 |          0.037282 |         -1.294151 |          2.469053 |   0.518749 |      0.201515 | 0.553033 | 0.146107 | -0.003362 | 0.024367 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$4.58**

Expected profit (USD): **0.64** [lowest: -2.90, highest: 2.98]

Delta: 0.9986 (price sensitivity)

Gamma: 0.0016 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0003 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.82%**

Profit probability: **35.43%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $4.58 | $4.67 | 0.81 | 0.6290 | -0.09 |
| $8 | $1.05 | $1.47 | 0.51 | 0.6290 | -0.42 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1321** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1281**

- Modal profit prediction correlation: **0.0338**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

