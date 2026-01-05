# Put Option. NVAX Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

## Current Stock Price: $7.130000114440918

### Calculate Stock Option Nr. 1

Expires At: **09.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **18** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 8.000000 |       0.040000 |          0.311052 |          0.332672 |          0.410111 |   0.970352 |      0.789160 | 0.030526 | 0.160877 | -0.004979 | 0.000537 |
| 7.500000 |       0.070000 |         -0.170048 |         -0.111507 |         -0.025591 |   0.792052 |      0.336851 | 0.211655 | 0.674766 | -0.020995 | 0.002252 |
| 7.000000 |       0.270000 |         -0.666338 |         -0.603012 |         -0.525615 |   0.369614 |      0.014244 | 0.635234 | 0.875809 | -0.027725 | 0.002923 |
| 6.000000 |       1.080000 |         -1.579804 |         -1.618029 |         -1.604498 |   0.001900 |      0.000000 | 0.998177 | 0.013584 | -0.001604 | 0.000045 |
| 5.000000 |       2.050000 |         -2.550000 |         -2.658974 |         -2.658873 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000991 | 0.000000 |
| 4.500000 |       2.530000 |         -3.030000 |         -3.107223 |         -3.107221 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000892 | 0.000000 |
| 3.500000 |       3.930000 |         -4.430000 |         -4.554571 |         -4.554571 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000694 | 0.000000 |
| 2.000000 |       5.550000 |         -6.050000 |         -6.227556 |         -6.227556 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000397 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$0.04**

Expected profit (USD): **0.31** [lowest: 0.33, highest: 0.41]

Delta: 0.0305 (price sensitivity)

Gamma: 0.1609 (delta sensitivity)

Theta: $-0.0050 (negative decay per trading-day)

Vega: $0.0005 (volatility sensitivity per 1%)

ITM (In The Money) probability: **97.04%**

Profit probability: **78.92%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $5.55 | $5.13 | 33.56 | 0.8926 | 0.42 |
| $4 | $3.93 | $3.63 | 7.38 | 0.8926 | 0.30 |
| $4 | $2.53 | $2.63 | 6.63 | 0.8926 | -0.10 |
| $5 | $2.05 | $2.13 | 10.45 | 0.8926 | -0.08 |
| $6 | $1.08 | $1.14 | 1.78 | 0.8926 | -0.06 |
| $7 | $0.27 | $0.35 | 0.57 | 0.8926 | -0.08 |
| $8 | $0.07 | $0.14 | 0.58 | 0.8926 | -0.07 |
| $8 | $0.04 | $0.04 | 0.88 | 0.8926 | -0.00 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **29** strikes prices..

Total of valuable options: 20

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 17.500000 |       0.010000 |          9.777717 |          9.770219 |          9.966186 |   1.000000 |      1.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 |
| 10.000000 |       0.030000 |          2.258375 |          2.261750 |          2.465971 |   0.998099 |      0.994746 | 0.002110 | 0.008101 | -0.000276 | 0.000095 |
|  9.500000 |       0.040000 |          1.750377 |          1.759146 |          1.969124 |   0.992836 |      0.981154 | 0.007845 | 0.026227 | -0.000896 | 0.000306 |
|  9.000000 |       0.050000 |          1.247393 |          1.278273 |          1.494619 |   0.976127 |      0.941736 | 0.025780 | 0.073003 | -0.002498 | 0.000852 |
|  8.000000 |       0.130000 |          0.245568 |          0.332398 |          0.551423 |   0.830794 |      0.648985 | 0.177622 | 0.316768 | -0.010924 | 0.003696 |
|  7.500000 |       0.250000 |         -0.248951 |         -0.139840 |          0.065229 |   0.654365 |      0.351918 | 0.357820 | 0.454471 | -0.015803 | 0.005303 |
|  7.000000 |       0.440000 |         -0.708803 |         -0.605605 |         -0.430713 |   0.420075 |      0.094070 | 0.592718 | 0.472475 | -0.016700 | 0.005513 |
|  6.500000 |       0.600000 |         -1.021224 |         -0.952512 |         -0.822264 |   0.199073 |      0.010253 | 0.809967 | 0.330380 | -0.012147 | 0.003855 |
|  6.000000 |       0.900000 |         -1.382294 |         -1.365883 |         -1.282570 |   0.061819 |      0.000104 | 0.942085 | 0.141045 | -0.005861 | 0.001646 |
|  5.500000 |       1.700000 |         -2.197728 |         -2.228790 |         -2.186665 |   0.010869 |      0.000000 | 0.990037 | 0.032339 | -0.002166 | 0.000377 |
|  5.000000 |       2.180000 |         -2.679862 |         -2.728430 |         -2.712764 |   0.000898 |      0.000000 | 0.999198 | 0.003348 | -0.001102 | 0.000039 |
|  4.500000 |       2.410000 |         -2.909997 |         -2.969206 |         -2.965256 |   0.000027 |      0.000000 | 0.999976 | 0.000123 | -0.000895 | 0.000001 |
|  4.000000 |       2.890000 |         -3.390000 |         -3.465094 |         -3.464489 |   0.000000 |      0.000000 | 1.000000 | 0.000001 | -0.000792 | 0.000000 |
|  3.500000 |       3.390000 |         -3.890000 |         -3.975424 |         -3.975377 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000693 | 0.000000 |
|  3.000000 |       3.700000 |         -4.200000 |         -4.291457 |         -4.291456 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000594 | 0.000000 |
|  2.500000 |       4.450000 |         -4.950000 |         -5.041457 |         -5.041457 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |
|  2.000000 |       5.160000 |         -5.660000 |         -5.781813 |         -5.781813 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000396 | 0.000000 |
|  1.000000 |       5.850000 |         -6.350000 |         -6.480375 |         -6.480375 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
|  0.500000 |       6.280000 |         -6.780000 |         -6.926526 |         -6.926526 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |
|  1.500000 |       6.750000 |         -7.250000 |         -7.393996 |         -7.393996 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$18**

