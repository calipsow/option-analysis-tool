# GOSS Option Analysis From: 05.01.2026 02:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

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
| 1.000000 |       1.900000 |         -0.506111 |         -0.660583 |         -0.510775 |   1.000000 |      0.140518 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 2.000000 |       1.000000 |         -0.603097 |         -0.734456 |         -0.583819 |   0.976145 |      0.107424 | 0.983930 | 0.078135 | -0.001419 | 0.000231 |
| 3.000000 |       0.170000 |         -0.509185 |         -0.576209 |         -0.478527 |   0.385540 |      0.066036 | 0.448977 | 0.769469 | -0.010399 | 0.002270 |
| 1.500000 |       1.900000 |         -1.006101 |         -1.175649 |         -1.025825 |   0.999835 |      0.032415 | 0.999913 | 0.000676 | -0.000306 | 0.000002 |
| 0.500000 |       3.030000 |         -1.136111 |         -1.337998 |         -1.188191 |   1.000000 |      0.021175 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$1.90**

Expected profit (USD): **-0.51** [lowest: -0.66, highest: -0.51]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **14.05%**

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
| 1.000000 |       2.200000 |         -0.756558 |         -1.237610 |         -0.569643 |   0.996084 |      0.164548 | 0.998670 | 0.004005 | -0.000249 | 0.000053 |
| 0.500000 |       2.710000 |         -0.766971 |         -1.286938 |         -0.618774 |   0.999996 |      0.162789 | 0.999999 | 0.000003 | -0.000098 | 0.000000 |
| 1.500000 |       1.850000 |         -0.895143 |         -1.374744 |         -0.715015 |   0.943992 |      0.139890 | 0.973477 | 0.056273 | -0.001022 | 0.000747 |
| 2.000000 |       1.840000 |         -1.324013 |         -1.772869 |         -1.156706 |   0.796726 |      0.081210 | 0.880070 | 0.183229 | -0.002734 | 0.002434 |
| 3.000000 |       1.300000 |         -1.381394 |         -1.664638 |         -1.253106 |   0.405142 |      0.048172 | 0.541928 | 0.363545 | -0.005042 | 0.004828 |
| 4.000000 |       0.930000 |         -1.278024 |         -1.418052 |         -1.207281 |   0.158832 |      0.023389 | 0.256583 | 0.295198 | -0.004025 | 0.003921 |
| 5.000000 |       0.860000 |         -1.307221 |         -1.387593 |         -1.291939 |   0.056125 |      0.008075 | 0.106970 | 0.168876 | -0.002286 | 0.002243 |
| 6.000000 |       0.540000 |         -1.021711 |         -1.061611 |         -1.018393 |   0.019258 |      0.003752 | 0.042357 | 0.082717 | -0.001115 | 0.001099 |
| 7.000000 |       0.490000 |         -0.983547 |         -1.012282 |         -0.992772 |   0.006641 |      0.001316 | 0.016554 | 0.037764 | -0.000508 | 0.000502 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$2.20**

Expected profit (USD): **-0.76** [lowest: -1.24, highest: -0.57]

Delta: 0.9987 (price sensitivity)

Gamma: 0.0040 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.61%**

Profit probability: **16.45%**

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
| 1.500000 |       1.700000 |         -0.682295 |         -1.374102 |         -0.335602 |   0.881557 |      0.178804 | 0.947680 | 0.076915 | -0.001274 | 0.001657 |
| 1.000000 |       2.300000 |         -0.813750 |         -1.549044 |         -0.474851 |   0.978453 |      0.164736 | 0.993106 | 0.013830 | -0.000374 | 0.000298 |
| 0.500000 |       3.020000 |         -1.037044 |         -1.803970 |         -0.725612 |   0.999729 |      0.137466 | 0.999952 | 0.000144 | -0.000100 | 0.000003 |
| 2.000000 |       1.800000 |         -1.184557 |         -1.808210 |         -0.860409 |   0.721339 |      0.109112 | 0.847737 | 0.169397 | -0.002519 | 0.003650 |
| 3.000000 |       1.450000 |         -1.387966 |         -1.810856 |         -1.139558 |   0.400070 |      0.063892 | 0.574087 | 0.282008 | -0.003958 | 0.006077 |
| 4.000000 |       1.000000 |         -1.226640 |         -1.478147 |         -1.059355 |   0.197900 |      0.040827 | 0.341198 | 0.263924 | -0.003639 | 0.005687 |
| 5.000000 |       0.920000 |         -1.286867 |         -1.438579 |         -1.189941 |   0.094857 |      0.019623 | 0.191748 | 0.196301 | -0.002684 | 0.004230 |
| 6.000000 |       0.550000 |         -0.984046 |         -1.076428 |         -0.930468 |   0.045597 |      0.012050 | 0.105799 | 0.131519 | -0.001790 | 0.002834 |
| 7.000000 |       0.650000 |         -1.116559 |         -1.169633 |         -1.083415 |   0.022296 |      0.005296 | 0.058378 | 0.083867 | -0.001138 | 0.001807 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.70**

