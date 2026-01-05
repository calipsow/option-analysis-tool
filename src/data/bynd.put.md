# Put Option. BYND Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

## Current Stock Price: $0.8809999823570251

### Calculate Stock Option Nr. 1

Expires At: **09.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 1.500000 |       0.010000 |          0.111670 |          0.103184 |          0.117291 |   0.999903 |      0.821840 | 0.000188 | 0.005542 | -0.000015 | 0.000001 |
| 1.000000 |       0.030000 |         -0.394211 |         -0.414133 |         -0.399037 |   0.831229 |      0.000016 | 0.215397 | 2.267065 | -0.006325 | 0.000281 |
| 0.500000 |       0.400000 |         -0.899999 |         -0.916579 |         -0.916579 |   0.000080 |      0.000000 | 0.999960 | 0.001290 | -0.000103 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$2**

Market price: **$0.01**

Expected profit (USD): **0.11** [lowest: 0.10, highest: 0.12]

Delta: 0.0002 (price sensitivity)

Gamma: 0.0055 (delta sensitivity)

Theta: $-0.0000 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.99%**

Profit probability: **82.18%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.40 | $0.38 | 2.75 | 0.8872 | 0.02 |
| $1 | $0.03 | $0.00 | 1.84 | 0.8872 | 0.03 |
| $2 | $0.01 | $0.00 | 3.25 | 0.8872 | 0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **26** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       0.010000 |          1.617852 |          1.591267 |          1.638041 |   0.999997 |      0.999959 | 0.000012 | 0.000216 | -0.000001 | 0.000000 |
| 2.500000 |       0.010000 |          1.117860 |          1.091267 |          1.138041 |   0.999951 |      0.999151 | 0.000176 | 0.002727 | -0.000008 | 0.000001 |
| 2.000000 |       0.020000 |          0.608013 |          0.580865 |          0.627640 |   0.999035 |      0.981345 | 0.002741 | 0.034144 | -0.000105 | 0.000015 |
| 1.500000 |       0.020000 |          0.111068 |          0.080921 |          0.127752 |   0.980984 |      0.729661 | 0.039965 | 0.348676 | -0.001070 | 0.000151 |
| 1.000000 |       0.050000 |         -0.369649 |         -0.427152 |         -0.384247 |   0.735046 |      0.015210 | 0.380293 | 1.542054 | -0.004758 | 0.000668 |
| 0.500000 |       0.390000 |         -0.888375 |         -0.906472 |         -0.906329 |   0.032559 |      0.000000 | 0.984916 | 0.154075 | -0.000566 | 0.000067 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$3**

Market price: **$0.01**

Expected profit (USD): **1.62** [lowest: 1.59, highest: 1.64]

Delta: 0.0000 (price sensitivity)

Gamma: 0.0002 (delta sensitivity)

Theta: $-0.0000 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **100.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.39 | $0.38 | 2.13 | 0.8872 | 0.01 |
| $1 | $0.05 | $0.02 | 1.44 | 0.8872 | 0.03 |
| $2 | $0.02 | $0.00 | 2.38 | 0.8872 | 0.02 |
| $2 | $0.02 | $0.00 | 2.81 | 0.8872 | 0.02 |
| $2 | $0.01 | $0.00 | 3.38 | 0.8872 | 0.01 |
| $3 | $0.01 | $0.00 | 3.75 | 0.8872 | 0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **23.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       0.030000 |          1.604078 |          1.557953 |          1.637059 |   0.999738 |      0.998757 | 0.001204 | 0.011952 | -0.000039 | 0.000009 |
| 2.500000 |       0.010000 |          1.124417 |          1.079197 |          1.158304 |   0.998591 |      0.992954 | 0.005330 | 0.045840 | -0.000151 | 0.000035 |
| 2.000000 |       0.030000 |          0.606340 |          0.557964 |          0.637082 |   0.991759 |      0.951111 | 0.024714 | 0.173366 | -0.000572 | 0.000132 |
| 1.500000 |       0.030000 |          0.118004 |          0.059227 |          0.138377 |   0.949390 |      0.711845 | 0.113949 | 0.577559 | -0.001910 | 0.000441 |
| 1.000000 |       0.080000 |         -0.362935 |         -0.450071 |         -0.384425 |   0.715356 |      0.049486 | 0.445944 | 1.183863 | -0.003942 | 0.000904 |
| 0.500000 |       0.400000 |         -0.891910 |         -0.917754 |         -0.916370 |   0.103860 |      0.000000 | 0.954776 | 0.285025 | -0.001024 | 0.000218 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$3**

Market price: **$0.03**

Expected profit (USD): **1.60** [lowest: 1.56, highest: 1.64]

Delta: 0.0012 (price sensitivity)

Gamma: 0.0120 (delta sensitivity)

Theta: $-0.0000 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.97%**

