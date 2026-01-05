# Put Option. RR Option Analysis From: 05.01.2026 03:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

## Current Stock Price: $3.4800000190734863

### Calculate Stock Option Nr. 1

Expires At: **09.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **15** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.500000 |       0.030000 |          1.442284 |          1.399374 |          1.583537 |   0.999752 |      0.997645 | 0.000276 | 0.002267 | -0.000077 | 0.000004 |
| 5.000000 |       0.040000 |          0.932845 |          0.893177 |          1.078784 |   0.997018 |      0.976856 | 0.003263 | 0.021825 | -0.000746 | 0.000037 |
| 4.500000 |       0.080000 |          0.398352 |          0.369392 |          0.555471 |   0.973730 |      0.841181 | 0.028123 | 0.142641 | -0.004877 | 0.000245 |
| 4.000000 |       0.160000 |         -0.144547 |         -0.149008 |          0.026826 |   0.848970 |      0.407787 | 0.158060 | 0.533918 | -0.018289 | 0.000916 |
| 3.500000 |       0.310000 |         -0.641562 |         -0.633754 |         -0.491304 |   0.501651 |      0.028765 | 0.510141 | 0.882170 | -0.030368 | 0.001514 |
| 3.000000 |       0.550000 |         -1.028537 |         -1.037940 |         -0.967406 |   0.118510 |      0.000006 | 0.887250 | 0.423350 | -0.014932 | 0.000727 |
| 2.500000 |       1.000000 |         -1.499521 |         -1.540493 |         -1.525066 |   0.004856 |      0.000000 | 0.995545 | 0.028856 | -0.001475 | 0.000050 |
| 2.000000 |       1.310000 |         -1.810000 |         -1.901775 |         -1.900946 |   0.000008 |      0.000000 | 0.999993 | 0.000074 | -0.000399 | 0.000000 |
| 1.500000 |       2.000000 |         -2.500000 |         -2.628981 |         -2.628977 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |
| 1.000000 |       3.500000 |         -4.000000 |         -4.183564 |         -4.183564 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$6**

Market price: **$0.03**

Expected profit (USD): **1.44** [lowest: 1.40, highest: 1.58]

Delta: 0.0003 (price sensitivity)

Gamma: 0.0023 (delta sensitivity)

Theta: $-0.0001 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.98%**

Profit probability: **99.76%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $3.50 | $2.48 | 30.63 | 1.6372 | 1.02 |
| $2 | $2.00 | $1.98 | 3.25 | 1.6372 | 0.02 |
| $2 | $1.31 | $1.48 | 8.66 | 1.6372 | -0.17 |
| $2 | $1.00 | $0.99 | 2.94 | 1.6372 | 0.01 |
| $3 | $0.55 | $0.55 | 1.88 | 1.6372 | 0.00 |
| $4 | $0.31 | $0.24 | 1.97 | 1.6372 | 0.07 |
| $4 | $0.16 | $0.08 | 2.05 | 1.6372 | 0.08 |
| $4 | $0.08 | $0.02 | 2.16 | 1.6372 | 0.06 |
| $5 | $0.04 | $0.01 | 2.16 | 1.6372 | 0.03 |
| $6 | $0.03 | $0.00 | 2.38 | 1.6372 | 0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **14** strikes prices..

