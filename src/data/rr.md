# RR Option Analysis From: 05.01.2026 03:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

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
| 2.000000 |       1.310000 |         -0.282238 |         -0.514428 |         -0.331167 |   0.999992 |      0.217629 | 0.999993 | 0.000074 | -0.000399 | 0.000000 |
| 2.500000 |       1.000000 |         -0.471759 |         -0.648799 |         -0.463177 |   0.995144 |      0.124079 | 0.995545 | 0.028856 | -0.001475 | 0.000050 |
| 1.500000 |       2.000000 |         -0.472238 |         -0.741727 |         -0.558674 |   1.000000 |      0.124079 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |
| 3.000000 |       0.550000 |         -0.500775 |         -0.615231 |         -0.433705 |   0.881490 |      0.105565 | 0.887250 | 0.423350 | -0.014932 | 0.000727 |
| 3.500000 |       0.310000 |         -0.613800 |         -0.650404 |         -0.500322 |   0.498349 |      0.041867 | 0.510141 | 0.882170 | -0.030368 | 0.001514 |
| 4.000000 |       0.160000 |         -0.616785 |         -0.618614 |         -0.526535 |   0.151030 |      0.009891 | 0.158060 | 0.533918 | -0.018289 | 0.000916 |
| 1.000000 |       3.500000 |         -1.472238 |         -1.796310 |         -1.613258 |   1.000000 |      0.002036 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 4.500000 |       0.080000 |         -0.573886 |         -0.573739 |         -0.529524 |   0.026270 |      0.001373 | 0.028123 | 0.142641 | -0.004877 | 0.000245 |
| 5.000000 |       0.040000 |         -0.539393 |         -0.540202 |         -0.522866 |   0.002982 |      0.000125 | 0.003263 | 0.021825 | -0.000746 | 0.000037 |
| 5.500000 |       0.030000 |         -0.529954 |         -0.531186 |         -0.525247 |   0.000248 |      0.000008 | 0.000276 | 0.002267 | -0.000077 | 0.000004 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.31**

Expected profit (USD): **-0.28** [lowest: -0.51, highest: -0.33]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0004 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **21.76%**

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
| 2.000000 |       1.350000 |         -0.206754 |         -0.721322 |         -0.115430 |   0.990344 |      0.284850 | 0.991903 | 0.026142 | -0.001329 | 0.000154 |
| 1.000000 |       2.450000 |         -0.308229 |         -0.890191 |         -0.280283 |   1.000000 |      0.250220 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 0.500000 |       3.030000 |         -0.388229 |         -0.986205 |         -0.376313 |   1.000000 |      0.224782 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |
| 2.500000 |       1.110000 |         -0.448908 |         -0.906708 |         -0.327341 |   0.922644 |      0.201335 | 0.931643 | 0.155572 | -0.006028 | 0.000914 |
| 3.000000 |       0.630000 |         -0.391236 |         -0.694509 |         -0.178726 |   0.749956 |      0.195778 | 0.770171 | 0.358177 | -0.013270 | 0.002104 |
| 3.500000 |       0.450000 |         -0.528508 |         -0.713574 |         -0.290096 |   0.516475 |      0.122361 | 0.542355 | 0.468125 | -0.017117 | 0.002750 |
| 4.000000 |       0.290000 |         -0.571857 |         -0.668736 |         -0.340871 |   0.306057 |      0.071376 | 0.329245 | 0.426969 | -0.015525 | 0.002508 |
| 4.500000 |       0.180000 |         -0.575715 |         -0.620107 |         -0.375917 |   0.160903 |      0.036963 | 0.177303 | 0.306721 | -0.011121 | 0.001802 |
| 5.000000 |       0.120000 |         -0.573102 |         -0.591450 |         -0.416603 |   0.077306 |      0.016924 | 0.087173 | 0.187130 | -0.006773 | 0.001099 |
| 6.000000 |       0.060000 |         -0.551615 |         -0.554629 |         -0.471174 |   0.014922 |      0.002917 | 0.017554 | 0.051134 | -0.001847 | 0.000300 |
| 6.500000 |       0.040000 |         -0.536589 |         -0.538036 |         -0.481509 |   0.006194 |      0.001156 | 0.007429 | 0.024235 | -0.000875 | 0.000142 |
| 7.000000 |       0.030000 |         -0.528633 |         -0.530780 |         -0.492729 |   0.002514 |      0.000445 | 0.003071 | 0.011025 | -0.000398 | 0.000065 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.35**

