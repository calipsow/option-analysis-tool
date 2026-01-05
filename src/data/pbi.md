# PBI Option Analysis From: 05.01.2026 02:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $10.329999923706055

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0641 [-0.1543, 0.1469]**

- Stock Volatility: **0.3908 [0.3458, 0.4374]**

- Based on **6522** observations


- Garch Volatility forecast: **0.3593**

### 2. Validate Stock Option Contracts

- Analyze **22** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       5.300000 |         -0.443704 |         -0.614793 |         -0.491366 |   1.000000 |      0.235067 | 1.000000 | 0.000000 | -0.000990 | 0.000000 |
|  8.000000 |       2.500000 |         -0.643699 |         -0.781764 |         -0.658192 |   0.999957 |      0.157790 | 0.999966 | 0.000213 | -0.001589 | 0.000003 |
| 10.000000 |       0.620000 |         -0.639817 |         -0.684553 |         -0.556274 |   0.692919 |      0.121015 | 0.712535 | 0.505945 | -0.012850 | 0.007015 |
|  1.000000 |       9.650000 |         -0.793704 |         -1.055114 |         -0.931688 |   1.000000 |      0.112903 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
|  9.000000 |       1.680000 |         -0.820182 |         -0.933266 |         -0.805388 |   0.982975 |      0.105206 | 0.985228 | 0.055471 | -0.003010 | 0.000769 |
|  3.000000 |       7.700000 |         -0.843704 |         -1.079402 |         -0.955976 |   1.000000 |      0.100302 | 1.000000 | 0.000000 | -0.000594 | 0.000000 |
|  4.000000 |       6.700000 |         -0.843704 |         -1.066217 |         -0.942790 |   1.000000 |      0.100302 | 1.000000 | 0.000000 | -0.000792 | 0.000000 |
|  7.000000 |       4.100000 |         -1.243704 |         -1.401607 |         -1.278181 |   1.000000 |      0.034544 | 1.000000 | 0.000000 | -0.001386 | 0.000000 |
|  6.000000 |       5.410000 |         -1.553704 |         -1.718332 |         -1.594906 |   1.000000 |      0.013135 | 1.000000 | 0.000000 | -0.001188 | 0.000000 |
|  2.000000 |      10.470000 |         -2.613704 |         -2.860874 |         -2.737448 |   1.000000 |      0.000208 | 1.000000 | 0.000000 | -0.000396 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$5.30**

Expected profit (USD): **-0.44** [lowest: -0.61, highest: -0.49]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **23.51%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $9.65 | $9.33 | 9.47 | 0.3908 | 0.32 |
| $2 | $10.47 | $8.33 | 14.34 | 0.3908 | 2.14 |
| $3 | $7.70 | $7.34 | 4.88 | 0.3908 | 0.36 |
| $4 | $6.70 | $6.34 | 3.84 | 0.3908 | 0.36 |
| $5 | $5.30 | $5.34 | 3.66 | 0.3908 | -0.04 |
| $6 | $5.41 | $4.34 | 4.48 | 0.3908 | 1.07 |
| $7 | $4.10 | $3.34 | 1.67 | 0.3908 | 0.76 |
| $8 | $2.50 | $2.35 | 1.59 | 0.3908 | 0.15 |
| $9 | $1.68 | $1.36 | 0.89 | 0.3908 | 0.32 |
| $10 | $0.62 | $0.52 | 0.49 | 0.3908 | 0.10 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6523** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0982**

- Modal profit prediction correlation: **-0.0074**

- Backtests total: **90**

- Profitable Trades (profitable trades / total trades): **52.22%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0641 [-0.1543, 0.1469]**

- Stock Volatility: **0.3908 [0.3458, 0.4374]**

- Based on **6522** observations


