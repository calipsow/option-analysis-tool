# VALE Option Analysis From: 05.01.2026 01:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $13.260000228881836

### Calculate Stock Option Nr. 1

Expires At: **09.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **14** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.000000 |       0.550000 |          0.244388 |          0.175821 |          0.234860 |   0.999701 |      0.716602 | 0.999657 | 0.003178 | -0.002461 | 0.000018 |
| 10.000000 |       2.850000 |         -0.055639 |         -0.176787 |         -0.121172 |   1.000000 |      0.423802 | 1.000000 | 0.000000 | -0.001983 | 0.000000 |
| 11.000000 |       2.180000 |         -0.385639 |         -0.482933 |         -0.427306 |   1.000000 |      0.155287 | 1.000000 | 0.000000 | -0.002181 | 0.000000 |
|  8.000000 |       5.220000 |         -0.425639 |         -0.574771 |         -0.519157 |   1.000000 |      0.133008 | 1.000000 | 0.000000 | -0.001586 | 0.000000 |
| 12.500000 |       0.750000 |         -0.452975 |         -0.503103 |         -0.432902 |   0.980242 |      0.117851 | 0.978381 | 0.131265 | -0.005817 | 0.000748 |
| 11.500000 |       1.790000 |         -0.495639 |         -0.588220 |         -0.532327 |   0.999999 |      0.099647 | 0.999999 | 0.000009 | -0.002281 | 0.000000 |
| 13.000000 |       0.350000 |         -0.504725 |         -0.488412 |         -0.408944 |   0.769966 |      0.076403 | 0.758466 | 0.791798 | -0.022415 | 0.004513 |
|  9.000000 |       4.400000 |         -0.605639 |         -0.745089 |         -0.689475 |   1.000000 |      0.060454 | 1.000000 | 0.000000 | -0.001785 | 0.000000 |
| 13.500000 |       0.070000 |         -0.493294 |         -0.449517 |         -0.382254 |   0.297545 |      0.024992 | 0.284736 | 0.861338 | -0.023018 | 0.004910 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$0.55**

Expected profit (USD): **0.24** [lowest: 0.18, highest: 0.23]

Delta: 0.9997 (price sensitivity)

Gamma: 0.0032 (delta sensitivity)

Theta: $-0.0025 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.97%**

Profit probability: **71.66%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $5.22 | $5.26 | 5.34 | 0.4283 | -0.04 |
| $9 | $4.40 | $4.27 | 4.45 | 0.4283 | 0.13 |
| $10 | $2.85 | $3.27 | 3.64 | 0.4283 | -0.42 |
| $11 | $2.18 | $2.27 | 2.12 | 0.4283 | -0.09 |
| $12 | $1.79 | $1.77 | 1.83 | 0.4283 | 0.02 |
| $12 | $0.55 | $1.27 | 0.62 | 0.4283 | -0.72 |
| $12 | $0.75 | $0.80 | 0.69 | 0.4283 | -0.05 |
| $13 | $0.35 | $0.40 | 0.37 | 0.4283 | -0.05 |
| $14 | $0.07 | $0.15 | 0.28 | 0.4283 | -0.08 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **28** strikes prices..

Total of valuable options: 16

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  9.000000 |       3.800000 |          0.074883 |         -0.165772 |          0.019825 |   1.000000 |      0.503575 | 1.000000 | 0.000000 | -0.001782 | 0.000000 |
|  2.000000 |      11.050000 |         -0.175117 |         -0.514052 |         -0.328457 |   1.000000 |      0.369691 | 1.000000 | 0.000000 | -0.000396 | 0.000000 |
|  3.000000 |      10.100000 |         -0.225117 |         -0.570565 |         -0.384970 |   1.000000 |      0.344489 | 1.000000 | 0.000000 | -0.000594 | 0.000000 |
| 12.500000 |       0.630000 |         -0.218800 |         -0.304485 |         -0.097814 |   0.887588 |      0.329728 | 0.874196 | 0.286076 | -0.009608 | 0.005462 |
|  5.000000 |       8.250000 |         -0.375117 |         -0.674385 |         -0.488790 |   1.000000 |      0.273763 | 1.000000 | 0.000000 | -0.000990 | 0.000000 |
|  7.000000 |       6.250000 |         -0.375117 |         -0.661360 |         -0.475765 |   1.000000 |      0.273763 | 1.000000 | 0.000000 | -0.001386 | 0.000000 |
| 12.000000 |       1.270000 |         -0.389095 |         -0.539402 |         -0.335370 |   0.975159 |      0.264957 | 0.970976 | 0.091586 | -0.004691 | 0.001749 |
|  8.000000 |       5.270000 |         -0.395117 |         -0.646666 |         -0.461071 |   1.000000 |      0.264957 | 1.000000 | 0.000000 | -0.001584 | 0.000000 |
|  1.000000 |      12.290000 |         -0.415117 |         -0.775248 |         -0.589652 |   1.000000 |      0.256310 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 10.000000 |       3.300000 |         -0.425117 |         -0.651487 |         -0.465717 |   1.000000 |      0.252047 | 1.000000 | 0.000001 | -0.001980 | 0.000000 |
|  6.000000 |       7.300000 |         -0.425117 |         -0.719057 |         -0.533461 |   1.000000 |      0.252047 | 1.000000 | 0.000000 | -0.001188 | 0.000000 |
| 11.000000 |       2.310000 |         -0.435089 |         -0.645802 |         -0.456937 |   0.999814 |      0.247825 | 0.999760 | 0.001243 | -0.002210 | 0.000024 |
| 13.000000 |       0.420000 |         -0.407690 |         -0.409273 |         -0.214300 |   0.689448 |      0.204148 | 0.665288 | 0.503859 | -0.014823 | 0.009620 |
| 13.500000 |       0.160000 |         -0.426128 |         -0.377057 |         -0.211083 |   0.421495 |      0.127040 | 0.395344 | 0.532835 | -0.014920 | 0.010173 |
| 14.000000 |       0.050000 |         -0.466204 |         -0.409252 |         -0.283680 |   0.193453 |      0.050613 | 0.175516 | 0.357299 | -0.009782 | 0.006822 |
| 15.000000 |       0.020000 |         -0.515058 |         -0.497011 |         -0.444630 |   0.016547 |      0.002379 | 0.013965 | 0.049265 | -0.001323 | 0.000941 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$9**