Total of valuable options: 12

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.030000 |          2.829596 |          2.688606 |          3.295924 |   0.997486 |      0.996536 | 0.003071 | 0.011025 | -0.000398 | 0.000065 |
| 6.500000 |       0.040000 |          2.321640 |          2.188714 |          2.792643 |   0.993806 |      0.990938 | 0.007429 | 0.024235 | -0.000875 | 0.000142 |
| 6.000000 |       0.060000 |          1.806615 |          1.684983 |          2.282081 |   0.985078 |      0.976605 | 0.017554 | 0.051134 | -0.001847 | 0.000300 |
| 5.000000 |       0.120000 |          0.785128 |          0.706636 |          1.266276 |   0.922694 |      0.863931 | 0.087173 | 0.187130 | -0.006773 | 0.001099 |
| 4.500000 |       0.180000 |          0.282514 |          0.235274 |          0.752805 |   0.839097 |      0.704148 | 0.177303 | 0.306721 | -0.011121 | 0.001802 |
| 4.000000 |       0.290000 |         -0.213628 |         -0.230175 |          0.219848 |   0.693943 |      0.429321 | 0.329245 | 0.426969 | -0.015525 | 0.002508 |
| 3.500000 |       0.450000 |         -0.670278 |         -0.673708 |         -0.314817 |   0.483525 |      0.130642 | 0.542355 | 0.468125 | -0.017117 | 0.002750 |
| 3.000000 |       0.630000 |         -1.033007 |         -1.042101 |         -0.799596 |   0.250044 |      0.008264 | 0.770171 | 0.358177 | -0.013270 | 0.002104 |
| 2.500000 |       1.110000 |         -1.590679 |         -1.657286 |         -1.533912 |   0.077356 |      0.000000 | 0.931643 | 0.155572 | -0.006028 | 0.000914 |
| 2.000000 |       1.350000 |         -1.848525 |         -1.917900 |         -1.878712 |   0.009656 |      0.000000 | 0.991903 | 0.026142 | -0.001329 | 0.000154 |
| 1.000000 |       2.450000 |         -2.950000 |         -3.070548 |         -3.070384 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 0.500000 |       3.030000 |         -3.530000 |         -3.666550 |         -3.666550 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$7**

Market price: **$0.03**

Expected profit (USD): **2.83** [lowest: 2.69, highest: 3.30]

Delta: 0.0031 (price sensitivity)

Gamma: 0.0110 (delta sensitivity)

Theta: $-0.0004 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.75%**

Profit probability: **99.65%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.03 | $2.98 | 17.56 | 1.6372 | 0.05 |
| $1 | $2.45 | $2.48 | 10.38 | 1.6372 | -0.03 |
| $2 | $1.35 | $1.50 | 4.61 | 1.6372 | -0.15 |
| $2 | $1.11 | $1.06 | 2.47 | 1.6372 | 0.05 |
| $3 | $0.63 | $0.71 | 1.74 | 1.6372 | -0.08 |
| $4 | $0.45 | $0.45 | 1.77 | 1.6372 | 0.00 |
| $4 | $0.29 | $0.27 | 1.85 | 1.6372 | 0.02 |
| $4 | $0.18 | $0.16 | 1.88 | 1.6372 | 0.02 |
| $5 | $0.12 | $0.09 | 1.91 | 1.6372 | 0.03 |
| $6 | $0.06 | $0.03 | 2.02 | 1.6372 | 0.03 |
| $6 | $0.04 | $0.02 | 2.13 | 1.6372 | 0.02 |
| $7 | $0.03 | $0.01 | 2.25 | 1.6372 | 0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **23.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **13** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 8.000000 |       0.050000 |          3.696444 |          3.454279 |          4.473005 |   0.993638 |      0.994623 | 0.008308 | 0.020085 | -0.000757 | 0.000205 |
| 6.500000 |       0.060000 |          2.210355 |          2.011589 |          2.989062 |   0.967912 |      0.967982 | 0.039663 | 0.075857 | -0.002864 | 0.000774 |
| 6.000000 |       0.070000 |          1.721497 |          1.548331 |          2.497843 |   0.945650 |      0.942375 | 0.065813 | 0.113474 | -0.004288 | 0.001157 |
| 5.500000 |       0.100000 |          1.227062 |          1.083556 |          1.992853 |   0.909172 |      0.895847 | 0.107611 | 0.164056 | -0.006206 | 0.001673 |
| 5.000000 |       0.160000 |          0.725894 |          0.615852 |          1.468298 |   0.851222 |      0.811624 | 0.172241 | 0.226183 | -0.008569 | 0.002307 |
| 4.500000 |       0.220000 |          0.260855 |          0.188256 |          0.962376 |   0.763220 |      0.676441 | 0.267511 | 0.291710 | -0.011074 | 0.002975 |
| 4.000000 |       0.330000 |         -0.201099 |         -0.241656 |          0.428561 |   0.638104 |      0.466098 | 0.398569 | 0.342114 | -0.013030 | 0.003489 |
| 3.500000 |       0.470000 |         -0.621101 |         -0.639758 |         -0.098116 |   0.476681 |      0.217495 | 0.561521 | 0.349393 | -0.013380 | 0.003563 |
| 3.000000 |       0.650000 |         -0.994554 |         -1.014010 |         -0.617830 |   0.296682 |      0.040385 | 0.735754 | 0.289900 | -0.011221 | 0.002956 |
| 2.500000 |       1.260000 |         -1.711043 |         -1.789581 |         -1.546949 |   0.136464 |      0.000002 | 0.883503 | 0.173631 | -0.006899 | 0.001771 |
| 2.000000 |       1.200000 |         -1.691393 |         -1.793272 |         -1.682337 |   0.037160 |      0.000000 | 0.970012 | 0.060289 | -0.002629 | 0.000615 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$0.05**