Profit probability: **99.88%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.40 | $0.38 | 1.94 | 0.8872 | 0.02 |
| $1 | $0.08 | $0.04 | 1.47 | 0.8872 | 0.04 |
| $2 | $0.03 | $0.00 | 2.06 | 0.8872 | 0.03 |
| $2 | $0.03 | $0.00 | 2.38 | 0.8872 | 0.03 |
| $2 | $0.01 | $0.00 | 2.63 | 0.8872 | 0.01 |
| $3 | $0.03 | $0.00 | 3.13 | 0.8872 | 0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **30.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       0.020000 |          1.122488 |          1.056553 |          1.167673 |   0.994408 |      0.982748 | 0.022143 | 0.129403 | -0.000452 | 0.000143 |
| 2.000000 |       0.030000 |          0.618098 |          0.545829 |          0.656960 |   0.980055 |      0.929320 | 0.063092 | 0.303785 | -0.001062 | 0.000337 |
| 1.500000 |       0.040000 |          0.128947 |          0.038903 |          0.149193 |   0.924130 |      0.708941 | 0.181976 | 0.647832 | -0.002270 | 0.000718 |
| 1.000000 |       0.090000 |         -0.340946 |         -0.453856 |         -0.367704 |   0.711410 |      0.098944 | 0.487253 | 0.977723 | -0.003449 | 0.001084 |
| 0.500000 |       0.390000 |         -0.872265 |         -0.907449 |         -0.903433 |   0.173645 |      0.000000 | 0.928596 | 0.334294 | -0.001241 | 0.000371 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$2**

Market price: **$0.02**

Expected profit (USD): **1.12** [lowest: 1.06, highest: 1.17]

Delta: 0.0221 (price sensitivity)

Gamma: 0.1294 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.44%**

Profit probability: **98.27%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.39 | $0.38 | 1.63 | 0.8872 | 0.01 |
| $1 | $0.09 | $0.05 | 1.47 | 0.8872 | 0.04 |
| $2 | $0.04 | $0.00 | 1.78 | 0.8872 | 0.04 |
| $2 | $0.03 | $0.00 | 2.03 | 0.8872 | 0.03 |
| $2 | $0.02 | $0.00 | 2.25 | 0.8872 | 0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **06.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 1.500000 |       0.050000 |          0.138445 |          0.019678 |          0.159519 |   0.908910 |      0.711546 | 0.230630 | 0.656126 | -0.002304 | 0.000940 |
| 1.000000 |       0.120000 |         -0.346206 |         -0.479811 |         -0.374575 |   0.713411 |      0.118257 | 0.513530 | 0.860226 | -0.003042 | 0.001232 |
| 0.500000 |       0.400000 |         -0.872889 |         -0.920645 |         -0.912997 |   0.225385 |      0.000000 | 0.911721 | 0.345360 | -0.001275 | 0.000495 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$2**

Market price: **$0.05**

Expected profit (USD): **0.14** [lowest: 0.02, highest: 0.16]

Delta: 0.2306 (price sensitivity)

Gamma: 0.6561 (delta sensitivity)

Theta: $-0.0023 (negative decay per trading-day)

Vega: $0.0009 (volatility sensitivity per 1%)

ITM (In The Money) probability: **90.89%**

Profit probability: **71.15%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.40 | $0.39 | 2.53 | 0.8872 | 0.01 |
| $1 | $0.12 | $0.07 | 1.55 | 0.8872 | 0.05 |
| $2 | $0.05 | $0.01 | 1.78 | 0.8872 | 0.04 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **13.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.000000 |       0.040000 |          0.635072 |          0.508469 |          0.682067 |   0.961186 |      0.907616 | 0.134945 | 0.422977 | -0.001484 | 0.000743 |
| 1.500000 |       0.060000 |          0.147567 |          0.000891 |          0.168660 |   0.898088 |      0.715760 | 0.271121 | 0.645658 | -0.002272 | 0.001134 |
| 1.000000 |       0.150000 |         -0.354031 |         -0.515866 |         -0.392601 |   0.717231 |      0.130124 | 0.534534 | 0.774498 | -0.002745 | 0.001360 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$2**

Market price: **$0.04**

Expected profit (USD): **0.64** [lowest: 0.51, highest: 0.68]

Delta: 0.1349 (price sensitivity)

Gamma: 0.4230 (delta sensitivity)

Theta: $-0.0015 (negative decay per trading-day)

Vega: $0.0007 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.12%**

Profit probability: **90.76%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $0.15 | $0.08 | 2.41 | 0.8872 | 0.07 |
| $2 | $0.06 | $0.01 | 1.56 | 0.8872 | 0.05 |
| $2 | $0.04 | $0.00 | 2.19 | 0.8872 | 0.04 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **21** strikes prices..

