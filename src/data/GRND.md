# GRND Option Analysis From: 05.01.2026 02:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $13.3100004196167

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2178 [-0.5106, 0.5383]**

- Stock Volatility: **0.5861 [0.5073, 0.6715]**

- Based on **1209** observations


- Garch Volatility forecast: **0.4251**

### 2. Validate Stock Option Contracts

- Analyze **27** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  3.000000 |       9.600000 |          0.325549 |         -0.255980 |          0.298351 |   1.000000 |      0.575206 | 1.000000 | 0.000000 | -0.000594 | 0.000000 |
|  5.000000 |       8.000000 |         -0.074451 |         -0.619128 |         -0.064797 |   1.000000 |      0.421576 | 1.000000 | 0.000000 | -0.000990 | 0.000000 |
|  8.000000 |       5.070000 |         -0.144451 |         -0.622350 |         -0.068013 |   1.000000 |      0.395700 | 1.000000 | 0.000000 | -0.001584 | 0.000000 |
| 10.000000 |       3.200000 |         -0.274435 |         -0.715872 |         -0.160393 |   0.999914 |      0.349255 | 0.999911 | 0.000344 | -0.001998 | 0.000009 |
| 12.000000 |       1.530000 |         -0.571867 |         -0.865214 |         -0.339669 |   0.920348 |      0.243845 | 0.919129 | 0.145087 | -0.009897 | 0.003974 |
| 13.000000 |       0.650000 |         -0.493492 |         -0.582736 |         -0.148203 |   0.646607 |      0.210781 | 0.643560 | 0.360882 | -0.020839 | 0.009885 |
| 11.000000 |       3.140000 |         -1.212920 |         -1.647690 |         -1.093617 |   0.994271 |      0.107061 | 0.994137 | 0.016126 | -0.003023 | 0.000442 |
| 14.000000 |       0.180000 |         -0.482369 |         -0.462062 |         -0.161208 |   0.281428 |      0.100719 | 0.278673 | 0.325089 | -0.018050 | 0.008905 |
|  9.000000 |       7.100000 |         -3.174451 |         -3.685103 |         -3.130617 |   1.000000 |      0.002111 | 1.000000 | 0.000001 | -0.001782 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$9.60**

Expected profit (USD): **0.33** [lowest: -0.26, highest: 0.30]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **57.52%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $9.60 | $10.32 | 5.25 | 0.5861 | -0.72 |
| $5 | $8.00 | $8.32 | 5.93 | 0.5861 | -0.32 |
| $8 | $5.07 | $5.33 | 0.00 | 0.5861 | -0.26 |
| $9 | $7.10 | $4.33 | 0.00 | 0.5861 | 2.77 |
| $10 | $3.20 | $3.33 | 1.61 | 0.5861 | -0.13 |
| $11 | $3.14 | $2.36 | 2.47 | 0.5861 | 0.78 |
| $12 | $1.53 | $1.48 | 1.47 | 0.5861 | 0.05 |
| $13 | $0.65 | $0.79 | 0.50 | 0.5861 | -0.14 |
| $14 | $0.18 | $0.36 | 0.47 | 0.5861 | -0.18 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1210** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1398**

- Modal profit prediction correlation: **0.2296**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **57.14%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2178 [-0.5106, 0.5383]**

- Stock Volatility: **0.5861 [0.5073, 0.6715]**

- Based on **1209** observations


- Garch Volatility forecast: **0.4251**

### 2. Validate Stock Option Contracts

- Analyze **18** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  9.000000 |       4.200000 |          0.145630 |         -1.537658 |          0.903987 |   0.986200 |      0.419213 | 0.987134 | 0.013307 | -0.002653 | 0.001866 |
| 11.000000 |       2.470000 |         -0.009366 |         -1.306490 |          0.875676 |   0.871105 |      0.379005 | 0.876763 | 0.081750 | -0.007451 | 0.011464 |
| 10.000000 |       3.800000 |         -0.425130 |         -1.988986 |          0.356285 |   0.949544 |      0.332603 | 0.952320 | 0.039826 | -0.004581 | 0.005585 |
| 12.000000 |       1.980000 |         -0.332103 |         -1.358487 |          0.597327 |   0.747651 |      0.308708 | 0.756298 | 0.125729 | -0.010321 | 0.017631 |
| 13.000000 |       1.120000 |         -0.144738 |         -0.876603 |          0.809566 |   0.594760 |      0.290857 | 0.605317 | 0.154404 | -0.012024 | 0.021652 |
| 14.000000 |       0.600000 |         -0.140407 |         -0.630840 |          0.769969 |   0.438087 |      0.234735 | 0.448879 | 0.158697 | -0.011996 | 0.022254 |
| 15.000000 |       0.320000 |         -0.227268 |         -0.533323 |          0.592136 |   0.300090 |      0.165523 | 0.309660 | 0.141435 | -0.010497 | 0.019833 |
| 16.000000 |       0.180000 |         -0.330848 |         -0.509003 |          0.369319 |   0.192510 |      0.104811 | 0.200074 | 0.112316 | -0.008235 | 0.015750 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$9**