Market price: **$3.80**

Expected profit (USD): **0.07** [lowest: -0.17, highest: 0.02]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0018 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **50.36%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $12.29 | $12.26 | 22.31 | 0.4283 | 0.03 |
| $2 | $11.05 | $11.26 | 8.84 | 0.4283 | -0.21 |
| $3 | $10.10 | $10.27 | 11.39 | 0.4283 | -0.17 |
| $5 | $8.25 | $8.27 | 3.02 | 0.4283 | -0.02 |
| $6 | $7.30 | $7.27 | 3.95 | 0.4283 | 0.03 |
| $7 | $6.25 | $6.27 | 2.73 | 0.4283 | -0.02 |
| $8 | $5.27 | $5.28 | 2.01 | 0.4283 | -0.01 |
| $9 | $3.80 | $4.28 | 2.06 | 0.4283 | -0.48 |
| $10 | $3.30 | $3.28 | 0.78 | 0.4283 | 0.02 |
| $11 | $2.31 | $2.29 | 0.59 | 0.4283 | 0.02 |
| $12 | $1.27 | $1.34 | 0.48 | 0.4283 | -0.07 |
| $12 | $0.63 | $0.94 | 0.84 | 0.4283 | -0.31 |
| $13 | $0.42 | $0.60 | 0.32 | 0.4283 | -0.18 |
| $14 | $0.16 | $0.36 | 0.28 | 0.4283 | -0.20 |
| $14 | $0.05 | $0.19 | 0.30 | 0.4283 | -0.14 |
| $15 | $0.02 | $0.04 | 0.41 | 0.4283 | -0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **23.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **14** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 10.000000 |       2.820000 |          0.135896 |         -0.256349 |          0.060892 |   0.999981 |      0.507916 | 0.999973 | 0.000122 | -0.001981 | 0.000004 |
| 11.500000 |       1.430000 |          0.030215 |         -0.287240 |          0.042799 |   0.984825 |      0.461994 | 0.981173 | 0.048609 | -0.003503 | 0.001584 |
| 10.500000 |       2.430000 |          0.025948 |         -0.342751 |         -0.023504 |   0.999710 |      0.461994 | 0.999601 | 0.001524 | -0.002115 | 0.000050 |
| 12.500000 |       0.790000 |         -0.261711 |         -0.418593 |         -0.098228 |   0.840616 |      0.320565 | 0.818615 | 0.278656 | -0.009313 | 0.009081 |
| 13.000000 |       0.480000 |         -0.332505 |         -0.381222 |         -0.085238 |   0.672690 |      0.255305 | 0.640749 | 0.395106 | -0.011982 | 0.012875 |
| 13.500000 |       0.230000 |         -0.368049 |         -0.344550 |         -0.086658 |   0.467506 |      0.182393 | 0.433122 | 0.415689 | -0.012028 | 0.013546 |
| 14.000000 |       0.120000 |         -0.442588 |         -0.389546 |         -0.178689 |   0.277195 |      0.099362 | 0.248858 | 0.335030 | -0.009450 | 0.010918 |
| 15.000000 |       0.130000 |         -0.601786 |         -0.562355 |         -0.445832 |   0.059609 |      0.013164 | 0.049990 | 0.108983 | -0.002997 | 0.003551 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$2.82**