Expected profit (USD): **-0.21** [lowest: -0.72, highest: -0.12]

Delta: 0.9919 (price sensitivity)

Gamma: 0.0261 (delta sensitivity)

Theta: $-0.0013 (negative decay per trading-day)

Vega: $0.0002 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.03%**

Profit probability: **28.48%**

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
| 2.000000 |       1.200000 |          0.068071 |         -0.746389 |          0.258019 |   0.962840 |      0.347607 | 0.970012 | 0.060289 | -0.002629 | 0.000615 |
| 3.000000 |       0.650000 |         -0.235090 |         -0.727455 |          0.104098 |   0.703318 |      0.227889 | 0.735754 | 0.289900 | -0.011221 | 0.002956 |
| 2.500000 |       1.260000 |         -0.451579 |         -1.140898 |         -0.204718 |   0.863536 |      0.204257 | 0.883503 | 0.173631 | -0.006899 | 0.001771 |
| 3.500000 |       0.470000 |         -0.361637 |         -0.708412 |         -0.000569 |   0.523319 |      0.164796 | 0.561521 | 0.349393 | -0.013380 | 0.003563 |
| 4.000000 |       0.330000 |         -0.441635 |         -0.672553 |         -0.089668 |   0.361896 |      0.112401 | 0.398569 | 0.342114 | -0.013030 | 0.003489 |
| 4.500000 |       0.220000 |         -0.479681 |         -0.625200 |         -0.156621 |   0.236780 |      0.073060 | 0.267511 | 0.291710 | -0.011074 | 0.002975 |
| 5.000000 |       0.160000 |         -0.514641 |         -0.605127 |         -0.231660 |   0.148778 |      0.044285 | 0.172241 | 0.226183 | -0.008569 | 0.002307 |
| 5.500000 |       0.100000 |         -0.513474 |         -0.567765 |         -0.270553 |   0.090828 |      0.026562 | 0.107611 | 0.164056 | -0.006206 | 0.001673 |
| 6.000000 |       0.070000 |         -0.519039 |         -0.552047 |         -0.317174 |   0.054350 |      0.015276 | 0.065813 | 0.113474 | -0.004288 | 0.001157 |
| 6.500000 |       0.060000 |         -0.530181 |         -0.552246 |         -0.367383 |   0.032088 |      0.008546 | 0.039663 | 0.075857 | -0.002864 | 0.000774 |
| 8.000000 |       0.050000 |         -0.544092 |         -0.552676 |         -0.463035 |   0.006362 |      0.001463 | 0.008308 | 0.020085 | -0.000757 | 0.000205 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.20**

Expected profit (USD): **0.07** [lowest: -0.75, highest: 0.26]

Delta: 0.9700 (price sensitivity)

Gamma: 0.0603 (delta sensitivity)

Theta: $-0.0026 (negative decay per trading-day)

Vega: $0.0006 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.28%**