Expected profit (USD): **-0.68** [lowest: -1.37, highest: -0.34]

Delta: 0.9477 (price sensitivity)

Gamma: 0.0769 (delta sensitivity)

Theta: $-0.0013 (negative decay per trading-day)

Vega: $0.0017 (volatility sensitivity per 1%)

ITM (In The Money) probability: **88.16%**

Profit probability: **17.88%**

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
| 0.500000 |       2.750000 |         -0.685072 |         -1.876248 |          0.018499 |   0.993862 |      0.172524 | 0.998996 | 0.001828 | -0.000120 | 0.000070 |
| 2.000000 |       1.800000 |         -1.001566 |         -1.928458 |         -0.336642 |   0.634576 |      0.123536 | 0.823543 | 0.140201 | -0.002094 | 0.005340 |
| 1.500000 |       2.300000 |         -1.146672 |         -2.213929 |         -0.459748 |   0.785895 |      0.123536 | 0.915777 | 0.083612 | -0.001330 | 0.003184 |
| 1.000000 |       2.900000 |         -1.317907 |         -2.484578 |         -0.624201 |   0.922784 |      0.116373 | 0.977732 | 0.028689 | -0.000557 | 0.001093 |
| 3.000000 |       1.600000 |         -1.304185 |         -1.980295 |         -0.758883 |   0.386753 |      0.077316 | 0.616828 | 0.206520 | -0.002946 | 0.007865 |
| 4.000000 |       1.400000 |         -1.406289 |         -1.878618 |         -0.979638 |   0.230849 |      0.049430 | 0.439947 | 0.213392 | -0.002991 | 0.008127 |
| 5.000000 |       1.000000 |         -1.187229 |         -1.507082 |         -0.851929 |   0.139237 |      0.035827 | 0.308959 | 0.190594 | -0.002647 | 0.007259 |
| 6.000000 |       0.750000 |         -1.047329 |         -1.269456 |         -0.790382 |   0.085680 |      0.024335 | 0.216845 | 0.158870 | -0.002193 | 0.006051 |
| 7.000000 |       0.750000 |         -1.115776 |         -1.272599 |         -0.919184 |   0.053913 |      0.014898 | 0.153133 | 0.127893 | -0.001758 | 0.004871 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$0**

Market price: **$2.75**

Expected profit (USD): **-0.69** [lowest: -1.88, highest: 0.02]

Delta: 0.9990 (price sensitivity)

Gamma: 0.0018 (delta sensitivity)

Theta: $-0.0001 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.39%**

Profit probability: **17.25%**

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
| 2.000000 |       1.900000 |         -0.815336 |         -2.176559 |          0.599065 |   0.552048 |      0.114151 | 0.817767 | 0.107841 | -0.001626 | 0.007228 |
| 3.000000 |       1.900000 |         -1.266693 |         -2.327207 |         -0.016611 |   0.364901 |      0.074190 | 0.666643 | 0.148287 | -0.002156 | 0.009939 |
| 7.000000 |       0.950000 |         -1.076788 |         -1.475030 |         -0.351306 |   0.090033 |      0.024351 | 0.286205 | 0.138733 | -0.001941 | 0.009299 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.90**

Expected profit (USD): **-0.82** [lowest: -2.18, highest: 0.60]

