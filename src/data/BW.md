# BW Option Analysis From: 05.01.2026 00:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $6.349999904632568

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1053 [-0.6606, 0.4640]**

- Stock Volatility: **0.9307 [0.8157, 1.0521]**

- Based on **2652** observations


- Garch Volatility forecast: **1.2709**

### 2. Validate Stock Option Contracts

- Analyze **14** strikes prices..

Total of valuable options: 12

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       2.400000 |          0.976600 |          0.666756 |          0.949050 |   0.999928 |      0.693015 | 0.999972 | 0.000078 | -0.000504 | 0.000002 |
| 0.500000 |       4.440000 |          0.936590 |          0.572882 |          0.855176 |   1.000000 |      0.682081 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |
| 3.000000 |       2.000000 |          0.876817 |          0.584252 |          0.866559 |   0.998804 |      0.665533 | 0.999455 | 0.001268 | -0.000739 | 0.000024 |
| 1.000000 |       4.600000 |          0.276590 |         -0.096213 |          0.186080 |   1.000000 |      0.497696 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 4.000000 |       2.350000 |         -0.461833 |         -0.774549 |         -0.491010 |   0.966561 |      0.311662 | 0.980406 | 0.031364 | -0.004374 | 0.000602 |
| 3.500000 |       2.860000 |         -0.481236 |         -0.809208 |         -0.526709 |   0.991608 |      0.309506 | 0.995618 | 0.008473 | -0.001662 | 0.000163 |
| 4.500000 |       1.900000 |         -0.482460 |         -0.783037 |         -0.497222 |   0.909794 |      0.300979 | 0.941701 | 0.076770 | -0.009644 | 0.001473 |
| 1.500000 |       5.000000 |         -0.623410 |         -1.003210 |         -0.720916 |   1.000000 |      0.280346 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |
| 5.500000 |       1.050000 |         -0.442946 |         -0.762938 |         -0.486937 |   0.691302 |      0.270400 | 0.767081 | 0.201565 | -0.023945 | 0.003868 |
| 2.000000 |       4.550000 |         -0.673410 |         -1.058457 |         -0.776164 |   0.999999 |      0.270400 | 1.000000 | 0.000001 | -0.000396 | 0.000000 |
| 5.000000 |       1.600000 |         -0.615297 |         -0.930995 |         -0.644965 |   0.815536 |      0.260701 | 0.870384 | 0.139157 | -0.016819 | 0.002670 |
| 7.500000 |       0.200000 |         -0.456486 |         -0.633014 |         -0.512672 |   0.212243 |      0.106734 | 0.284699 | 0.223673 | -0.026051 | 0.004292 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.40**

Expected profit (USD): **0.98** [lowest: 0.67, highest: 0.95]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.99%**

Profit probability: **69.30%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $4.44 | $5.85 | 11.31 | 0.9307 | -1.41 |
| $1 | $4.60 | $5.35 | 9.16 | 0.9307 | -0.75 |
| $2 | $5.00 | $4.85 | 4.59 | 0.9307 | 0.15 |
| $2 | $4.55 | $4.35 | 4.84 | 0.9307 | 0.20 |
| $2 | $2.40 | $3.85 | 4.00 | 0.9307 | -1.45 |
| $3 | $2.00 | $3.36 | 2.97 | 0.9307 | -1.36 |
| $4 | $2.86 | $2.86 | 2.75 | 0.9307 | 0.00 |
| $4 | $2.35 | $2.36 | 2.13 | 0.9307 | -0.01 |
| $4 | $1.90 | $1.87 | 1.59 | 0.9307 | 0.03 |
| $5 | $1.60 | $1.41 | 1.41 | 0.9307 | 0.19 |
| $6 | $1.05 | $1.00 | 1.23 | 0.9307 | 0.05 |
| $8 | $0.20 | $0.13 | 1.24 | 0.9307 | 0.07 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2653** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2749**

- Modal profit prediction correlation: **-0.0409**

- Backtests total: **34**

- Profitable Trades (profitable trades / total trades): **41.18%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1053 [-0.6606, 0.4640]**