Total of valuable options: 18

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |       0.010000 |         13.648141 |         13.529364 |         13.734713 |   0.999999 |      1.000000 | 0.000017 | 0.000135 | -0.000000 | 0.000000 |
| 11.000000 |       0.020000 |          9.638150 |          9.518514 |          9.723863 |   0.999994 |      0.999995 | 0.000130 | 0.000908 | -0.000003 | 0.000002 |
| 10.000000 |       0.020000 |          8.638158 |          8.518514 |          8.723863 |   0.999988 |      0.999989 | 0.000231 | 0.001555 | -0.000005 | 0.000003 |
|  9.000000 |       0.010000 |          7.648176 |          7.528939 |          7.734288 |   0.999975 |      0.999977 | 0.000426 | 0.002744 | -0.000010 | 0.000006 |
|  8.000000 |       0.020000 |          6.638214 |          6.518514 |          6.723863 |   0.999945 |      0.999946 | 0.000818 | 0.005013 | -0.000017 | 0.000010 |
|  7.000000 |       0.020000 |          5.638299 |          5.517239 |          5.722588 |   0.999873 |      0.999868 | 0.001648 | 0.009519 | -0.000033 | 0.000020 |
|  6.000000 |       0.030000 |          4.628506 |          4.508089 |          4.713438 |   0.999681 |      0.999638 | 0.003513 | 0.018885 | -0.000066 | 0.000039 |
|  5.500000 |       0.020000 |          4.138712 |          4.018939 |          4.224288 |   0.999477 |      0.999386 | 0.005259 | 0.027084 | -0.000095 | 0.000056 |
|  5.000000 |       0.030000 |          3.629054 |          3.508515 |          3.713863 |   0.999119 |      0.998900 | 0.008021 | 0.039344 | -0.000137 | 0.000082 |
|  4.500000 |       0.020000 |          3.139641 |          3.011716 |          3.217064 |   0.998469 |      0.998002 | 0.012490 | 0.057903 | -0.000202 | 0.000120 |
|  4.000000 |       0.020000 |          2.640680 |          2.514695 |          2.720042 |   0.997245 |      0.996170 | 0.019896 | 0.086319 | -0.000302 | 0.000179 |
|  3.500000 |       0.030000 |          2.132589 |          2.006412 |          2.211755 |   0.994840 |      0.992169 | 0.032501 | 0.130186 | -0.000456 | 0.000271 |
|  3.000000 |       0.040000 |          1.626257 |          1.498192 |          1.703505 |   0.989875 |      0.982976 | 0.054572 | 0.197975 | -0.000693 | 0.000412 |
|  2.500000 |       0.050000 |          1.123669 |          0.987772 |          1.192882 |   0.979028 |      0.960196 | 0.094352 | 0.301141 | -0.001056 | 0.000626 |
|  2.000000 |       0.050000 |          0.639567 |          0.490747 |          0.694463 |   0.953718 |      0.900703 | 0.167928 | 0.449591 | -0.001580 | 0.000935 |
|  1.500000 |       0.080000 |          0.146085 |         -0.024295 |          0.169885 |   0.890310 |      0.714926 | 0.305540 | 0.627742 | -0.002212 | 0.001305 |
|  1.000000 |       0.160000 |         -0.343798 |         -0.511681 |         -0.371237 |   0.721904 |      0.158033 | 0.552167 | 0.708276 | -0.002515 | 0.001473 |
|  0.500000 |       0.390000 |         -0.843846 |         -0.905427 |         -0.888155 |   0.306773 |      0.000000 | 0.889649 | 0.337490 | -0.001240 | 0.000702 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$15**

Market price: **$0.01**

Expected profit (USD): **13.65** [lowest: 13.53, highest: 13.73]

Delta: 0.0000 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0000 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **100.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.39 | $0.39 | 1.53 | 0.8872 | -0.00 |
| $1 | $0.16 | $0.09 | 1.58 | 0.8872 | 0.07 |
| $2 | $0.08 | $0.02 | 1.81 | 0.8872 | 0.06 |
| $2 | $0.05 | $0.00 | 1.97 | 0.8872 | 0.05 |
| $2 | $0.05 | $0.00 | 2.09 | 0.8872 | 0.05 |
| $3 | $0.04 | $0.00 | 2.25 | 0.8872 | 0.04 |
| $4 | $0.03 | $0.00 | 2.64 | 0.8872 | 0.03 |
| $4 | $0.02 | $0.00 | 3.09 | 0.8872 | 0.02 |
| $4 | $0.02 | $0.00 | 3.50 | 0.8872 | 0.02 |
| $5 | $0.03 | $0.00 | 2.66 | 0.8872 | 0.03 |
| $6 | $0.02 | $0.00 | 2.53 | 0.8872 | 0.02 |
| $6 | $0.03 | $0.00 | 2.75 | 0.8872 | 0.03 |
| $7 | $0.02 | $0.00 | 3.19 | 0.8872 | 0.02 |
| $8 | $0.02 | $0.00 | 3.03 | 0.8872 | 0.02 |
| $9 | $0.01 | $0.00 | 3.13 | 0.8872 | 0.01 |
| $10 | $0.02 | $0.00 | 3.25 | 0.8872 | 0.02 |
| $11 | $0.02 | $0.00 | 3.31 | 0.8872 | 0.02 |
| $15 | $0.01 | $0.00 | 3.44 | 0.8872 | 0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 8

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **21** strikes prices..

