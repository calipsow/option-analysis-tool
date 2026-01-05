# NAT Option Analysis From: 05.01.2026 02:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $3.369999885559082

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3240 [-0.3992, 0.5260]**

- Stock Volatility: **0.4747 [0.4094, 0.5458]**

- Based on **1019** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       0.390000 |         -0.475513 |         -0.565792 |         -0.444332 |   0.985505 |      0.009540 | 0.980095 | 0.245158 | -0.001055 | 0.000324 |
| 2.500000 |       0.900000 |         -0.486392 |         -0.599556 |         -0.475450 |   1.000000 |      0.008471 | 1.000000 | 0.000003 | -0.000495 | 0.000000 |
| 0.500000 |       2.900000 |         -0.486392 |         -0.624259 |         -0.500202 |   1.000000 |      0.008471 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |
| 1.000000 |       2.400000 |         -0.486392 |         -0.616864 |         -0.492807 |   1.000000 |      0.008471 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 1.500000 |       1.920000 |         -0.506392 |         -0.633413 |         -0.509356 |   1.000000 |      0.006651 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |
| 3.500000 |       0.070000 |         -0.525449 |         -0.523059 |         -0.453524 |   0.323697 |      0.000907 | 0.279173 | 1.708901 | -0.003486 | 0.002257 |
| 2.000000 |       1.850000 |         -0.936392 |         -1.064399 |         -0.940342 |   1.000000 |      0.000010 | 1.000000 | 0.000000 | -0.000396 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$0.39**

Expected profit (USD): **-0.48** [lowest: -0.57, highest: -0.44]

Delta: 0.9801 (price sensitivity)

Gamma: 0.2452 (delta sensitivity)

Theta: $-0.0011 (negative decay per trading-day)

Vega: $0.0003 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.55%**

Profit probability: **0.95%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $2.90 | $2.87 | 9.13 | 0.4747 | 0.03 |
| $1 | $2.40 | $2.37 | 4.81 | 0.4747 | 0.03 |
| $2 | $1.92 | $1.87 | 2.13 | 0.4747 | 0.05 |
| $2 | $1.85 | $1.37 | 2.59 | 0.4747 | 0.48 |
| $2 | $0.90 | $0.88 | 1.89 | 0.4747 | 0.02 |
| $3 | $0.39 | $0.39 | 1.45 | 0.4747 | -0.00 |
| $4 | $0.07 | $0.08 | 0.52 | 0.4747 | -0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1020** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0963**

- Modal profit prediction correlation: **-0.1735**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **36.36%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3240 [-0.3992, 0.5260]**

- Stock Volatility: **0.4747 [0.4094, 0.5458]**

- Based on **1019** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       0.510000 |         -0.419276 |         -0.719701 |         -0.253152 |   0.890993 |      0.139545 | 0.841588 | 0.534960 | -0.001690 | 0.003442 |
| 3.500000 |       0.120000 |         -0.393570 |         -0.518204 |         -0.197539 |   0.532742 |      0.099537 | 0.440912 | 0.873185 | -0.002248 | 0.005619 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$0.51**

Expected profit (USD): **-0.42** [lowest: -0.72, highest: -0.25]

Delta: 0.8416 (price sensitivity)

Gamma: 0.5350 (delta sensitivity)

Theta: $-0.0017 (negative decay per trading-day)

Vega: $0.0034 (volatility sensitivity per 1%)

ITM (In The Money) probability: **89.10%**

Profit probability: **13.95%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $0.51 | $0.50 | 0.73 | 0.4747 | 0.01 |
| $4 | $0.12 | $0.23 | 0.43 | 0.4747 | -0.11 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1020** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0963**

- Modal profit prediction correlation: **-0.1735**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **36.36%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3240 [-0.3992, 0.5260]**

- Stock Volatility: **0.4747 [0.4094, 0.5458]**