Market price: **$4.20**

Expected profit (USD): **0.15** [lowest: -1.54, highest: 0.90]

Delta: 0.9871 (price sensitivity)

Gamma: 0.0133 (delta sensitivity)

Theta: $-0.0027 (negative decay per trading-day)

Vega: $0.0019 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.62%**

Profit probability: **41.92%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $9 | $4.20 | $4.45 | 0.90 | 0.5861 | -0.25 |
| $10 | $3.80 | $3.56 | 1.74 | 0.5861 | 0.24 |
| $11 | $2.47 | $2.76 | 0.78 | 0.5861 | -0.29 |
| $12 | $1.98 | $2.08 | 0.80 | 0.5861 | -0.10 |
| $13 | $1.12 | $1.51 | 0.50 | 0.5861 | -0.39 |
| $14 | $0.60 | $1.08 | 0.49 | 0.5861 | -0.48 |
| $15 | $0.32 | $0.75 | 0.51 | 0.5861 | -0.43 |
| $16 | $0.18 | $0.51 | 0.53 | 0.5861 | -0.33 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1210** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1398**

- Modal profit prediction correlation: **0.2296**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **57.14%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2178 [-0.5106, 0.5383]**

- Stock Volatility: **0.5861 [0.5073, 0.6715]**

- Based on **1209** observations


- Garch Volatility forecast: **0.4251**

### 2. Validate Stock Option Contracts

- Analyze **16** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 10.000000 |       4.000000 |          0.632344 |         -2.939141 |          3.234188 |   0.838440 |      0.362272 | 0.859977 | 0.048791 | -0.005425 | 0.021198 |
|  9.000000 |       5.000000 |          0.504072 |         -3.454514 |          3.083744 |   0.902416 |      0.362272 | 0.917369 | 0.033391 | -0.004177 | 0.014507 |
| 12.000000 |       2.700000 |          0.412706 |         -2.287588 |          3.024367 |   0.675868 |      0.312090 | 0.708264 | 0.075237 | -0.007419 | 0.032689 |
| 13.000000 |       1.900000 |          0.580729 |         -1.709974 |          3.144245 |   0.588101 |      0.298725 | 0.623547 | 0.083214 | -0.007943 | 0.036154 |
| 14.000000 |       1.400000 |          0.535742 |         -1.387524 |          3.012656 |   0.502579 |      0.267206 | 0.539277 | 0.087018 | -0.008113 | 0.037807 |
| 15.000000 |       1.250000 |          0.223652 |         -1.371922 |          2.589700 |   0.422770 |      0.219697 | 0.459115 | 0.086982 | -0.007969 | 0.037791 |
| 16.000000 |       0.660000 |          0.427567 |         -0.873634 |          2.673120 |   0.350826 |      0.199400 | 0.385547 | 0.083818 | -0.007577 | 0.036417 |
| 17.000000 |       0.510000 |          0.259032 |         -0.797637 |          2.363058 |   0.287755 |      0.162359 | 0.319961 | 0.078379 | -0.007010 | 0.034053 |
| 18.000000 |       0.300000 |          0.209043 |         -0.640230 |          2.165875 |   0.233704 |      0.133489 | 0.262859 | 0.071496 | -0.006340 | 0.031063 |
| 19.000000 |       0.200000 |          0.098762 |         -0.580951 |          1.902841 |   0.188230 |      0.106296 | 0.214096 | 0.063887 | -0.005625 | 0.027757 |
| 20.000000 |       0.280000 |         -0.150017 |         -0.694726 |          1.498520 |   0.150550 |      0.080432 | 0.173114 | 0.056112 | -0.004912 | 0.024379 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$4.00**

Expected profit (USD): **0.63** [lowest: -2.94, highest: 3.23]

Delta: 0.8600 (price sensitivity)

Gamma: 0.0488 (delta sensitivity)

Theta: $-0.0054 (negative decay per trading-day)

Vega: $0.0212 (volatility sensitivity per 1%)

ITM (In The Money) probability: **83.84%**