Total of valuable options: 19

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |       0.050000 |         13.679395 |         13.319992 |         13.881371 |   0.999515 |      0.999722 | 0.018721 | 0.048413 | -0.000170 | 0.000289 |
| 14.000000 |       0.090000 |         12.639938 |         12.277870 |         12.839247 |   0.999392 |      0.999641 | 0.021867 | 0.055228 | -0.000194 | 0.000329 |
| 12.000000 |       0.080000 |         10.651503 |         10.287034 |         10.848398 |   0.999004 |      0.999388 | 0.030535 | 0.073026 | -0.000257 | 0.000435 |
| 10.000000 |       0.060000 |          8.674155 |          8.307081 |          8.868403 |   0.998259 |      0.998877 | 0.044274 | 0.098946 | -0.000348 | 0.000590 |
|  9.000000 |       0.080000 |          7.656193 |          7.286290 |          7.847560 |   0.997624 |      0.998406 | 0.054254 | 0.116391 | -0.000410 | 0.000694 |
|  8.000000 |       0.090000 |          6.649012 |          6.278961 |          6.840123 |   0.996672 |      0.997672 | 0.067433 | 0.137975 | -0.000486 | 0.000822 |
|  7.000000 |       0.070000 |          5.673023 |          5.300922 |          5.861850 |   0.995190 |      0.996510 | 0.085225 | 0.164904 | -0.000581 | 0.000983 |
|  6.000000 |       0.100000 |          4.648940 |          4.268127 |          4.828514 |   0.992769 |      0.994380 | 0.109887 | 0.198728 | -0.000701 | 0.001184 |
|  5.500000 |       0.100000 |          4.152983 |          3.763611 |          4.323474 |   0.990973 |      0.992749 | 0.125887 | 0.218796 | -0.000772 | 0.001304 |
|  5.000000 |       0.100000 |          3.658068 |          3.271787 |          3.830799 |   0.988568 |      0.990469 | 0.145200 | 0.241284 | -0.000852 | 0.001438 |
|  4.500000 |       0.090000 |          3.174562 |          2.783801 |          3.341391 |   0.985279 |      0.987268 | 0.168762 | 0.266387 | -0.000941 | 0.001588 |
|  4.000000 |       0.100000 |          2.673008 |          2.275693 |          2.830834 |   0.980669 |      0.982313 | 0.197851 | 0.294177 | -0.001040 | 0.001753 |
|  3.500000 |       0.120000 |          2.164231 |          1.759740 |          2.310523 |   0.974013 |      0.974376 | 0.234257 | 0.324445 | -0.001149 | 0.001934 |
|  3.000000 |       0.120000 |          1.679541 |          1.267559 |          1.810291 |   0.964047 |      0.961779 | 0.280531 | 0.356353 | -0.001263 | 0.002124 |
|  2.500000 |       0.130000 |          1.191114 |          0.776453 |          1.303727 |   0.948431 |      0.939069 | 0.340396 | 0.387703 | -0.001377 | 0.002311 |
|  2.000000 |       0.170000 |          0.682805 |          0.270462 |          0.766899 |   0.922473 |      0.890556 | 0.419387 | 0.413294 | -0.001471 | 0.002463 |
|  1.500000 |       0.200000 |          0.202029 |         -0.185752 |          0.247432 |   0.875719 |      0.775129 | 0.525752 | 0.421058 | -0.001504 | 0.002509 |
|  1.000000 |       0.260000 |         -0.275202 |         -0.584917 |         -0.279354 |   0.781139 |      0.357184 | 0.670900 | 0.382603 | -0.001377 | 0.002280 |
|  0.500000 |       0.460000 |         -0.817773 |         -0.964039 |         -0.867466 |   0.551789 |      0.000000 | 0.861760 | 0.233387 | -0.000858 | 0.001391 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$15**

Market price: **$0.05**

Expected profit (USD): **13.68** [lowest: 13.32, highest: 13.88]

Delta: 0.0187 (price sensitivity)

Gamma: 0.0484 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0003 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.95%**

Profit probability: **99.97%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.46 | $0.43 | 1.39 | 0.8872 | 0.03 |
| $1 | $0.26 | $0.19 | 1.52 | 0.8872 | 0.07 |
| $2 | $0.20 | $0.08 | 1.66 | 0.8872 | 0.12 |
| $2 | $0.17 | $0.04 | 1.78 | 0.8872 | 0.13 |
| $2 | $0.13 | $0.02 | 1.83 | 0.8872 | 0.11 |
| $3 | $0.12 | $0.01 | 1.81 | 0.8872 | 0.11 |
| $4 | $0.12 | $0.01 | 1.97 | 0.8872 | 0.11 |
| $4 | $0.10 | $0.00 | 2.02 | 0.8872 | 0.10 |
| $4 | $0.09 | $0.00 | 2.06 | 0.8872 | 0.09 |
| $5 | $0.10 | $0.00 | 2.14 | 0.8872 | 0.10 |
| $6 | $0.10 | $0.00 | 2.47 | 0.8872 | 0.10 |
| $6 | $0.10 | $0.00 | 2.17 | 0.8872 | 0.10 |
| $7 | $0.07 | $0.00 | 2.17 | 0.8872 | 0.07 |
| $8 | $0.09 | $0.00 | 2.25 | 0.8872 | 0.09 |
| $9 | $0.08 | $0.00 | 2.36 | 0.8872 | 0.08 |
| $10 | $0.06 | $0.00 | 2.63 | 0.8872 | 0.06 |
| $12 | $0.08 | $0.00 | 2.47 | 0.8872 | 0.08 |
| $14 | $0.09 | $0.00 | 2.42 | 0.8872 | 0.09 |
| $15 | $0.05 | $0.00 | 2.30 | 0.8872 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 9

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.000000 |       0.250000 |          0.745320 |          0.115564 |          0.838224 |   0.926292 |      0.914281 | 0.566546 | 0.313640 | -0.001126 | 0.003289 |
| 1.500000 |       0.270000 |          0.269555 |         -0.283105 |          0.329897 |   0.893736 |      0.838864 | 0.644183 | 0.297069 | -0.001071 | 0.003115 |
| 1.000000 |       0.330000 |         -0.223708 |         -0.648459 |         -0.208940 |   0.831935 |      0.486519 | 0.743595 | 0.256756 | -0.000932 | 0.002693 |
| 0.500000 |       0.490000 |         -0.768765 |         -0.988331 |         -0.805850 |   0.682592 |      0.000000 | 0.873137 | 0.165828 | -0.000611 | 0.001739 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$2**

Market price: **$0.25**

Expected profit (USD): **0.75** [lowest: 0.12, highest: 0.84]

Delta: 0.5665 (price sensitivity)

Gamma: 0.3136 (delta sensitivity)

Theta: $-0.0011 (negative decay per trading-day)

Vega: $0.0033 (volatility sensitivity per 1%)

ITM (In The Money) probability: **92.63%**