Expected profit (USD): **0.14** [lowest: -0.26, highest: 0.06]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0020 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **50.79%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $10 | $2.82 | $3.30 | 2.95 | 0.4283 | -0.48 |
| $10 | $2.43 | $2.80 | 1.68 | 0.4283 | -0.37 |
| $12 | $1.43 | $1.86 | 0.98 | 0.4283 | -0.43 |
| $12 | $0.79 | $1.06 | 1.12 | 0.4283 | -0.27 |
| $13 | $0.48 | $0.75 | 0.45 | 0.4283 | -0.27 |
| $14 | $0.23 | $0.50 | 0.29 | 0.4283 | -0.27 |
| $14 | $0.12 | $0.32 | 0.30 | 0.4283 | -0.20 |
| $15 | $0.13 | $0.11 | 0.43 | 0.4283 | 0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **30.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.500000 |       0.810000 |         -0.168910 |         -0.387367 |          0.038644 |   0.814525 |      0.352118 | 0.785924 | 0.258389 | -0.008726 | 0.011927 |
| 13.000000 |       0.400000 |         -0.131088 |         -0.224362 |          0.167849 |   0.667724 |      0.324205 | 0.629791 | 0.334789 | -0.010408 | 0.015453 |
| 13.500000 |       0.290000 |         -0.312417 |         -0.326013 |          0.020827 |   0.496004 |      0.217325 | 0.455272 | 0.351451 | -0.010440 | 0.016223 |
| 14.000000 |       0.120000 |         -0.348229 |         -0.315360 |         -0.021378 |   0.330862 |      0.146942 | 0.294643 | 0.305714 | -0.008839 | 0.014111 |
| 14.500000 |       0.100000 |         -0.458697 |         -0.408876 |         -0.170046 |   0.197649 |      0.076446 | 0.170451 | 0.224722 | -0.006386 | 0.010373 |
| 15.000000 |       0.060000 |         -0.492872 |         -0.443682 |         -0.257446 |   0.105910 |      0.037362 | 0.088362 | 0.142010 | -0.003988 | 0.006555 |
| 16.000000 |       0.070000 |         -0.558330 |         -0.533823 |         -0.432681 |   0.022361 |      0.005843 | 0.017447 | 0.038214 | -0.001057 | 0.001764 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$0.81**

Expected profit (USD): **-0.17** [lowest: -0.39, highest: 0.04]

Delta: 0.7859 (price sensitivity)

Gamma: 0.2584 (delta sensitivity)

Theta: $-0.0087 (negative decay per trading-day)

Vega: $0.0119 (volatility sensitivity per 1%)

ITM (In The Money) probability: **81.45%**

Profit probability: **35.21%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $12 | $0.81 | $1.16 | 0.83 | 0.4283 | -0.35 |
| $13 | $0.40 | $0.86 | 0.36 | 0.4283 | -0.46 |
| $14 | $0.29 | $0.62 | 0.29 | 0.4283 | -0.33 |
| $14 | $0.12 | $0.43 | 0.29 | 0.4283 | -0.31 |
| $14 | $0.10 | $0.29 | 0.31 | 0.4283 | -0.19 |
| $15 | $0.06 | $0.19 | 0.37 | 0.4283 | -0.13 |
| $16 | $0.07 | $0.07 | 0.55 | 0.4283 | -0.00 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **06.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 13.000000 |       0.630000 |         -0.247599 |         -0.398240 |          0.087871 |   0.666994 |      0.293041 | 0.624066 | 0.295201 | -0.009373 | 0.017649 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$13**

Market price: **$0.63**

Expected profit (USD): **-0.25** [lowest: -0.40, highest: 0.09]

Delta: 0.6241 (price sensitivity)

Gamma: 0.2952 (delta sensitivity)

Theta: $-0.0094 (negative decay per trading-day)

Vega: $0.0176 (volatility sensitivity per 1%)

ITM (In The Money) probability: **66.70%**

Profit probability: **29.30%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $13 | $0.63 | $0.97 | 0.50 | 0.4283 | -0.34 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **13.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 13.000000 |       0.620000 |         -0.129301 |         -0.338142 |          0.240589 |   0.668203 |      0.322125 | 0.620934 | 0.266694 | -0.008625 | 0.019591 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$13**

Market price: **$0.62**

Expected profit (USD): **-0.13** [lowest: -0.34, highest: 0.24]

Delta: 0.6209 (price sensitivity)

Gamma: 0.2667 (delta sensitivity)

Theta: $-0.0086 (negative decay per trading-day)

Vega: $0.0196 (volatility sensitivity per 1%)

ITM (In The Money) probability: **66.82%**

Profit probability: **32.21%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $13 | $0.62 | $1.06 | 0.53 | 0.4283 | -0.44 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **13** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  8.000000 |       4.800000 |          0.484870 |         -0.454292 |          0.386277 |   0.999998 |      0.542582 | 0.999996 | 0.000013 | -0.001574 | 0.000001 |
| 11.000000 |       2.070000 |          0.229858 |         -0.493223 |          0.328089 |   0.968918 |      0.474334 | 0.957972 | 0.057666 | -0.003597 | 0.005026 |
| 10.000000 |       3.300000 |         -0.013836 |         -0.863248 |         -0.025616 |   0.996292 |      0.417751 | 0.994459 | 0.010186 | -0.002225 | 0.000888 |
| 12.000000 |       1.440000 |         -0.067421 |         -0.574563 |          0.193643 |   0.869364 |      0.384495 | 0.837908 | 0.157750 | -0.006147 | 0.013750 |
| 13.000000 |       0.690000 |         -0.094653 |         -0.355350 |          0.315281 |   0.670419 |      0.328081 | 0.619273 | 0.244919 | -0.008052 | 0.021348 |
| 14.000000 |       0.250000 |         -0.202130 |         -0.280879 |          0.260220 |   0.424395 |      0.219122 | 0.371396 | 0.243024 | -0.007437 | 0.021182 |
| 15.000000 |       0.090000 |         -0.357323 |         -0.346859 |          0.056963 |   0.218052 |      0.106143 | 0.179758 | 0.168547 | -0.004976 | 0.014691 |
| 16.000000 |       0.050000 |         -0.465638 |         -0.429551 |         -0.148863 |   0.091933 |      0.039485 | 0.071264 | 0.087512 | -0.002531 | 0.007628 |
| 17.000000 |       0.030000 |         -0.503553 |         -0.474642 |         -0.291220 |   0.032465 |      0.012317 | 0.023671 | 0.035888 | -0.001024 | 0.003128 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$4.80**