Market price: **$0.01**

Expected profit (USD): **9.78** [lowest: 9.77, highest: 9.97]

Delta: 0.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0000 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **100.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $6.28 | $6.63 | 21.63 | 0.8926 | -0.35 |
| $1 | $5.85 | $6.13 | 11.47 | 0.8926 | -0.28 |
| $2 | $6.75 | $5.63 | 0.00 | 0.8926 | 1.12 |
| $2 | $5.16 | $5.13 | 4.44 | 0.8926 | 0.03 |
| $2 | $4.45 | $4.63 | 3.72 | 0.8926 | -0.18 |
| $3 | $3.70 | $4.14 | 2.44 | 0.8926 | -0.44 |
| $4 | $3.39 | $3.64 | 2.06 | 0.8926 | -0.25 |
| $4 | $2.89 | $3.14 | 1.91 | 0.8926 | -0.25 |
| $4 | $2.41 | $2.64 | 2.48 | 0.8926 | -0.23 |
| $5 | $2.18 | $2.15 | 0.88 | 0.8926 | 0.03 |
| $6 | $1.70 | $1.68 | 1.95 | 0.8926 | 0.02 |
| $6 | $0.90 | $1.24 | 1.04 | 0.8926 | -0.34 |
| $6 | $0.60 | $0.87 | 0.81 | 0.8926 | -0.27 |
| $7 | $0.44 | $0.58 | 0.77 | 0.8926 | -0.14 |
| $8 | $0.25 | $0.36 | 0.72 | 0.8926 | -0.11 |
| $8 | $0.13 | $0.21 | 0.63 | 0.8926 | -0.08 |
| $9 | $0.05 | $0.06 | 0.90 | 0.8926 | -0.01 |
| $10 | $0.04 | $0.03 | 1.45 | 0.8926 | 0.01 |
| $10 | $0.03 | $0.02 | 1.02 | 0.8926 | 0.01 |
| $18 | $0.01 | $0.00 | 2.13 | 0.8926 | 0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **23.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **10** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 8.000000 |       0.150000 |          0.275134 |          0.391845 |          0.720840 |   0.755456 |      0.625621 | 0.261231 | 0.292760 | -0.010959 | 0.006021 |
| 7.500000 |       0.270000 |         -0.187659 |         -0.057871 |          0.243597 |   0.609280 |      0.403052 | 0.410896 | 0.350199 | -0.013227 | 0.007203 |
| 7.000000 |       0.470000 |         -0.649236 |         -0.531321 |         -0.271063 |   0.434289 |      0.170926 | 0.586156 | 0.350787 | -0.013453 | 0.007215 |
| 6.500000 |       0.500000 |         -0.852142 |         -0.759438 |         -0.552366 |   0.260692 |      0.061645 | 0.755975 | 0.282437 | -0.011153 | 0.005809 |
| 5.500000 |       1.330000 |         -1.815669 |         -1.818659 |         -1.726846 |   0.043297 |      0.000018 | 0.961289 | 0.075548 | -0.003770 | 0.001554 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$0.15**