- Stock Volatility: **0.9307 [0.8157, 1.0521]**

- Based on **2652** observations


- Garch Volatility forecast: **1.2709**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  1.000000 |       4.200000 |          0.770666 |         -0.252683 |          1.002411 |   0.999035 |      0.425834 | 0.999861 | 0.000153 | -0.000217 | 0.000014 |
|  1.500000 |       4.400000 |          0.072658 |         -0.960173 |          0.294938 |   0.991045 |      0.345871 | 0.998149 | 0.001683 | -0.000523 | 0.000159 |
|  2.000000 |       4.350000 |         -0.367774 |         -1.407412 |         -0.152342 |   0.967637 |      0.301743 | 0.991394 | 0.006656 | -0.001292 | 0.000627 |
|  2.500000 |       4.000000 |         -0.491834 |         -1.538719 |         -0.284872 |   0.925567 |      0.288227 | 0.976068 | 0.016048 | -0.002652 | 0.001512 |
|  5.000000 |       1.920000 |         -0.306479 |         -1.363995 |         -0.279526 |   0.575294 |      0.253357 | 0.765743 | 0.087376 | -0.012525 | 0.008232 |
|  7.500000 |       0.720000 |         -0.160935 |         -0.968001 |         -0.329197 |   0.293398 |      0.169548 | 0.496627 | 0.113627 | -0.015986 | 0.010705 |
| 10.000000 |       0.260000 |         -0.225475 |         -0.708532 |         -0.408731 |   0.143708 |      0.090747 | 0.298479 | 0.098805 | -0.013807 | 0.009308 |
| 12.500000 |       0.630000 |         -0.853019 |         -1.142850 |         -1.008956 |   0.071133 |      0.038882 | 0.175572 | 0.073574 | -0.010245 | 0.006931 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$4.20**

Expected profit (USD): **0.77** [lowest: -0.25, highest: 1.00]

Delta: 0.9999 (price sensitivity)

Gamma: 0.0002 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.90%**

Profit probability: **42.58%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $4.20 | $5.36 | 6.17 | 0.9307 | -1.16 |
| $2 | $4.40 | $4.86 | 3.13 | 0.9307 | -0.46 |
| $2 | $4.35 | $4.37 | 2.52 | 0.9307 | -0.02 |
| $2 | $4.00 | $3.88 | 2.09 | 0.9307 | 0.12 |
| $5 | $1.92 | $1.74 | 1.28 | 0.9307 | 0.18 |
| $8 | $0.72 | $0.62 | 1.11 | 0.9307 | 0.10 |
| $10 | $0.26 | $0.20 | 1.18 | 0.9307 | 0.06 |
| $12 | $0.63 | $0.06 | 1.27 | 0.9307 | 0.57 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2653** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2749**

- Modal profit prediction correlation: **-0.0409**

- Backtests total: **34**

- Profitable Trades (profitable trades / total trades): **41.18%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1053 [-0.6606, 0.4640]**

- Stock Volatility: **0.9307 [0.8157, 1.0521]**

- Based on **2652** observations


- Garch Volatility forecast: **1.2709**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       2.950000 |          1.066458 |         -1.397755 |          2.013958 |   0.691894 |      0.274684 | 0.928197 | 0.021782 | -0.003665 | 0.006220 |
|  5.000000 |       2.450000 |          0.208457 |         -2.121289 |          0.667770 |   0.421126 |      0.186343 | 0.777046 | 0.047467 | -0.007665 | 0.013555 |
|  7.500000 |       1.500000 |          0.310578 |         -1.663760 |          0.395075 |   0.271385 |      0.141995 | 0.637821 | 0.059642 | -0.009514 | 0.017032 |
| 10.000000 |       1.150000 |          0.100199 |         -1.520459 |         -0.045476 |   0.184258 |      0.100713 | 0.524724 | 0.063347 | -0.010043 | 0.018090 |
| 12.500000 |       0.600000 |          0.261980 |         -1.057883 |         -0.002681 |   0.130362 |      0.075808 | 0.435097 | 0.062627 | -0.009891 | 0.017885 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.95**

