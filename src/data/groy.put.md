# Put Option. GROY Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

## Current Stock Price: $4.079999923706055

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 4.000000 |       0.200000 |         -0.595961 |         -0.609847 |         -0.513777 |   0.404963 |      0.013560 | 0.609364 | 0.994842 | -0.007859 | 0.003120 |
| 3.500000 |       0.600000 |         -1.093442 |         -1.110144 |         -1.085310 |   0.049216 |      0.000000 | 0.954452 | 0.248064 | -0.002501 | 0.000778 |
| 2.500000 |       1.510000 |         -2.010000 |         -2.041375 |         -2.041368 |   0.000000 |      0.000000 | 1.000000 | 0.000001 | -0.000495 | 0.000000 |
| 2.000000 |       2.000000 |         -2.500000 |         -2.537954 |         -2.537954 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000396 | 0.000000 |
| 1.500000 |       2.650000 |         -3.150000 |         -3.204823 |         -3.204823 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |
| 0.500000 |       3.000000 |         -3.500000 |         -3.564100 |         -3.564100 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |
| 1.000000 |       3.000000 |         -3.500000 |         -3.567474 |         -3.567474 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$4**

Market price: **$0.20**

Expected profit (USD): **-0.60** [lowest: -0.61, highest: -0.51]

Delta: 0.6094 (price sensitivity)

Gamma: 0.9948 (delta sensitivity)

Theta: $-0.0079 (negative decay per trading-day)

Vega: $0.0031 (volatility sensitivity per 1%)

ITM (In The Money) probability: **40.50%**

Profit probability: **1.36%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.00 | $3.58 | 6.38 | 0.5562 | -0.58 |
| $1 | $3.00 | $3.08 | 4.25 | 0.5562 | -0.08 |
| $2 | $2.65 | $2.58 | 5.30 | 0.5562 | 0.07 |
| $2 | $2.00 | $2.08 | 3.03 | 0.5562 | -0.08 |
| $2 | $1.51 | $1.58 | 2.23 | 0.5562 | -0.07 |
| $4 | $0.60 | $0.60 | 1.22 | 0.5562 | -0.00 |
| $4 | $0.20 | $0.23 | 0.54 | 0.5562 | -0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       0.100000 |          0.303625 |          0.124602 |          0.727499 |   0.814292 |      0.666628 | 0.214633 | 0.330695 | -0.003017 | 0.005033 |
| 4.500000 |       0.250000 |         -0.217161 |         -0.352694 |          0.148391 |   0.657931 |      0.378951 | 0.380775 | 0.431626 | -0.004004 | 0.006569 |
| 4.000000 |       0.450000 |         -0.694655 |         -0.783329 |         -0.423527 |   0.445279 |      0.103248 | 0.595213 | 0.439028 | -0.004202 | 0.006681 |
| 3.000000 |       1.120000 |         -1.601134 |         -1.640775 |         -1.558626 |   0.071143 |      0.000000 | 0.941875 | 0.131635 | -0.001678 | 0.002003 |
| 2.500000 |       1.750000 |         -2.248200 |         -2.288478 |         -2.269569 |   0.010442 |      0.000000 | 0.992099 | 0.024563 | -0.000697 | 0.000374 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$5**

Market price: **$0.10**

Expected profit (USD): **0.30** [lowest: 0.12, highest: 0.73]

Delta: 0.2146 (price sensitivity)

Gamma: 0.3307 (delta sensitivity)

Theta: $-0.0030 (negative decay per trading-day)

Vega: $0.0050 (volatility sensitivity per 1%)

ITM (In The Money) probability: **81.43%**

