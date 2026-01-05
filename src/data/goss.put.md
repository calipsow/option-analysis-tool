# Put Option. GOSS Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

## Current Stock Price: $2.880000114440918

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1212 [-0.7372, 0.5777]**

- Stock Volatility: **0.8799 [0.7664, 1.0012]**

- Based on **1734** observations


- Garch Volatility forecast: **0.8966**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       0.170000 |         -0.403073 |         -0.459378 |         -0.343376 |   0.614460 |      0.149504 | 0.448977 | 0.769469 | -0.010399 | 0.002270 |
| 2.000000 |       1.000000 |         -1.496986 |         -1.533490 |         -1.526479 |   0.023855 |      0.000000 | 0.983930 | 0.078135 | -0.001419 | 0.000231 |
| 1.500000 |       1.900000 |         -2.399990 |         -2.472630 |         -2.472549 |   0.000165 |      0.000000 | 0.999913 | 0.000676 | -0.000306 | 0.000002 |
| 1.000000 |       1.900000 |         -2.400000 |         -2.457556 |         -2.457556 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 0.500000 |       3.030000 |         -3.530000 |         -3.634971 |         -3.634971 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$3**

Market price: **$0.17**

Expected profit (USD): **-0.40** [lowest: -0.46, highest: -0.34]

Delta: 0.4490 (price sensitivity)

Gamma: 0.7695 (delta sensitivity)

Theta: $-0.0104 (negative decay per trading-day)

Vega: $0.0023 (volatility sensitivity per 1%)

ITM (In The Money) probability: **61.45%**

Profit probability: **14.95%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.03 | $2.38 | 11.94 | 0.8799 | 0.65 |
| $1 | $1.90 | $1.88 | 4.69 | 0.8799 | 0.02 |
| $2 | $1.90 | $1.38 | 4.50 | 0.8799 | 0.52 |
| $2 | $1.00 | $0.89 | 1.72 | 0.8799 | 0.11 |
| $3 | $0.17 | $0.15 | 1.09 | 0.8799 | 0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1735** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1875**

- Modal profit prediction correlation: **0.1834**

- Backtests total: **21**

- Profitable Trades (profitable trades / total trades): **33.33%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1212 [-0.7372, 0.5777]**

- Stock Volatility: **0.8799 [0.7664, 1.0012]**

- Based on **1734** observations


- Garch Volatility forecast: **0.8966**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.490000 |          3.073424 |          2.800674 |          3.465519 |   0.993359 |      0.987969 | 0.016554 | 0.037764 | -0.000508 | 0.000502 |
| 6.000000 |       0.540000 |          2.035260 |          1.762712 |          2.420022 |   0.980742 |      0.959887 | 0.042357 | 0.082717 | -0.001115 | 0.001099 |
| 5.000000 |       0.860000 |          0.749750 |          0.470087 |          1.103225 |   0.943875 |      0.824536 | 0.106970 | 0.168876 | -0.002286 | 0.002243 |
| 4.000000 |       0.930000 |         -0.221053 |         -0.469546 |          0.091649 |   0.841168 |      0.505663 | 0.256583 | 0.295198 | -0.004025 | 0.003921 |
| 3.000000 |       1.300000 |         -1.324423 |         -1.517265 |         -1.131788 |   0.594858 |      0.022985 | 0.541928 | 0.363545 | -0.005042 | 0.004828 |
| 2.000000 |       1.840000 |         -2.267042 |         -2.377115 |         -2.254615 |   0.203274 |      0.000000 | 0.880070 | 0.183229 | -0.002734 | 0.002434 |
| 1.500000 |       1.850000 |         -2.338172 |         -2.415310 |         -2.382449 |   0.056008 |      0.000000 | 0.973477 | 0.056273 | -0.001022 | 0.000747 |
| 1.000000 |       2.200000 |         -2.699587 |         -2.763021 |         -2.760577 |   0.003916 |      0.000000 | 0.998670 | 0.004005 | -0.000249 | 0.000053 |
| 0.500000 |       2.710000 |         -3.210000 |         -3.311719 |         -3.311714 |   0.000004 |      0.000000 | 0.999999 | 0.000003 | -0.000098 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$0.49**