Expected profit (USD): **0.28** [lowest: 0.39, highest: 0.72]

Delta: 0.2612 (price sensitivity)

Gamma: 0.2928 (delta sensitivity)

Theta: $-0.0110 (negative decay per trading-day)

Vega: $0.0060 (volatility sensitivity per 1%)

ITM (In The Money) probability: **75.55%**

Profit probability: **62.56%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $6 | $1.33 | $1.74 | 1.44 | 0.8926 | -0.41 |
| $6 | $0.50 | $1.01 | 0.65 | 0.8926 | -0.51 |
| $7 | $0.47 | $0.73 | 0.60 | 0.8926 | -0.26 |
| $8 | $0.27 | $0.52 | 0.58 | 0.8926 | -0.25 |
| $8 | $0.15 | $0.35 | 0.85 | 0.8926 | -0.20 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **30.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.000000 |       0.030000 |          4.143619 |          4.147920 |          4.623504 |   0.996367 |      0.995933 | 0.004479 | 0.009655 | -0.000377 | 0.000288 |
|  9.000000 |       0.080000 |          1.201313 |          1.300076 |          1.768257 |   0.879745 |      0.846879 | 0.135036 | 0.159941 | -0.006317 | 0.004778 |
|  8.000000 |       0.200000 |          0.277065 |          0.412307 |          0.838193 |   0.710618 |      0.607797 | 0.314061 | 0.261305 | -0.010430 | 0.007807 |
|  7.500000 |       0.350000 |         -0.198008 |         -0.058964 |          0.329348 |   0.585614 |      0.414436 | 0.442175 | 0.290736 | -0.011712 | 0.008686 |
|  7.000000 |       0.540000 |         -0.645388 |         -0.521588 |         -0.183069 |   0.441948 |      0.214350 | 0.585838 | 0.287000 | -0.011728 | 0.008574 |
|  6.500000 |       0.700000 |         -0.989590 |         -0.924068 |         -0.646028 |   0.296256 |      0.079604 | 0.727749 | 0.244537 | -0.010240 | 0.007306 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$12**

Market price: **$0.03**

Expected profit (USD): **4.14** [lowest: 4.15, highest: 4.62]

Delta: 0.0045 (price sensitivity)

Gamma: 0.0097 (delta sensitivity)

Theta: $-0.0004 (negative decay per trading-day)

Vega: $0.0003 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.64%**

Profit probability: **99.59%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $6 | $0.70 | $1.12 | 1.67 | 0.8926 | -0.42 |
| $7 | $0.54 | $0.86 | 0.69 | 0.8926 | -0.32 |
| $8 | $0.35 | $0.64 | 0.55 | 0.8926 | -0.29 |
| $8 | $0.20 | $0.48 | 0.56 | 0.8926 | -0.28 |
| $9 | $0.08 | $0.25 | 0.68 | 0.8926 | -0.17 |
| $12 | $0.03 | $0.03 | 1.14 | 0.8926 | 0.00 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **06.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 8.000000 |       0.170000 |          0.357216 |          0.501153 |          1.016053 |   0.680842 |      0.616517 | 0.351400 | 0.234986 | -0.009875 | 0.009276 |
| 7.000000 |       0.560000 |         -0.601309 |         -0.470699 |         -0.058565 |   0.447065 |      0.256753 | 0.587685 | 0.246598 | -0.010601 | 0.009735 |
| 6.500000 |       0.810000 |         -1.042927 |         -0.945645 |         -0.600421 |   0.319959 |      0.103286 | 0.711006 | 0.216494 | -0.009510 | 0.008546 |
| 4.000000 |       3.000000 |         -3.498997 |         -3.636314 |         -3.600382 |   0.003898 |      0.000000 | 0.997014 | 0.005772 | -0.001016 | 0.000228 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$0.17**

Expected profit (USD): **0.36** [lowest: 0.50, highest: 1.02]

Delta: 0.3514 (price sensitivity)

Gamma: 0.2350 (delta sensitivity)

Theta: $-0.0099 (negative decay per trading-day)

Vega: $0.0093 (volatility sensitivity per 1%)

ITM (In The Money) probability: **68.08%**