Profit probability: **36.23%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $9 | $5.00 | $4.91 | 1.15 | 0.5861 | 0.09 |
| $10 | $4.00 | $4.19 | 1.00 | 0.5861 | -0.19 |
| $12 | $2.70 | $2.98 | 0.55 | 0.5861 | -0.28 |
| $13 | $1.90 | $2.49 | 0.52 | 0.5861 | -0.59 |
| $14 | $1.40 | $2.07 | 0.52 | 0.5861 | -0.67 |
| $15 | $1.25 | $1.72 | 0.52 | 0.5861 | -0.47 |
| $16 | $0.66 | $1.42 | 0.51 | 0.5861 | -0.76 |
| $17 | $0.51 | $1.18 | 0.51 | 0.5861 | -0.67 |
| $18 | $0.30 | $0.97 | 0.52 | 0.5861 | -0.67 |
| $19 | $0.20 | $0.80 | 0.53 | 0.5861 | -0.60 |
| $20 | $0.28 | $0.66 | 0.53 | 0.5861 | -0.38 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1210** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1398**

- Modal profit prediction correlation: **0.2296**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **57.14%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2178 [-0.5106, 0.5383]**

- Stock Volatility: **0.5861 [0.5073, 0.6715]**

- Based on **1209** observations


- Garch Volatility forecast: **0.4251**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 10.000000 |       4.400000 |          1.745410 |         -3.832469 |          7.039313 |   0.789830 |      0.349815 | 0.827623 | 0.041299 | -0.004775 | 0.032252 |
| 13.000000 |       2.400000 |          1.666458 |         -2.373932 |          6.772844 |   0.595207 |      0.299557 | 0.648006 | 0.060039 | -0.006204 | 0.046887 |
| 14.000000 |       1.810000 |          1.692888 |         -1.890962 |          6.690209 |   0.532440 |      0.280792 | 0.587215 | 0.062984 | -0.006374 | 0.049187 |
| 15.000000 |       1.600000 |          1.400386 |         -1.770880 |          6.262436 |   0.473236 |      0.247516 | 0.528638 | 0.064366 | -0.006406 | 0.050267 |
| 20.000000 |       0.500000 |          0.750888 |         -0.888193 |          4.779515 |   0.246193 |      0.130369 | 0.292005 | 0.055549 | -0.005267 | 0.043381 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$4.40**

Expected profit (USD): **1.75** [lowest: -3.83, highest: 7.04]

Delta: 0.8276 (price sensitivity)

Gamma: 0.0413 (delta sensitivity)

Theta: $-0.0048 (negative decay per trading-day)

Vega: $0.0323 (volatility sensitivity per 1%)

ITM (In The Money) probability: **78.98%**

Profit probability: **34.98%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $10 | $4.40 | $4.80 | 0.54 | 0.5861 | -0.40 |
| $13 | $2.40 | $3.28 | 0.54 | 0.5861 | -0.88 |
| $14 | $1.81 | $2.89 | 0.52 | 0.5861 | -1.08 |
| $15 | $1.60 | $2.54 | 0.51 | 0.5861 | -0.94 |
| $20 | $0.50 | $1.35 | 0.52 | 0.5861 | -0.85 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1210** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1398**

- Modal profit prediction correlation: **0.2296**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **57.14%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2178 [-0.5106, 0.5383]**

- Stock Volatility: **0.5861 [0.5073, 0.6715]**

- Based on **1209** observations


- Garch Volatility forecast: **0.4251**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       8.000000 |          4.920209 |         -6.570978 |         15.910379 |   0.968543 |      0.416306 | 0.979775 | 0.006094 | -0.001377 | 0.007926 |
| 10.000000 |       4.500000 |          4.037679 |         -4.427851 |         14.937276 |   0.761023 |      0.349680 | 0.815653 | 0.033206 | -0.003992 | 0.043187 |
|  8.000000 |       7.000000 |          3.160349 |         -6.607291 |         14.125988 |   0.859902 |      0.329753 | 0.897816 | 0.022227 | -0.003013 | 0.028909 |
| 12.000000 |       3.480000 |          3.638882 |         -3.584293 |         14.390527 |   0.658017 |      0.311641 | 0.724540 | 0.041634 | -0.004681 | 0.054149 |
| 15.000000 |       2.660000 |          2.704933 |         -2.963707 |         13.010946 |   0.514668 |      0.240900 | 0.589438 | 0.048482 | -0.005146 | 0.063055 |
| 17.000000 |       1.570000 |          2.850034 |         -1.919046 |         12.818346 |   0.432145 |      0.216360 | 0.507343 | 0.049728 | -0.005153 | 0.064677 |
| 20.000000 |       0.800000 |          2.483456 |         -1.205925 |         11.842487 |   0.329752 |      0.166508 | 0.400801 | 0.048191 | -0.004869 | 0.062678 |
| 22.000000 |       0.750000 |          1.930665 |         -1.189262 |         10.844605 |   0.274668 |      0.132765 | 0.341112 | 0.045738 | -0.004565 | 0.059487 |
| 25.000000 |       0.400000 |          1.560153 |         -0.858810 |          9.810677 |   0.208718 |      0.098087 | 0.267117 | 0.041000 | -0.004035 | 0.053325 |
| 30.000000 |       0.200000 |          0.921382 |         -0.721883 |          8.045588 |   0.132764 |      0.057668 | 0.177718 | 0.032452 | -0.003142 | 0.042208 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$8.00**