Profit probability: **91.43%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.49 | $0.47 | 1.80 | 0.8872 | 0.02 |
| $1 | $0.33 | $0.26 | 1.45 | 0.8872 | 0.07 |
| $2 | $0.27 | $0.16 | 1.38 | 0.8872 | 0.11 |
| $2 | $0.25 | $0.10 | 1.23 | 0.8872 | 0.15 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 10

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **15** strikes prices..

Total of valuable options: 15

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |       0.090000 |         13.869838 |         12.639023 |         14.161838 |   0.996226 |      0.998508 | 0.275261 | 0.207358 | -0.000740 | 0.003583 |
| 12.000000 |       0.110000 |         10.863371 |          9.633671 |         11.138548 |   0.994607 |      0.997749 | 0.317442 | 0.221381 | -0.000791 | 0.003825 |
| 10.000000 |       0.120000 |          8.865786 |          7.643620 |          9.127842 |   0.992852 |      0.996875 | 0.353796 | 0.230970 | -0.000826 | 0.003991 |
|  7.000000 |       0.230000 |          5.783628 |          4.588219 |          6.011563 |   0.987920 |      0.994030 | 0.428612 | 0.243825 | -0.000874 | 0.004213 |
|  5.500000 |       0.150000 |          4.385040 |          3.235539 |          4.599008 |   0.983106 |      0.991188 | 0.480884 | 0.247519 | -0.000888 | 0.004277 |
|  5.000000 |       0.180000 |          3.864045 |          2.732497 |          4.067659 |   0.980794 |      0.989558 | 0.501684 | 0.247801 | -0.000890 | 0.004282 |
|  4.500000 |       0.190000 |          3.364337 |          2.258685 |          3.559400 |   0.977931 |      0.987498 | 0.524670 | 0.247330 | -0.000889 | 0.004274 |
|  4.000000 |       0.200000 |          2.866240 |          1.792164 |          3.050461 |   0.974312 |      0.984717 | 0.550266 | 0.245834 | -0.000885 | 0.004248 |
|  3.500000 |       0.200000 |          2.380203 |          1.345158 |          2.550507 |   0.969621 |      0.980904 | 0.579027 | 0.242925 | -0.000875 | 0.004197 |
|  3.000000 |       0.250000 |          1.846881 |          0.861476 |          1.999689 |   0.963345 |      0.974596 | 0.611704 | 0.238025 | -0.000859 | 0.004113 |
|  2.500000 |       0.260000 |          1.357266 |          0.440581 |          1.492119 |   0.954594 |      0.965041 | 0.649338 | 0.230232 | -0.000832 | 0.003978 |
|  2.000000 |       0.280000 |          0.862972 |          0.036846 |          0.974123 |   0.941678 |      0.947185 | 0.693448 | 0.218066 | -0.000790 | 0.003768 |
|  1.500000 |       0.350000 |          0.326862 |         -0.376059 |          0.407025 |   0.920964 |      0.898597 | 0.746359 | 0.198900 | -0.000723 | 0.003437 |
|  1.000000 |       0.410000 |         -0.185204 |         -0.717883 |         -0.147636 |   0.882918 |      0.575982 | 0.811911 | 0.167513 | -0.000612 | 0.002894 |
|  0.500000 |       0.550000 |         -0.747777 |         -1.038281 |         -0.761499 |   0.791141 |      0.000000 | 0.896934 | 0.111435 | -0.000413 | 0.001925 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$15**

Market price: **$0.09**

Expected profit (USD): **13.87** [lowest: 12.64, highest: 14.16]

Delta: 0.2753 (price sensitivity)

Gamma: 0.2074 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0036 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.62%**

Profit probability: **99.85%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.55 | $0.53 | 1.00 | 0.8872 | 0.02 |
| $1 | $0.41 | $0.35 | 1.39 | 0.8872 | 0.06 |
| $2 | $0.35 | $0.25 | 1.38 | 0.8872 | 0.10 |
| $2 | $0.28 | $0.19 | 1.40 | 0.8872 | 0.09 |
| $2 | $0.26 | $0.14 | 1.42 | 0.8872 | 0.12 |
| $3 | $0.25 | $0.11 | 1.49 | 0.8872 | 0.14 |
| $4 | $0.20 | $0.09 | 1.51 | 0.8872 | 0.11 |
| $4 | $0.20 | $0.08 | 1.48 | 0.8872 | 0.12 |
| $4 | $0.19 | $0.06 | 1.48 | 0.8872 | 0.13 |
| $5 | $0.18 | $0.05 | 1.64 | 0.8872 | 0.13 |
| $6 | $0.15 | $0.04 | 1.55 | 0.8872 | 0.11 |
| $7 | $0.23 | $0.03 | 1.59 | 0.8872 | 0.20 |
| $10 | $0.12 | $0.01 | 1.71 | 0.8872 | 0.11 |
| $12 | $0.11 | $0.01 | 1.70 | 0.8872 | 0.10 |
| $15 | $0.09 | $0.01 | 1.62 | 0.8872 | 0.08 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 11