Profit probability: **61.65%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $4 | $3.00 | $3.17 | 5.36 | 0.8926 | -0.17 |
| $6 | $0.81 | $1.22 | 0.57 | 0.8926 | -0.41 |
| $7 | $0.56 | $0.97 | 0.61 | 0.8926 | -0.41 |
| $8 | $0.17 | $0.58 | 0.57 | 0.8926 | -0.41 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **13.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.500000 |       0.380000 |         -0.111079 |          0.031314 |          0.576916 |   0.560735 |      0.457616 | 0.481019 | 0.223849 | -0.009900 | 0.011033 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$0.38**

Expected profit (USD): **-0.11** [lowest: 0.03, highest: 0.58]

Delta: 0.4810 (price sensitivity)

Gamma: 0.2238 (delta sensitivity)

Theta: $-0.0099 (negative decay per trading-day)

Vega: $0.0110 (volatility sensitivity per 1%)

ITM (In The Money) probability: **56.07%**

Profit probability: **45.76%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $0.38 | $0.85 | 0.69 | 0.8926 | -0.47 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.000000 |       0.070000 |          3.969703 |          4.012253 |          4.878391 |   0.966973 |      0.972542 | 0.042986 | 0.046448 | -0.002051 | 0.002752 |
| 10.000000 |       0.110000 |          2.065769 |          2.173321 |          2.993311 |   0.880419 |      0.886247 | 0.145469 | 0.116142 | -0.005171 | 0.006882 |
|  8.000000 |       0.330000 |          0.288941 |          0.439449 |          1.116943 |   0.643606 |      0.590532 | 0.402416 | 0.196748 | -0.008928 | 0.011659 |
|  7.000000 |       0.710000 |         -0.642855 |         -0.507134 |          0.042431 |   0.453833 |      0.292504 | 0.593671 | 0.197229 | -0.009143 | 0.011687 |
|  6.000000 |       1.320000 |         -1.603636 |         -1.524264 |         -1.137149 |   0.249892 |      0.042057 | 0.786939 | 0.147786 | -0.007176 | 0.008757 |
|  5.000000 |       1.820000 |         -2.267786 |         -2.265476 |         -2.048981 |   0.090806 |      0.000421 | 0.927417 | 0.070196 | -0.003883 | 0.004160 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$12**

Market price: **$0.07**

Expected profit (USD): **3.97** [lowest: 4.01, highest: 4.88]

Delta: 0.0430 (price sensitivity)

Gamma: 0.0464 (delta sensitivity)

Theta: $-0.0021 (negative decay per trading-day)

Vega: $0.0028 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.70%**

Profit probability: **97.25%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $1.82 | $2.37 | 1.21 | 0.8926 | -0.55 |
| $6 | $1.32 | $1.68 | 0.63 | 0.8926 | -0.36 |
| $7 | $0.71 | $1.15 | 0.65 | 0.8926 | -0.44 |
| $8 | $0.33 | $0.77 | 0.55 | 0.8926 | -0.44 |
| $10 | $0.11 | $0.33 | 0.81 | 0.8926 | -0.22 |
| $12 | $0.07 | $0.14 | 1.11 | 0.8926 | -0.07 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 8

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **16** strikes prices..