Expected profit (USD): **3.07** [lowest: 2.80, highest: 3.47]

Delta: 0.0166 (price sensitivity)

Gamma: 0.0378 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0005 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.34%**

Profit probability: **98.80%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $2.71 | $2.38 | 6.03 | 0.8799 | 0.33 |
| $1 | $2.20 | $1.89 | 4.27 | 0.8799 | 0.31 |
| $2 | $1.85 | $1.40 | 4.18 | 0.8799 | 0.45 |
| $2 | $1.84 | $0.97 | 3.49 | 0.8799 | 0.87 |
| $3 | $1.30 | $0.39 | 3.44 | 0.8799 | 0.91 |
| $4 | $0.93 | $0.13 | 3.11 | 0.8799 | 0.80 |
| $5 | $0.86 | $0.04 | 2.73 | 0.8799 | 0.82 |
| $6 | $0.54 | $0.01 | 3.04 | 0.8799 | 0.53 |
| $7 | $0.49 | $0.00 | 3.29 | 0.8799 | 0.49 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1735** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1875**

- Modal profit prediction correlation: **0.1834**

- Backtests total: **21**

- Profitable Trades (profitable trades / total trades): **33.33%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1212 [-0.7372, 0.5777]**

- Stock Volatility: **0.8799 [0.7664, 1.0012]**

- Based on **1734** observations


- Garch Volatility forecast: **0.8966**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.650000 |          2.900500 |          2.466690 |          3.512546 |   0.977704 |      0.969187 | 0.058378 | 0.083867 | -0.001138 | 0.001807 |
| 6.000000 |       0.550000 |          2.033013 |          1.600023 |          2.612606 |   0.954403 |      0.936108 | 0.105799 | 0.131519 | -0.001790 | 0.002834 |
| 5.000000 |       0.920000 |          0.730192 |          0.318343 |          1.262586 |   0.905143 |      0.802790 | 0.191748 | 0.196301 | -0.002684 | 0.004230 |
| 4.000000 |       1.000000 |         -0.209580 |         -0.566304 |          0.242160 |   0.802100 |      0.542903 | 0.341198 | 0.263924 | -0.003639 | 0.005687 |
| 3.000000 |       1.450000 |         -1.370907 |         -1.634804 |         -1.069918 |   0.599930 |      0.045569 | 0.574087 | 0.282008 | -0.003958 | 0.006077 |
| 1.500000 |       1.700000 |         -2.165235 |         -2.255538 |         -2.164641 |   0.118443 |      0.000000 | 0.947680 | 0.076915 | -0.001274 | 0.001657 |
| 2.000000 |       1.800000 |         -2.167497 |         -2.305781 |         -2.074190 |   0.278661 |      0.000000 | 0.847737 | 0.169397 | -0.002519 | 0.003650 |
| 1.000000 |       2.300000 |         -2.796690 |         -2.881724 |         -2.865982 |   0.021547 |      0.000000 | 0.993106 | 0.013830 | -0.000374 | 0.000298 |
| 0.500000 |       3.020000 |         -3.519985 |         -3.630233 |         -3.629987 |   0.000271 |      0.000000 | 0.999952 | 0.000144 | -0.000100 | 0.000003 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$0.65**

Expected profit (USD): **2.90** [lowest: 2.47, highest: 3.51]

Delta: 0.0584 (price sensitivity)

Gamma: 0.0839 (delta sensitivity)

Theta: $-0.0011 (negative decay per trading-day)

Vega: $0.0018 (volatility sensitivity per 1%)

ITM (In The Money) probability: **97.77%**