Profit probability: **66.66%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.75 | $1.61 | 1.52 | 0.5562 | 0.14 |
| $3 | $1.12 | $1.14 | 0.56 | 0.5562 | -0.02 |
| $4 | $0.45 | $0.44 | 0.66 | 0.5562 | 0.01 |
| $4 | $0.25 | $0.24 | 0.65 | 0.5562 | 0.01 |
| $5 | $0.10 | $0.12 | 0.63 | 0.5562 | -0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **10** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.500000 |       0.100000 |          2.549224 |          1.997273 |          3.553651 |   0.959991 |      0.954220 | 0.057562 | 0.083730 | -0.000827 | 0.002978 |
| 6.000000 |       0.160000 |          1.108836 |          0.651360 |          2.028318 |   0.862028 |      0.823269 | 0.180236 | 0.190699 | -0.001913 | 0.006783 |
| 5.000000 |       0.200000 |          0.275604 |         -0.064119 |          1.057066 |   0.708604 |      0.612616 | 0.354090 | 0.270094 | -0.002767 | 0.009607 |
| 4.500000 |       0.500000 |         -0.351071 |         -0.627285 |          0.312396 |   0.593734 |      0.373069 | 0.475221 | 0.289134 | -0.003016 | 0.010285 |
| 4.000000 |       0.580000 |         -0.694183 |         -0.886400 |         -0.158533 |   0.455493 |      0.194752 | 0.612869 | 0.278020 | -0.002983 | 0.009889 |
| 3.500000 |       0.850000 |         -1.154614 |         -1.286574 |         -0.783654 |   0.305934 |      0.038577 | 0.752513 | 0.229516 | -0.002587 | 0.008164 |
| 3.000000 |       1.400000 |         -1.821941 |         -1.908092 |         -1.614485 |   0.167495 |      0.000087 | 0.872674 | 0.151415 | -0.001882 | 0.005386 |
| 2.500000 |       1.660000 |         -2.138382 |         -2.188844 |         -2.056216 |   0.066255 |      0.000000 | 0.953452 | 0.070726 | -0.001107 | 0.002516 |
| 1.000000 |       3.300000 |         -3.799999 |         -3.878814 |         -3.878629 |   0.000012 |      0.000000 | 0.999994 | 0.000019 | -0.000195 | 0.000001 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$0.10**

Expected profit (USD): **2.55** [lowest: 2.00, highest: 3.55]

Delta: 0.0576 (price sensitivity)

Gamma: 0.0837 (delta sensitivity)

Theta: $-0.0008 (negative decay per trading-day)

Vega: $0.0030 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.00%**

Profit probability: **95.42%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $3.30 | $3.10 | 1.45 | 0.5562 | 0.20 |
| $2 | $1.66 | $1.67 | 0.76 | 0.5562 | -0.01 |
| $3 | $1.40 | $1.25 | 0.79 | 0.5562 | 0.15 |
| $4 | $0.85 | $0.91 | 0.60 | 0.5562 | -0.06 |
| $4 | $0.58 | $0.64 | 0.54 | 0.5562 | -0.06 |
| $4 | $0.50 | $0.44 | 0.94 | 0.5562 | 0.06 |
| $5 | $0.20 | $0.30 | 0.69 | 0.5562 | -0.10 |
| $6 | $0.16 | $0.13 | 0.71 | 0.5562 | 0.03 |
| $8 | $0.10 | $0.04 | 0.85 | 0.5562 | 0.06 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.250000 |          1.846754 |          0.945875 |          3.459802 |   0.858785 |      0.860909 | 0.206057 | 0.147219 | -0.001567 | 0.010150 |
| 5.500000 |       0.330000 |          0.575003 |         -0.066989 |          1.935730 |   0.714509 |      0.680898 | 0.377556 | 0.196296 | -0.002142 | 0.013533 |
| 5.000000 |       0.650000 |         -0.084869 |         -0.618738 |          1.155257 |   0.642717 |      0.525223 | 0.455795 | 0.204814 | -0.002265 | 0.014120 |
| 4.500000 |       0.720000 |         -0.455405 |         -0.878446 |          0.638129 |   0.557121 |      0.391876 | 0.544201 | 0.204814 | -0.002307 | 0.014120 |
| 4.000000 |       0.850000 |         -0.839781 |         -1.166161 |          0.069543 |   0.458360 |      0.234549 | 0.640301 | 0.193201 | -0.002232 | 0.013320 |
| 3.500000 |       1.050000 |         -1.242102 |         -1.466632 |         -0.524559 |   0.349750 |      0.085280 | 0.739139 | 0.167842 | -0.002016 | 0.011571 |
| 3.000000 |       1.350000 |         -1.689077 |         -1.839605 |         -1.186503 |   0.238579 |      0.006508 | 0.832872 | 0.129295 | -0.001656 | 0.008914 |
| 2.500000 |       1.850000 |         -2.282216 |         -2.385192 |         -1.992373 |   0.136728 |      0.000000 | 0.911466 | 0.082867 | -0.001195 | 0.005713 |
| 2.000000 |       2.250000 |         -2.729802 |         -2.805622 |         -2.617246 |   0.058740 |      0.000000 | 0.965631 | 0.039324 | -0.000732 | 0.002711 |
| 1.000000 |       3.300000 |         -3.799853 |         -3.879924 |         -3.871386 |   0.001238 |      0.000000 | 0.999483 | 0.000947 | -0.000200 | 0.000065 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$0.25**