Total of valuable options: 14

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 20.000000 |       0.100000 |         11.430722 |         11.427553 |         13.337691 |   0.989393 |      0.995316 | 0.018617 | 0.014548 | -0.000729 | 0.002056 |
| 15.000000 |       0.140000 |          6.516424 |          6.577974 |          8.407320 |   0.950440 |      0.972151 | 0.076621 | 0.045946 | -0.002321 | 0.006495 |
| 13.000000 |       0.180000 |          4.614352 |          4.712691 |          6.460949 |   0.907134 |      0.941153 | 0.135155 | 0.069389 | -0.003524 | 0.009808 |
| 12.000000 |       0.180000 |          3.723383 |          3.838232 |          5.525963 |   0.873078 |      0.914935 | 0.178760 | 0.083431 | -0.004253 | 0.011793 |
| 11.000000 |       0.220000 |          2.832150 |          2.968417 |          4.577274 |   0.827146 |      0.875414 | 0.235151 | 0.098167 | -0.005028 | 0.013876 |
| 10.000000 |       0.380000 |          1.874140 |          2.024105 |          3.531187 |   0.766062 |      0.810503 | 0.306787 | 0.112146 | -0.005780 | 0.015852 |
|  9.000000 |       0.510000 |          1.016183 |          1.168510 |          2.546079 |   0.686533 |      0.718560 | 0.395472 | 0.122999 | -0.006392 | 0.017386 |
|  8.000000 |       0.780000 |          0.108027 |          0.249458 |          1.465507 |   0.586235 |      0.573164 | 0.501233 | 0.127396 | -0.006700 | 0.018008 |
|  7.000000 |       1.140000 |         -0.779468 |         -0.653269 |          0.367223 |   0.465668 |      0.370541 | 0.620626 | 0.121528 | -0.006509 | 0.017178 |
|  6.000000 |       1.700000 |         -1.738511 |         -1.658575 |         -0.864502 |   0.331003 |      0.132730 | 0.744765 | 0.102592 | -0.005665 | 0.014501 |
|  5.000000 |       2.410000 |         -2.711601 |         -2.692039 |         -2.142502 |   0.197033 |      0.006666 | 0.858416 | 0.071622 | -0.004194 | 0.010124 |
|  4.000000 |       3.200000 |         -3.640508 |         -3.690918 |         -3.377218 |   0.086862 |      0.000000 | 0.943095 | 0.036491 | -0.002451 | 0.005158 |
|  3.000000 |       3.890000 |         -4.380665 |         -4.481979 |         -4.355155 |   0.021934 |      0.000000 | 0.987334 | 0.010452 | -0.001070 | 0.001477 |
|  1.000000 |       5.750000 |         -6.250000 |         -6.426511 |         -6.425868 |   0.000003 |      0.000000 | 0.999999 | 0.000002 | -0.000195 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$20**

Market price: **$0.10**

Expected profit (USD): **11.43** [lowest: 11.43, highest: 13.34]

Delta: 0.0186 (price sensitivity)

Gamma: 0.0145 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0021 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.94%**

Profit probability: **99.53%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $5.75 | $6.15 | 5.20 | 0.8926 | -0.40 |
| $3 | $3.89 | $4.25 | 2.07 | 0.8926 | -0.36 |
| $4 | $3.20 | $3.43 | 0.91 | 0.8926 | -0.23 |
| $5 | $2.41 | $2.73 | 0.82 | 0.8926 | -0.32 |
| $6 | $1.70 | $2.15 | 0.62 | 0.8926 | -0.45 |
| $7 | $1.14 | $1.69 | 0.68 | 0.8926 | -0.55 |
| $8 | $0.78 | $1.33 | 0.72 | 0.8926 | -0.55 |
| $9 | $0.51 | $1.05 | 0.75 | 0.8926 | -0.54 |
| $10 | $0.38 | $0.83 | 0.74 | 0.8926 | -0.45 |
| $11 | $0.22 | $0.66 | 0.75 | 0.8926 | -0.44 |
| $12 | $0.18 | $0.52 | 0.73 | 0.8926 | -0.34 |
| $13 | $0.18 | $0.42 | 0.84 | 0.8926 | -0.24 |
| $15 | $0.14 | $0.27 | 0.91 | 0.8926 | -0.13 |
| $20 | $0.10 | $0.09 | 1.08 | 0.8926 | 0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 9

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **10** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 13.000000 |       0.380000 |          4.314136 |          4.466668 |          7.248485 |   0.821743 |      0.902646 | 0.277051 | 0.075403 | -0.004152 | 0.020842 |
| 12.000000 |       0.510000 |          3.379569 |          3.534632 |          6.186222 |   0.786265 |      0.872786 | 0.321636 | 0.080689 | -0.004463 | 0.022304 |
| 11.000000 |       0.550000 |          2.574068 |          2.735339 |          5.235822 |   0.743394 |      0.836473 | 0.373180 | 0.085246 | -0.004740 | 0.023563 |
| 10.000000 |       0.780000 |          1.625702 |          1.793653 |          4.119124 |   0.691758 |      0.778825 | 0.432333 | 0.088529 | -0.004956 | 0.024470 |
|  9.000000 |       0.950000 |          0.793947 |          0.953573 |          3.077078 |   0.629941 |      0.704347 | 0.499483 | 0.089824 | -0.005072 | 0.024828 |
|  8.000000 |       1.200000 |         -0.050367 |          0.091411 |          1.983315 |   0.556702 |      0.597306 | 0.574479 | 0.088254 | -0.005040 | 0.024395 |
|  7.000000 |       1.520000 |         -0.885421 |         -0.768768 |          0.860333 |   0.471400 |      0.447859 | 0.656215 | 0.082846 | -0.004807 | 0.022900 |
|  6.000000 |       2.100000 |         -1.889364 |         -1.817280 |         -0.481284 |   0.374780 |      0.228510 | 0.742031 | 0.072737 | -0.004322 | 0.020105 |
|  5.000000 |       2.470000 |         -2.582310 |         -2.543846 |         -1.525519 |   0.270299 |      0.058009 | 0.826984 | 0.057620 | -0.003557 | 0.015927 |
|  4.000000 |       3.300000 |         -3.629946 |         -3.666884 |         -2.976338 |   0.165989 |      0.000000 | 0.903292 | 0.038558 | -0.002554 | 0.010658 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$13**