Expected profit (USD): **4.92** [lowest: -6.57, highest: 15.91]

Delta: 0.9798 (price sensitivity)

Gamma: 0.0061 (delta sensitivity)

Theta: $-0.0014 (negative decay per trading-day)

Vega: $0.0079 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.85%**

Profit probability: **41.63%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $8.00 | $8.83 | 0.79 | 0.5861 | -0.83 |
| $8 | $7.00 | $6.68 | 0.51 | 0.5861 | 0.32 |
| $10 | $4.50 | $5.53 | 0.63 | 0.5861 | -1.03 |
| $12 | $3.48 | $4.59 | 0.53 | 0.5861 | -1.11 |
| $15 | $2.66 | $3.50 | 0.57 | 0.5861 | -0.84 |
| $17 | $1.57 | $2.93 | 0.50 | 0.5861 | -1.36 |
| $20 | $0.80 | $2.27 | 0.48 | 0.5861 | -1.47 |
| $22 | $0.75 | $1.92 | 0.54 | 0.5861 | -1.17 |
| $25 | $0.40 | $1.51 | 0.51 | 0.5861 | -1.11 |
| $30 | $0.20 | $1.03 | 0.81 | 0.5861 | -0.83 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1210** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1398**

- Modal profit prediction correlation: **0.2296**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **57.14%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.2178 [-0.5106, 0.5383]**

- Stock Volatility: **0.5861 [0.5073, 0.6715]**

- Based on **1209** observations


- Garch Volatility forecast: **0.4251**

### 2. Validate Stock Option Contracts

- Analyze **10** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  3.000000 |      10.900000 |         10.956935 |        -10.615879 |         50.717882 |   0.980291 |      0.358802 | 0.990323 | 0.002269 | -0.000676 | 0.005927 |
|  5.000000 |      10.000000 |          9.943805 |        -10.154066 |         49.667248 |   0.928412 |      0.327254 | 0.959327 | 0.007653 | -0.001364 | 0.019990 |
| 10.000000 |       6.000000 |          9.752415 |         -6.466901 |         49.135733 |   0.743995 |      0.301385 | 0.824998 | 0.022586 | -0.002883 | 0.058993 |
| 13.000000 |       4.000000 |          9.684252 |         -4.503131 |         48.631828 |   0.636734 |      0.277917 | 0.735198 | 0.028688 | -0.003419 | 0.074931 |
| 15.000000 |       4.250000 |          8.226030 |         -4.797322 |         46.760972 |   0.572545 |      0.232666 | 0.677861 | 0.031420 | -0.003635 | 0.082068 |
| 17.000000 |       3.050000 |          8.339823 |         -3.576682 |         46.465161 |   0.514714 |      0.218756 | 0.623907 | 0.033255 | -0.003763 | 0.086859 |
| 22.000000 |       1.700000 |          7.427554 |         -2.248216 |         44.267122 |   0.395971 |      0.166755 | 0.506015 | 0.034951 | -0.003808 | 0.091289 |
| 25.000000 |       1.200000 |          6.826323 |         -1.706413 |         42.866482 |   0.339851 |      0.139689 | 0.446701 | 0.034642 | -0.003716 | 0.090483 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$10.90**

Expected profit (USD): **10.96** [lowest: -10.62, highest: 50.72]

Delta: 0.9903 (price sensitivity)

Gamma: 0.0023 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0059 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.03%**

Profit probability: **35.88%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $10.90 | $10.84 | 0.61 | 0.5861 | 0.06 |
| $5 | $10.00 | $9.46 | 0.51 | 0.5861 | 0.54 |
| $10 | $6.00 | $6.92 | 0.55 | 0.5861 | -0.92 |
| $13 | $4.00 | $5.84 | 0.57 | 0.5861 | -1.84 |
| $15 | $4.25 | $5.25 | 0.73 | 0.5861 | -1.00 |
| $17 | $3.05 | $4.74 | 0.62 | 0.5861 | -1.69 |
| $22 | $1.70 | $3.74 | 0.51 | 0.5861 | -2.04 |
| $25 | $1.20 | $3.28 | 0.49 | 0.5861 | -2.08 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1210** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1398**

- Modal profit prediction correlation: **0.2296**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **57.14%**

--------------------------------------------------

