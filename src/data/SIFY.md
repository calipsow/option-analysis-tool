# SIFY Option Analysis From: 06.01.2026 21:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $12.529999732971191

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1405 [-0.3595, 0.2547]**

- Stock Volatility: **0.7940 [0.7025, 0.8887]**

- Based on **6470** observations


- Garch Volatility forecast: **0.6656**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       3.900000 |          5.693032 |          5.361183 |          5.635543 |   1.000000 |      1.000000 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |
|  5.000000 |       6.800000 |          0.293032 |         -0.111456 |          0.162904 |   1.000000 |      0.519832 | 1.000000 | 0.000000 | -0.000990 | 0.000000 |
|  7.500000 |       4.400000 |          0.193033 |         -0.171022 |          0.103548 |   0.999996 |      0.491685 | 0.999997 | 0.000009 | -0.001486 | 0.000000 |
| 10.000000 |       2.800000 |         -0.696327 |         -0.994868 |         -0.705705 |   0.974543 |      0.263838 | 0.979263 | 0.034730 | -0.005914 | 0.001182 |
| 12.500000 |       1.190000 |         -1.068337 |         -1.091740 |         -0.816941 |   0.502898 |      0.115823 | 0.537375 | 0.276292 | -0.032939 | 0.009405 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.90**

Expected profit (USD): **5.69** [lowest: 5.36, highest: 5.64]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **100.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.90 | $10.03 | 9.19 | 0.7940 | -6.13 |
| $5 | $6.80 | $7.54 | 6.66 | 0.7940 | -0.74 |
| $8 | $4.40 | $5.04 | 4.30 | 0.7940 | -0.64 |
| $10 | $2.80 | $2.60 | 2.96 | 0.7940 | 0.20 |
| $12 | $1.19 | $0.77 | 1.40 | 0.7940 | 0.42 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6471** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2683**

- Modal profit prediction correlation: **-0.1285**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **51.69%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1405 [-0.3595, 0.2547]**

- Stock Volatility: **0.7940 [0.7025, 0.8887]**

- Based on **6470** observations


- Garch Volatility forecast: **0.6656**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.500000 |       1.810000 |         -0.676126 |         -1.266304 |         -0.280503 |   0.479454 |      0.203821 | 0.572638 | 0.108246 | -0.017283 | 0.020540 |
| 15.000000 |       1.050000 |         -0.805177 |         -1.122478 |         -0.415354 |   0.247665 |      0.112738 | 0.327352 | 0.099599 | -0.015547 | 0.018900 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$1.81**

Expected profit (USD): **-0.68** [lowest: -1.27, highest: -0.28]

Delta: 0.5726 (price sensitivity)

Gamma: 0.1082 (delta sensitivity)

Theta: $-0.0173 (negative decay per trading-day)

Vega: $0.0205 (volatility sensitivity per 1%)

ITM (In The Money) probability: **47.95%**

Profit probability: **20.38%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $12 | $1.81 | $1.71 | 1.01 | 0.7940 | 0.10 |
| $15 | $1.05 | $0.87 | 1.12 | 0.7940 | 0.18 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6471** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2683**

- Modal profit prediction correlation: **-0.1285**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **51.69%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1405 [-0.3595, 0.2547]**

- Stock Volatility: **0.7940 [0.7025, 0.8887]**

- Based on **6470** observations


- Garch Volatility forecast: **0.6656**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       7.580000 |          0.192793 |         -2.428776 |          0.550672 |   0.968677 |      0.317764 | 0.987769 | 0.005447 | -0.001862 | 0.002506 |
|  7.500000 |       5.500000 |         -0.007846 |         -2.361557 |          0.471074 |   0.838973 |      0.293947 | 0.915950 | 0.026467 | -0.005693 | 0.012179 |
| 10.000000 |       3.570000 |          0.062068 |         -1.859807 |          0.649898 |   0.645032 |      0.264094 | 0.776381 | 0.051264 | -0.009910 | 0.023590 |
| 12.500000 |       3.000000 |         -0.739340 |         -2.214549 |         -0.125310 |   0.457135 |      0.182191 | 0.610428 | 0.065792 | -0.012218 | 0.030275 |
| 15.000000 |       2.250000 |         -0.937340 |         -1.978430 |         -0.313909 |   0.308709 |      0.129209 | 0.455640 | 0.068007 | -0.012380 | 0.031294 |
| 17.500000 |       2.300000 |         -1.618799 |         -2.432538 |         -1.118646 |   0.203037 |      0.078001 | 0.328979 | 0.062042 | -0.011163 | 0.028549 |
| 20.000000 |       1.070000 |         -0.801261 |         -1.365951 |         -0.346125 |   0.131822 |      0.060683 | 0.232778 | 0.052435 | -0.009362 | 0.024128 |
| 22.500000 |       0.050000 |         -0.048339 |         -0.432696 |          0.351076 |   0.085193 |      0.045352 | 0.162834 | 0.042216 | -0.007497 | 0.019426 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$7.58**

