# SIFY Option Analysis From: 04.01.2026 18:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $12.289999961853027

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1398 [-0.3598, 0.2545]**

- Stock Volatility: **0.7941 [0.7026, 0.8888]**

- Based on **6469** observations


- Garch Volatility forecast: **0.6689**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       3.900000 |          5.465236 |          5.087834 |          5.416678 |   1.000000 |      0.999993 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |
|  5.000000 |       6.800000 |          0.065236 |         -0.387973 |         -0.059129 |   1.000000 |      0.448212 | 1.000000 | 0.000000 | -0.000990 | 0.000000 |
|  7.500000 |       4.400000 |         -0.034748 |         -0.440362 |         -0.110731 |   0.999927 |      0.423583 | 0.999951 | 0.000126 | -0.001499 | 0.000005 |
| 10.000000 |       2.800000 |         -0.904402 |         -1.217416 |         -0.871463 |   0.942426 |      0.231458 | 0.952995 | 0.061707 | -0.008957 | 0.002521 |
| 12.500000 |       0.700000 |         -0.623582 |         -0.657611 |         -0.357491 |   0.440989 |      0.167779 | 0.480335 | 0.250476 | -0.029874 | 0.010231 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.90**

Expected profit (USD): **5.47** [lowest: 5.09, highest: 5.42]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **100.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.90 | $9.80 | 6.45 | 0.7941 | -5.90 |
| $5 | $6.80 | $7.30 | 6.36 | 0.7941 | -0.50 |
| $8 | $4.40 | $4.81 | 1.25 | 0.7941 | -0.41 |
| $10 | $2.80 | $2.40 | 1.19 | 0.7941 | 0.40 |
| $12 | $0.70 | $0.73 | 1.29 | 0.7941 | -0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6470** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2683**

- Modal profit prediction correlation: **-0.1285**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **51.69%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1398 [-0.3598, 0.2545]**

- Stock Volatility: **0.7941 [0.7026, 0.8888]**

- Based on **6469** observations


- Garch Volatility forecast: **0.6689**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.500000 |       1.810000 |         -0.768583 |         -1.353120 |         -0.374501 |   0.452158 |      0.188785 | 0.548856 | 0.108111 | -0.016820 | 0.020791 |
| 15.000000 |       1.400000 |         -1.193692 |         -1.524091 |         -0.829421 |   0.232075 |      0.092524 | 0.312405 | 0.096651 | -0.014727 | 0.018587 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$1.81**

Expected profit (USD): **-0.77** [lowest: -1.35, highest: -0.37]

Delta: 0.5489 (price sensitivity)

Gamma: 0.1081 (delta sensitivity)

Theta: $-0.0168 (negative decay per trading-day)

Vega: $0.0208 (volatility sensitivity per 1%)

ITM (In The Money) probability: **45.22%**

Profit probability: **18.88%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $12 | $1.81 | $1.61 | 1.17 | 0.7941 | 0.20 |
| $15 | $1.40 | $0.82 | 1.24 | 0.7941 | 0.58 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6470** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2683**

- Modal profit prediction correlation: **-0.1285**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **51.69%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1398 [-0.3598, 0.2545]**

- Stock Volatility: **0.7941 [0.7026, 0.8888]**

- Based on **6469** observations


- Garch Volatility forecast: **0.6689**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       6.510000 |          1.024803 |         -1.553645 |          1.422529 |   0.963506 |      0.367894 | 0.985629 | 0.006302 | -0.001967 | 0.002854 |
|  7.500000 |       5.500000 |         -0.220897 |         -2.547146 |          0.267047 |   0.824461 |      0.279069 | 0.907680 | 0.028573 | -0.005870 | 0.012939 |
| 10.000000 |       3.570000 |         -0.107980 |         -2.001097 |          0.474050 |   0.626285 |      0.250357 | 0.763046 | 0.053302 | -0.009925 | 0.024138 |
| 12.500000 |       2.470000 |         -0.333442 |         -1.783549 |          0.263128 |   0.439796 |      0.190880 | 0.595849 | 0.066885 | -0.011993 | 0.030289 |
| 15.000000 |       2.250000 |         -1.022634 |         -2.033884 |         -0.411799 |   0.295158 |      0.121726 | 0.442641 | 0.068169 | -0.011994 | 0.030870 |
| 17.500000 |       2.300000 |         -1.675197 |         -2.468418 |         -1.191994 |   0.193385 |      0.073355 | 0.318682 | 0.061639 | -0.010724 | 0.027913 |
| 20.000000 |       1.070000 |         -0.837640 |         -1.387916 |         -0.399724 |   0.125309 |      0.057051 | 0.225201 | 0.051810 | -0.008947 | 0.023462 |
| 22.500000 |       0.050000 |         -0.071431 |         -0.447297 |          0.310974 |   0.080938 |      0.042639 | 0.157524 | 0.041584 | -0.007144 | 0.018831 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$6.51**