- Garch Volatility forecast: **0.3593**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  8.000000 |       1.700000 |          0.276503 |         -0.148379 |          0.403351 |   0.945528 |      0.494643 | 0.959583 | 0.052996 | -0.003068 | 0.003793 |
|  7.000000 |       3.000000 |         -0.048616 |         -0.509620 |          0.046354 |   0.992741 |      0.422290 | 0.995160 | 0.008566 | -0.001622 | 0.000613 |
|  9.000000 |       1.100000 |         -0.007919 |         -0.378701 |          0.138947 |   0.805372 |      0.399071 | 0.842282 | 0.146991 | -0.005809 | 0.010522 |
| 10.000000 |       1.000000 |         -0.604227 |         -0.878059 |         -0.449043 |   0.578178 |      0.220909 | 0.633127 | 0.229616 | -0.007985 | 0.016436 |
| 11.000000 |       0.550000 |         -0.611949 |         -0.782873 |         -0.475118 |   0.343406 |      0.143793 | 0.397327 | 0.235188 | -0.007757 | 0.016835 |
| 12.000000 |       0.250000 |         -0.562480 |         -0.650386 |         -0.458555 |   0.170720 |      0.077927 | 0.209426 | 0.175474 | -0.005636 | 0.012560 |
| 13.000000 |       0.200000 |         -0.628684 |         -0.670048 |         -0.566232 |   0.072756 |      0.030612 | 0.094650 | 0.102794 | -0.003252 | 0.007358 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$1.70**

Expected profit (USD): **0.28** [lowest: -0.15, highest: 0.40]

Delta: 0.9596 (price sensitivity)

Gamma: 0.0530 (delta sensitivity)

Theta: $-0.0031 (negative decay per trading-day)

Vega: $0.0038 (volatility sensitivity per 1%)

ITM (In The Money) probability: **94.55%**

Profit probability: **49.46%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $7 | $3.00 | $3.40 | 1.08 | 0.3908 | -0.40 |
| $8 | $1.70 | $2.44 | 0.75 | 0.3908 | -0.74 |
| $9 | $1.10 | $1.57 | 0.62 | 0.3908 | -0.47 |
| $10 | $1.00 | $0.90 | 0.53 | 0.3908 | 0.10 |
| $11 | $0.55 | $0.45 | 0.52 | 0.3908 | 0.10 |
| $12 | $0.25 | $0.20 | 0.52 | 0.3908 | 0.05 |
| $13 | $0.20 | $0.08 | 0.54 | 0.3908 | 0.12 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6523** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0982**

- Modal profit prediction correlation: **-0.0074**

- Backtests total: **90**

- Profitable Trades (profitable trades / total trades): **52.22%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0641 [-0.1543, 0.1469]**

- Stock Volatility: **0.3908 [0.3458, 0.4374]**

- Based on **6522** observations


- Garch Volatility forecast: **0.3593**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  9.000000 |       1.150000 |          0.146918 |         -0.426187 |          0.362024 |   0.737146 |      0.394772 | 0.795756 | 0.129900 | -0.005524 | 0.015762 |
|  8.000000 |       2.400000 |         -0.288141 |         -0.950906 |         -0.084541 |   0.883381 |      0.353188 | 0.916828 | 0.070146 | -0.003664 | 0.008512 |
| 10.000000 |       1.300000 |         -0.649968 |         -1.106255 |         -0.449424 |   0.554042 |      0.225953 | 0.628494 | 0.173229 | -0.006720 | 0.021020 |
| 11.000000 |       0.650000 |         -0.463123 |         -0.789514 |         -0.292041 |   0.376290 |      0.186574 | 0.450953 | 0.181411 | -0.006712 | 0.022013 |
| 12.000000 |       0.350000 |         -0.464490 |         -0.677207 |         -0.327948 |   0.233589 |      0.123898 | 0.296292 | 0.158412 | -0.005702 | 0.019222 |
| 13.000000 |       0.260000 |         -0.554960 |         -0.684215 |         -0.453782 |   0.134377 |      0.069494 | 0.180371 | 0.120387 | -0.004259 | 0.014608 |
| 14.000000 |       0.170000 |         -0.565770 |         -0.647426 |         -0.504602 |   0.072599 |      0.037319 | 0.102986 | 0.082155 | -0.002872 | 0.009969 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$9**