Expected profit (USD): **3.70** [lowest: 3.45, highest: 4.47]

Delta: 0.0083 (price sensitivity)

Gamma: 0.0201 (delta sensitivity)

Theta: $-0.0008 (negative decay per trading-day)

Vega: $0.0002 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.36%**

Profit probability: **99.46%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.20 | $1.54 | 1.86 | 1.6372 | -0.34 |
| $2 | $1.26 | $1.14 | 1.68 | 1.6372 | 0.12 |
| $3 | $0.65 | $0.82 | 1.34 | 1.6372 | -0.17 |
| $4 | $0.47 | $0.58 | 1.57 | 1.6372 | -0.11 |
| $4 | $0.33 | $0.41 | 1.66 | 1.6372 | -0.08 |
| $4 | $0.22 | $0.28 | 1.63 | 1.6372 | -0.06 |
| $5 | $0.16 | $0.19 | 1.55 | 1.6372 | -0.03 |
| $6 | $0.10 | $0.13 | 1.52 | 1.6372 | -0.03 |
| $6 | $0.07 | $0.09 | 1.74 | 1.6372 | -0.02 |
| $6 | $0.06 | $0.06 | 1.98 | 1.6372 | -0.00 |
| $8 | $0.05 | $0.02 | 2.38 | 1.6372 | 0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **30.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **15** strikes prices..

Total of valuable options: 12

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.500000 |       0.070000 |          3.088864 |          2.789377 |          4.159240 |   0.969785 |      0.977341 | 0.039877 | 0.063053 | -0.002465 | 0.000923 |
| 6.500000 |       0.080000 |          2.124381 |          1.874427 |          3.175609 |   0.934778 |      0.945154 | 0.082747 | 0.111865 | -0.004380 | 0.001638 |
| 6.000000 |       0.100000 |          1.644082 |          1.431451 |          2.681863 |   0.904568 |      0.913856 | 0.118503 | 0.145443 | -0.005700 | 0.002129 |
| 5.500000 |       0.120000 |          1.181995 |          1.001987 |          2.186635 |   0.861241 |      0.865727 | 0.168430 | 0.184522 | -0.007240 | 0.002702 |
| 5.000000 |       0.180000 |          0.705779 |          0.564379 |          1.664733 |   0.800277 |      0.786771 | 0.236660 | 0.226293 | -0.008894 | 0.003313 |
| 4.500000 |       0.250000 |          0.255459 |          0.152777 |          1.146812 |   0.716900 |      0.667878 | 0.327028 | 0.264681 | -0.010426 | 0.003875 |
| 4.000000 |       0.350000 |         -0.176773 |         -0.243057 |          0.620079 |   0.607570 |      0.495607 | 0.441381 | 0.289474 | -0.011441 | 0.004238 |
| 3.500000 |       0.490000 |         -0.587847 |         -0.628326 |          0.079347 |   0.472943 |      0.277333 | 0.576676 | 0.287217 | -0.011412 | 0.004205 |
| 3.000000 |       0.840000 |         -1.136969 |         -1.178207 |         -0.641289 |   0.322265 |      0.049858 | 0.721364 | 0.246340 | -0.009880 | 0.003607 |
| 2.500000 |       1.100000 |         -1.520958 |         -1.589332 |         -1.231384 |   0.177018 |      0.000666 | 0.853672 | 0.168217 | -0.006881 | 0.002463 |
| 2.000000 |       1.210000 |         -1.689952 |         -1.790155 |         -1.598050 |   0.067274 |      0.000000 | 0.947591 | 0.078540 | -0.003393 | 0.001150 |
| 1.500000 |       1.480000 |         -1.977665 |         -2.097054 |         -2.026706 |   0.012848 |      0.000000 | 0.990771 | 0.018226 | -0.000995 | 0.000267 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$0.07**

