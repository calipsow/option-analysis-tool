# EAF Option Analysis From: 05.01.2026 02:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $16.420000076293945

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0444 [-0.5527, 0.3921]**

- Stock Volatility: **0.6683 [0.5831, 0.7590]**

- Based on **1937** observations


- Garch Volatility forecast: **0.9276**

### 2. Validate Stock Option Contracts

- Analyze **23** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  3.000000 |       6.200000 |          6.691080 |          6.126284 |          6.740019 |   1.000000 |      0.998127 | 1.000000 | 0.000000 | -0.000594 | 0.000000 |
| 11.000000 |       2.360000 |          2.539340 |          2.082686 |          2.697090 |   0.986862 |      0.797619 | 0.992166 | 0.007585 | -0.005204 | 0.000704 |
| 13.000000 |       1.100000 |          1.895844 |          1.423600 |          2.042439 |   0.895297 |      0.702667 | 0.926423 | 0.049173 | -0.022102 | 0.004563 |
| 12.000000 |       3.190000 |          0.735152 |          0.251522 |          0.868005 |   0.957146 |      0.545913 | 0.972122 | 0.022566 | -0.011359 | 0.002094 |
| 15.000000 |       1.400000 |          0.014874 |         -0.586036 |         -0.011176 |   0.665286 |      0.376515 | 0.732829 | 0.115936 | -0.048652 | 0.010758 |
| 14.000000 |       2.500000 |         -0.352696 |         -0.958754 |         -0.347426 |   0.795672 |      0.363622 | 0.846307 | 0.083526 | -0.035834 | 0.007751 |
| 16.000000 |       1.700000 |         -0.878708 |         -1.485965 |         -0.989012 |   0.521288 |      0.228564 | 0.597873 | 0.136372 | -0.056556 | 0.012654 |
| 17.000000 |       1.020000 |         -0.649680 |         -1.138962 |         -0.752300 |   0.383039 |      0.199205 | 0.458962 | 0.139881 | -0.057606 | 0.012980 |
|  7.000000 |      12.300000 |         -3.408920 |         -4.149822 |         -3.536087 |   0.999999 |      0.109109 | 1.000000 | 0.000000 | -0.001386 | 0.000000 |
| 18.000000 |       1.770000 |         -1.721580 |         -2.139951 |         -1.859541 |   0.264890 |      0.085802 | 0.332187 | 0.127993 | -0.052474 | 0.011877 |
| 20.000000 |       0.370000 |         -0.676903 |         -0.861401 |         -0.749992 |   0.107827 |      0.062281 | 0.148311 | 0.081568 | -0.033267 | 0.007569 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$6.20**

Expected profit (USD): **6.69** [lowest: 6.13, highest: 6.74]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **99.81%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $6.20 | $13.43 | 19.81 | 0.6683 | -7.23 |
| $7 | $12.30 | $9.43 | 0.00 | 0.6683 | 2.87 |
| $11 | $2.36 | $5.44 | 2.89 | 0.6683 | -3.08 |
| $12 | $3.19 | $4.45 | 1.91 | 0.6683 | -1.26 |
| $13 | $1.10 | $3.48 | 1.70 | 0.6683 | -2.38 |
| $14 | $2.50 | $2.56 | 0.89 | 0.6683 | -0.06 |
| $15 | $1.40 | $1.75 | 0.84 | 0.6683 | -0.35 |
| $16 | $1.70 | $1.10 | 0.88 | 0.6683 | 0.60 |
| $17 | $1.02 | $0.64 | 0.84 | 0.6683 | 0.38 |
| $18 | $1.77 | $0.34 | 0.88 | 0.6683 | 1.43 |
| $20 | $0.37 | $0.08 | 1.03 | 0.6683 | 0.29 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1938** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1677**

- Modal profit prediction correlation: **-0.0683**

- Backtests total: **24**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0444 [-0.5527, 0.3921]**

- Stock Volatility: **0.6683 [0.5831, 0.7590]**

- Based on **1937** observations


- Garch Volatility forecast: **0.9276**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |       2.680000 |          0.028357 |         -1.846979 |          0.213651 |   0.500404 |      0.283709 | 0.672871 | 0.054235 | -0.028205 | 0.025040 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$15**

Market price: **$2.68**

Expected profit (USD): **0.03** [lowest: -1.85, highest: 0.21]

Delta: 0.6729 (price sensitivity)

Gamma: 0.0542 (delta sensitivity)

Theta: $-0.0282 (negative decay per trading-day)

Vega: $0.0250 (volatility sensitivity per 1%)

ITM (In The Money) probability: **50.04%**

Profit probability: **28.37%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $15 | $2.68 | $2.64 | 0.88 | 0.6683 | 0.04 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1938** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1677**