Market price: **$1.15**

Expected profit (USD): **0.15** [lowest: -0.43, highest: 0.36]

Delta: 0.7958 (price sensitivity)

Gamma: 0.1299 (delta sensitivity)

Theta: $-0.0055 (negative decay per trading-day)

Vega: $0.0158 (volatility sensitivity per 1%)

ITM (In The Money) probability: **73.71%**

Profit probability: **39.48%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $2.40 | $2.53 | 0.68 | 0.3908 | -0.13 |
| $9 | $1.15 | $1.73 | 0.61 | 0.3908 | -0.58 |
| $10 | $1.30 | $1.10 | 0.53 | 0.3908 | 0.20 |
| $11 | $0.65 | $0.65 | 0.52 | 0.3908 | -0.00 |
| $12 | $0.35 | $0.36 | 0.51 | 0.3908 | -0.01 |
| $13 | $0.26 | $0.19 | 0.53 | 0.3908 | 0.07 |
| $14 | $0.17 | $0.10 | 0.74 | 0.3908 | 0.07 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6523** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0982**

- Modal profit prediction correlation: **-0.0074**

- Backtests total: **90**

- Profitable Trades (profitable trades / total trades): **52.22%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0641 [-0.1543, 0.1469]**

- Stock Volatility: **0.3908 [0.3458, 0.4374]**

- Based on **6522** observations


- Garch Volatility forecast: **0.3593**

### 2. Validate Stock Option Contracts

- Analyze **17** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  7.000000 |       2.800000 |          0.345823 |         -0.585385 |          0.637328 |   0.933583 |      0.446237 | 0.958658 | 0.033675 | -0.002419 | 0.005789 |
|  9.000000 |       1.700000 |         -0.212143 |         -0.969344 |          0.076818 |   0.696847 |      0.321184 | 0.772663 | 0.114769 | -0.005131 | 0.019728 |
|  8.000000 |       2.720000 |         -0.463104 |         -1.344778 |         -0.182213 |   0.836023 |      0.318677 | 0.886963 | 0.072945 | -0.003787 | 0.012539 |
| 10.000000 |       1.300000 |         -0.431013 |         -1.054860 |         -0.173211 |   0.540338 |      0.251594 | 0.630651 | 0.143562 | -0.005944 | 0.024678 |
|  6.000000 |       5.300000 |         -1.192423 |         -2.174892 |         -0.932468 |   0.982521 |      0.251594 | 0.990387 | 0.009796 | -0.001480 | 0.001684 |
| 11.000000 |       0.850000 |         -0.445768 |         -0.924926 |         -0.229020 |   0.392317 |      0.198074 | 0.483651 | 0.151649 | -0.006008 | 0.026068 |
| 12.000000 |       0.500000 |         -0.424080 |         -0.768695 |         -0.250830 |   0.269198 |      0.146835 | 0.350879 | 0.141046 | -0.005435 | 0.024245 |
| 13.000000 |       0.300000 |         -0.444302 |         -0.680328 |         -0.310911 |   0.176235 |      0.099431 | 0.242740 | 0.119002 | -0.004501 | 0.020456 |
| 14.000000 |       0.150000 |         -0.435839 |         -0.590043 |         -0.333528 |   0.111033 |      0.064293 | 0.161390 | 0.093091 | -0.003475 | 0.016002 |
| 15.000000 |       0.150000 |         -0.523701 |         -0.622508 |         -0.450059 |   0.067824 |      0.037603 | 0.103852 | 0.068630 | -0.002537 | 0.011797 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$7**

Market price: **$2.80**

Expected profit (USD): **0.35** [lowest: -0.59, highest: 0.64]