Expected profit (USD): **1.85** [lowest: 0.95, highest: 3.46]

Delta: 0.2061 (price sensitivity)

Gamma: 0.1472 (delta sensitivity)

Theta: $-0.0016 (negative decay per trading-day)

Vega: $0.0101 (volatility sensitivity per 1%)

ITM (In The Money) probability: **85.88%**

Profit probability: **86.09%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $3.30 | $3.12 | 1.06 | 0.5562 | 0.18 |
| $2 | $2.25 | $2.19 | 0.67 | 0.5562 | 0.06 |
| $2 | $1.85 | $1.78 | 0.70 | 0.5562 | 0.07 |
| $3 | $1.35 | $1.42 | 0.82 | 0.5562 | -0.07 |
| $4 | $1.05 | $1.12 | 0.62 | 0.5562 | -0.07 |
| $4 | $0.85 | $0.88 | 0.81 | 0.5562 | -0.03 |
| $4 | $0.72 | $0.69 | 0.73 | 0.5562 | 0.03 |
| $5 | $0.65 | $0.53 | 0.68 | 0.5562 | 0.12 |
| $6 | $0.33 | $0.41 | 0.76 | 0.5562 | -0.08 |
| $7 | $0.25 | $0.20 | 0.88 | 0.5562 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.650000 |          1.398643 |          0.011166 |          3.887881 |   0.766334 |      0.788635 | 0.358991 | 0.136888 | -0.001560 | 0.018577 |
| 5.500000 |       0.850000 |          0.134911 |         -0.814082 |          2.225432 |   0.642988 |      0.613574 | 0.499686 | 0.146114 | -0.001711 | 0.019829 |
| 5.000000 |       0.900000 |         -0.223305 |         -1.010938 |          1.706455 |   0.588635 |      0.530368 | 0.556316 | 0.144655 | -0.001717 | 0.019631 |
| 4.500000 |       1.000000 |         -0.602433 |         -1.235401 |          1.140019 |   0.526547 |      0.422207 | 0.617559 | 0.139723 | -0.001687 | 0.018962 |
| 4.000000 |       1.150000 |         -0.998512 |         -1.499884 |          0.516772 |   0.456438 |      0.287345 | 0.682635 | 0.130521 | -0.001613 | 0.017713 |
| 3.500000 |       1.400000 |         -1.457589 |         -1.832112 |         -0.185722 |   0.378680 |      0.128065 | 0.750041 | 0.116376 | -0.001484 | 0.015794 |
| 3.000000 |       1.700000 |         -1.926168 |         -2.189953 |         -0.916924 |   0.294841 |      0.014952 | 0.817259 | 0.097018 | -0.001295 | 0.013166 |
| 2.500000 |       2.050000 |         -2.401992 |         -2.581564 |         -1.672266 |   0.208470 |      0.000000 | 0.880484 | 0.073057 | -0.001048 | 0.009915 |
| 2.000000 |       2.150000 |         -2.585278 |         -2.700312 |         -2.126619 |   0.126066 |      0.000000 | 0.934588 | 0.046667 | -0.000760 | 0.006333 |
| 1.500000 |       2.730000 |         -3.210371 |         -3.296096 |         -3.004275 |   0.057620 |      0.000000 | 0.973855 | 0.022223 | -0.000470 | 0.003016 |
| 1.000000 |       2.850000 |         -3.347170 |         -3.421946 |         -3.326590 |   0.014593 |      0.000000 | 0.994562 | 0.005707 | -0.000236 | 0.000775 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$0.65**

Expected profit (USD): **1.40** [lowest: 0.01, highest: 3.89]

Delta: 0.3590 (price sensitivity)

Gamma: 0.1369 (delta sensitivity)

Theta: $-0.0016 (negative decay per trading-day)

Vega: $0.0186 (volatility sensitivity per 1%)

ITM (In The Money) probability: **76.63%**