Expected profit (USD): **3.09** [lowest: 2.79, highest: 4.16]

Delta: 0.0399 (price sensitivity)

Gamma: 0.0631 (delta sensitivity)

Theta: $-0.0025 (negative decay per trading-day)

Vega: $0.0009 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.98%**

Profit probability: **97.73%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.48 | $2.01 | 1.84 | 1.6372 | -0.53 |
| $2 | $1.21 | $1.58 | 1.50 | 1.6372 | -0.37 |
| $2 | $1.10 | $1.21 | 2.05 | 1.6372 | -0.11 |
| $3 | $0.84 | $0.92 | 1.57 | 1.6372 | -0.08 |
| $4 | $0.49 | $0.69 | 1.39 | 1.6372 | -0.20 |
| $4 | $0.35 | $0.52 | 1.41 | 1.6372 | -0.17 |
| $4 | $0.25 | $0.39 | 1.41 | 1.6372 | -0.14 |
| $5 | $0.18 | $0.29 | 1.45 | 1.6372 | -0.11 |
| $6 | $0.12 | $0.22 | 1.44 | 1.6372 | -0.10 |
| $6 | $0.10 | $0.16 | 1.61 | 1.6372 | -0.06 |
| $6 | $0.08 | $0.12 | 1.74 | 1.6372 | -0.04 |
| $8 | $0.07 | $0.07 | 1.98 | 1.6372 | -0.00 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **06.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.160000 |          2.455902 |          2.115684 |          3.759903 |   0.928126 |      0.946063 | 0.095259 | 0.107819 | -0.004345 | 0.002067 |
| 6.500000 |       0.130000 |          2.027848 |          1.727148 |          3.312916 |   0.902820 |      0.924666 | 0.126133 | 0.131881 | -0.005319 | 0.002528 |
| 6.000000 |       0.140000 |          1.574541 |          1.314029 |          2.827848 |   0.868740 |      0.891735 | 0.166639 | 0.159048 | -0.006421 | 0.003049 |
| 5.500000 |       0.080000 |          1.211013 |          0.994572 |          2.420221 |   0.823214 |      0.852229 | 0.219242 | 0.188131 | -0.007606 | 0.003607 |
| 5.000000 |       0.220000 |          0.673747 |          0.498199 |          1.816584 |   0.763166 |      0.769530 | 0.286514 | 0.216684 | -0.008776 | 0.004154 |
| 4.500000 |       0.300000 |          0.230790 |          0.097005 |          1.286357 |   0.685487 |      0.660812 | 0.370635 | 0.240508 | -0.009764 | 0.004611 |
| 4.000000 |       0.440000 |         -0.228409 |         -0.325720 |          0.711046 |   0.587901 |      0.497573 | 0.472406 | 0.253373 | -0.010321 | 0.004858 |
| 3.500000 |       0.620000 |         -0.673802 |         -0.742769 |          0.118144 |   0.470629 |      0.286762 | 0.589638 | 0.247543 | -0.010135 | 0.004746 |
| 3.000000 |       0.850000 |         -1.106599 |         -1.172674 |         -0.505694 |   0.338995 |      0.084649 | 0.715028 | 0.216128 | -0.008924 | 0.004144 |
| 2.500000 |       0.990000 |         -1.382576 |         -1.451068 |         -0.983524 |   0.206353 |      0.006911 | 0.834491 | 0.158349 | -0.006646 | 0.003036 |
| 1.500000 |       2.180000 |         -2.674338 |         -2.824136 |         -2.705161 |   0.025536 |      0.000000 | 0.982302 | 0.027779 | -0.001387 | 0.000533 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$7**

Market price: **$0.16**

Expected profit (USD): **2.46** [lowest: 2.12, highest: 3.76]

Delta: 0.0953 (price sensitivity)

Gamma: 0.1078 (delta sensitivity)

Theta: $-0.0043 (negative decay per trading-day)

Vega: $0.0021 (volatility sensitivity per 1%)

ITM (In The Money) probability: **92.81%**