Market price: **$0.38**

Expected profit (USD): **4.31** [lowest: 4.47, highest: 7.25]

Delta: 0.2771 (price sensitivity)

Gamma: 0.0754 (delta sensitivity)

Theta: $-0.0042 (negative decay per trading-day)

Vega: $0.0208 (volatility sensitivity per 1%)

ITM (In The Money) probability: **82.17%**

Profit probability: **90.26%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $4 | $3.30 | $3.76 | 0.66 | 0.8926 | -0.46 |
| $5 | $2.47 | $3.18 | 0.73 | 0.8926 | -0.71 |
| $6 | $2.10 | $2.70 | 0.71 | 0.8926 | -0.60 |
| $7 | $1.52 | $2.30 | 0.72 | 0.8926 | -0.78 |
| $8 | $1.20 | $1.97 | 0.71 | 0.8926 | -0.77 |
| $9 | $0.95 | $1.70 | 0.72 | 0.8926 | -0.75 |
| $10 | $0.78 | $1.47 | 0.75 | 0.8926 | -0.69 |
| $11 | $0.55 | $1.27 | 0.78 | 0.8926 | -0.72 |
| $12 | $0.51 | $1.11 | 0.79 | 0.8926 | -0.60 |
| $13 | $0.38 | $0.97 | 0.76 | 0.8926 | -0.59 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 10

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **13** strikes prices..

Total of valuable options: 12

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 30.000000 |       0.250000 |         19.246022 |         19.348468 |         25.386361 |   0.943297 |      0.986934 | 0.135108 | 0.034520 | -0.001958 | 0.018869 |
| 25.000000 |       0.250000 |         14.593007 |         14.742229 |         20.450449 |   0.915667 |      0.977883 | 0.185126 | 0.042434 | -0.002420 | 0.023196 |
| 22.500000 |       0.310000 |         12.267769 |         12.435875 |         17.929884 |   0.895648 |      0.970317 | 0.218689 | 0.046889 | -0.002684 | 0.025631 |
| 20.000000 |       0.430000 |          9.939915 |         10.118120 |         15.353527 |   0.869428 |      0.959036 | 0.260052 | 0.051548 | -0.002963 | 0.028178 |
| 17.500000 |       0.460000 |          7.777794 |          7.981388 |         12.901685 |   0.834575 |      0.942757 | 0.311396 | 0.056169 | -0.003247 | 0.030704 |
| 15.000000 |       0.610000 |          5.597184 |          5.814629 |         10.347130 |   0.787493 |      0.916287 | 0.375528 | 0.060282 | -0.003510 | 0.032952 |
| 12.500000 |       0.890000 |          3.424929 |          3.641394 |          7.691793 |   0.722802 |      0.870234 | 0.455934 | 0.063006 | -0.003705 | 0.034441 |
| 10.000000 |       1.350000 |          1.264449 |          1.446987 |          4.892567 |   0.632458 |      0.781265 | 0.556513 | 0.062756 | -0.003745 | 0.034304 |
|  7.500000 |       1.910000 |         -0.726479 |         -0.609016 |          2.074433 |   0.504960 |      0.596050 | 0.680133 | 0.056815 | -0.003477 | 0.031057 |
|  5.000000 |       3.000000 |         -2.868348 |         -2.821096 |         -1.086076 |   0.327456 |      0.126904 | 0.823154 | 0.041234 | -0.002660 | 0.022540 |
|  4.000000 |       3.320000 |         -3.473655 |         -3.477829 |         -2.170742 |   0.242037 |      0.000198 | 0.881053 | 0.031590 | -0.002127 | 0.017268 |
|  2.500000 |       4.600000 |         -5.016260 |         -5.110695 |         -4.460791 |   0.108925 |      0.000000 | 0.956623 | 0.014622 | -0.001141 | 0.007993 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$30**