Expected profit (USD): **1.07** [lowest: -1.40, highest: 2.01]

Delta: 0.9282 (price sensitivity)

Gamma: 0.0218 (delta sensitivity)

Theta: $-0.0037 (negative decay per trading-day)

Vega: $0.0062 (volatility sensitivity per 1%)

ITM (In The Money) probability: **69.19%**

Profit probability: **27.47%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.95 | $4.00 | 1.66 | 0.9307 | -1.05 |
| $5 | $2.45 | $2.31 | 1.21 | 0.9307 | 0.14 |
| $8 | $1.50 | $1.34 | 1.22 | 0.9307 | 0.16 |
| $10 | $1.15 | $0.80 | 1.31 | 0.9307 | 0.35 |
| $12 | $0.60 | $0.49 | 1.38 | 0.9307 | 0.11 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2653** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2749**

- Modal profit prediction correlation: **-0.0409**

- Backtests total: **34**

- Profitable Trades (profitable trades / total trades): **41.18%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1053 [-0.6606, 0.4640]**

- Stock Volatility: **0.9307 [0.8157, 1.0521]**

- Based on **2652** observations


- Garch Volatility forecast: **1.2709**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       2.950000 |          0.586117 |         -2.886675 |          1.943220 |   0.338481 |      0.135127 | 0.810539 | 0.031983 | -0.005362 | 0.016326 |
|  7.500000 |       2.330000 |          0.500901 |         -2.566727 |          1.364102 |   0.235580 |      0.105088 | 0.717659 | 0.039904 | -0.006624 | 0.020369 |
| 10.000000 |       1.530000 |          0.794135 |         -1.913419 |          1.287469 |   0.174566 |      0.085765 | 0.640659 | 0.044142 | -0.007288 | 0.022533 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.95**

Expected profit (USD): **0.59** [lowest: -2.89, highest: 1.94]

Delta: 0.8105 (price sensitivity)

Gamma: 0.0320 (delta sensitivity)

Theta: $-0.0054 (negative decay per trading-day)

Vega: $0.0163 (volatility sensitivity per 1%)

ITM (In The Money) probability: **33.85%**

Profit probability: **13.51%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $2.95 | $2.77 | 1.36 | 0.9307 | 0.18 |
| $8 | $2.33 | $1.92 | 1.24 | 0.9307 | 0.41 |
| $10 | $1.53 | $1.37 | 1.31 | 0.9307 | 0.16 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2653** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2749**

- Modal profit prediction correlation: **-0.0409**

- Backtests total: **34**

- Profitable Trades (profitable trades / total trades): **41.18%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1053 [-0.6606, 0.4640]**

- Stock Volatility: **0.9307 [0.8157, 1.0521]**

- Based on **2652** observations


- Garch Volatility forecast: **1.2709**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  1.000000 |       3.600000 |          2.547453 |         -2.732262 |          7.383155 |   0.617395 |      0.154392 | 0.975977 | 0.005157 | -0.000939 | 0.004372 |
|  1.500000 |       3.800000 |          2.063143 |         -3.209776 |          6.725773 |   0.525400 |      0.137351 | 0.959248 | 0.007983 | -0.001422 | 0.006768 |
|  0.500000 |       6.000000 |          0.488451 |         -4.868892 |          5.362760 |   0.758120 |      0.114825 | 0.991310 | 0.002151 | -0.000414 | 0.001823 |
|  2.000000 |       4.700000 |          0.917850 |         -4.351540 |          5.368310 |   0.458991 |      0.111691 | 0.942411 | 0.010525 | -0.001852 | 0.008923 |
|  2.500000 |       4.540000 |          0.861579 |         -4.324981 |          5.160870 |   0.408164 |      0.106691 | 0.925918 | 0.012796 | -0.002234 | 0.010848 |
|  5.000000 |       3.350000 |          1.238545 |         -3.539311 |          4.757177 |   0.263076 |      0.090589 | 0.851855 | 0.021099 | -0.003616 | 0.017888 |
|  7.500000 |       2.650000 |          1.377644 |         -2.995215 |          4.268758 |   0.192471 |      0.074312 | 0.790883 | 0.026232 | -0.004460 | 0.022240 |
| 10.000000 |       2.200000 |          1.403209 |         -2.617188 |          3.794790 |   0.150215 |      0.061002 | 0.739823 | 0.029608 | -0.005011 | 0.025101 |
| 12.500000 |       1.930000 |          1.335021 |         -2.417335 |          3.291192 |   0.122049 |      0.050487 | 0.696202 | 0.031906 | -0.005383 | 0.027050 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$3.60**