Delta: 0.9587 (price sensitivity)

Gamma: 0.0337 (delta sensitivity)

Theta: $-0.0024 (negative decay per trading-day)

Vega: $0.0058 (volatility sensitivity per 1%)

ITM (In The Money) probability: **93.36%**

Profit probability: **44.62%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $6 | $5.30 | $4.46 | 0.94 | 0.3908 | 0.84 |
| $7 | $2.80 | $3.51 | 0.82 | 0.3908 | -0.71 |
| $8 | $2.72 | $2.64 | 0.62 | 0.3908 | 0.08 |
| $9 | $1.70 | $1.88 | 0.54 | 0.3908 | -0.18 |
| $10 | $1.30 | $1.28 | 0.50 | 0.3908 | 0.02 |
| $11 | $0.85 | $0.83 | 0.49 | 0.3908 | 0.02 |
| $12 | $0.50 | $0.52 | 0.49 | 0.3908 | -0.02 |
| $13 | $0.30 | $0.31 | 0.51 | 0.3908 | -0.01 |
| $14 | $0.15 | $0.18 | 0.54 | 0.3908 | -0.03 |
| $15 | $0.15 | $0.10 | 0.53 | 0.3908 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6523** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0982**

- Modal profit prediction correlation: **-0.0074**

- Backtests total: **90**

- Profitable Trades (profitable trades / total trades): **52.22%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0641 [-0.1543, 0.1469]**

- Stock Volatility: **0.3908 [0.3458, 0.4374]**

- Based on **6522** observations


- Garch Volatility forecast: **0.3593**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       5.740000 |         -0.378009 |         -2.138536 |          0.217435 |   0.974938 |      0.329919 | 0.989024 | 0.007732 | -0.001211 | 0.002606 |
|  7.000000 |       3.970000 |         -0.451872 |         -2.091834 |          0.129080 |   0.848303 |      0.309909 | 0.913317 | 0.042238 | -0.002662 | 0.014238 |
|  8.000000 |       3.100000 |         -0.380253 |         -1.895837 |          0.168906 |   0.745442 |      0.299011 | 0.839524 | 0.065209 | -0.003498 | 0.021981 |
|  9.000000 |       2.300000 |         -0.268936 |         -1.597572 |          0.257537 |   0.631098 |      0.282821 | 0.747631 | 0.085426 | -0.004175 | 0.028796 |
| 11.000000 |       1.250000 |         -0.256902 |         -1.210060 |          0.152620 |   0.413046 |      0.215220 | 0.544815 | 0.106038 | -0.004703 | 0.035744 |
| 12.000000 |       0.920000 |         -0.293509 |         -1.067707 |          0.055497 |   0.322707 |      0.176198 | 0.449133 | 0.105843 | -0.004568 | 0.035679 |
| 13.000000 |       0.550000 |         -0.207496 |         -0.819446 |          0.087943 |   0.247837 |      0.145321 | 0.363536 | 0.100406 | -0.004247 | 0.033846 |
| 14.000000 |       0.350000 |         -0.224135 |         -0.701791 |          0.019541 |   0.187787 |      0.113191 | 0.289860 | 0.091541 | -0.003813 | 0.030858 |
| 15.000000 |       0.290000 |         -0.327429 |         -0.696392 |         -0.130182 |   0.140803 |      0.083898 | 0.228308 | 0.080886 | -0.003329 | 0.027266 |
| 16.000000 |       0.230000 |         -0.389378 |         -0.675859 |         -0.235738 |   0.104731 |      0.061889 | 0.178066 | 0.069713 | -0.002841 | 0.023500 |
| 17.000000 |       0.330000 |         -0.579812 |         -0.804938 |         -0.465349 |   0.077431 |      0.043167 | 0.137796 | 0.058897 | -0.002381 | 0.019854 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$5.74**

Expected profit (USD): **-0.38** [lowest: -2.14, highest: 0.22]

Delta: 0.9890 (price sensitivity)