- Based on **1019** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **10** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       0.540000 |         -0.160817 |         -0.789383 |          0.206262 |   0.857598 |      0.285766 | 0.774956 | 0.424634 | -0.001462 | 0.006399 |
| 2.500000 |       1.120000 |         -0.277831 |         -1.126853 |          0.045134 |   0.973776 |      0.254836 | 0.947930 | 0.150799 | -0.000821 | 0.002273 |
| 3.500000 |       0.220000 |         -0.216237 |         -0.603347 |          0.171895 |   0.630866 |      0.219535 | 0.507910 | 0.564673 | -0.001684 | 0.008510 |
| 2.000000 |       1.780000 |         -0.442553 |         -1.412274 |         -0.148171 |   0.998668 |      0.200140 | 0.996424 | 0.015168 | -0.000424 | 0.000229 |
| 0.500000 |       3.360000 |         -0.522702 |         -1.545535 |         -0.256254 |   1.000000 |      0.176322 | 1.000000 | 0.000000 | -0.000097 | 0.000000 |
| 4.000000 |       0.070000 |         -0.317901 |         -0.519030 |          0.043507 |   0.380976 |      0.124270 | 0.268539 | 0.466823 | -0.001312 | 0.007035 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$0.54**

Expected profit (USD): **-0.16** [lowest: -0.79, highest: 0.21]

Delta: 0.7750 (price sensitivity)

Gamma: 0.4246 (delta sensitivity)

Theta: $-0.0015 (negative decay per trading-day)

Vega: $0.0064 (volatility sensitivity per 1%)

ITM (In The Money) probability: **85.76%**

Profit probability: **28.58%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.36 | $2.88 | 2.56 | 0.4747 | 0.48 |
| $2 | $1.78 | $1.42 | 0.96 | 0.4747 | 0.36 |
| $2 | $1.12 | $0.98 | 0.65 | 0.4747 | 0.14 |
| $3 | $0.54 | $0.63 | 0.58 | 0.4747 | -0.09 |
| $4 | $0.22 | $0.38 | 0.50 | 0.4747 | -0.16 |
| $4 | $0.07 | $0.21 | 0.41 | 0.4747 | -0.14 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1020** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0963**

- Modal profit prediction correlation: **-0.1735**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **36.36%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3240 [-0.3992, 0.5260]**

- Stock Volatility: **0.4747 [0.4094, 0.5458]**

- Based on **1019** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.000000 |       1.500000 |          0.314807 |         -1.397828 |          1.010441 |   0.993031 |      0.427566 | 0.979616 | 0.049510 | -0.000494 | 0.001447 |
| 3.000000 |       0.550000 |          0.318947 |         -0.859281 |          1.075906 |   0.860810 |      0.411108 | 0.748888 | 0.320500 | -0.001195 | 0.009370 |
| 2.500000 |       1.050000 |          0.275663 |         -1.202612 |          1.002135 |   0.955641 |      0.411108 | 0.901340 | 0.174853 | -0.000851 | 0.005112 |
| 3.500000 |       0.370000 |          0.103904 |         -0.763613 |          0.879494 |   0.712689 |      0.314704 | 0.558941 | 0.397027 | -0.001317 | 0.011607 |
| 4.000000 |       0.250000 |         -0.090182 |         -0.694731 |          0.667031 |   0.543187 |      0.222046 | 0.380371 | 0.383230 | -0.001195 | 0.011204 |
| 4.500000 |       0.100000 |         -0.171354 |         -0.569105 |          0.540501 |   0.385555 |      0.157117 | 0.240748 | 0.313332 | -0.000943 | 0.009160 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.50**

Expected profit (USD): **0.31** [lowest: -1.40, highest: 1.01]

Delta: 0.9796 (price sensitivity)

Gamma: 0.0495 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0014 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.30%**