Expires At: **19.03.2027**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **15** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.170000 |          5.899794 |          4.517995 |          6.117749 |   0.988099 |      0.994689 | 0.492930 | 0.229210 | -0.000824 | 0.004628 |
| 3.500000 |       0.210000 |          2.423188 |          1.253014 |          2.565144 |   0.971896 |      0.983829 | 0.630503 | 0.216868 | -0.000783 | 0.004378 |
| 3.000000 |       0.200000 |          1.948527 |          0.861970 |          2.093250 |   0.966478 |      0.979443 | 0.659546 | 0.210660 | -0.000762 | 0.004253 |
| 2.500000 |       0.300000 |          1.367052 |          0.338794 |          1.468979 |   0.958989 |      0.970577 | 0.692703 | 0.201952 | -0.000732 | 0.004077 |
| 2.000000 |       0.260000 |          0.930108 |          0.030697 |          1.032012 |   0.948037 |      0.958150 | 0.731215 | 0.189571 | -0.000689 | 0.003827 |
| 1.500000 |       0.330000 |          0.390070 |         -0.370113 |          0.463199 |   0.930626 |      0.921900 | 0.777010 | 0.171464 | -0.000625 | 0.003462 |
| 1.000000 |       0.440000 |         -0.178213 |         -0.742313 |         -0.133350 |   0.898881 |      0.577855 | 0.833328 | 0.143576 | -0.000526 | 0.002899 |
| 0.500000 |       0.500000 |         -0.671922 |         -0.982637 |         -0.676519 |   0.822333 |      0.000000 | 0.906300 | 0.096142 | -0.000356 | 0.001941 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$7**

Market price: **$0.17**

Expected profit (USD): **5.90** [lowest: 4.52, highest: 6.12]

Delta: 0.4929 (price sensitivity)

Gamma: 0.2292 (delta sensitivity)

Theta: $-0.0008 (negative decay per trading-day)

Vega: $0.0046 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.81%**

Profit probability: **99.47%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.50 | $0.54 | 1.32 | 0.8872 | -0.04 |
| $1 | $0.44 | $0.38 | 1.27 | 0.8872 | 0.06 |
| $2 | $0.33 | $0.28 | 1.27 | 0.8872 | 0.05 |
| $2 | $0.26 | $0.22 | 1.52 | 0.8872 | 0.04 |
| $2 | $0.30 | $0.17 | 1.58 | 0.8872 | 0.13 |
| $3 | $0.20 | $0.14 | 1.49 | 0.8872 | 0.06 |
| $4 | $0.21 | $0.12 | 2.04 | 0.8872 | 0.09 |
| $7 | $0.17 | $0.04 | 1.45 | 0.8872 | 0.13 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 12

Expires At: **17.06.2027**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **15** strikes prices..

Total of valuable options: 14

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |       0.120000 |         13.965396 |         12.132232 |         14.223762 |   0.995815 |      0.998636 | 0.430920 | 0.205618 | -0.000738 | 0.005006 |
| 12.000000 |       0.210000 |         10.889956 |          9.090589 |         11.121567 |   0.994360 |      0.998044 | 0.471635 | 0.208228 | -0.000748 | 0.005070 |
|  7.000000 |       0.210000 |          5.929338 |          4.310747 |          6.134528 |   0.988856 |      0.995546 | 0.570371 | 0.205499 | -0.000741 | 0.005003 |
|  5.500000 |       0.260000 |          4.398603 |          2.872794 |          4.575702 |   0.985156 |      0.993524 | 0.613516 | 0.200247 | -0.000723 | 0.004875 |
|  5.000000 |       0.310000 |          3.856444 |          2.361161 |          4.011944 |   0.983426 |      0.992414 | 0.630219 | 0.197533 | -0.000714 | 0.004809 |
|  4.500000 |       0.290000 |          3.385240 |          1.894944 |          3.485535 |   0.981316 |      0.991158 | 0.648400 | 0.194140 | -0.000702 | 0.004727 |
|  4.000000 |       0.280000 |          2.905213 |          1.521431 |          3.041882 |   0.978691 |      0.989468 | 0.668328 | 0.189885 | -0.000688 | 0.004623 |
|  3.500000 |       0.200000 |          2.496669 |          1.189303 |          2.627158 |   0.975343 |      0.987533 | 0.690356 | 0.184515 | -0.000669 | 0.004492 |
|  3.000000 |       0.280000 |          1.930045 |          0.723057 |          2.062445 |   0.970941 |      0.983637 | 0.714957 | 0.177664 | -0.000645 | 0.004326 |
|  2.500000 |       0.240000 |          1.485997 |          0.368084 |          1.588366 |   0.964910 |      0.978739 | 0.742791 | 0.168785 | -0.000614 | 0.004109 |
|  2.000000 |       0.300000 |          0.945580 |         -0.050212 |          1.023456 |   0.956171 |      0.967974 | 0.774829 | 0.157004 | -0.000572 | 0.003823 |
|  1.500000 |       0.370000 |          0.400647 |         -0.427160 |          0.462178 |   0.942402 |      0.939999 | 0.812586 | 0.140803 | -0.000515 | 0.003428 |
|  1.000000 |       0.450000 |         -0.145030 |         -0.751047 |         -0.099281 |   0.917483 |      0.650519 | 0.858676 | 0.117215 | -0.000431 | 0.002854 |
|  0.500000 |       0.380000 |         -0.521444 |         -0.851647 |         -0.512598 |   0.857420 |      0.000000 | 0.918331 | 0.079015 | -0.000293 | 0.001924 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$15**

Market price: **$0.12**

Expected profit (USD): **13.97** [lowest: 12.13, highest: 14.22]

Delta: 0.4309 (price sensitivity)

Gamma: 0.2056 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0050 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.58%**