Expected profit (USD): **0.48** [lowest: -0.45, highest: 0.39]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0016 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **54.26%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $4.80 | $5.33 | 1.24 | 0.4283 | -0.53 |
| $10 | $3.30 | $3.40 | 0.98 | 0.4283 | -0.10 |
| $11 | $2.07 | $2.51 | 0.75 | 0.4283 | -0.44 |
| $12 | $1.44 | $1.75 | 0.63 | 0.4283 | -0.31 |
| $13 | $0.69 | $1.14 | 0.30 | 0.4283 | -0.45 |
| $14 | $0.25 | $0.70 | 0.29 | 0.4283 | -0.45 |
| $15 | $0.09 | $0.41 | 0.42 | 0.4283 | -0.32 |
| $16 | $0.05 | $0.22 | 0.34 | 0.4283 | -0.17 |
| $17 | $0.03 | $0.12 | 0.50 | 0.4283 | -0.09 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 8

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **22** strikes prices..

Total of valuable options: 17

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  3.000000 |       7.400000 |          3.221889 |          1.753574 |          3.123073 |   1.000000 |      0.929470 | 1.000000 | 0.000000 | -0.000587 | 0.000000 |
|  5.000000 |       7.800000 |          0.821889 |         -0.653608 |          0.715895 |   1.000000 |      0.558490 | 1.000000 | 0.000000 | -0.000978 | 0.000000 |
|  8.000000 |       5.050000 |          0.571918 |         -0.895729 |          0.471848 |   0.999895 |      0.509245 | 0.999796 | 0.000387 | -0.001574 | 0.000055 |
|  6.000000 |       7.100000 |          0.521889 |         -0.973832 |          0.395715 |   1.000000 |      0.499464 | 1.000000 | 0.000000 | -0.001173 | 0.000000 |
| 10.000000 |       3.250000 |          0.378457 |         -0.903404 |          0.427402 |   0.986873 |      0.470361 | 0.979811 | 0.024502 | -0.002565 | 0.003483 |
|  9.000000 |       4.300000 |          0.322537 |         -1.060323 |          0.296181 |   0.998271 |      0.460758 | 0.997031 | 0.004550 | -0.001876 | 0.000647 |
|  1.000000 |      12.300000 |          0.321889 |         -1.213501 |          0.155998 |   1.000000 |      0.460758 | 1.000000 | 0.000000 | -0.000196 | 0.000000 |
| 11.000000 |       2.380000 |          0.279254 |         -0.792030 |          0.481679 |   0.943853 |      0.445514 | 0.921524 | 0.073555 | -0.003929 | 0.010457 |
|  7.000000 |       6.450000 |          0.171889 |         -1.315588 |          0.053939 |   0.999998 |      0.432312 | 0.999995 | 0.000011 | -0.001369 | 0.000002 |
| 12.000000 |       1.500000 |          0.260162 |         -0.544663 |          0.629500 |   0.843452 |      0.422967 | 0.798474 | 0.141190 | -0.005606 | 0.020072 |
| 13.000000 |       0.830000 |          0.162815 |         -0.360005 |          0.676228 |   0.682934 |      0.363395 | 0.619189 | 0.191272 | -0.006624 | 0.027191 |
| 14.000000 |       0.360000 |          0.044222 |         -0.239749 |          0.634798 |   0.493057 |      0.277207 | 0.424666 | 0.196696 | -0.006350 | 0.027963 |
| 15.000000 |       0.160000 |         -0.158033 |         -0.277880 |          0.429642 |   0.316796 |      0.173552 | 0.258090 | 0.162219 | -0.005031 | 0.023061 |
| 16.000000 |       0.080000 |         -0.323599 |         -0.352852 |          0.198170 |   0.182389 |      0.093377 | 0.140324 | 0.111914 | -0.003384 | 0.015910 |
| 17.000000 |       0.040000 |         -0.418690 |         -0.407513 |          0.007645 |   0.095121 |      0.045044 | 0.069113 | 0.066747 | -0.001984 | 0.009489 |
| 19.000000 |       0.020000 |         -0.497724 |         -0.480602 |         -0.263063 |   0.020169 |      0.008044 | 0.013113 | 0.016932 | -0.000493 | 0.002407 |
| 20.000000 |       0.020000 |         -0.511216 |         -0.497886 |         -0.345288 |   0.008385 |      0.003077 | 0.005169 | 0.007478 | -0.000216 | 0.001063 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$7.40**