Market price: **$0.25**

Expected profit (USD): **19.25** [lowest: 19.35, highest: 25.39]

Delta: 0.1351 (price sensitivity)

Gamma: 0.0345 (delta sensitivity)

Theta: $-0.0020 (negative decay per trading-day)

Vega: $0.0189 (volatility sensitivity per 1%)

ITM (In The Money) probability: **94.33%**

Profit probability: **98.69%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $4.60 | $5.12 | 1.15 | 0.8926 | -0.52 |
| $4 | $3.32 | $4.29 | 0.66 | 0.8926 | -0.97 |
| $5 | $3.00 | $3.84 | 0.75 | 0.8926 | -0.84 |
| $8 | $1.91 | $3.00 | 0.88 | 0.8926 | -1.09 |
| $10 | $1.35 | $2.40 | 0.78 | 0.8926 | -1.05 |
| $12 | $0.89 | $1.97 | 0.74 | 0.8926 | -1.08 |
| $15 | $0.61 | $1.65 | 0.76 | 0.8926 | -1.04 |
| $18 | $0.46 | $1.39 | 0.74 | 0.8926 | -0.93 |
| $20 | $0.43 | $1.19 | 0.89 | 0.8926 | -0.76 |
| $22 | $0.31 | $1.03 | 0.82 | 0.8926 | -0.72 |
| $25 | $0.25 | $0.90 | 0.80 | 0.8926 | -0.65 |
| $30 | $0.25 | $0.70 | 0.86 | 0.8926 | -0.45 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 11

Expires At: **17.12.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 20.000000 |       0.840000 |          9.022911 |          9.363646 |         16.589927 |   0.785085 |      0.950431 | 0.454484 | 0.045373 | -0.002749 | 0.047434 |
| 17.000000 |       1.070000 |          6.496122 |          6.775752 |         13.366359 |   0.744354 |      0.932400 | 0.507306 | 0.045663 | -0.002787 | 0.047737 |
| 15.000000 |       1.200000 |          4.910272 |          5.221671 |         11.328866 |   0.710438 |      0.915070 | 0.547948 | 0.045341 | -0.002784 | 0.047400 |
| 12.000000 |       1.820000 |          2.251732 |          2.507559 |          7.777629 |   0.645249 |      0.867217 | 0.618909 | 0.043627 | -0.002713 | 0.045608 |
| 10.000000 |       2.000000 |          0.835832 |          1.058620 |          5.678360 |   0.588507 |      0.817283 | 0.674162 | 0.041246 | -0.002595 | 0.043120 |
|  7.000000 |       2.800000 |         -1.567545 |         -1.458774 |          2.006699 |   0.473121 |      0.628668 | 0.771129 | 0.034666 | -0.002242 | 0.036240 |
|  5.000000 |       3.500000 |         -3.111813 |         -3.078537 |         -0.531459 |   0.366150 |      0.229774 | 0.845474 | 0.027224 | -0.001823 | 0.028460 |
|  4.000000 |       3.750000 |         -3.695716 |         -3.721348 |         -1.685386 |   0.300067 |      0.000000 | 0.884804 | 0.022248 | -0.001533 | 0.023258 |
|  2.000000 |       5.100000 |         -5.490193 |         -5.606741 |         -4.688364 |   0.137860 |      0.000000 | 0.961229 | 0.009618 | -0.000760 | 0.010055 |
|  1.000000 |       5.850000 |         -6.333043 |         -6.495880 |         -6.139203 |   0.048885 |      0.000000 | 0.990121 | 0.003019 | -0.000311 | 0.003156 |
|  3.000000 |       7.160000 |         -7.368580 |         -7.523648 |         -6.033418 |   0.223918 |      0.000000 | 0.924238 | 0.016331 | -0.001179 | 0.017072 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$20**

Market price: **$0.84**

Expected profit (USD): **9.02** [lowest: 9.36, highest: 16.59]

Delta: 0.4545 (price sensitivity)

Gamma: 0.0454 (delta sensitivity)

Theta: $-0.0027 (negative decay per trading-day)

Vega: $0.0474 (volatility sensitivity per 1%)

ITM (In The Money) probability: **78.51%**