Profit probability: **94.61%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.18 | $2.03 | 1.91 | 1.6372 | 0.15 |
| $2 | $0.99 | $1.28 | 1.66 | 1.6372 | -0.29 |
| $3 | $0.85 | $1.00 | 1.62 | 1.6372 | -0.15 |
| $4 | $0.62 | $0.79 | 1.53 | 1.6372 | -0.17 |
| $4 | $0.44 | $0.62 | 1.47 | 1.6372 | -0.18 |
| $4 | $0.30 | $0.48 | 1.38 | 1.6372 | -0.18 |
| $5 | $0.22 | $0.38 | 1.39 | 1.6372 | -0.16 |
| $6 | $0.08 | $0.30 | 1.51 | 1.6372 | -0.22 |
| $6 | $0.14 | $0.24 | 1.53 | 1.6372 | -0.10 |
| $6 | $0.13 | $0.19 | 1.71 | 1.6372 | -0.06 |
| $7 | $0.16 | $0.15 | 2.04 | 1.6372 | 0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **13.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 6.000000 |       0.080000 |          1.616211 |          1.317900 |          3.066543 |   0.838636 |      0.882498 | 0.208922 | 0.163364 | -0.006761 | 0.003883 |
| 5.000000 |       0.180000 |          0.725297 |          0.496293 |          2.010327 |   0.735040 |      0.769969 | 0.326561 | 0.205034 | -0.008513 | 0.004873 |
| 4.000000 |       0.360000 |         -0.114628 |         -0.235353 |          0.959754 |   0.574020 |      0.542808 | 0.496841 | 0.226815 | -0.009472 | 0.005391 |
| 3.500000 |       0.450000 |         -0.466049 |         -0.555622 |          0.446392 |   0.469079 |      0.380453 | 0.601135 | 0.219494 | -0.009211 | 0.005217 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$6**

Market price: **$0.08**

Expected profit (USD): **1.62** [lowest: 1.32, highest: 3.07]

Delta: 0.2089 (price sensitivity)

Gamma: 0.1634 (delta sensitivity)

Theta: $-0.0068 (negative decay per trading-day)

Vega: $0.0039 (volatility sensitivity per 1%)

ITM (In The Money) probability: **83.86%**

Profit probability: **88.25%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $4 | $0.45 | $0.87 | 1.45 | 1.6372 | -0.42 |
| $4 | $0.36 | $0.70 | 1.39 | 1.6372 | -0.34 |
| $5 | $0.18 | $0.46 | 2.07 | 1.6372 | -0.28 |
| $6 | $0.08 | $0.31 | 1.52 | 1.6372 | -0.23 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       0.130000 |          2.403421 |          1.975911 |          4.138023 |   0.878621 |      0.923542 | 0.167236 | 0.129604 | -0.005464 | 0.003682 |
| 6.000000 |       0.200000 |          1.485030 |          1.146122 |          3.106757 |   0.813392 |      0.863915 | 0.245887 | 0.163027 | -0.006888 | 0.004632 |
| 5.000000 |       0.300000 |          0.618339 |          0.376569 |          2.068310 |   0.712965 |      0.751456 | 0.359763 | 0.193595 | -0.008207 | 0.005500 |
| 4.000000 |       0.530000 |         -0.254526 |         -0.401368 |          0.939268 |   0.563615 |      0.521899 | 0.517083 | 0.206298 | -0.008796 | 0.005861 |
| 3.000000 |       0.920000 |         -1.110445 |         -1.201477 |         -0.295540 |   0.360159 |      0.139652 | 0.712604 | 0.176421 | -0.007613 | 0.005012 |
| 2.000000 |       1.500000 |         -1.937617 |         -2.023797 |         -1.587522 |   0.138218 |      0.000000 | 0.901706 | 0.089700 | -0.004023 | 0.002549 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$7**

Market price: **$0.13**

Expected profit (USD): **2.40** [lowest: 1.98, highest: 4.14]

Delta: 0.1672 (price sensitivity)

Gamma: 0.1296 (delta sensitivity)

Theta: $-0.0055 (negative decay per trading-day)

Vega: $0.0037 (volatility sensitivity per 1%)

ITM (In The Money) probability: **87.86%**