Profit probability: **78.86%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $2.85 | $3.16 | 1.93 | 0.5562 | -0.31 |
| $2 | $2.73 | $2.72 | 0.73 | 0.5562 | 0.01 |
| $2 | $2.15 | $2.33 | 0.98 | 0.5562 | -0.18 |
| $2 | $2.05 | $1.99 | 0.90 | 0.5562 | 0.06 |
| $3 | $1.70 | $1.69 | 0.75 | 0.5562 | 0.01 |
| $4 | $1.40 | $1.44 | 0.74 | 0.5562 | -0.04 |
| $4 | $1.15 | $1.23 | 0.84 | 0.5562 | -0.08 |
| $4 | $1.00 | $1.05 | 0.67 | 0.5562 | -0.05 |
| $5 | $0.90 | $0.90 | 0.76 | 0.5562 | 0.00 |
| $6 | $0.85 | $0.77 | 0.83 | 0.5562 | 0.08 |
| $7 | $0.65 | $0.49 | 0.75 | 0.5562 | 0.16 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       1.000000 |          1.027573 |         -0.866127 |          4.539037 |   0.677788 |      0.754625 | 0.524735 | 0.102767 | -0.001260 | 0.027933 |
| 5.500000 |       1.270000 |         -0.191325 |         -1.481388 |          2.765588 |   0.582219 |      0.610332 | 0.623995 | 0.097950 | -0.001235 | 0.026624 |
| 5.000000 |       1.400000 |         -0.602735 |         -1.695975 |          2.141058 |   0.542689 |      0.534016 | 0.661425 | 0.094416 | -0.001205 | 0.025663 |
| 4.500000 |       1.420000 |         -0.883238 |         -1.781610 |          1.634460 |   0.498509 |      0.457006 | 0.701008 | 0.089601 | -0.001162 | 0.024354 |
| 4.000000 |       2.000000 |         -1.700383 |         -2.432524 |          0.552688 |   0.449167 |      0.248550 | 0.742584 | 0.083285 | -0.001101 | 0.022637 |
| 3.500000 |       1.750000 |         -1.661468 |         -2.208701 |          0.337506 |   0.394204 |      0.191864 | 0.785803 | 0.075249 | -0.001020 | 0.020453 |
| 3.000000 |       2.160000 |         -2.253602 |         -2.671338 |         -0.569602 |   0.333342 |      0.012479 | 0.830026 | 0.065305 | -0.000916 | 0.017750 |
| 2.000000 |       2.400000 |         -2.759567 |         -2.953272 |         -1.737718 |   0.195538 |      0.000000 | 0.916396 | 0.039666 | -0.000628 | 0.010781 |
| 1.500000 |       2.800000 |         -3.239127 |         -3.368058 |         -2.576091 |   0.122902 |      0.000000 | 0.953925 | 0.024933 | -0.000449 | 0.006777 |
| 1.000000 |       3.190000 |         -3.673414 |         -3.768198 |         -3.361368 |   0.056192 |      0.000000 | 0.982620 | 0.011089 | -0.000262 | 0.003014 |
| 0.500000 |       3.500000 |         -3.998732 |         -4.084612 |         -3.977190 |   0.010239 |      0.000000 | 0.997752 | 0.001820 | -0.000101 | 0.000495 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$1.00**

Expected profit (USD): **1.03** [lowest: -0.87, highest: 4.54]

Delta: 0.5247 (price sensitivity)

Gamma: 0.1028 (delta sensitivity)

Theta: $-0.0013 (negative decay per trading-day)

Vega: $0.0279 (volatility sensitivity per 1%)

ITM (In The Money) probability: **67.78%**

Profit probability: **75.46%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.50 | $3.65 | 1.27 | 0.5562 | -0.15 |
| $1 | $3.19 | $3.25 | 1.02 | 0.5562 | -0.06 |
| $2 | $2.80 | $2.90 | 0.86 | 0.5562 | -0.10 |
| $2 | $2.40 | $2.59 | 0.74 | 0.5562 | -0.19 |
| $3 | $2.16 | $2.09 | 0.83 | 0.5562 | 0.07 |
| $4 | $1.75 | $1.89 | 0.75 | 0.5562 | -0.14 |
| $4 | $2.00 | $1.72 | 0.73 | 0.5562 | 0.28 |
| $4 | $1.42 | $1.56 | 0.68 | 0.5562 | -0.14 |
| $5 | $1.40 | $1.43 | 0.65 | 0.5562 | -0.03 |
| $6 | $1.27 | $1.31 | 0.66 | 0.5562 | -0.04 |
| $7 | $1.00 | $1.02 | 0.72 | 0.5562 | -0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