Profit probability: **34.76%**

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
| 1.500000 |       1.480000 |          0.403296 |         -0.759058 |          0.687963 |   0.987152 |      0.403881 | 0.990771 | 0.018226 | -0.000995 | 0.000267 |
| 2.000000 |       1.210000 |          0.191009 |         -0.865586 |          0.521945 |   0.932726 |      0.342120 | 0.947591 | 0.078540 | -0.003393 | 0.001150 |
| 2.500000 |       1.100000 |         -0.139997 |         -1.024793 |          0.258632 |   0.822982 |      0.254037 | 0.853672 | 0.168217 | -0.006881 | 0.002463 |
| 3.000000 |       0.840000 |         -0.256008 |         -0.945774 |          0.202914 |   0.677735 |      0.209817 | 0.721364 | 0.246340 | -0.009880 | 0.003607 |
| 3.500000 |       0.490000 |         -0.206886 |         -0.723972 |          0.277813 |   0.527057 |      0.185716 | 0.576676 | 0.287217 | -0.011412 | 0.004205 |
| 4.000000 |       0.350000 |         -0.295812 |         -0.674579 |          0.182757 |   0.392430 |      0.137708 | 0.441381 | 0.289474 | -0.011441 | 0.004238 |
| 4.500000 |       0.250000 |         -0.363580 |         -0.635738 |          0.088464 |   0.283100 |      0.098010 | 0.327028 | 0.264681 | -0.010426 | 0.003875 |
| 5.000000 |       0.180000 |         -0.413260 |         -0.604930 |          0.001575 |   0.199723 |      0.067597 | 0.236660 | 0.226293 | -0.008894 | 0.003313 |
| 5.500000 |       0.120000 |         -0.437044 |         -0.570843 |         -0.065594 |   0.138759 |      0.046053 | 0.168430 | 0.184522 | -0.007240 | 0.002702 |
| 6.000000 |       0.100000 |         -0.474957 |         -0.564808 |         -0.145136 |   0.095432 |      0.030249 | 0.118503 | 0.145443 | -0.005700 | 0.002129 |
| 6.500000 |       0.080000 |         -0.494658 |         -0.561838 |         -0.210285 |   0.065222 |      0.019874 | 0.082747 | 0.111865 | -0.004380 | 0.001638 |
| 7.500000 |       0.070000 |         -0.530175 |         -0.564208 |         -0.316288 |   0.030215 |      0.008414 | 0.039877 | 0.063053 | -0.002465 | 0.000923 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.48**

Expected profit (USD): **0.40** [lowest: -0.76, highest: 0.69]

Delta: 0.9908 (price sensitivity)

Gamma: 0.0182 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0003 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.72%**

Profit probability: **40.39%**

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
| 2.500000 |       0.990000 |          0.123808 |         -0.959346 |          0.671801 |   0.793647 |      0.280332 | 0.834491 | 0.158349 | -0.006646 | 0.003036 |
| 1.500000 |       2.180000 |         -0.167954 |         -1.624867 |          0.230783 |   0.974464 |      0.246697 | 0.982302 | 0.027779 | -0.001387 | 0.000533 |
| 3.000000 |       0.850000 |         -0.100214 |         -0.989263 |          0.483504 |   0.661005 |      0.219690 | 0.715028 | 0.216128 | -0.008924 | 0.004144 |
| 3.500000 |       0.620000 |         -0.167418 |         -0.863063 |          0.444292 |   0.529371 |      0.182294 | 0.589638 | 0.247543 | -0.010135 | 0.004746 |
| 4.000000 |       0.440000 |         -0.222025 |         -0.761869 |          0.385122 |   0.412099 |      0.145706 | 0.472406 | 0.253373 | -0.010321 | 0.004858 |
| 4.500000 |       0.300000 |         -0.262825 |         -0.675505 |          0.323061 |   0.314513 |      0.112973 | 0.370635 | 0.240508 | -0.009764 | 0.004611 |
| 5.000000 |       0.220000 |         -0.319869 |         -0.633496 |          0.231705 |   0.236834 |      0.083820 | 0.286514 | 0.216684 | -0.008776 | 0.004154 |
| 5.500000 |       0.080000 |         -0.282602 |         -0.518498 |          0.229148 |   0.176786 |      0.064879 | 0.219242 | 0.188131 | -0.007606 | 0.003607 |
| 6.000000 |       0.140000 |         -0.419075 |         -0.600503 |          0.044805 |   0.131260 |      0.043609 | 0.166639 | 0.159048 | -0.006421 | 0.003049 |
| 6.500000 |       0.130000 |         -0.465767 |         -0.606280 |         -0.049358 |   0.097180 |      0.030881 | 0.126133 | 0.131881 | -0.005319 | 0.002528 |
| 7.000000 |       0.160000 |         -0.537714 |         -0.651373 |         -0.170413 |   0.071874 |      0.021339 | 0.095259 | 0.107819 | -0.004345 | 0.002067 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$0.99**