Profit probability: **99.86%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.38 | $0.57 | 1.36 | 0.8872 | -0.19 |
| $1 | $0.45 | $0.42 | 1.35 | 0.8872 | 0.03 |
| $2 | $0.37 | $0.32 | 1.83 | 0.8872 | 0.05 |
| $2 | $0.30 | $0.26 | 2.17 | 0.8872 | 0.04 |
| $2 | $0.24 | $0.22 | 1.86 | 0.8872 | 0.02 |
| $3 | $0.28 | $0.18 | 1.45 | 0.8872 | 0.10 |
| $4 | $0.20 | $0.16 | 1.94 | 0.8872 | 0.04 |
| $4 | $0.28 | $0.14 | 1.87 | 0.8872 | 0.14 |
| $4 | $0.29 | $0.12 | 4.88 | 0.8872 | 0.17 |
| $5 | $0.31 | $0.11 | 1.64 | 0.8872 | 0.20 |
| $6 | $0.26 | $0.10 | 1.24 | 0.8872 | 0.16 |
| $7 | $0.21 | $0.07 | 1.46 | 0.8872 | 0.14 |
| $12 | $0.21 | $0.03 | 1.65 | 0.8872 | 0.18 |
| $15 | $0.12 | $0.02 | 1.45 | 0.8872 | 0.10 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 13

Expires At: **17.12.2027**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **15** strikes prices..

Total of valuable options: 15

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |       0.130000 |         14.072034 |         11.557140 |         14.279940 |   0.996202 |      0.999009 | 0.574939 | 0.176669 | -0.000638 | 0.005795 |
| 12.000000 |       0.400000 |         10.814992 |          8.390693 |         10.977318 |   0.995073 |      0.998607 | 0.609336 | 0.173054 | -0.000626 | 0.005677 |
| 10.000000 |       0.690000 |          8.535912 |          6.216816 |          8.680631 |   0.993938 |      0.998126 | 0.636831 | 0.169166 | -0.000612 | 0.005549 |
|  7.000000 |       0.250000 |          5.997952 |          3.962958 |          6.160906 |   0.991030 |      0.997130 | 0.688521 | 0.159376 | -0.000578 | 0.005228 |
|  5.500000 |       0.390000 |          4.373208 |          2.498758 |          4.502531 |   0.988429 |      0.995871 | 0.721548 | 0.151348 | -0.000550 | 0.004965 |
|  5.000000 |       0.390000 |          3.879283 |          2.080270 |          4.005239 |   0.987233 |      0.995281 | 0.734113 | 0.147914 | -0.000538 | 0.004852 |
|  4.500000 |       0.300000 |          3.476016 |          1.761811 |          3.598836 |   0.985787 |      0.994676 | 0.747661 | 0.143968 | -0.000524 | 0.004722 |
|  4.000000 |       0.330000 |          2.953552 |          1.326240 |          3.064412 |   0.984007 |      0.993660 | 0.762364 | 0.139391 | -0.000508 | 0.004572 |
|  3.500000 |       0.410000 |          2.382087 |          0.864995 |          2.491116 |   0.981761 |      0.992075 | 0.778448 | 0.134023 | -0.000489 | 0.004396 |
|  3.000000 |       0.300000 |          2.001903 |          0.609249 |          2.107084 |   0.978838 |      0.990551 | 0.796218 | 0.127636 | -0.000466 | 0.004187 |
|  2.500000 |       0.290000 |          1.523419 |          0.253645 |          1.602834 |   0.974880 |      0.987695 | 0.816100 | 0.119892 | -0.000438 | 0.003933 |
|  2.000000 |       0.450000 |          0.877305 |         -0.222534 |          0.951843 |   0.969209 |      0.980001 | 0.838724 | 0.110261 | -0.000404 | 0.003617 |
|  1.500000 |       0.450000 |          0.394727 |         -0.513235 |          0.451662 |   0.960373 |      0.963828 | 0.865092 | 0.097836 | -0.000359 | 0.003209 |
|  1.000000 |       0.490000 |         -0.121942 |         -0.792775 |         -0.085077 |   0.944531 |      0.581346 | 0.896980 | 0.080852 | -0.000298 | 0.002652 |
|  0.500000 |       0.540000 |         -0.636387 |         -1.018431 |         -0.636183 |   0.906363 |      0.000000 | 0.938199 | 0.054960 | -0.000205 | 0.001803 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$15**

Market price: **$0.13**

Expected profit (USD): **14.07** [lowest: 11.56, highest: 14.28]

Delta: 0.5749 (price sensitivity)

Gamma: 0.1767 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0058 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.62%**

Profit probability: **99.90%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.54 | $0.61 | 1.53 | 0.8872 | -0.07 |
| $1 | $0.49 | $0.48 | 1.23 | 0.8872 | 0.01 |
| $2 | $0.45 | $0.40 | 1.25 | 0.8872 | 0.05 |
| $2 | $0.45 | $0.34 | 1.30 | 0.8872 | 0.11 |
| $2 | $0.29 | $0.30 | 1.14 | 0.8872 | -0.01 |
| $3 | $0.30 | $0.26 | 1.35 | 0.8872 | 0.04 |
| $4 | $0.41 | $0.24 | 1.22 | 0.8872 | 0.17 |
| $4 | $0.33 | $0.21 | 1.50 | 0.8872 | 0.12 |
| $4 | $0.30 | $0.19 | 1.41 | 0.8872 | 0.11 |
| $5 | $0.39 | $0.18 | 1.42 | 0.8872 | 0.21 |
| $6 | $0.39 | $0.16 | 1.43 | 0.8872 | 0.23 |
| $7 | $0.25 | $0.13 | 1.38 | 0.8872 | 0.12 |
| $10 | $0.69 | $0.09 | 1.64 | 0.8872 | 0.60 |
| $12 | $0.40 | $0.07 | 1.75 | 0.8872 | 0.33 |
| $15 | $0.13 | $0.06 | 1.45 | 0.8872 | 0.07 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 14

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **-0.2545 [-0.8685, 0.4797]**