Profit probability: **96.92%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.02 | $2.39 | 2.25 | 0.8799 | 0.63 |
| $1 | $2.30 | $1.90 | 3.94 | 0.8799 | 0.40 |
| $2 | $1.70 | $1.44 | 4.13 | 0.8799 | 0.26 |
| $2 | $1.80 | $1.04 | 2.91 | 0.8799 | 0.76 |
| $3 | $1.45 | $0.51 | 3.19 | 0.8799 | 0.94 |
| $4 | $1.00 | $0.24 | 2.97 | 0.8799 | 0.76 |
| $5 | $0.92 | $0.11 | 2.74 | 0.8799 | 0.81 |
| $6 | $0.55 | $0.05 | 2.98 | 0.8799 | 0.50 |
| $7 | $0.65 | $0.03 | 2.65 | 0.8799 | 0.62 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1735** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1875**

- Modal profit prediction correlation: **0.1834**

- Backtests total: **21**

- Profitable Trades (profitable trades / total trades): **33.33%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1212 [-0.7372, 0.5777]**

- Stock Volatility: **0.8799 [0.7664, 1.0012]**

- Based on **1734** observations


- Garch Volatility forecast: **0.8966**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.750000 |          2.819828 |          2.082299 |          3.772045 |   0.946087 |      0.946331 | 0.153133 | 0.127893 | -0.001758 | 0.004871 |
| 6.000000 |       0.750000 |          1.888275 |          1.194293 |          2.783885 |   0.914320 |      0.905337 | 0.216845 | 0.158870 | -0.002193 | 0.006051 |
| 5.000000 |       1.000000 |          0.748375 |          0.122351 |          1.558760 |   0.860763 |      0.798630 | 0.308959 | 0.190594 | -0.002647 | 0.007259 |
| 4.000000 |       1.400000 |         -0.470685 |         -1.000852 |          0.203880 |   0.769151 |      0.516262 | 0.439947 | 0.213392 | -0.002991 | 0.008127 |
| 3.000000 |       1.600000 |         -1.368581 |         -1.749796 |         -0.880497 |   0.613247 |      0.100365 | 0.616828 | 0.206520 | -0.002946 | 0.007865 |
| 2.000000 |       1.800000 |         -2.065962 |         -2.268841 |         -1.827204 |   0.365424 |      0.000000 | 0.823543 | 0.140201 | -0.002094 | 0.005340 |
| 1.500000 |       2.300000 |         -2.711068 |         -2.860450 |         -2.628882 |   0.214105 |      0.000000 | 0.915777 | 0.083612 | -0.001330 | 0.003184 |
| 0.500000 |       2.750000 |         -3.249468 |         -3.352800 |         -3.347315 |   0.006138 |      0.000000 | 0.998996 | 0.001828 | -0.000120 | 0.000070 |
| 1.000000 |       2.900000 |         -3.382303 |         -3.502891 |         -3.429400 |   0.077216 |      0.000000 | 0.977732 | 0.028689 | -0.000557 | 0.001093 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$0.75**

Expected profit (USD): **2.82** [lowest: 2.08, highest: 3.77]

Delta: 0.1531 (price sensitivity)

Gamma: 0.1279 (delta sensitivity)

Theta: $-0.0018 (negative decay per trading-day)

Vega: $0.0049 (volatility sensitivity per 1%)

ITM (In The Money) probability: **94.61%**

Profit probability: **94.63%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $2.75 | $2.39 | 7.38 | 0.8799 | 0.36 |
| $1 | $2.90 | $1.92 | 3.20 | 0.8799 | 0.98 |
| $2 | $2.30 | $1.51 | 3.20 | 0.8799 | 0.79 |
| $2 | $1.80 | $1.17 | 2.31 | 0.8799 | 0.63 |
| $3 | $1.60 | $0.70 | 2.70 | 0.8799 | 0.90 |
| $4 | $1.40 | $0.42 | 2.49 | 0.8799 | 0.98 |
| $5 | $1.00 | $0.26 | 2.41 | 0.8799 | 0.74 |
| $6 | $0.75 | $0.16 | 2.26 | 0.8799 | 0.59 |
| $7 | $0.75 | $0.11 | 1.78 | 0.8799 | 0.64 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1735** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1875**