Expected profit (USD): **3.22** [lowest: 1.75, highest: 3.12]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **92.95%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $12.30 | $12.27 | 4.55 | 0.4283 | 0.03 |
| $3 | $7.40 | $10.30 | 0.00 | 0.4283 | -2.90 |
| $5 | $7.80 | $8.33 | 1.78 | 0.4283 | -0.53 |
| $6 | $7.10 | $7.35 | 2.79 | 0.4283 | -0.25 |
| $7 | $6.45 | $6.36 | 2.46 | 0.4283 | 0.09 |
| $8 | $5.05 | $5.38 | 0.96 | 0.4283 | -0.33 |
| $9 | $4.30 | $4.43 | 1.01 | 0.4283 | -0.13 |
| $10 | $3.25 | $3.53 | 0.63 | 0.4283 | -0.28 |
| $11 | $2.38 | $2.71 | 0.52 | 0.4283 | -0.33 |
| $12 | $1.50 | $2.01 | 0.36 | 0.4283 | -0.51 |
| $13 | $0.83 | $1.43 | 0.30 | 0.4283 | -0.60 |
| $14 | $0.36 | $0.99 | 0.28 | 0.4283 | -0.63 |
| $15 | $0.16 | $0.66 | 0.29 | 0.4283 | -0.50 |
| $16 | $0.08 | $0.43 | 0.31 | 0.4283 | -0.35 |
| $17 | $0.04 | $0.28 | 0.34 | 0.4283 | -0.24 |
| $19 | $0.02 | $0.11 | 0.54 | 0.4283 | -0.09 |
| $20 | $0.02 | $0.06 | 0.51 | 0.4283 | -0.04 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 9

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **19** strikes prices..

Total of valuable options: 13

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  8.000000 |       4.710000 |          2.053534 |         -0.993329 |          2.039413 |   0.996984 |      0.603915 | 0.993661 | 0.005959 | -0.001683 | 0.001904 |
|  9.000000 |       3.950000 |          1.820619 |         -1.052639 |          1.891421 |   0.986948 |      0.572915 | 0.975659 | 0.019076 | -0.002184 | 0.006095 |
| 10.000000 |       3.450000 |          1.345054 |         -1.262619 |          1.561693 |   0.960654 |      0.508874 | 0.933842 | 0.042907 | -0.002909 | 0.013708 |
|  7.000000 |       6.500000 |          1.262151 |         -1.908079 |          1.173088 |   0.999577 |      0.502557 | 0.998978 | 0.001147 | -0.001373 | 0.000366 |
|  6.000000 |       7.500000 |          1.261994 |         -1.945146 |          1.156502 |   0.999971 |      0.502557 | 0.999917 | 0.000111 | -0.001155 | 0.000035 |
| 11.000000 |       2.550000 |          1.307725 |         -0.975573 |          1.686179 |   0.909302 |      0.496262 | 0.860634 | 0.074067 | -0.003739 | 0.023663 |
| 12.000000 |       1.750000 |          1.236097 |         -0.656489 |          1.806912 |   0.829285 |      0.471328 | 0.757425 | 0.104372 | -0.004445 | 0.033346 |
| 13.000000 |       1.150000 |          1.057393 |         -0.452499 |          1.788005 |   0.724767 |      0.422906 | 0.634487 | 0.125526 | -0.004822 | 0.040104 |
|  5.000000 |       9.300000 |          0.461986 |         -2.786246 |          0.321413 |   0.999999 |      0.405338 | 0.999998 | 0.000004 | -0.000961 | 0.000001 |
| 14.000000 |       0.700000 |          0.841317 |         -0.311006 |          1.694484 |   0.606054 |      0.360325 | 0.506282 | 0.133150 | -0.004787 | 0.042540 |
| 15.000000 |       0.390000 |          0.605872 |         -0.233818 |          1.535954 |   0.485511 |      0.289759 | 0.386051 | 0.127697 | -0.004389 | 0.040797 |
| 16.000000 |       0.230000 |          0.337328 |         -0.250652 |          1.291856 |   0.373732 |      0.217079 | 0.282550 | 0.112857 | -0.003757 | 0.036056 |
| 20.000000 |       0.060000 |         -0.337998 |         -0.430349 |          0.382288 |   0.095156 |      0.045083 | 0.059032 | 0.039259 | -0.001222 | 0.012543 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$4.71**

Expected profit (USD): **2.05** [lowest: -0.99, highest: 2.04]

Delta: 0.9937 (price sensitivity)

Gamma: 0.0060 (delta sensitivity)

Theta: $-0.0017 (negative decay per trading-day)

Vega: $0.0019 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.70%**