- Modal profit prediction correlation: **-0.0683**

- Backtests total: **24**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0444 [-0.5527, 0.3921]**

- Stock Volatility: **0.6683 [0.5831, 0.7590]**

- Based on **1937** observations


- Garch Volatility forecast: **0.9276**

### 2. Validate Stock Option Contracts

- Analyze **21** strikes prices..

Total of valuable options: 17

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  6.000000 |       5.000000 |          4.789937 |          1.457140 |          7.493694 |   0.890007 |      0.527644 | 0.972903 | 0.005954 | -0.004301 | 0.006499 |
|  9.000000 |       3.600000 |          3.763379 |          0.243816 |          6.052369 |   0.723265 |      0.446567 | 0.901696 | 0.016504 | -0.010310 | 0.018017 |
| 10.000000 |       6.000000 |          0.669045 |         -2.952461 |          2.690531 |   0.665610 |      0.310249 | 0.870030 | 0.020142 | -0.012331 | 0.021987 |
| 11.000000 |       5.700000 |          0.331540 |         -3.320159 |          2.110070 |   0.609798 |      0.287702 | 0.835840 | 0.023561 | -0.014215 | 0.025719 |
| 15.000000 |       2.370000 |          1.624019 |         -1.625933 |          2.630861 |   0.418326 |      0.267673 | 0.688829 | 0.033651 | -0.019659 | 0.036734 |
| 12.000000 |       6.410000 |         -0.961477 |         -4.605646 |          0.570414 |   0.556751 |      0.239375 | 0.799952 | 0.026664 | -0.015910 | 0.029107 |
| 16.000000 |       3.200000 |          0.395456 |         -2.756227 |          1.173894 |   0.379387 |      0.219965 | 0.652330 | 0.035186 | -0.020460 | 0.038410 |
| 14.000000 |       5.330000 |         -0.896696 |         -4.372722 |          0.206729 |   0.460848 |      0.216932 | 0.725884 | 0.031724 | -0.018638 | 0.034631 |
|  8.000000 |      11.900000 |         -3.784278 |         -7.461283 |         -1.535649 |   0.781343 |      0.204145 | 0.929954 | 0.012792 | -0.008226 | 0.013965 |
| 17.000000 |       2.940000 |          0.294099 |         -2.717835 |          0.889131 |   0.343884 |      0.203278 | 0.616699 | 0.036353 | -0.021055 | 0.039684 |
| 18.000000 |       2.450000 |          0.456608 |         -2.400587 |          0.892700 |   0.311621 |      0.192559 | 0.582170 | 0.037182 | -0.021463 | 0.040588 |
| 21.000000 |       1.950000 |          0.147183 |         -2.167134 |          0.279482 |   0.231994 |      0.148063 | 0.486603 | 0.037969 | -0.021750 | 0.041448 |
| 20.000000 |       3.300000 |         -0.959068 |         -3.533068 |         -0.822410 |   0.255910 |      0.142773 | 0.517031 | 0.037956 | -0.021791 | 0.041433 |
| 19.000000 |       4.800000 |         -2.190148 |         -4.953565 |         -1.960061 |   0.282374 |      0.135568 | 0.548910 | 0.037704 | -0.021702 | 0.041159 |
| 24.000000 |       1.500000 |         -0.006287 |         -1.886007 |         -0.112998 |   0.173329 |      0.113873 | 0.404243 | 0.036891 | -0.021021 | 0.040270 |
| 25.000000 |       1.000000 |          0.328451 |         -1.462464 |          0.124468 |   0.157467 |      0.108235 | 0.379722 | 0.036250 | -0.020626 | 0.039572 |
| 30.000000 |       1.250000 |         -0.549061 |         -1.819517 |         -0.920265 |   0.098524 |      0.064432 | 0.277161 | 0.031897 | -0.018050 | 0.034819 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$6**

Market price: **$5.00**

Expected profit (USD): **4.79** [lowest: 1.46, highest: 7.49]

Delta: 0.9729 (price sensitivity)

Gamma: 0.0060 (delta sensitivity)

Theta: $-0.0043 (negative decay per trading-day)

Vega: $0.0065 (volatility sensitivity per 1%)

ITM (In The Money) probability: **89.00%**