- Modal profit prediction correlation: **0.1834**

- Backtests total: **21**

- Profitable Trades (profitable trades / total trades): **33.33%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1212 [-0.7372, 0.5777]**

- Stock Volatility: **0.8799 [0.7664, 1.0012]**

- Based on **1734** observations


- Garch Volatility forecast: **0.8966**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.950000 |          2.710881 |          1.544874 |          4.070849 |   0.909967 |      0.930224 | 0.286205 | 0.138733 | -0.001941 | 0.009299 |
| 3.000000 |       1.900000 |         -1.479024 |         -2.020206 |         -0.737799 |   0.635099 |      0.128104 | 0.666643 | 0.148287 | -0.002156 | 0.009939 |
| 2.000000 |       1.900000 |         -2.027667 |         -2.333369 |         -1.580300 |   0.447952 |      0.000000 | 0.817767 | 0.107841 | -0.001626 | 0.007228 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$0.95**

Expected profit (USD): **2.71** [lowest: 1.54, highest: 4.07]

Delta: 0.2862 (price sensitivity)

Gamma: 0.1387 (delta sensitivity)

Theta: $-0.0019 (negative decay per trading-day)

Vega: $0.0093 (volatility sensitivity per 1%)

ITM (In The Money) probability: **91.00%**

Profit probability: **93.02%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.90 | $1.34 | 2.07 | 0.8799 | 0.56 |
| $3 | $1.90 | $0.94 | 1.97 | 0.8799 | 0.96 |
| $7 | $0.95 | $0.28 | 1.52 | 0.8799 | 0.67 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1735** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1875**

- Modal profit prediction correlation: **0.1834**

- Backtests total: **21**

- Profitable Trades (profitable trades / total trades): **33.33%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1212 [-0.7372, 0.5777]**

- Stock Volatility: **0.8799 [0.7664, 1.0012]**

- Based on **1734** observations


- Garch Volatility forecast: **0.8966**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       1.250000 |          2.573659 |          0.916749 |          4.282361 |   0.883848 |      0.927421 | 0.421420 | 0.124279 | -0.001773 | 0.013725 |
| 5.000000 |       1.600000 |          0.519672 |         -0.735373 |          1.945052 |   0.812347 |      0.819586 | 0.543639 | 0.125986 | -0.001819 | 0.013913 |
| 4.000000 |       1.900000 |         -0.564664 |         -1.573308 |          0.665159 |   0.752508 |      0.644175 | 0.623155 | 0.120657 | -0.001759 | 0.013325 |
| 3.000000 |       1.590000 |         -0.965388 |         -1.676279 |          0.036312 |   0.662457 |      0.441685 | 0.718031 | 0.107309 | -0.001589 | 0.011851 |
| 2.000000 |       1.800000 |         -1.772089 |         -2.189241 |         -1.093253 |   0.519215 |      0.000000 | 0.828435 | 0.080869 | -0.001234 | 0.008931 |
| 1.500000 |       2.100000 |         -2.306765 |         -2.600964 |         -1.840780 |   0.414868 |      0.000000 | 0.887095 | 0.060864 | -0.000957 | 0.006722 |
| 0.500000 |       2.900000 |         -3.380115 |         -3.504513 |         -3.375481 |   0.111184 |      0.000000 | 0.986669 | 0.010869 | -0.000224 | 0.001200 |
| 1.000000 |       3.200000 |         -3.581673 |         -3.790514 |         -3.366984 |   0.278926 |      0.000000 | 0.943200 | 0.036251 | -0.000607 | 0.004003 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$1.25**

Expected profit (USD): **2.57** [lowest: 0.92, highest: 4.28]

Delta: 0.4214 (price sensitivity)

Gamma: 0.1243 (delta sensitivity)

Theta: $-0.0018 (negative decay per trading-day)

Vega: $0.0137 (volatility sensitivity per 1%)

ITM (In The Money) probability: **88.38%**