Expected profit (USD): **1.02** [lowest: -1.55, highest: 1.42]

Delta: 0.9856 (price sensitivity)

Gamma: 0.0063 (delta sensitivity)

Theta: $-0.0020 (negative decay per trading-day)

Vega: $0.0029 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.35%**

Profit probability: **36.79%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $6.51 | $7.44 | 1.40 | 0.7941 | -0.93 |
| $8 | $5.50 | $5.32 | 1.17 | 0.7941 | 0.18 |
| $10 | $3.57 | $3.66 | 1.09 | 0.7941 | -0.09 |
| $12 | $2.47 | $2.47 | 1.10 | 0.7941 | 0.00 |
| $15 | $2.25 | $1.65 | 1.02 | 0.7941 | 0.60 |
| $18 | $2.30 | $1.10 | 1.26 | 0.7941 | 1.20 |
| $20 | $1.07 | $0.74 | 1.35 | 0.7941 | 0.33 |
| $22 | $0.05 | $0.50 | 1.43 | 0.7941 | -0.45 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6470** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2683**

- Modal profit prediction correlation: **-0.1285**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **51.69%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1398 [-0.3598, 0.2545]**

- Stock Volatility: **0.7941 [0.7026, 0.8888]**

- Based on **6469** observations


- Garch Volatility forecast: **0.6689**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       6.790000 |          1.540935 |         -2.837013 |          2.580707 |   0.880244 |      0.296349 | 0.959047 | 0.010720 | -0.002684 | 0.009447 |
|  7.500000 |       5.400000 |          0.932921 |         -2.965930 |          2.030932 |   0.714997 |      0.253145 | 0.871093 | 0.025667 | -0.005437 | 0.022620 |
| 10.000000 |       4.320000 |          0.430889 |         -2.878587 |          1.562070 |   0.554305 |      0.207336 | 0.758059 | 0.038107 | -0.007608 | 0.033583 |
| 12.500000 |       3.560000 |         -0.022355 |         -2.792867 |          1.065119 |   0.421463 |      0.162998 | 0.642585 | 0.045545 | -0.008833 | 0.040138 |
| 15.000000 |       2.570000 |          0.048433 |         -2.227352 |          1.082566 |   0.318599 |      0.132833 | 0.536615 | 0.048483 | -0.009243 | 0.042727 |
| 17.500000 |       2.490000 |         -0.566488 |         -2.439623 |          0.382370 |   0.241080 |      0.096524 | 0.444605 | 0.048218 | -0.009089 | 0.042494 |
| 20.000000 |       1.800000 |         -0.403334 |         -1.934441 |          0.465798 |   0.183231 |      0.076562 | 0.367083 | 0.045960 | -0.008594 | 0.040504 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$6.79**

Expected profit (USD): **1.54** [lowest: -2.84, highest: 2.58]

Delta: 0.9590 (price sensitivity)

Gamma: 0.0107 (delta sensitivity)

Theta: $-0.0027 (negative decay per trading-day)

Vega: $0.0094 (volatility sensitivity per 1%)

ITM (In The Money) probability: **88.02%**

Profit probability: **29.63%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $6.79 | $7.69 | 1.12 | 0.7941 | -0.90 |
| $8 | $5.40 | $5.88 | 1.05 | 0.7941 | -0.48 |
| $10 | $4.32 | $4.48 | 1.14 | 0.7941 | -0.16 |
| $12 | $3.56 | $3.44 | 1.01 | 0.7941 | 0.12 |
| $15 | $2.57 | $2.65 | 0.97 | 0.7941 | -0.08 |
| $18 | $2.49 | $2.06 | 1.03 | 0.7941 | 0.43 |
| $20 | $1.80 | $1.62 | 1.10 | 0.7941 | 0.18 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6470** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2683**

- Modal profit prediction correlation: **-0.1285**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **51.69%**

--------------------------------------------------