Profit probability: **95.04%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $5.85 | $6.37 | 1.98 | 0.8926 | -0.52 |
| $2 | $5.10 | $5.80 | 1.09 | 0.8926 | -0.70 |
| $3 | $7.16 | $5.35 | 1.13 | 0.8926 | 1.81 |
| $4 | $3.75 | $4.98 | 0.75 | 0.8926 | -1.23 |
| $5 | $3.50 | $4.66 | 0.88 | 0.8926 | -1.16 |
| $7 | $2.80 | $4.15 | 0.90 | 0.8926 | -1.35 |
| $10 | $2.00 | $3.57 | 0.74 | 0.8926 | -1.57 |
| $12 | $1.82 | $3.27 | 0.73 | 0.8926 | -1.45 |
| $15 | $1.20 | $2.91 | 0.72 | 0.8926 | -1.71 |
| $17 | $1.07 | $2.70 | 0.94 | 0.8926 | -1.63 |
| $20 | $0.84 | $2.45 | 0.74 | 0.8926 | -1.61 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

### Calculate Stock Option Nr. 12

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.2892 [-0.3795, 0.3140]**

- Stock Volatility: **0.8926 [0.7897, 0.9992]**

- Based on **6415** observations


- Garch Volatility forecast: **0.6275**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |       1.260000 |          4.845497 |          5.166569 |         11.383154 |   0.705137 |      0.915889 | 0.560820 | 0.044049 | -0.002716 | 0.048338 |
| 12.000000 |       1.800000 |          2.281244 |          2.544098 |          7.906503 |   0.641134 |      0.870788 | 0.629599 | 0.042195 | -0.002634 | 0.046304 |
| 10.000000 |       2.000000 |          0.852427 |          1.075801 |          5.777311 |   0.585610 |      0.822579 | 0.682968 | 0.039794 | -0.002513 | 0.043669 |
|  7.000000 |       3.000000 |         -1.746052 |         -1.635699 |          1.897157 |   0.472957 |      0.624822 | 0.776408 | 0.033386 | -0.002167 | 0.036637 |
|  5.000000 |       3.400000 |         -2.992418 |         -2.945030 |         -0.339656 |   0.368492 |      0.272995 | 0.848056 | 0.026272 | -0.001764 | 0.028830 |
|  4.000000 |       5.000000 |         -4.929345 |         -4.966007 |         -2.876741 |   0.303769 |      0.000000 | 0.886066 | 0.021541 | -0.001487 | 0.023638 |
|  2.000000 |       5.400000 |         -5.783406 |         -5.905406 |         -4.948651 |   0.143278 |      0.000000 | 0.960625 | 0.009504 | -0.000748 | 0.010430 |
|  1.000000 |       5.750000 |         -6.231199 |         -6.430532 |         -6.050357 |   0.052851 |      0.000000 | 0.989559 | 0.003092 | -0.000312 | 0.003393 |
|  3.000000 |       6.600000 |         -6.796539 |         -6.922700 |         -5.385295 |   0.228820 |      0.000000 | 0.924359 | 0.015917 | -0.001149 | 0.017467 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$15**

Market price: **$1.26**

Expected profit (USD): **4.85** [lowest: 5.17, highest: 11.38]

Delta: 0.5608 (price sensitivity)

Gamma: 0.0440 (delta sensitivity)

Theta: $-0.0027 (negative decay per trading-day)

Vega: $0.0483 (volatility sensitivity per 1%)

ITM (In The Money) probability: **70.51%**

Profit probability: **91.59%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $5.75 | $6.39 | 2.18 | 0.8926 | -0.64 |
| $2 | $5.40 | $5.84 | 1.06 | 0.8926 | -0.44 |
| $3 | $6.60 | $5.40 | 0.72 | 0.8926 | 1.20 |
| $4 | $5.00 | $5.04 | 0.91 | 0.8926 | -0.04 |
| $5 | $3.40 | $4.73 | 0.91 | 0.8926 | -1.33 |
| $7 | $3.00 | $4.23 | 0.85 | 0.8926 | -1.23 |
| $10 | $2.00 | $3.67 | 0.72 | 0.8926 | -1.67 |
| $12 | $1.80 | $3.37 | 0.73 | 0.8926 | -1.57 |
| $15 | $1.26 | $3.01 | 0.72 | 0.8926 | -1.75 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6416** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2980**

- Modal profit prediction correlation: **0.0799**

- Backtests total: **88**

- Profitable Trades (profitable trades / total trades): **44.32%**

--------------------------------------------------