Expected profit (USD): **0.12** [lowest: -0.96, highest: 0.67]

Delta: 0.8345 (price sensitivity)

Gamma: 0.1583 (delta sensitivity)

Theta: $-0.0066 (negative decay per trading-day)

Vega: $0.0030 (volatility sensitivity per 1%)

ITM (In The Money) probability: **79.36%**

Profit probability: **28.03%**

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
| 3.500000 |       0.450000 |          0.169812 |         -0.699536 |          0.926467 |   0.530921 |      0.212607 | 0.601135 | 0.219494 | -0.009211 | 0.005217 |
| 4.000000 |       0.360000 |          0.021234 |         -0.678195 |          0.774019 |   0.425980 |      0.165578 | 0.496841 | 0.226815 | -0.009472 | 0.005391 |
| 5.000000 |       0.180000 |         -0.138842 |         -0.606570 |          0.537854 |   0.264960 |      0.100224 | 0.326561 | 0.205034 | -0.008513 | 0.004873 |
| 6.000000 |       0.080000 |         -0.247928 |         -0.530024 |          0.366984 |   0.161364 |      0.058057 | 0.208922 | 0.163364 | -0.006761 | 0.003883 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$4**

Market price: **$0.45**

Expected profit (USD): **0.17** [lowest: -0.70, highest: 0.93]

Delta: 0.6011 (price sensitivity)

Gamma: 0.2195 (delta sensitivity)

Theta: $-0.0092 (negative decay per trading-day)

Vega: $0.0052 (volatility sensitivity per 1%)

ITM (In The Money) probability: **53.09%**

Profit probability: **21.26%**

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
| 2.000000 |       1.500000 |          0.331905 |         -1.372282 |          1.154403 |   0.861782 |      0.277194 | 0.901706 | 0.089700 | -0.004023 | 0.002549 |
| 3.000000 |       0.920000 |          0.159078 |         -1.098172 |          1.054745 |   0.639841 |      0.220342 | 0.712604 | 0.176421 | -0.007613 | 0.005012 |
| 4.000000 |       0.530000 |          0.014996 |         -0.851925 |          0.921765 |   0.436385 |      0.157713 | 0.517083 | 0.206298 | -0.008796 | 0.005861 |
| 5.000000 |       0.300000 |         -0.112138 |         -0.703350 |          0.740159 |   0.287035 |      0.103752 | 0.359763 | 0.193595 | -0.008207 | 0.005500 |
| 6.000000 |       0.200000 |         -0.245448 |         -0.645940 |          0.526583 |   0.186608 |      0.064220 | 0.245887 | 0.163027 | -0.006888 | 0.004632 |
| 7.000000 |       0.130000 |         -0.327057 |         -0.598790 |          0.356401 |   0.121379 |      0.039681 | 0.167236 | 0.129604 | -0.005464 | 0.003682 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.50**

Expected profit (USD): **0.33** [lowest: -1.37, highest: 1.15]

Delta: 0.9017 (price sensitivity)

Gamma: 0.0897 (delta sensitivity)

Theta: $-0.0040 (negative decay per trading-day)

Vega: $0.0025 (volatility sensitivity per 1%)

ITM (In The Money) probability: **86.18%**