Gamma: 0.0077 (delta sensitivity)

Theta: $-0.0012 (negative decay per trading-day)

Vega: $0.0026 (volatility sensitivity per 1%)

ITM (In The Money) probability: **97.49%**

Profit probability: **32.99%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $5.74 | $5.53 | 1.12 | 0.3908 | 0.21 |
| $7 | $3.97 | $3.73 | 0.66 | 0.3908 | 0.24 |
| $8 | $3.10 | $2.95 | 0.55 | 0.3908 | 0.15 |
| $9 | $2.30 | $2.28 | 0.52 | 0.3908 | 0.02 |
| $11 | $1.25 | $1.29 | 0.49 | 0.3908 | -0.04 |
| $12 | $0.92 | $0.95 | 0.50 | 0.3908 | -0.03 |
| $13 | $0.55 | $0.69 | 0.45 | 0.3908 | -0.14 |
| $14 | $0.35 | $0.50 | 0.46 | 0.3908 | -0.15 |
| $15 | $0.29 | $0.36 | 0.47 | 0.3908 | -0.07 |
| $16 | $0.23 | $0.25 | 0.52 | 0.3908 | -0.02 |
| $17 | $0.33 | $0.18 | 0.62 | 0.3908 | 0.15 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6523** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0982**

- Modal profit prediction correlation: **-0.0074**

- Backtests total: **90**

- Profitable Trades (profitable trades / total trades): **52.22%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.0641 [-0.1543, 0.1469]**

- Stock Volatility: **0.3908 [0.3458, 0.4374]**

- Based on **6522** observations


- Garch Volatility forecast: **0.3593**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 12

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.000000 |       6.320000 |          2.540671 |         -0.710885 |          3.918669 |   0.999113 |      0.506145 | 0.999840 | 0.000116 | -0.000372 | 0.000077 |
|  4.000000 |       6.690000 |          0.196678 |         -3.062109 |          1.526064 |   0.962124 |      0.327060 | 0.987736 | 0.006000 | -0.000932 | 0.004005 |
|  5.000000 |       6.000000 |         -0.051364 |         -3.233563 |          1.262522 |   0.910098 |      0.308095 | 0.965180 | 0.014505 | -0.001378 | 0.009683 |
|  1.000000 |      10.120000 |         -0.259549 |         -3.630957 |          0.998918 |   0.999996 |      0.301019 | 1.000000 | 0.000000 | -0.000184 | 0.000000 |
|  7.000000 |       4.240000 |          0.036683 |         -2.783351 |          1.308440 |   0.753693 |      0.294089 | 0.876779 | 0.038418 | -0.002401 | 0.025647 |
|  3.000000 |       9.060000 |         -1.195182 |         -4.487836 |          0.135098 |   0.990256 |      0.250490 | 0.997515 | 0.001455 | -0.000601 | 0.000971 |
| 10.000000 |       2.280000 |          0.129359 |         -1.962912 |          1.167604 |   0.496654 |      0.239857 | 0.678852 | 0.067513 | -0.003425 | 0.045071 |
| 12.000000 |       1.430000 |          0.130290 |         -1.483308 |          0.988311 |   0.358146 |      0.190911 | 0.543582 | 0.074754 | -0.003571 | 0.049905 |
| 15.000000 |       0.750000 |         -0.028354 |         -1.068708 |          0.586286 |   0.212452 |      0.120093 | 0.372568 | 0.071333 | -0.003239 | 0.047621 |
| 17.000000 |       0.650000 |         -0.285890 |         -1.053617 |          0.192895 |   0.148783 |      0.082288 | 0.284750 | 0.063971 | -0.002844 | 0.042707 |
| 20.000000 |       0.400000 |         -0.381571 |         -0.861521 |         -0.053822 |   0.087210 |      0.048000 | 0.188009 | 0.050823 | -0.002210 | 0.033929 |
| 22.000000 |       0.240000 |         -0.368539 |         -0.721367 |         -0.116931 |   0.061327 |      0.033710 | 0.142118 | 0.042387 | -0.001824 | 0.028297 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$6.32**