Profit probability: **92.35%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.50 | $1.70 | 1.59 | 1.6372 | -0.20 |
| $3 | $0.92 | $1.15 | 1.41 | 1.6372 | -0.23 |
| $4 | $0.53 | $0.78 | 1.43 | 1.6372 | -0.25 |
| $5 | $0.30 | $0.54 | 1.35 | 1.6372 | -0.24 |
| $6 | $0.20 | $0.38 | 1.38 | 1.6372 | -0.18 |
| $7 | $0.13 | $0.27 | 1.38 | 1.6372 | -0.14 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 8

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 12

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.000000 |       0.080000 |          6.838877 |          5.786885 |          9.654145 |   0.946553 |      0.981211 | 0.092630 | 0.065747 | -0.002914 | 0.003107 |
| 11.000000 |       0.070000 |          5.909178 |          4.924859 |          8.668734 |   0.932191 |      0.974670 | 0.114154 | 0.076522 | -0.003395 | 0.003617 |
| 10.000000 |       0.120000 |          4.936025 |          4.031111 |          7.628012 |   0.913221 |      0.964698 | 0.141573 | 0.088882 | -0.003946 | 0.004201 |
|  9.000000 |       0.120000 |          4.034837 |          3.220752 |          6.641714 |   0.887922 |      0.950788 | 0.176712 | 0.102792 | -0.004569 | 0.004858 |
|  8.000000 |       0.170000 |          3.113093 |          2.403744 |          5.613117 |   0.853854 |      0.928935 | 0.221979 | 0.117949 | -0.005250 | 0.005574 |
|  7.000000 |       0.220000 |          2.231189 |          1.632245 |          4.586178 |   0.807561 |      0.895202 | 0.280498 | 0.133524 | -0.005954 | 0.006310 |
|  6.000000 |       0.300000 |          1.373641 |          0.890137 |          3.535018 |   0.744199 |      0.839989 | 0.356152 | 0.147714 | -0.006602 | 0.006981 |
|  5.000000 |       0.450000 |          0.520645 |          0.161626 |          2.433020 |   0.657221 |      0.742057 | 0.453308 | 0.157023 | -0.007043 | 0.007421 |
|  4.000000 |       0.660000 |         -0.290276 |         -0.531501 |          1.292168 |   0.538691 |      0.563643 | 0.575520 | 0.155265 | -0.007003 | 0.007338 |
|  3.000000 |       1.000000 |         -1.093973 |         -1.240537 |          0.058840 |   0.382231 |      0.235711 | 0.721468 | 0.133068 | -0.006064 | 0.006289 |
|  2.000000 |       1.650000 |         -2.034046 |         -2.139352 |         -1.416876 |   0.195216 |      0.000000 | 0.874189 | 0.081952 | -0.003833 | 0.003873 |
|  1.000000 |       2.400000 |         -2.892108 |         -3.010735 |         -2.812514 |   0.034777 |      0.000000 | 0.982240 | 0.017344 | -0.000935 | 0.000820 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$0.08**

Expected profit (USD): **6.84** [lowest: 5.79, highest: 9.65]

Delta: 0.0926 (price sensitivity)

Gamma: 0.0657 (delta sensitivity)

Theta: $-0.0029 (negative decay per trading-day)

Vega: $0.0031 (volatility sensitivity per 1%)

ITM (In The Money) probability: **94.66%**

Profit probability: **98.12%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $2.40 | $2.55 | 3.14 | 1.6372 | -0.15 |
| $2 | $1.65 | $1.85 | 1.66 | 1.6372 | -0.20 |
| $3 | $1.00 | $1.37 | 1.27 | 1.6372 | -0.37 |
| $4 | $0.66 | $1.04 | 1.34 | 1.6372 | -0.38 |
| $5 | $0.45 | $0.81 | 1.36 | 1.6372 | -0.36 |
| $6 | $0.30 | $0.64 | 1.32 | 1.6372 | -0.34 |
| $7 | $0.22 | $0.51 | 1.43 | 1.6372 | -0.29 |
| $8 | $0.17 | $0.41 | 1.45 | 1.6372 | -0.24 |
| $9 | $0.12 | $0.34 | 1.47 | 1.6372 | -0.22 |
| $10 | $0.12 | $0.28 | 1.65 | 1.6372 | -0.16 |
| $11 | $0.07 | $0.24 | 1.67 | 1.6372 | -0.17 |
| $12 | $0.08 | $0.20 | 1.55 | 1.6372 | -0.12 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 9

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **14** strikes prices..