Profit probability: **52.76%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $6 | $5.00 | $10.55 | 3.53 | 0.6683 | -5.55 |
| $8 | $11.90 | $8.66 | 0.00 | 0.6683 | 3.24 |
| $9 | $3.60 | $7.76 | 2.63 | 0.6683 | -4.16 |
| $10 | $6.00 | $6.90 | 0.84 | 0.6683 | -0.90 |
| $11 | $5.70 | $6.11 | 0.75 | 0.6683 | -0.41 |
| $12 | $6.41 | $5.37 | 0.73 | 0.6683 | 1.04 |
| $14 | $5.33 | $4.09 | 0.86 | 0.6683 | 1.24 |
| $15 | $2.37 | $3.55 | 0.78 | 0.6683 | -1.18 |
| $16 | $3.20 | $3.07 | 0.77 | 0.6683 | 0.13 |
| $17 | $2.94 | $2.65 | 0.84 | 0.6683 | 0.29 |
| $18 | $2.45 | $2.28 | 0.89 | 0.6683 | 0.17 |
| $19 | $4.80 | $1.96 | 0.89 | 0.6683 | 2.84 |
| $20 | $3.30 | $1.68 | 0.98 | 0.6683 | 1.62 |
| $21 | $1.95 | $1.44 | 0.96 | 0.6683 | 0.51 |
| $24 | $1.50 | $0.90 | 0.91 | 0.6683 | 0.60 |
| $25 | $1.00 | $0.77 | 1.20 | 0.6683 | 0.23 |
| $30 | $1.25 | $0.35 | 1.30 | 0.6683 | 0.90 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1938** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1677**

- Modal profit prediction correlation: **-0.0683**

- Backtests total: **24**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0444 [-0.5527, 0.3921]**

- Stock Volatility: **0.6683 [0.5831, 0.7590]**

- Based on **1937** observations


- Garch Volatility forecast: **0.9276**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 17.000000 |       3.700000 |          0.981810 |         -3.598686 |          3.423699 |   0.298863 |      0.168453 | 0.675641 | 0.024238 | -0.014957 | 0.051543 |
| 16.000000 |       4.880000 |          0.112331 |         -4.669509 |          2.769316 |   0.322549 |      0.166110 | 0.699386 | 0.023456 | -0.014521 | 0.049879 |
| 20.000000 |       3.600000 |          0.278138 |         -3.797817 |          2.064890 |   0.239618 |      0.135191 | 0.608606 | 0.025885 | -0.015852 | 0.055046 |
| 22.000000 |       2.650000 |          0.781335 |         -2.950138 |          2.226611 |   0.208106 |      0.125200 | 0.567577 | 0.026501 | -0.016166 | 0.056356 |
| 21.000000 |       4.350000 |         -0.703135 |         -4.642435 |          0.868204 |   0.223171 |      0.119048 | 0.587723 | 0.026235 | -0.016034 | 0.055791 |
| 23.000000 |       2.600000 |          0.630237 |         -2.947856 |          1.913163 |   0.194288 |      0.116942 | 0.548160 | 0.026692 | -0.016255 | 0.056761 |
| 25.000000 |       2.050000 |          0.816707 |         -2.472591 |          1.810165 |   0.169920 |      0.105605 | 0.511463 | 0.026877 | -0.016319 | 0.057155 |
| 30.000000 |       1.450000 |          0.690019 |         -1.912113 |          1.206478 |   0.123789 |      0.078648 | 0.431312 | 0.026489 | -0.015992 | 0.056329 |
| 35.000000 |       1.100000 |          0.504645 |         -1.657134 |          0.624022 |   0.092279 |      0.058839 | 0.365562 | 0.025347 | -0.015240 | 0.053900 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$17**

Market price: **$3.70**

Expected profit (USD): **0.98** [lowest: -3.60, highest: 3.42]

Delta: 0.6756 (price sensitivity)

Gamma: 0.0242 (delta sensitivity)

Theta: $-0.0150 (negative decay per trading-day)

Vega: $0.0515 (volatility sensitivity per 1%)

ITM (In The Money) probability: **29.89%**

Profit probability: **16.85%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $16 | $4.88 | $4.18 | 0.83 | 0.6683 | 0.70 |
| $17 | $3.70 | $3.79 | 0.82 | 0.6683 | -0.09 |
| $20 | $3.60 | $2.82 | 0.84 | 0.6683 | 0.78 |
| $21 | $4.35 | $2.56 | 0.85 | 0.6683 | 1.79 |
| $22 | $2.65 | $2.32 | 0.86 | 0.6683 | 0.33 |
| $23 | $2.60 | $2.11 | 0.87 | 0.6683 | 0.49 |
| $25 | $2.05 | $1.74 | 0.86 | 0.6683 | 0.31 |
| $30 | $1.45 | $1.09 | 0.97 | 0.6683 | 0.36 |
| $35 | $1.10 | $0.70 | 1.02 | 0.6683 | 0.40 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1938** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1677**

- Modal profit prediction correlation: **-0.0683**

- Backtests total: **24**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