Profit probability: **92.74%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $2.90 | $2.44 | 2.13 | 0.8799 | 0.46 |
| $1 | $3.20 | $2.07 | 1.89 | 0.8799 | 1.13 |
| $2 | $2.10 | $1.78 | 1.52 | 0.8799 | 0.32 |
| $2 | $1.80 | $1.55 | 1.69 | 0.8799 | 0.25 |
| $3 | $1.59 | $1.20 | 1.56 | 0.8799 | 0.39 |
| $4 | $1.90 | $0.96 | 1.47 | 0.8799 | 0.94 |
| $5 | $1.60 | $0.79 | 1.42 | 0.8799 | 0.81 |
| $7 | $1.25 | $0.55 | 1.25 | 0.8799 | 0.70 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1735** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1875**

- Modal profit prediction correlation: **0.1834**

- Backtests total: **21**

- Profitable Trades (profitable trades / total trades): **33.33%**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.1212 [-0.7372, 0.5777]**

- Stock Volatility: **0.8799 [0.7664, 1.0012]**

- Based on **1734** observations


- Garch Volatility forecast: **0.8966**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       1.350000 |          2.844482 |          0.317722 |          4.787236 |   0.867506 |      0.951296 | 0.614616 | 0.086067 | -0.001266 | 0.018934 |
| 5.000000 |       2.500000 |          0.007106 |         -1.862875 |          1.611113 |   0.815022 |      0.851847 | 0.694798 | 0.078869 | -0.001174 | 0.017351 |
| 4.000000 |       2.000000 |         -0.288548 |         -1.765934 |          1.132544 |   0.773944 |      0.804524 | 0.743493 | 0.072502 | -0.001089 | 0.015950 |
| 3.000000 |       1.900000 |         -0.934615 |         -1.992277 |          0.266172 |   0.714101 |      0.604067 | 0.799727 | 0.063069 | -0.000959 | 0.013875 |
| 1.500000 |       1.710000 |         -1.707478 |         -2.175306 |         -1.021746 |   0.546197 |      0.000000 | 0.901473 | 0.039077 | -0.000620 | 0.008597 |
| 2.000000 |       2.350000 |         -2.055219 |         -2.738195 |         -1.195568 |   0.618885 |      0.000000 | 0.865094 | 0.048848 | -0.000760 | 0.010746 |
| 1.000000 |       3.000000 |         -3.246186 |         -3.566714 |         -2.821610 |   0.441648 |      0.000000 | 0.939770 | 0.026894 | -0.000443 | 0.005917 |
| 0.500000 |       2.900000 |         -3.329118 |         -3.499307 |         -3.171184 |   0.275542 |      0.000000 | 0.977368 | 0.012100 | -0.000218 | 0.002662 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$1.35**

Expected profit (USD): **2.84** [lowest: 0.32, highest: 4.79]

Delta: 0.6146 (price sensitivity)

Gamma: 0.0861 (delta sensitivity)

Theta: $-0.0013 (negative decay per trading-day)

Vega: $0.0189 (volatility sensitivity per 1%)

ITM (In The Money) probability: **86.75%**

Profit probability: **95.13%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $2.90 | $2.52 | 1.91 | 0.8799 | 0.38 |
| $1 | $3.00 | $2.26 | 1.91 | 0.8799 | 0.74 |
| $2 | $1.71 | $2.06 | 1.66 | 0.8799 | -0.35 |
| $2 | $2.35 | $1.90 | 1.63 | 0.8799 | 0.45 |
| $3 | $1.90 | $1.65 | 1.30 | 0.8799 | 0.25 |
| $4 | $2.00 | $1.47 | 1.15 | 0.8799 | 0.53 |
| $5 | $2.50 | $1.32 | 1.28 | 0.8799 | 1.18 |
| $7 | $1.35 | $1.10 | 1.04 | 0.8799 | 0.25 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1735** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1875**

- Modal profit prediction correlation: **0.1834**

- Backtests total: **21**

- Profitable Trades (profitable trades / total trades): **33.33%**

--------------------------------------------------