- Stock Volatility: **0.8872 [0.7723, 1.0101]**

- Based on **1677** observations


- Garch Volatility forecast: **1.5000**

### 2. Validate Stock Option Contracts

- Analyze **15** strikes prices..

Total of valuable options: 15

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |       0.170000 |         14.050508 |         11.410115 |         14.246898 |   0.996323 |      0.999076 | 0.597834 | 0.170270 | -0.000615 | 0.005861 |
| 12.000000 |       0.190000 |         11.043021 |          8.541876 |         11.226144 |   0.995255 |      0.998745 | 0.630910 | 0.166036 | -0.000601 | 0.005715 |
| 10.000000 |       0.190000 |          9.053517 |          6.673867 |          9.222423 |   0.994185 |      0.998393 | 0.657246 | 0.161754 | -0.000586 | 0.005567 |
|  7.000000 |       0.270000 |          5.994581 |          3.870384 |          6.129969 |   0.991457 |      0.997371 | 0.706522 | 0.151489 | -0.000550 | 0.005214 |
|  5.500000 |       0.270000 |          4.509077 |          2.583390 |          4.635361 |   0.989029 |      0.996363 | 0.737859 | 0.143358 | -0.000521 | 0.004934 |
|  5.000000 |       0.310000 |          3.974833 |          2.133458 |          4.101878 |   0.987915 |      0.995818 | 0.749753 | 0.139928 | -0.000509 | 0.004816 |
|  4.500000 |       0.260000 |          3.531200 |          1.773887 |          3.649503 |   0.986570 |      0.995242 | 0.762561 | 0.136016 | -0.000495 | 0.004682 |
|  4.000000 |       0.300000 |          2.998313 |          1.336631 |          3.108451 |   0.984917 |      0.994337 | 0.776442 | 0.131512 | -0.000479 | 0.004527 |
|  3.500000 |       0.330000 |          2.476355 |          0.928634 |          2.583416 |   0.982833 |      0.993097 | 0.791606 | 0.126266 | -0.000461 | 0.004346 |
|  3.000000 |       0.340000 |          1.975584 |          0.550141 |          2.071682 |   0.980126 |      0.991346 | 0.808334 | 0.120070 | -0.000439 | 0.004133 |
|  2.500000 |       0.370000 |          1.456387 |          0.175006 |          1.543079 |   0.976464 |      0.988425 | 0.827023 | 0.112612 | -0.000412 | 0.003876 |
|  2.000000 |       0.410000 |          0.929379 |         -0.188673 |          1.000069 |   0.971227 |      0.982782 | 0.848257 | 0.103406 | -0.000379 | 0.003559 |
|  1.500000 |       0.450000 |          0.405635 |         -0.509668 |          0.465635 |   0.963079 |      0.967822 | 0.872967 | 0.091622 | -0.000337 | 0.003154 |
|  1.000000 |       0.500000 |         -0.122665 |         -0.799129 |         -0.084045 |   0.948490 |      0.000000 | 0.902812 | 0.075642 | -0.000279 | 0.002604 |
|  0.500000 |       0.630000 |         -0.719710 |         -1.104015 |         -0.716143 |   0.913342 |      0.000000 | 0.941384 | 0.051476 | -0.000192 | 0.001772 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$15**

Market price: **$0.17**

Expected profit (USD): **14.05** [lowest: 11.41, highest: 14.25]

Delta: 0.5978 (price sensitivity)

Gamma: 0.1703 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0059 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.63%**

Profit probability: **99.91%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $0.63 | $0.62 | 1.13 | 0.8872 | 0.01 |
| $1 | $0.50 | $0.49 | 1.19 | 0.8872 | 0.01 |
| $2 | $0.45 | $0.41 | 1.24 | 0.8872 | 0.04 |
| $2 | $0.41 | $0.35 | 1.45 | 0.8872 | 0.06 |
| $2 | $0.37 | $0.31 | 1.25 | 0.8872 | 0.06 |
| $3 | $0.34 | $0.28 | 1.37 | 0.8872 | 0.06 |
| $4 | $0.33 | $0.25 | 1.42 | 0.8872 | 0.08 |
| $4 | $0.30 | $0.23 | 1.59 | 0.8872 | 0.07 |
| $4 | $0.26 | $0.21 | 1.41 | 0.8872 | 0.05 |
| $5 | $0.31 | $0.19 | 1.49 | 0.8872 | 0.12 |
| $6 | $0.27 | $0.18 | 1.37 | 0.8872 | 0.09 |
| $7 | $0.27 | $0.14 | 1.64 | 0.8872 | 0.13 |
| $10 | $0.19 | $0.10 | 1.54 | 0.8872 | 0.09 |
| $12 | $0.19 | $0.08 | 1.38 | 0.8872 | 0.11 |
| $15 | $0.17 | $0.07 | 1.44 | 0.8872 | 0.10 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1678** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2067**

- Modal profit prediction correlation: **0.2785**

- Backtests total: **20**

- Profitable Trades (profitable trades / total trades): **35.00%**

--------------------------------------------------