Profit probability: **27.72%**

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
|  1.000000 |       2.400000 |          0.956675 |         -2.074843 |          2.498950 |   0.965223 |      0.275037 | 0.982240 | 0.017344 | -0.000935 | 0.000820 |
|  2.000000 |       1.650000 |          0.814736 |         -1.729171 |          2.442769 |   0.804784 |      0.247196 | 0.874189 | 0.081952 | -0.003833 | 0.003873 |
|  3.000000 |       1.000000 |          0.754810 |         -1.258396 |          2.434897 |   0.617769 |      0.213304 | 0.721468 | 0.133068 | -0.006064 | 0.006289 |
|  4.000000 |       0.660000 |          0.558506 |         -1.013806 |          2.228253 |   0.461309 |      0.162616 | 0.575520 | 0.155265 | -0.007003 | 0.007338 |
|  5.000000 |       0.450000 |          0.369427 |         -0.857981 |          1.987272 |   0.342779 |      0.118954 | 0.453308 | 0.157023 | -0.007043 | 0.007421 |
|  6.000000 |       0.300000 |          0.222423 |         -0.741604 |          1.762765 |   0.255801 |      0.086222 | 0.356152 | 0.147714 | -0.006602 | 0.006981 |
|  7.000000 |       0.220000 |          0.079971 |         -0.677904 |          1.535576 |   0.192439 |      0.061853 | 0.280498 | 0.133524 | -0.005954 | 0.006310 |
|  8.000000 |       0.170000 |         -0.038125 |         -0.640423 |          1.324793 |   0.146146 |      0.044616 | 0.221979 | 0.117949 | -0.005250 | 0.005574 |
|  9.000000 |       0.120000 |         -0.116380 |         -0.603091 |          1.149578 |   0.112078 |      0.032675 | 0.176712 | 0.102792 | -0.004569 | 0.004858 |
| 10.000000 |       0.120000 |         -0.215193 |         -0.609585 |          0.960311 |   0.086779 |      0.023894 | 0.141573 | 0.088882 | -0.003946 | 0.004201 |
| 11.000000 |       0.070000 |         -0.242040 |         -0.562909 |          0.849046 |   0.067809 |      0.017978 | 0.114154 | 0.076522 | -0.003395 | 0.003617 |
| 12.000000 |       0.080000 |         -0.312341 |         -0.572565 |          0.702227 |   0.053447 |      0.013454 | 0.092630 | 0.065747 | -0.002914 | 0.003107 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$2.40**

Expected profit (USD): **0.96** [lowest: -2.07, highest: 2.50]

Delta: 0.9822 (price sensitivity)

Gamma: 0.0173 (delta sensitivity)

Theta: $-0.0009 (negative decay per trading-day)

Vega: $0.0008 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.52%**

Profit probability: **27.50%**

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
|  1.000000 |       2.520000 |          3.318417 |         -2.827105 |          9.922447 |   0.889713 |      0.211827 | 0.955892 | 0.024036 | -0.001249 | 0.002610 |
|  2.000000 |       1.810000 |          3.221951 |         -2.222040 |          9.872090 |   0.726875 |      0.194188 | 0.860655 | 0.057176 | -0.002828 | 0.006210 |
|  3.000000 |       1.360000 |          3.013926 |         -1.808744 |          9.667658 |   0.594745 |      0.165955 | 0.764128 | 0.079354 | -0.003865 | 0.008618 |
|  4.000000 |       1.000000 |          2.832392 |         -1.468263 |          9.449072 |   0.492730 |      0.139801 | 0.677834 | 0.092416 | -0.004466 | 0.010037 |
|  5.000000 |       0.790000 |          2.590863 |         -1.263900 |          9.149526 |   0.413582 |      0.114764 | 0.603160 | 0.099351 | -0.004778 | 0.010790 |
|  6.000000 |       0.630000 |          2.369629 |         -1.114784 |          8.842917 |   0.351287 |      0.094425 | 0.539045 | 0.102315 | -0.004904 | 0.011112 |
|  7.000000 |       0.520000 |          2.154133 |         -1.013096 |          8.530368 |   0.301501 |      0.077880 | 0.483961 | 0.102725 | -0.004912 | 0.011157 |
|  8.000000 |       0.380000 |          2.013496 |         -0.883544 |          8.281430 |   0.261138 |      0.065416 | 0.436454 | 0.101501 | -0.004844 | 0.011024 |
|  9.000000 |       0.350000 |          1.799457 |         -0.857889 |          7.959559 |   0.227994 |      0.054379 | 0.395276 | 0.099245 | -0.004729 | 0.010779 |
| 10.000000 |       0.180000 |          1.755640 |         -0.680722 |          7.816204 |   0.200467 |      0.046834 | 0.359393 | 0.096355 | -0.004585 | 0.010465 |
| 11.000000 |       0.200000 |          1.547050 |         -0.694682 |          7.505428 |   0.177371 |      0.039360 | 0.327959 | 0.093093 | -0.004425 | 0.010111 |
| 12.000000 |       0.200000 |          1.379719 |         -0.699914 |          7.224329 |   0.157819 |      0.033498 | 0.300283 | 0.089639 | -0.004257 | 0.009735 |
| 13.000000 |       0.170000 |          1.260459 |         -0.670711 |          6.996289 |   0.141133 |      0.028867 | 0.275798 | 0.086111 | -0.004086 | 0.009352 |
| 14.000000 |       0.200000 |          1.096675 |         -0.701943 |          6.724462 |   0.126788 |      0.024831 | 0.254040 | 0.082587 | -0.003916 | 0.008970 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$2.52**