Total of valuable options: 14

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 14.000000 |       0.200000 |          7.798189 |          5.589066 |         12.523374 |   0.873212 |      0.969473 | 0.254040 | 0.082587 | -0.003916 | 0.008970 |
| 13.000000 |       0.170000 |          6.961973 |          4.903981 |         11.556772 |   0.858867 |      0.964478 | 0.275798 | 0.086111 | -0.004086 | 0.009352 |
| 12.000000 |       0.200000 |          6.081233 |          4.180502 |         10.530010 |   0.842181 |      0.957913 | 0.300283 | 0.089639 | -0.004257 | 0.009735 |
| 11.000000 |       0.200000 |          5.248564 |          3.516080 |          9.538006 |   0.822629 |      0.949898 | 0.327959 | 0.093093 | -0.004425 | 0.010111 |
| 10.000000 |       0.180000 |          4.457154 |          2.888001 |          8.555110 |   0.799533 |      0.939932 | 0.359393 | 0.096355 | -0.004585 | 0.010465 |
|  9.000000 |       0.350000 |          3.500971 |          2.099883 |          7.381538 |   0.772006 |      0.924200 | 0.395276 | 0.099245 | -0.004729 | 0.010779 |
|  8.000000 |       0.380000 |          2.715010 |          1.498406 |          6.360012 |   0.738862 |      0.905364 | 0.436454 | 0.101501 | -0.004844 | 0.011024 |
|  7.000000 |       0.520000 |          1.855647 |          0.832842 |          5.235216 |   0.698499 |      0.876211 | 0.483961 | 0.102725 | -0.004912 | 0.011157 |
|  6.000000 |       0.630000 |          1.071143 |          0.240320 |          4.139005 |   0.648713 |      0.834503 | 0.539045 | 0.102315 | -0.004904 | 0.011112 |
|  5.000000 |       0.790000 |          0.292377 |         -0.348476 |          2.996148 |   0.586418 |      0.766733 | 0.603160 | 0.099351 | -0.004778 | 0.010790 |
|  4.000000 |       1.000000 |         -0.466094 |         -0.935269 |          1.798735 |   0.507270 |      0.645844 | 0.677834 | 0.092416 | -0.004466 | 0.010037 |
|  3.000000 |       1.360000 |         -1.284560 |         -1.596419 |          0.465285 |   0.405255 |      0.370662 | 0.764128 | 0.079354 | -0.003865 | 0.008618 |
|  2.000000 |       1.810000 |         -2.076535 |         -2.271904 |         -0.943420 |   0.273125 |      0.000000 | 0.860655 | 0.057176 | -0.002828 | 0.006210 |
|  1.000000 |       2.520000 |         -2.980069 |         -3.119067 |         -2.557432 |   0.110287 |      0.000000 | 0.955892 | 0.024036 | -0.001249 | 0.002610 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$14**

Market price: **$0.20**

Expected profit (USD): **7.80** [lowest: 5.59, highest: 12.52]

Delta: 0.2540 (price sensitivity)

Gamma: 0.0826 (delta sensitivity)

Theta: $-0.0039 (negative decay per trading-day)

Vega: $0.0090 (volatility sensitivity per 1%)

ITM (In The Money) probability: **87.32%**