Profit probability: **60.39%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $9.30 | $8.42 | 1.87 | 0.4283 | 0.88 |
| $6 | $7.50 | $7.46 | 0.88 | 0.4283 | 0.04 |
| $7 | $6.50 | $6.51 | 1.33 | 0.4283 | -0.01 |
| $8 | $4.71 | $5.60 | 0.63 | 0.4283 | -0.89 |
| $9 | $3.95 | $4.74 | 0.54 | 0.4283 | -0.79 |
| $10 | $3.45 | $3.96 | 0.48 | 0.4283 | -0.51 |
| $11 | $2.55 | $3.26 | 0.63 | 0.4283 | -0.71 |
| $12 | $1.75 | $2.64 | 0.31 | 0.4283 | -0.89 |
| $13 | $1.15 | $2.12 | 0.30 | 0.4283 | -0.97 |
| $14 | $0.70 | $1.69 | 0.34 | 0.4283 | -0.99 |
| $15 | $0.39 | $1.33 | 0.28 | 0.4283 | -0.94 |
| $16 | $0.23 | $1.05 | 0.29 | 0.4283 | -0.82 |
| $20 | $0.06 | $0.38 | 0.35 | 0.4283 | -0.32 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 10

Expires At: **18.09.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **13** strikes prices..

Total of valuable options: 13

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  3.000000 |       8.020000 |          5.002608 |         -0.098145 |          4.854419 |   1.000000 |      0.789361 | 1.000000 | 0.000000 | -0.000566 | 0.000000 |
|  5.000000 |       6.030000 |          4.992615 |         -0.063591 |          4.875071 |   0.999977 |      0.788476 | 0.999917 | 0.000089 | -0.000945 | 0.000045 |
|  7.000000 |       5.650000 |          3.373635 |         -1.506077 |          3.327598 |   0.998082 |      0.631889 | 0.995007 | 0.003846 | -0.001412 | 0.001926 |
|  8.000000 |       5.360000 |          2.667949 |         -1.994230 |          2.720479 |   0.992235 |      0.560073 | 0.982344 | 0.011597 | -0.001778 | 0.005808 |
| 10.000000 |       3.510000 |          2.567740 |         -1.446171 |          2.893319 |   0.948633 |      0.545040 | 0.906036 | 0.044652 | -0.002836 | 0.022363 |
| 12.000000 |       1.940000 |          2.338947 |         -0.800508 |          3.035112 |   0.838392 |      0.502545 | 0.749483 | 0.084725 | -0.003817 | 0.042434 |
| 13.000000 |       1.400000 |          2.078884 |         -0.601516 |          2.951747 |   0.759657 |      0.458440 | 0.651803 | 0.098461 | -0.004052 | 0.049313 |
| 14.000000 |       0.860000 |          1.902851 |         -0.333366 |          2.930993 |   0.671294 |      0.416155 | 0.551116 | 0.105376 | -0.004071 | 0.052776 |
| 15.000000 |       0.640000 |          1.497535 |         -0.333769 |          2.643642 |   0.579197 |      0.349500 | 0.454156 | 0.105547 | -0.003894 | 0.052862 |
| 16.000000 |       0.450000 |          1.153876 |         -0.319194 |          2.379850 |   0.488800 |      0.287877 | 0.365767 | 0.100176 | -0.003571 | 0.050172 |
| 17.000000 |       0.280000 |          0.877944 |         -0.286815 |          2.147226 |   0.404323 |      0.233177 | 0.288702 | 0.090973 | -0.003157 | 0.045563 |
| 18.000000 |       0.210000 |          0.582326 |         -0.322756 |          1.862801 |   0.328511 |      0.181814 | 0.223916 | 0.079656 | -0.002707 | 0.039895 |
| 20.000000 |       0.140000 |          0.123440 |         -0.401034 |          1.343292 |   0.207219 |      0.104708 | 0.129003 | 0.056041 | -0.001846 | 0.028067 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$8.02**

Expected profit (USD): **5.00** [lowest: -0.10, highest: 4.85]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **78.94%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $8.02 | $10.41 | 1.21 | 0.4283 | -2.39 |
| $5 | $6.03 | $8.52 | 0.82 | 0.4283 | -2.49 |
| $7 | $5.65 | $6.70 | 0.53 | 0.4283 | -1.05 |
| $8 | $5.36 | $5.85 | 0.56 | 0.4283 | -0.49 |
| $10 | $3.51 | $4.36 | 0.38 | 0.4283 | -0.85 |
| $12 | $1.94 | $3.15 | 0.33 | 0.4283 | -1.21 |
| $13 | $1.40 | $2.66 | 0.31 | 0.4283 | -1.26 |
| $14 | $0.86 | $2.24 | 0.29 | 0.4283 | -1.38 |
| $15 | $0.64 | $1.88 | 0.30 | 0.4283 | -1.24 |
| $16 | $0.45 | $1.57 | 0.35 | 0.4283 | -1.12 |
| $17 | $0.28 | $1.31 | 0.35 | 0.4283 | -1.03 |
| $18 | $0.21 | $1.10 | 0.38 | 0.4283 | -0.89 |
| $20 | $0.14 | $0.76 | 0.34 | 0.4283 | -0.62 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 11