Expected profit (USD): **2.55** [lowest: -2.73, highest: 7.38]

Delta: 0.9760 (price sensitivity)

Gamma: 0.0052 (delta sensitivity)

Theta: $-0.0009 (negative decay per trading-day)

Vega: $0.0044 (volatility sensitivity per 1%)

ITM (In The Money) probability: **61.74%**

Profit probability: **15.44%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $6.00 | $5.89 | 2.10 | 0.9307 | 0.11 |
| $1 | $3.60 | $5.47 | 2.20 | 0.9307 | -1.87 |
| $2 | $3.80 | $5.08 | 1.48 | 0.9307 | -1.28 |
| $2 | $4.70 | $4.74 | 1.44 | 0.9307 | -0.04 |
| $2 | $4.54 | $4.43 | 1.24 | 0.9307 | 0.11 |
| $5 | $3.35 | $3.29 | 1.22 | 0.9307 | 0.06 |
| $8 | $2.65 | $2.56 | 1.20 | 0.9307 | 0.09 |
| $10 | $2.20 | $2.05 | 1.15 | 0.9307 | 0.15 |
| $12 | $1.93 | $1.69 | 1.29 | 0.9307 | 0.24 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2653** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2749**

- Modal profit prediction correlation: **-0.0409**

- Backtests total: **34**

- Profitable Trades (profitable trades / total trades): **41.18%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.1053 [-0.6606, 0.4640]**

- Stock Volatility: **0.9307 [0.8157, 1.0521]**

- Based on **2652** observations


- Garch Volatility forecast: **1.2709**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       3.800000 |          3.417787 |         -4.217162 |         18.483535 |   0.236393 |      0.049606 | 0.952147 | 0.006399 | -0.001133 | 0.010873 |
|  5.000000 |       2.850000 |          3.889285 |         -3.344959 |         17.976378 |   0.158464 |      0.041595 | 0.916698 | 0.009849 | -0.001723 | 0.016734 |
|  7.500000 |       2.510000 |          3.883463 |         -3.042638 |         17.131501 |   0.121759 |      0.033899 | 0.888340 | 0.012213 | -0.002125 | 0.020752 |
| 10.000000 |       2.230000 |          3.888704 |         -2.780035 |         16.417891 |   0.099636 |      0.028420 | 0.864413 | 0.013993 | -0.002426 | 0.023776 |
| 12.500000 |       2.930000 |          2.959465 |         -3.526639 |         14.823272 |   0.084615 |      0.022964 | 0.843587 | 0.015404 | -0.002664 | 0.026173 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.80**

Expected profit (USD): **3.42** [lowest: -4.22, highest: 18.48]

Delta: 0.9521 (price sensitivity)

Gamma: 0.0064 (delta sensitivity)

Theta: $-0.0011 (negative decay per trading-day)

Vega: $0.0109 (volatility sensitivity per 1%)

ITM (In The Money) probability: **23.64%**

Profit probability: **4.96%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.80 | $4.93 | 1.28 | 0.9307 | -1.13 |
| $5 | $2.85 | $4.16 | 1.26 | 0.9307 | -1.31 |
| $8 | $2.51 | $3.63 | 1.25 | 0.9307 | -1.12 |
| $10 | $2.23 | $3.24 | 1.24 | 0.9307 | -1.01 |
| $12 | $2.93 | $2.93 | 1.26 | 0.9307 | -0.00 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2653** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2749**

- Modal profit prediction correlation: **-0.0409**

- Backtests total: **34**

- Profitable Trades (profitable trades / total trades): **41.18%**

--------------------------------------------------