Profit probability: **96.95%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $2.52 | $2.70 | 1.14 | 1.6372 | -0.18 |
| $2 | $1.81 | $2.21 | 1.24 | 1.6372 | -0.40 |
| $3 | $1.36 | $1.86 | 1.29 | 1.6372 | -0.50 |
| $4 | $1.00 | $1.61 | 1.35 | 1.6372 | -0.61 |
| $5 | $0.79 | $1.41 | 1.29 | 1.6372 | -0.62 |
| $6 | $0.63 | $1.25 | 1.29 | 1.6372 | -0.62 |
| $7 | $0.52 | $1.12 | 1.25 | 1.6372 | -0.60 |
| $8 | $0.38 | $1.01 | 1.41 | 1.6372 | -0.63 |
| $9 | $0.35 | $0.92 | 1.54 | 1.6372 | -0.57 |
| $10 | $0.18 | $0.84 | 1.52 | 1.6372 | -0.66 |
| $11 | $0.20 | $0.78 | 1.34 | 1.6372 | -0.58 |
| $12 | $0.20 | $0.72 | 1.41 | 1.6372 | -0.52 |
| $13 | $0.17 | $0.66 | 1.43 | 1.6372 | -0.49 |
| $14 | $0.20 | $0.62 | 1.40 | 1.6372 | -0.42 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 10

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.000000 |       0.710000 |          4.968767 |          1.946276 |         10.645237 |   0.721342 |      0.954117 | 0.570180 | 0.065900 | -0.003267 | 0.016651 |
| 10.000000 |       0.840000 |          3.431438 |          0.992499 |          8.515231 |   0.684520 |      0.940354 | 0.611523 | 0.064305 | -0.003194 | 0.016248 |
|  7.000000 |       1.070000 |          1.255421 |         -0.318929 |          5.277987 |   0.607232 |      0.900638 | 0.688483 | 0.059320 | -0.002960 | 0.014988 |
|  5.000000 |       1.390000 |         -0.206715 |         -1.229732 |          2.949921 |   0.530149 |      0.831416 | 0.754281 | 0.052830 | -0.002649 | 0.013349 |
|  3.000000 |       1.800000 |         -1.568384 |         -2.096993 |          0.528183 |   0.411912 |      0.535459 | 0.838006 | 0.041156 | -0.002084 | 0.010399 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$0.71**

Expected profit (USD): **4.97** [lowest: 1.95, highest: 10.65]

Delta: 0.5702 (price sensitivity)

Gamma: 0.0659 (delta sensitivity)

Theta: $-0.0033 (negative decay per trading-day)

Vega: $0.0167 (volatility sensitivity per 1%)

ITM (In The Money) probability: **72.13%**

Profit probability: **95.41%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $1.80 | $2.49 | 1.23 | 1.6372 | -0.69 |
| $5 | $1.39 | $2.21 | 1.28 | 1.6372 | -0.82 |
| $7 | $1.07 | $2.00 | 1.28 | 1.6372 | -0.93 |
| $10 | $0.84 | $1.78 | 1.28 | 1.6372 | -0.94 |
| $12 | $0.71 | $1.66 | 1.30 | 1.6372 | -0.95 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 11

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **1.1450 [-2.2691, 2.1520]**

- Stock Volatility: **1.6372 [1.3898, 1.9163]**

- Based on **531** observations


- Garch Volatility forecast: **1.2822**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.000000 |       1.440000 |          3.775530 |         -0.155182 |          9.988465 |   0.629758 |      0.970569 | 0.778250 | 0.035176 | -0.001787 | 0.017797 |
| 10.000000 |       1.550000 |          2.433704 |         -0.730857 |          7.870039 |   0.601093 |      0.963461 | 0.799919 | 0.033117 | -0.001685 | 0.016756 |
|  7.000000 |       1.840000 |          0.421230 |         -1.632378 |          4.569648 |   0.543552 |      0.942084 | 0.838453 | 0.028956 | -0.001479 | 0.014650 |
|  5.000000 |       1.960000 |         -0.733858 |         -2.082067 |          2.452571 |   0.488397 |      0.907042 | 0.870044 | 0.025012 | -0.001283 | 0.012655 |
|  3.000000 |       2.340000 |         -2.014333 |         -2.745739 |          0.052174 |   0.405428 |      0.573354 | 0.909361 | 0.019306 | -0.000997 | 0.009768 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$1.44**

Expected profit (USD): **3.78** [lowest: -0.16, highest: 9.99]

Delta: 0.7782 (price sensitivity)

Gamma: 0.0352 (delta sensitivity)

Theta: $-0.0018 (negative decay per trading-day)

Vega: $0.0178 (volatility sensitivity per 1%)

ITM (In The Money) probability: **62.98%**

Profit probability: **97.06%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $2.34 | $3.00 | 1.26 | 1.6372 | -0.66 |
| $5 | $1.96 | $2.86 | 1.32 | 1.6372 | -0.90 |
| $7 | $1.84 | $2.76 | 1.28 | 1.6372 | -0.92 |
| $10 | $1.55 | $2.64 | 1.30 | 1.6372 | -1.09 |
| $12 | $1.44 | $2.57 | 1.27 | 1.6372 | -1.13 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **532** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **1.0123**

- Modal profit prediction correlation: **-0.9654**

- Backtests total: **4**

- Profitable Trades (profitable trades / total trades): **25.00%**

--------------------------------------------------