Delta: 0.8178 (price sensitivity)

Gamma: 0.1078 (delta sensitivity)

Theta: $-0.0016 (negative decay per trading-day)

Vega: $0.0072 (volatility sensitivity per 1%)

ITM (In The Money) probability: **55.20%**

Profit probability: **11.42%**

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
| 0.500000 |       2.900000 |         -0.432383 |         -2.945091 |          2.789182 |   0.888816 |      0.118035 | 0.986669 | 0.010869 | -0.000224 | 0.001200 |
| 1.500000 |       2.100000 |         -0.359033 |         -2.441727 |          2.756739 |   0.585132 |      0.109231 | 0.887095 | 0.060864 | -0.000957 | 0.006722 |
| 2.000000 |       1.800000 |         -0.324357 |         -2.193937 |          2.711986 |   0.480785 |      0.101295 | 0.828435 | 0.080869 | -0.001234 | 0.008931 |
| 1.000000 |       3.200000 |         -1.133941 |         -3.460691 |          2.028750 |   0.721074 |      0.087615 | 0.943200 | 0.036251 | -0.000607 | 0.004003 |
| 3.000000 |       1.590000 |         -0.517657 |         -2.056602 |          2.310748 |   0.337543 |      0.076570 | 0.718031 | 0.107309 | -0.001589 | 0.011851 |
| 4.000000 |       1.900000 |         -1.116933 |         -2.418566 |          1.487127 |   0.247492 |      0.050702 | 0.623155 | 0.120657 | -0.001759 | 0.013325 |
| 5.000000 |       1.600000 |         -1.032597 |         -2.130635 |          1.383278 |   0.187653 |      0.041543 | 0.543639 | 0.125986 | -0.001819 | 0.013913 |
| 7.000000 |       1.250000 |         -0.978609 |         -1.781446 |          1.112320 |   0.116152 |      0.027162 | 0.421420 | 0.124279 | -0.001773 | 0.013725 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$0**

Market price: **$2.90**

Expected profit (USD): **-0.43** [lowest: -2.95, highest: 2.79]

Delta: 0.9867 (price sensitivity)

Gamma: 0.0109 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0012 (volatility sensitivity per 1%)

ITM (In The Money) probability: **88.88%**

Profit probability: **11.80%**

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
| 1.500000 |       1.710000 |          0.913949 |         -2.226206 |         12.316912 |   0.453803 |      0.074237 | 0.901473 | 0.039077 | -0.000620 | 0.008597 |
| 0.500000 |       2.900000 |          0.292308 |         -3.373439 |         11.903979 |   0.724458 |      0.069795 | 0.977368 | 0.012100 | -0.000218 | 0.002662 |
| 1.000000 |       3.000000 |         -0.124759 |         -3.527096 |         11.375659 |   0.558352 |      0.058197 | 0.939770 | 0.026894 | -0.000443 | 0.005917 |
| 2.000000 |       2.350000 |          0.066208 |         -2.898086 |         11.308495 |   0.381115 |      0.052762 | 0.865094 | 0.048848 | -0.000760 | 0.010746 |
| 3.000000 |       1.900000 |          0.186812 |         -2.432340 |         11.166321 |   0.285899 |      0.045679 | 0.799727 | 0.063069 | -0.000959 | 0.013875 |
| 4.000000 |       2.000000 |         -0.167122 |         -2.562597 |         10.500804 |   0.226056 |      0.035267 | 0.743493 | 0.072502 | -0.001089 | 0.015950 |
| 5.000000 |       2.500000 |         -0.871468 |         -3.081317 |          9.504768 |   0.184978 |      0.026003 | 0.694798 | 0.078869 | -0.001174 | 0.017351 |
| 7.000000 |       1.350000 |         -0.034091 |         -1.901216 |          9.863042 |   0.132494 |      0.022293 | 0.614616 | 0.086067 | -0.001266 | 0.018934 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.71**

Expected profit (USD): **0.91** [lowest: -2.23, highest: 12.32]

Delta: 0.9015 (price sensitivity)

Gamma: 0.0391 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0086 (volatility sensitivity per 1%)

ITM (In The Money) probability: **45.38%**

Profit probability: **7.42%**

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