Expected profit (USD): **0.19** [lowest: -2.43, highest: 0.55]

Delta: 0.9878 (price sensitivity)

Gamma: 0.0054 (delta sensitivity)

Theta: $-0.0019 (negative decay per trading-day)

Vega: $0.0025 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.87%**

Profit probability: **31.78%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $7.58 | $7.67 | 3.24 | 0.7940 | -0.09 |
| $8 | $5.50 | $5.52 | 1.05 | 0.7940 | -0.02 |
| $10 | $3.57 | $3.82 | 0.99 | 0.7940 | -0.25 |
| $12 | $3.00 | $2.59 | 1.29 | 0.7940 | 0.41 |
| $15 | $2.25 | $1.73 | 0.99 | 0.7940 | 0.52 |
| $18 | $2.30 | $1.16 | 1.21 | 0.7940 | 1.14 |
| $20 | $1.07 | $0.78 | 1.30 | 0.7940 | 0.29 |
| $22 | $0.05 | $0.53 | 1.37 | 0.7940 | -0.48 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6471** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2683**

- Modal profit prediction correlation: **-0.1285**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **51.69%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1405 [-0.3595, 0.2547]**

- Stock Volatility: **0.7940 [0.7025, 0.8887]**

- Based on **6470** observations


- Garch Volatility forecast: **0.6656**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       7.780000 |          0.797549 |         -3.662231 |          1.819803 |   0.888077 |      0.268006 | 0.962072 | 0.009942 | -0.002621 | 0.009002 |
|  7.500000 |       5.400000 |          1.153753 |         -2.829008 |          2.246967 |   0.727173 |      0.263551 | 0.877621 | 0.024435 | -0.005398 | 0.022125 |
| 10.000000 |       4.320000 |          0.619449 |         -2.795879 |          1.732782 |   0.567498 |      0.216378 | 0.766968 | 0.036851 | -0.007652 | 0.033366 |
| 12.500000 |       3.560000 |          0.134103 |         -2.726299 |          1.221576 |   0.433746 |      0.170532 | 0.652488 | 0.044508 | -0.008967 | 0.040300 |
| 15.000000 |       2.570000 |          0.176189 |         -2.175740 |          1.220892 |   0.329218 |      0.139228 | 0.546498 | 0.047737 | -0.009448 | 0.043223 |
| 17.500000 |       2.490000 |         -0.463031 |         -2.413832 |          0.488787 |   0.249909 |      0.101416 | 0.453872 | 0.047742 | -0.009340 | 0.043228 |
| 20.000000 |       1.800000 |         -0.319854 |         -1.920402 |          0.553048 |   0.190420 |      0.080561 | 0.375447 | 0.045701 | -0.008867 | 0.041380 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$7.78**

Expected profit (USD): **0.80** [lowest: -3.66, highest: 1.82]

Delta: 0.9621 (price sensitivity)

Gamma: 0.0099 (delta sensitivity)

Theta: $-0.0026 (negative decay per trading-day)

Vega: $0.0090 (volatility sensitivity per 1%)

ITM (In The Money) probability: **88.81%**

Profit probability: **26.80%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $7.78 | $7.91 | 0.98 | 0.7940 | -0.13 |
| $8 | $5.40 | $6.08 | 0.95 | 0.7940 | -0.68 |
| $10 | $4.32 | $4.65 | 0.99 | 0.7940 | -0.33 |
| $12 | $3.56 | $3.57 | 0.98 | 0.7940 | -0.01 |
| $15 | $2.57 | $2.76 | 0.96 | 0.7940 | -0.19 |
| $18 | $2.49 | $2.15 | 1.04 | 0.7940 | 0.34 |
| $20 | $1.80 | $1.69 | 1.17 | 0.7940 | 0.11 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6471** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2683**

- Modal profit prediction correlation: **-0.1285**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **51.69%**

--------------------------------------------------