Expires At: **18.12.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  8.000000 |       4.800000 |          4.581497 |         -1.709282 |          4.698253 |   0.988380 |      0.636207 | 0.971513 | 0.014888 | -0.001809 | 0.010127 |
|  5.000000 |       8.050000 |          4.321973 |         -2.589316 |          4.213060 |   0.999889 |      0.614832 | 0.999561 | 0.000360 | -0.000935 | 0.000245 |
|  3.000000 |      10.450000 |          3.921932 |         -3.102463 |          3.747243 |   1.000000 |      0.580752 | 0.999999 | 0.000001 | -0.000556 | 0.000000 |
| 10.000000 |       3.630000 |          3.811081 |         -1.685599 |          4.203839 |   0.944487 |      0.565522 | 0.890210 | 0.042892 | -0.002698 | 0.029176 |
| 12.000000 |       2.210000 |          3.427168 |         -1.068090 |          4.208494 |   0.851150 |      0.517206 | 0.750298 | 0.072540 | -0.003421 | 0.049343 |
| 15.000000 |       0.840000 |          2.543857 |         -0.446210 |          3.842235 |   0.642636 |      0.391600 | 0.499826 | 0.091126 | -0.003553 | 0.061986 |
| 17.000000 |       0.460000 |          1.788097 |         -0.367202 |          3.296133 |   0.494581 |      0.287239 | 0.352145 | 0.084793 | -0.003101 | 0.057678 |
| 20.000000 |       0.260000 |          0.800118 |         -0.435273 |          2.406961 |   0.306489 |      0.158585 | 0.191665 | 0.062318 | -0.002151 | 0.042390 |
| 22.000000 |       0.130000 |          0.414557 |         -0.409875 |          1.973197 |   0.213451 |      0.103561 | 0.122932 | 0.046475 | -0.001564 | 0.031613 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$4.80**

Expected profit (USD): **4.58** [lowest: -1.71, highest: 4.70]

Delta: 0.9715 (price sensitivity)

Gamma: 0.0149 (delta sensitivity)

Theta: $-0.0018 (negative decay per trading-day)

Vega: $0.0101 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.84%**

Profit probability: **63.62%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $10.45 | $10.46 | 1.04 | 0.4283 | -0.01 |
| $5 | $8.05 | $8.62 | 0.52 | 0.4283 | -0.57 |
| $8 | $4.80 | $6.10 | 0.46 | 0.4283 | -1.30 |
| $10 | $3.63 | $4.71 | 0.36 | 0.4283 | -1.08 |
| $12 | $2.21 | $3.58 | 0.31 | 0.4283 | -1.37 |
| $15 | $0.84 | $2.34 | 0.30 | 0.4283 | -1.50 |
| $17 | $0.46 | $1.76 | 0.30 | 0.4283 | -1.30 |
| $20 | $0.26 | $1.14 | 0.35 | 0.4283 | -0.88 |
| $22 | $0.13 | $0.86 | 0.34 | 0.4283 | -0.73 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 12

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  4.000000 |       7.100000 |          6.708877 |         -0.859169 |          6.574244 |   0.999990 |      0.776689 | 0.999947 | 0.000047 | -0.000738 | 0.000035 |
|  5.000000 |       8.050000 |          4.758934 |         -2.734315 |          4.653184 |   0.999846 |      0.621144 | 0.999378 | 0.000478 | -0.000933 | 0.000351 |
|  8.000000 |       5.100000 |          4.719660 |         -2.094094 |          4.845479 |   0.987450 |      0.617056 | 0.968529 | 0.015550 | -0.001809 | 0.011436 |
|  3.000000 |      10.350000 |          4.458874 |         -3.154610 |          4.294633 |   1.000000 |      0.596657 | 0.999999 | 0.000001 | -0.000553 | 0.000001 |
| 10.000000 |       3.650000 |          4.231071 |         -1.746441 |          4.634629 |   0.944073 |      0.572321 | 0.886795 | 0.042161 | -0.002655 | 0.031006 |
| 12.000000 |       2.160000 |          3.914282 |         -1.021193 |          4.717785 |   0.855171 |      0.531545 | 0.751310 | 0.069607 | -0.003324 | 0.051190 |
| 15.000000 |       0.900000 |          2.891458 |         -0.487829 |          4.227521 |   0.658705 |      0.402251 | 0.511439 | 0.087595 | -0.003468 | 0.064418 |
| 17.000000 |       0.550000 |          2.066069 |         -0.432506 |          3.635384 |   0.517697 |      0.299185 | 0.368480 | 0.082824 | -0.003073 | 0.060910 |
| 20.000000 |       0.230000 |          1.120210 |         -0.381713 |          2.829624 |   0.333966 |      0.176195 | 0.209187 | 0.063161 | -0.002209 | 0.046450 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$4**

Market price: **$7.10**

Expected profit (USD): **6.71** [lowest: -0.86, highest: 6.57]

Delta: 0.9999 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **77.67%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $10.35 | $10.48 | 1.38 | 0.4283 | -0.13 |
| $4 | $7.10 | $9.55 | 0.00 | 0.4283 | -2.45 |
| $5 | $8.05 | $8.65 | 1.26 | 0.4283 | -0.60 |
| $8 | $5.10 | $6.17 | 0.44 | 0.4283 | -1.07 |
| $10 | $3.65 | $4.81 | 0.35 | 0.4283 | -1.16 |
| $12 | $2.16 | $3.71 | 0.30 | 0.4283 | -1.55 |
| $15 | $0.90 | $2.48 | 0.29 | 0.4283 | -1.58 |
| $17 | $0.55 | $1.89 | 0.30 | 0.4283 | -1.34 |
| $20 | $0.23 | $1.26 | 0.32 | 0.4283 | -1.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 13