Profit probability: **42.76%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.50 | $1.49 | 1.40 | 0.4747 | 0.01 |
| $2 | $1.05 | $1.10 | 0.81 | 0.4747 | -0.05 |
| $3 | $0.55 | $0.79 | 0.71 | 0.4747 | -0.24 |
| $4 | $0.37 | $0.55 | 0.41 | 0.4747 | -0.18 |
| $4 | $0.25 | $0.38 | 0.42 | 0.4747 | -0.13 |
| $4 | $0.10 | $0.26 | 0.47 | 0.4747 | -0.16 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1020** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0963**

- Modal profit prediction correlation: **-0.1735**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **36.36%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.3240 [-0.3992, 0.5260]**

- Stock Volatility: **0.4747 [0.4094, 0.5458]**

- Based on **1019** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 1.000000 |       1.890000 |          2.060816 |         -1.573431 |          3.878053 |   0.999945 |      0.702452 | 0.999527 | 0.001205 | -0.000187 | 0.000069 |
| 1.500000 |       1.830000 |          1.621123 |         -1.805857 |          3.493406 |   0.998090 |      0.594140 | 0.990138 | 0.018776 | -0.000318 | 0.001081 |
| 2.000000 |       1.400000 |          1.554381 |         -1.583078 |          3.452001 |   0.986142 |      0.577180 | 0.949521 | 0.074104 | -0.000523 | 0.004267 |
| 2.500000 |       1.000000 |          1.468713 |         -1.314495 |          3.385605 |   0.952050 |      0.553237 | 0.865203 | 0.154662 | -0.000754 | 0.008905 |
| 0.500000 |       3.000000 |          1.450811 |         -2.188886 |          3.303366 |   1.000000 |      0.553237 | 1.000000 | 0.000001 | -0.000092 | 0.000000 |
| 3.000000 |       0.610000 |          1.397037 |         -1.000552 |          3.333190 |   0.890076 |      0.527367 | 0.747252 | 0.227912 | -0.000930 | 0.013122 |
| 3.500000 |       0.420000 |          1.162663 |         -0.851409 |          3.111577 |   0.804139 |      0.457755 | 0.616169 | 0.272329 | -0.001007 | 0.015679 |
| 4.000000 |       0.260000 |          0.945286 |         -0.716397 |          2.887615 |   0.703887 |      0.388137 | 0.489847 | 0.284385 | -0.000990 | 0.016373 |
| 4.500000 |       0.160000 |          0.719419 |         -0.633103 |          2.632552 |   0.599700 |      0.316297 | 0.378854 | 0.271257 | -0.000907 | 0.015617 |
| 5.000000 |       0.170000 |          0.434862 |         -0.654023 |          2.298114 |   0.499753 |      0.240537 | 0.287166 | 0.242963 | -0.000790 | 0.013988 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$1.89**

Expected profit (USD): **2.06** [lowest: -1.57, highest: 3.88]

Delta: 0.9995 (price sensitivity)

Gamma: 0.0012 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.99%**

Profit probability: **70.25%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.00 | $2.91 | 1.34 | 0.4747 | 0.09 |
| $1 | $1.89 | $2.45 | 1.49 | 0.4747 | -0.56 |
| $2 | $1.83 | $2.01 | 0.59 | 0.4747 | -0.18 |
| $2 | $1.40 | $1.62 | 0.62 | 0.4747 | -0.22 |
| $2 | $1.00 | $1.30 | 0.58 | 0.4747 | -0.30 |
| $3 | $0.61 | $1.03 | 0.47 | 0.4747 | -0.42 |
| $4 | $0.42 | $0.81 | 0.41 | 0.4747 | -0.39 |
| $4 | $0.26 | $0.64 | 0.38 | 0.4747 | -0.38 |
| $4 | $0.16 | $0.51 | 0.43 | 0.4747 | -0.35 |
| $5 | $0.17 | $0.41 | 0.50 | 0.4747 | -0.24 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1020** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0963**

- Modal profit prediction correlation: **-0.1735**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **36.36%**

--------------------------------------------------

