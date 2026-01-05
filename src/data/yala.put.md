# Put Option. YALA Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

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
| 5.000000 |       2.050000 |         -2.550000 |         -2.588031 |         -2.585259 |   0.000000 |      0.000000 | 1.000000 | 0.000002 | -0.000990 | 0.000000 |
| 2.500000 |       6.450000 |         -6.950000 |         -7.070451 |         -7.070451 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$5**

Market price: **$2.05**

Expected profit (USD): **-2.55** [lowest: -2.59, highest: -2.59]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **0.00%**

Profit probability: **0.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $6.45 | $4.56 | 10.31 | 0.6290 | 1.89 |
| $5 | $2.05 | $2.07 | 1.03 | 0.6290 | -0.02 |

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
| 7.500000 |       0.600000 |         -0.507490 |         -0.502715 |          0.338645 |   0.591728 |      0.307456 | 0.411619 | 0.328620 | -0.005632 | 0.011609 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$0.60**

Expected profit (USD): **-0.51** [lowest: -0.50, highest: 0.34]

Delta: 0.4116 (price sensitivity)

Gamma: 0.3286 (delta sensitivity)

Theta: $-0.0056 (negative decay per trading-day)

Vega: $0.0116 (volatility sensitivity per 1%)

ITM (In The Money) probability: **59.17%**

Profit probability: **30.75%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $0.60 | $0.59 | 0.55 | 0.6290 | 0.01 |

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
| 12.500000 |       0.200000 |          4.187605 |          3.367949 |          6.154011 |   0.974949 |      0.979299 | 0.027928 | 0.033719 | -0.000639 | 0.002866 |
| 10.000000 |       0.300000 |          1.749144 |          1.260441 |          3.648077 |   0.870875 |      0.867641 | 0.139269 | 0.116645 | -0.002259 | 0.009913 |
|  7.500000 |       0.910000 |         -0.670352 |         -0.797055 |          0.800611 |   0.524857 |      0.338504 | 0.493849 | 0.209792 | -0.004321 | 0.017829 |
|  5.000000 |       2.500000 |         -2.959496 |         -2.977517 |         -2.434553 |   0.074485 |      0.000003 | 0.931903 | 0.069132 | -0.002102 | 0.005875 |
|  2.500000 |       5.200000 |         -5.699996 |         -5.826517 |         -5.808234 |   0.000029 |      0.000000 | 0.999976 | 0.000054 | -0.000487 | 0.000005 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$12**

Market price: **$0.20**

Expected profit (USD): **4.19** [lowest: 3.37, highest: 6.15]

Delta: 0.0279 (price sensitivity)

Gamma: 0.0337 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0029 (volatility sensitivity per 1%)

ITM (In The Money) probability: **97.49%**

Profit probability: **97.93%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $5.20 | $4.61 | 1.34 | 0.6290 | 0.59 |
| $5 | $2.50 | $2.38 | 0.71 | 0.6290 | 0.12 |
| $8 | $0.91 | $1.00 | 0.84 | 0.6290 | -0.09 |
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
| 7.500000 |       1.050000 |         -0.681285 |         -0.931974 |          1.664018 |   0.481251 |      0.398279 | 0.553033 | 0.146107 | -0.003362 | 0.024367 |
| 2.500000 |       4.580000 |         -5.079551 |         -5.170471 |         -5.022251 |   0.001790 |      0.000000 | 0.998647 | 0.001641 | -0.000507 | 0.000274 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$1.05**

Expected profit (USD): **-0.68** [lowest: -0.93, highest: 1.66]

Delta: 0.5530 (price sensitivity)

Gamma: 0.1461 (delta sensitivity)

Theta: $-0.0034 (negative decay per trading-day)

Vega: $0.0244 (volatility sensitivity per 1%)

ITM (In The Money) probability: **48.13%**

Profit probability: **39.83%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $4.58 | $4.67 | 0.82 | 0.6290 | -0.09 |
| $8 | $1.05 | $1.47 | 0.51 | 0.6290 | -0.42 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1321** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1281**

- Modal profit prediction correlation: **0.0338**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