Expected profit (USD): **2.54** [lowest: -0.71, highest: 3.92]

Delta: 0.9998 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0004 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.91%**

Profit probability: **50.61%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $10.12 | $9.40 | 4.34 | 0.3908 | 0.72 |
| $2 | $6.32 | $8.47 | 0.00 | 0.3908 | -2.15 |
| $3 | $9.06 | $7.55 | 1.44 | 0.3908 | 1.51 |
| $4 | $6.69 | $6.63 | 1.07 | 0.3908 | 0.06 |
| $5 | $6.00 | $5.75 | 0.78 | 0.3908 | 0.25 |
| $7 | $4.24 | $4.17 | 0.53 | 0.3908 | 0.07 |
| $10 | $2.28 | $2.41 | 0.52 | 0.3908 | -0.13 |
| $12 | $1.43 | $1.64 | 0.51 | 0.3908 | -0.21 |
| $15 | $0.75 | $0.91 | 0.50 | 0.3908 | -0.16 |
| $17 | $0.65 | $0.61 | 0.51 | 0.3908 | 0.04 |
| $20 | $0.40 | $0.34 | 0.53 | 0.3908 | 0.06 |
| $22 | $0.24 | $0.23 | 0.54 | 0.3908 | 0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6523** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0982**

- Modal profit prediction correlation: **-0.0074**

- Backtests total: **90**

- Profitable Trades (profitable trades / total trades): **52.22%**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.0641 [-0.1543, 0.1469]**

- Stock Volatility: **0.3908 [0.3458, 0.4374]**

- Based on **6522** observations


- Garch Volatility forecast: **0.3593**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  1.000000 |       8.350000 |          2.634337 |         -3.509404 |          5.890095 |   0.998993 |      0.363112 | 0.999916 | 0.000045 | -0.000173 | 0.000060 |
|  5.000000 |       6.300000 |          0.962274 |         -4.626369 |          4.146192 |   0.812272 |      0.275167 | 0.940664 | 0.015639 | -0.001280 | 0.020974 |
|  8.000000 |       4.100000 |          1.055867 |         -3.563880 |          3.942873 |   0.596120 |      0.246042 | 0.820531 | 0.034686 | -0.002113 | 0.046520 |
| 10.000000 |       3.150000 |          0.938388 |         -3.012202 |          3.571367 |   0.475300 |      0.212871 | 0.729772 | 0.043807 | -0.002451 | 0.058752 |
| 12.000000 |       2.140000 |          1.099050 |         -2.223369 |          3.489101 |   0.377758 |      0.186120 | 0.641586 | 0.049470 | -0.002625 | 0.066347 |
| 20.000000 |       0.500000 |          0.745275 |         -0.943927 |          2.213880 |   0.156199 |      0.082900 | 0.368387 | 0.049931 | -0.002400 | 0.066966 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$8.35**

Expected profit (USD): **2.63** [lowest: -3.51, highest: 5.89]

Delta: 0.9999 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.90%**

Profit probability: **36.31%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $8.35 | $9.47 | 1.29 | 0.3908 | -1.12 |
| $5 | $6.30 | $6.21 | 0.68 | 0.3908 | 0.09 |
| $8 | $4.10 | $4.36 | 0.73 | 0.3908 | -0.26 |
| $10 | $3.15 | $3.43 | 0.70 | 0.3908 | -0.28 |
| $12 | $2.14 | $2.71 | 0.55 | 0.3908 | -0.57 |
| $20 | $0.50 | $1.11 | 0.63 | 0.3908 | -0.61 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6523** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0982**

- Modal profit prediction correlation: **-0.0074**

- Backtests total: **90**

- Profitable Trades (profitable trades / total trades): **52.22%**

--------------------------------------------------