Expected profit (USD): **3.32** [lowest: -2.83, highest: 9.92]

Delta: 0.9559 (price sensitivity)

Gamma: 0.0240 (delta sensitivity)

Theta: $-0.0012 (negative decay per trading-day)

Vega: $0.0026 (volatility sensitivity per 1%)

ITM (In The Money) probability: **88.97%**

Profit probability: **21.18%**

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
|  3.000000 |       1.800000 |         14.468961 |         -2.366911 |         80.113225 |   0.588088 |      0.101856 | 0.838006 | 0.041156 | -0.002084 | 0.010399 |
|  5.000000 |       1.390000 |         13.830630 |         -1.942715 |         79.308897 |   0.469851 |      0.077188 | 0.754281 | 0.052830 | -0.002649 | 0.013349 |
|  7.000000 |       1.070000 |         13.292766 |         -1.612913 |         78.551195 |   0.392768 |      0.060373 | 0.688483 | 0.059320 | -0.002960 | 0.014988 |
| 10.000000 |       0.840000 |         12.468783 |         -1.373852 |         77.344395 |   0.315480 |      0.043156 | 0.611523 | 0.064305 | -0.003194 | 0.016248 |
| 12.000000 |       0.710000 |         12.006112 |         -1.242957 |         76.604725 |   0.278658 |      0.035591 | 0.570180 | 0.065900 | -0.003267 | 0.016651 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$1.80**

Expected profit (USD): **14.47** [lowest: -2.37, highest: 80.11]

Delta: 0.8380 (price sensitivity)

Gamma: 0.0412 (delta sensitivity)

Theta: $-0.0021 (negative decay per trading-day)

Vega: $0.0104 (volatility sensitivity per 1%)

ITM (In The Money) probability: **58.81%**

Profit probability: **10.19%**

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
|  3.000000 |       2.340000 |         97.719506 |         -2.944181 |       2011.071046 |   0.594572 |      0.047916 | 0.909361 | 0.019306 | -0.000997 | 0.009768 |
|  5.000000 |       1.960000 |         96.999981 |         -2.543695 |       2010.124000 |   0.511603 |      0.038684 | 0.870044 | 0.025012 | -0.001283 | 0.012655 |
|  7.000000 |       1.840000 |         96.155069 |         -2.426560 |       2008.987703 |   0.456448 |      0.031538 | 0.838453 | 0.028956 | -0.001479 | 0.014650 |
| 10.000000 |       1.550000 |         95.167543 |         -2.126110 |       2007.532933 |   0.398907 |      0.024794 | 0.799919 | 0.033117 | -0.001685 | 0.016756 |
| 12.000000 |       1.440000 |         94.509369 |         -2.007656 |       2006.545445 |   0.370242 |      0.021513 | 0.778250 | 0.035176 | -0.001787 | 0.017797 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$2.34**

Expected profit (USD): **97.72** [lowest: -2.94, highest: 2011.07]

Delta: 0.9094 (price sensitivity)

Gamma: 0.0193 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0098 (volatility sensitivity per 1%)

ITM (In The Money) probability: **59.46%**

Profit probability: **4.79%**

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