Expires At: **17.12.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  8.000000 |       5.300000 |         10.684728 |         -3.071873 |         10.923062 |   0.983140 |      0.665101 | 0.945334 | 0.017629 | -0.001689 | 0.024640 |
| 10.000000 |       3.770000 |         10.277322 |         -2.260031 |         10.847432 |   0.950758 |      0.638971 | 0.870771 | 0.033547 | -0.002214 | 0.046891 |
| 12.000000 |       2.580000 |          9.615769 |         -1.592222 |         10.564431 |   0.897472 |      0.594499 | 0.771886 | 0.048129 | -0.002592 | 0.067272 |
| 15.000000 |       1.370000 |          8.291931 |         -0.900827 |          9.868821 |   0.787016 |      0.500916 | 0.607923 | 0.061187 | -0.002787 | 0.085525 |
| 17.000000 |       0.840000 |          7.331636 |         -0.600572 |          9.314358 |   0.702579 |      0.430888 | 0.503842 | 0.063523 | -0.002706 | 0.088790 |
| 20.000000 |       0.500000 |          5.756795 |         -0.505775 |          8.229584 |   0.574827 |      0.322726 | 0.369369 | 0.060089 | -0.002392 | 0.083990 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$5.30**

Expected profit (USD): **10.68** [lowest: -3.07, highest: 10.92]

Delta: 0.9453 (price sensitivity)

Gamma: 0.0176 (delta sensitivity)

Theta: $-0.0017 (negative decay per trading-day)

Vega: $0.0246 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.31%**

Profit probability: **66.51%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $5.30 | $6.98 | 0.59 | 0.4283 | -1.68 |
| $10 | $3.77 | $5.86 | 0.30 | 0.4283 | -2.09 |
| $12 | $2.58 | $4.92 | 0.29 | 0.4283 | -2.34 |
| $15 | $1.37 | $3.81 | 0.29 | 0.4283 | -2.44 |
| $17 | $0.84 | $3.22 | 0.30 | 0.4283 | -2.38 |
| $20 | $0.50 | $2.53 | 0.40 | 0.4283 | -2.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

### Calculate Stock Option Nr. 14

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.2174 [-0.1347, 0.2101]**

- Stock Volatility: **0.4283 [0.3787, 0.4798]**

- Based on **5973** observations


- Garch Volatility forecast: **0.2762**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  3.000000 |       9.000000 |         12.714820 |         -3.672518 |         12.563896 |   0.999983 |      0.740452 | 0.999847 | 0.000092 | -0.000516 | 0.000134 |
|  8.000000 |       5.100000 |         11.635066 |         -2.944214 |         11.876041 |   0.983149 |      0.681143 | 0.943945 | 0.017553 | -0.001672 | 0.025746 |
|  5.000000 |       8.110000 |         11.605407 |         -4.365053 |         11.517193 |   0.999007 |      0.680602 | 0.994729 | 0.002356 | -0.000905 | 0.003455 |
| 10.000000 |       3.800000 |         10.996713 |         -2.330902 |         11.575895 |   0.951911 |      0.643358 | 0.870519 | 0.032792 | -0.002178 | 0.048097 |
| 12.000000 |       2.370000 |         10.570587 |         -1.400846 |         11.533697 |   0.901106 |      0.612900 | 0.774291 | 0.046702 | -0.002541 | 0.068500 |
| 15.000000 |       1.400000 |          8.987933 |         -0.934106 |         10.574151 |   0.796150 |      0.509224 | 0.615285 | 0.059405 | -0.002738 | 0.087131 |
| 17.000000 |       0.900000 |          7.975402 |         -0.657561 |          9.978854 |   0.715649 |      0.439534 | 0.514015 | 0.061974 | -0.002671 | 0.090900 |
| 20.000000 |       0.560000 |          6.353466 |         -0.550306 |          8.880130 |   0.592891 |      0.333431 | 0.382150 | 0.059287 | -0.002387 | 0.086958 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$9.00**

Expected profit (USD): **12.71** [lowest: -3.67, highest: 12.56]

Delta: 0.9998 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **74.05%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $9.00 | $10.69 | 1.81 | 0.4283 | -1.69 |
| $5 | $8.11 | $9.09 | 1.27 | 0.4283 | -0.98 |
| $8 | $5.10 | $7.05 | 0.58 | 0.4283 | -1.95 |
| $10 | $3.80 | $5.95 | 0.31 | 0.4283 | -2.15 |
| $12 | $2.37 | $5.03 | 0.28 | 0.4283 | -2.66 |
| $15 | $1.40 | $3.93 | 0.29 | 0.4283 | -2.53 |
| $17 | $0.90 | $3.35 | 0.28 | 0.4283 | -2.45 |
| $20 | $0.56 | $2.65 | 0.28 | 0.4283 | -2.09 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5974** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1020**

- Modal profit prediction correlation: **0.0012**

- Backtests total: **82**

- Profitable Trades (profitable trades / total trades): **45.12%**

--------------------------------------------------

