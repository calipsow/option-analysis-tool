# RILY Option Analysis From: 05.01.2026 00:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $5.179999828338623

### Calculate Stock Option Nr. 1

Expires At: **09.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       1.210000 |          0.474517 |          0.348948 |          0.403541 |   0.999779 |      0.701695 | 0.999876 | 0.000615 | -0.000659 | 0.000003 |
| 2.000000 |       2.860000 |         -0.175507 |         -0.362132 |         -0.307539 |   1.000000 |      0.374891 | 1.000000 | 0.000000 | -0.000397 | 0.000000 |
| 4.000000 |       0.980000 |         -0.282899 |         -0.393409 |         -0.338590 |   0.947986 |      0.321252 | 0.962155 | 0.104339 | -0.011591 | 0.000466 |
| 4.500000 |       0.680000 |         -0.425552 |         -0.563710 |         -0.505074 |   0.803123 |      0.242153 | 0.842180 | 0.305432 | -0.032445 | 0.001363 |
| 5.000000 |       0.330000 |         -0.419746 |         -0.608819 |         -0.544787 |   0.564164 |      0.192036 | 0.622541 | 0.481288 | -0.050556 | 0.002148 |
| 5.500000 |       0.210000 |         -0.519221 |         -0.675803 |         -0.631753 |   0.321390 |      0.099445 | 0.377069 | 0.481134 | -0.050331 | 0.002147 |
| 6.000000 |       0.090000 |         -0.513542 |         -0.591493 |         -0.578680 |   0.150400 |      0.047025 | 0.188324 | 0.341853 | -0.035691 | 0.001525 |
| 6.500000 |       0.050000 |         -0.523147 |         -0.553451 |         -0.551572 |   0.059392 |      0.017125 | 0.079378 | 0.187199 | -0.019523 | 0.000835 |
| 7.000000 |       0.040000 |         -0.531572 |         -0.542392 |         -0.542221 |   0.020372 |      0.005264 | 0.029013 | 0.083824 | -0.008736 | 0.000374 |
| 8.000000 |       0.050000 |         -0.549362 |         -0.560380 |         -0.560379 |   0.001737 |      0.000359 | 0.002789 | 0.010850 | -0.001130 | 0.000048 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$1.21**

Expected profit (USD): **0.47** [lowest: 0.35, highest: 0.40]

Delta: 0.9999 (price sensitivity)

Gamma: 0.0006 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.98%**

Profit probability: **70.17%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.86 | $3.18 | 7.22 | 0.7886 | -0.32 |
| $3 | $1.21 | $2.18 | 5.52 | 0.7886 | -0.97 |
| $4 | $0.98 | $1.18 | 1.97 | 0.7886 | -0.20 |
| $4 | $0.68 | $0.69 | 1.45 | 0.7886 | -0.01 |
| $5 | $0.33 | $0.28 | 1.36 | 0.7886 | 0.05 |
| $6 | $0.21 | $0.07 | 1.13 | 0.7886 | 0.14 |
| $6 | $0.09 | $0.01 | 1.21 | 0.7886 | 0.08 |
| $6 | $0.05 | $0.00 | 1.39 | 0.7886 | 0.05 |
| $7 | $0.04 | $0.00 | 1.61 | 0.7886 | 0.04 |
| $8 | $0.05 | $0.00 | 2.73 | 0.7886 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **32** strikes prices..

Total of valuable options: 15

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       2.150000 |          0.046022 |         -0.193261 |         -0.011634 |   0.994820 |      0.440807 | 0.997681 | 0.005164 | -0.001001 | 0.000075 |
|  4.000000 |       0.990000 |         -0.185603 |         -0.464280 |         -0.279307 |   0.796489 |      0.350175 | 0.863632 | 0.155748 | -0.015974 | 0.002256 |
|  4.500000 |       0.740000 |         -0.298943 |         -0.620991 |         -0.439398 |   0.653392 |      0.291442 | 0.746058 | 0.228263 | -0.023069 | 0.003306 |
|  5.000000 |       0.470000 |         -0.317680 |         -0.659914 |         -0.502178 |   0.502269 |      0.243791 | 0.607699 | 0.273788 | -0.027469 | 0.003966 |
|  5.500000 |       0.280000 |         -0.343523 |         -0.662870 |         -0.542936 |   0.364659 |      0.189166 | 0.468758 | 0.283337 | -0.028310 | 0.004104 |
|  6.000000 |       0.180000 |         -0.396608 |         -0.642518 |         -0.565820 |   0.252345 |      0.133750 | 0.344767 | 0.262412 | -0.026151 | 0.003801 |
|  6.500000 |       0.110000 |         -0.430544 |         -0.609370 |         -0.568148 |   0.167898 |      0.090277 | 0.243570 | 0.223250 | -0.022209 | 0.003234 |
|  7.500000 |       0.080000 |         -0.512020 |         -0.584310 |         -0.576413 |   0.068035 |      0.035071 | 0.110675 | 0.134547 | -0.013356 | 0.001949 |
| 10.000000 |       0.040000 |         -0.534986 |         -0.544681 |         -0.544641 |   0.005352 |      0.002621 | 0.011169 | 0.020907 | -0.002070 | 0.000303 |
| 12.500000 |       0.050000 |         -0.549655 |         -0.553121 |         -0.553121 |   0.000368 |      0.000172 | 0.000942 | 0.002270 | -0.000225 | 0.000033 |
| 15.000000 |       0.020000 |         -0.519975 |         -0.535213 |         -0.535213 |   0.000026 |      0.000012 | 0.000078 | 0.000224 | -0.000022 | 0.000003 |
| 17.500000 |       0.040000 |         -0.539998 |         -0.549362 |         -0.549362 |   0.000002 |      0.000001 | 0.000007 | 0.000022 | -0.000002 | 0.000000 |
| 20.000000 |       0.030000 |         -0.530000 |         -0.531560 |         -0.531560 |   0.000000 |      0.000000 | 0.000001 | 0.000002 | -0.000000 | 0.000000 |
| 27.500000 |       0.180000 |         -0.680000 |         -0.694433 |         -0.694433 |   0.000000 |      0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 |
| 52.500000 |       7.100000 |         -7.600000 |         -8.025189 |         -8.025189 |   0.000000 |      0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.15**

Expected profit (USD): **0.05** [lowest: -0.19, highest: -0.01]

Delta: 0.9977 (price sensitivity)

Gamma: 0.0052 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.48%**

Profit probability: **44.08%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.15 | $2.68 | 3.38 | 0.7886 | -0.53 |
| $4 | $0.99 | $1.20 | 1.56 | 0.7886 | -0.21 |
| $4 | $0.74 | $0.76 | 0.95 | 0.7886 | -0.02 |
| $5 | $0.47 | $0.42 | 1.08 | 0.7886 | 0.05 |
| $6 | $0.28 | $0.20 | 0.77 | 0.7886 | 0.08 |
| $6 | $0.18 | $0.08 | 1.18 | 0.7886 | 0.10 |
| $6 | $0.11 | $0.03 | 1.59 | 0.7886 | 0.08 |
| $8 | $0.08 | $0.00 | 1.48 | 0.7886 | 0.08 |
| $10 | $0.04 | $0.00 | 2.19 | 0.7886 | 0.04 |
| $12 | $0.05 | $0.00 | 2.41 | 0.7886 | 0.05 |
| $15 | $0.02 | $0.00 | 3.85 | 0.7886 | 0.02 |
| $18 | $0.04 | $0.00 | 3.73 | 0.7886 | 0.04 |
| $20 | $0.03 | $0.00 | 3.19 | 0.7886 | 0.03 |
| $28 | $0.18 | $0.00 | 4.64 | 0.7886 | 0.18 |
| $52 | $7.10 | $0.00 | 14.45 | 0.7886 | 7.10 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **23.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **13** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       1.990000 |         -0.252858 |         -0.605816 |         -0.297086 |   0.922742 |      0.349193 | 0.961178 | 0.047031 | -0.004971 | 0.001132 |
| 4.500000 |       0.620000 |         -0.044590 |         -0.496123 |         -0.209319 |   0.598420 |      0.324449 | 0.722413 | 0.187449 | -0.018162 | 0.004510 |
| 4.000000 |       1.450000 |         -0.544220 |         -0.986470 |         -0.680327 |   0.722551 |      0.267440 | 0.824125 | 0.144605 | -0.014171 | 0.003479 |
| 1.500000 |       4.040000 |         -0.834452 |         -1.235097 |         -0.926915 |   0.999700 |      0.253325 | 0.999919 | 0.000181 | -0.000314 | 0.000004 |
| 5.000000 |       0.550000 |         -0.243237 |         -0.699964 |         -0.454442 |   0.477697 |      0.251794 | 0.612113 | 0.214221 | -0.020619 | 0.005154 |
| 3.500000 |       2.250000 |         -0.953849 |         -1.327356 |         -1.017637 |   0.835773 |      0.222713 | 0.906248 | 0.093598 | -0.009381 | 0.002252 |
| 5.500000 |       0.550000 |         -0.454478 |         -0.888445 |         -0.696809 |   0.369938 |      0.184361 | 0.503490 | 0.223081 | -0.021382 | 0.005367 |
| 6.000000 |       0.250000 |         -0.316098 |         -0.672231 |         -0.533901 |   0.279590 |      0.162068 | 0.403888 | 0.216583 | -0.020701 | 0.005211 |
| 7.000000 |       0.120000 |         -0.396113 |         -0.618255 |         -0.560880 |   0.151368 |      0.090584 | 0.245154 | 0.175853 | -0.016748 | 0.004231 |
| 7.500000 |       0.170000 |         -0.510755 |         -0.681684 |         -0.648053 |   0.109268 |      0.061897 | 0.186822 | 0.150178 | -0.014286 | 0.003613 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$1.99**

Expected profit (USD): **-0.25** [lowest: -0.61, highest: -0.30]

Delta: 0.9612 (price sensitivity)

Gamma: 0.0470 (delta sensitivity)

Theta: $-0.0050 (negative decay per trading-day)

Vega: $0.0011 (volatility sensitivity per 1%)

ITM (In The Money) probability: **92.27%**

Profit probability: **34.92%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $4.04 | $3.69 | 6.14 | 0.7886 | 0.35 |
| $3 | $1.99 | $2.19 | 3.10 | 0.7886 | -0.20 |
| $4 | $2.25 | $1.70 | 0.95 | 0.7886 | 0.55 |
| $4 | $1.45 | $1.24 | 1.64 | 0.7886 | 0.21 |
| $4 | $0.62 | $0.83 | 0.59 | 0.7886 | -0.21 |
| $5 | $0.55 | $0.52 | 0.99 | 0.7886 | 0.03 |
| $6 | $0.55 | $0.30 | 0.89 | 0.7886 | 0.25 |
| $6 | $0.25 | $0.16 | 1.18 | 0.7886 | 0.09 |
| $7 | $0.12 | $0.04 | 1.52 | 0.7886 | 0.08 |
| $8 | $0.17 | $0.02 | 1.55 | 0.7886 | 0.15 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **30.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       1.400000 |          0.376636 |         -0.062371 |          0.372560 |   0.880015 |      0.452578 | 0.941981 | 0.055723 | -0.005554 | 0.001855 |
| 4.000000 |       0.910000 |          0.083334 |         -0.459595 |         -0.040824 |   0.677019 |      0.357379 | 0.803985 | 0.132830 | -0.012531 | 0.004421 |
| 2.000000 |       3.230000 |         -0.510311 |         -0.971212 |         -0.536916 |   0.985510 |      0.305574 | 0.995065 | 0.006865 | -0.001009 | 0.000228 |
| 4.500000 |       0.850000 |         -0.167314 |         -0.732606 |         -0.347828 |   0.566065 |      0.287741 | 0.713257 | 0.163522 | -0.015271 | 0.005443 |
| 5.000000 |       0.790000 |         -0.363878 |         -0.920702 |         -0.590374 |   0.461861 |      0.229527 | 0.618223 | 0.183121 | -0.016994 | 0.006095 |
| 5.500000 |       0.450000 |         -0.231187 |         -0.734535 |         -0.470317 |   0.369622 |      0.211017 | 0.525399 | 0.191208 | -0.017670 | 0.006364 |
| 6.000000 |       0.330000 |         -0.275847 |         -0.717589 |         -0.516543 |   0.291394 |      0.172251 | 0.439296 | 0.189374 | -0.017448 | 0.006303 |
| 6.500000 |       0.300000 |         -0.374910 |         -0.753864 |         -0.607512 |   0.227097 |      0.133313 | 0.362464 | 0.180094 | -0.016556 | 0.005995 |
| 8.000000 |       0.010000 |         -0.321256 |         -0.520870 |         -0.475845 |   0.102936 |      0.067796 | 0.192578 | 0.131407 | -0.012030 | 0.004374 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$1.40**

Expected profit (USD): **0.38** [lowest: -0.06, highest: 0.37]

Delta: 0.9420 (price sensitivity)

Gamma: 0.0557 (delta sensitivity)

Theta: $-0.0056 (negative decay per trading-day)

Vega: $0.0019 (volatility sensitivity per 1%)

ITM (In The Money) probability: **88.00%**

Profit probability: **45.26%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.23 | $3.19 | 5.09 | 0.7886 | 0.04 |
| $3 | $1.40 | $2.20 | 2.84 | 0.7886 | -0.80 |
| $4 | $0.91 | $1.28 | 1.79 | 0.7886 | -0.37 |
| $4 | $0.85 | $0.90 | 0.53 | 0.7886 | -0.05 |
| $5 | $0.79 | $0.60 | 0.93 | 0.7886 | 0.19 |
| $6 | $0.45 | $0.38 | 1.08 | 0.7886 | 0.07 |
| $6 | $0.33 | $0.23 | 1.09 | 0.7886 | 0.10 |
| $6 | $0.30 | $0.14 | 1.16 | 0.7886 | 0.16 |
| $8 | $0.01 | $0.02 | 1.66 | 0.7886 | -0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **06.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       2.250000 |          0.010029 |         -0.523781 |          0.036428 |   0.921994 |      0.374642 | 0.968642 | 0.030357 | -0.003101 | 0.001282 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.25**

Expected profit (USD): **0.01** [lowest: -0.52, highest: 0.04]

Delta: 0.9686 (price sensitivity)

Gamma: 0.0304 (delta sensitivity)

Theta: $-0.0031 (negative decay per trading-day)

Vega: $0.0013 (volatility sensitivity per 1%)

ITM (In The Money) probability: **92.20%**

Profit probability: **37.46%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.25 | $2.70 | 3.82 | 0.7886 | -0.45 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **13.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.500000 |       0.750000 |         -0.338621 |         -1.001302 |         -0.587054 |   0.365150 |      0.195158 | 0.554715 | 0.155903 | -0.013573 | 0.007949 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$6**

Market price: **$0.75**

Expected profit (USD): **-0.34** [lowest: -1.00, highest: -0.59]

Delta: 0.5547 (price sensitivity)

Gamma: 0.1559 (delta sensitivity)

Theta: $-0.0136 (negative decay per trading-day)

Vega: $0.0079 (volatility sensitivity per 1%)

ITM (In The Money) probability: **36.51%**

Profit probability: **19.52%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $6 | $0.75 | $0.52 | 1.19 | 0.7886 | 0.23 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       2.310000 |          0.004208 |         -0.709441 |          0.099144 |   0.874657 |      0.347975 | 0.952175 | 0.036574 | -0.003439 | 0.002179 |
| 5.000000 |       0.760000 |         -0.069967 |         -0.832545 |         -0.254380 |   0.432260 |      0.240696 | 0.635706 | 0.138024 | -0.011781 | 0.008222 |
| 7.500000 |       0.290000 |         -0.311944 |         -0.748336 |         -0.547385 |   0.173001 |      0.107735 | 0.335512 | 0.133945 | -0.011275 | 0.007979 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.31**

Expected profit (USD): **0.00** [lowest: -0.71, highest: 0.10]

Delta: 0.9522 (price sensitivity)

Gamma: 0.0366 (delta sensitivity)

Theta: $-0.0034 (negative decay per trading-day)

Vega: $0.0022 (volatility sensitivity per 1%)

ITM (In The Money) probability: **87.47%**

Profit probability: **34.80%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.31 | $2.71 | 2.66 | 0.7886 | -0.40 |
| $5 | $0.76 | $0.79 | 0.99 | 0.7886 | -0.03 |
| $8 | $0.29 | $0.15 | 1.14 | 0.7886 | 0.14 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 8

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       2.100000 |          0.438376 |         -0.901546 |          0.843752 |   0.744109 |      0.316497 | 0.916598 | 0.040082 | -0.003266 | 0.005031 |
|  5.000000 |       1.300000 |         -0.138849 |         -1.345136 |         -0.112311 |   0.388948 |      0.193005 | 0.671631 | 0.094434 | -0.007222 | 0.011853 |
|  7.500000 |       0.650000 |         -0.201454 |         -1.047187 |         -0.375069 |   0.203035 |      0.116521 | 0.458447 | 0.103670 | -0.007809 | 0.013012 |
| 10.000000 |       0.400000 |         -0.331177 |         -0.889803 |         -0.549532 |   0.111197 |      0.066101 | 0.310757 | 0.092276 | -0.006903 | 0.011582 |
| 12.500000 |       0.420000 |         -0.563912 |         -0.936676 |         -0.764582 |   0.063980 |      0.036971 | 0.213099 | 0.075950 | -0.005659 | 0.009533 |
| 15.000000 |       0.240000 |         -0.508834 |         -0.751542 |         -0.661351 |   0.038451 |      0.022600 | 0.148596 | 0.060538 | -0.004499 | 0.007598 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.10**

Expected profit (USD): **0.44** [lowest: -0.90, highest: 0.84]

Delta: 0.9166 (price sensitivity)

Gamma: 0.0401 (delta sensitivity)

Theta: $-0.0033 (negative decay per trading-day)

Vega: $0.0050 (volatility sensitivity per 1%)

ITM (In The Money) probability: **74.41%**

Profit probability: **31.65%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.10 | $2.78 | 2.00 | 0.7886 | -0.68 |
| $5 | $1.30 | $1.14 | 1.13 | 0.7886 | 0.16 |
| $8 | $0.65 | $0.43 | 1.22 | 0.7886 | 0.22 |
| $10 | $0.40 | $0.17 | 1.35 | 0.7886 | 0.23 |
| $12 | $0.42 | $0.07 | 1.42 | 0.7886 | 0.35 |
| $15 | $0.24 | $0.03 | 1.38 | 0.7886 | 0.21 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 9

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       2.600000 |          0.284875 |         -1.883944 |          1.259946 |   0.620085 |      0.225001 | 0.898187 | 0.034911 | -0.002651 | 0.008040 |
|  5.000000 |       1.500000 |          0.220292 |         -1.628549 |          0.704580 |   0.344859 |      0.162964 | 0.714421 | 0.066720 | -0.004831 | 0.015365 |
|  7.500000 |       1.040000 |          0.007111 |         -1.401933 |          0.195952 |   0.208511 |      0.107035 | 0.561189 | 0.077403 | -0.005521 | 0.017825 |
| 10.000000 |       0.820000 |         -0.193278 |         -1.290287 |         -0.203595 |   0.134758 |      0.070620 | 0.444886 | 0.077578 | -0.005491 | 0.017866 |
| 12.500000 |       0.640000 |         -0.291713 |         -1.143497 |         -0.394167 |   0.091575 |      0.048377 | 0.357357 | 0.073264 | -0.005161 | 0.016872 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.60**

Expected profit (USD): **0.28** [lowest: -1.88, highest: 1.26]

Delta: 0.8982 (price sensitivity)

Gamma: 0.0349 (delta sensitivity)

Theta: $-0.0027 (negative decay per trading-day)

Vega: $0.0080 (volatility sensitivity per 1%)

ITM (In The Money) probability: **62.01%**

Profit probability: **22.50%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.60 | $2.93 | 0.72 | 0.7886 | -0.33 |
| $5 | $1.50 | $1.54 | 1.10 | 0.7886 | -0.04 |
| $8 | $1.04 | $0.83 | 1.12 | 0.7886 | 0.21 |
| $10 | $0.82 | $0.47 | 1.19 | 0.7886 | 0.35 |
| $12 | $0.64 | $0.28 | 1.25 | 0.7886 | 0.36 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 10

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       2.900000 |          0.606380 |         -2.780398 |          3.143754 |   0.480283 |      0.151100 | 0.897825 | 0.025608 | -0.001876 | 0.011250 |
|  5.000000 |       2.040000 |          0.542827 |         -2.286754 |          2.514596 |   0.285965 |      0.112330 | 0.774421 | 0.043145 | -0.003051 | 0.018954 |
|  7.500000 |       1.650000 |          0.346125 |         -2.037933 |          1.837402 |   0.192993 |      0.081082 | 0.674286 | 0.051748 | -0.003610 | 0.022733 |
| 10.000000 |       1.730000 |         -0.144451 |         -2.203531 |          0.962709 |   0.139852 |      0.057729 | 0.593950 | 0.055711 | -0.003857 | 0.024474 |
| 12.500000 |       1.120000 |          0.160905 |         -1.649358 |          0.973883 |   0.106194 |      0.046376 | 0.528570 | 0.057160 | -0.003937 | 0.025111 |
| 15.000000 |       0.990000 |          0.055650 |         -1.488585 |          0.713083 |   0.083380 |      0.036206 | 0.474489 | 0.057190 | -0.003925 | 0.025124 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.90**

Expected profit (USD): **0.61** [lowest: -2.78, highest: 3.14]

Delta: 0.8978 (price sensitivity)

Gamma: 0.0256 (delta sensitivity)

Theta: $-0.0019 (negative decay per trading-day)

Vega: $0.0112 (volatility sensitivity per 1%)

ITM (In The Money) probability: **48.03%**

Profit probability: **15.11%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.90 | $3.21 | 1.20 | 0.7886 | -0.31 |
| $5 | $2.04 | $2.09 | 1.03 | 0.7886 | -0.05 |
| $8 | $1.65 | $1.45 | 1.08 | 0.7886 | 0.20 |
| $10 | $1.73 | $1.04 | 1.18 | 0.7886 | 0.69 |
| $12 | $1.12 | $0.78 | 1.38 | 0.7886 | 0.34 |
| $15 | $0.99 | $0.60 | 1.20 | 0.7886 | 0.39 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

### Calculate Stock Option Nr. 11

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.0728 [-0.5145, 0.3716]**

- Stock Volatility: **0.7886 [0.6924, 0.8897]**

- Based on **3067** observations


- Garch Volatility forecast: **1.2859**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       3.200000 |          1.413831 |         -3.572308 |          9.547856 |   0.332006 |      0.079441 | 0.919983 | 0.015307 | -0.001106 | 0.013243 |
|  5.000000 |       3.000000 |          0.958557 |         -3.489760 |          8.279050 |   0.210700 |      0.057387 | 0.849745 | 0.024029 | -0.001693 | 0.020790 |
|  7.500000 |       2.590000 |          0.920031 |         -3.146503 |          7.530809 |   0.153815 |      0.045102 | 0.793644 | 0.029363 | -0.002046 | 0.025405 |
| 10.000000 |       1.410000 |          1.760597 |         -1.924430 |          7.858363 |   0.120276 |      0.039462 | 0.747207 | 0.032905 | -0.002278 | 0.028470 |
| 12.500000 |       1.850000 |          1.049368 |         -2.397381 |          6.636614 |   0.098075 |      0.030424 | 0.707720 | 0.035367 | -0.002437 | 0.030599 |
| 15.000000 |       1.520000 |          1.154938 |         -2.063189 |          6.332568 |   0.082292 |      0.025747 | 0.673470 | 0.037122 | -0.002549 | 0.032117 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.20**

Expected profit (USD): **1.41** [lowest: -3.57, highest: 9.55]

Delta: 0.9200 (price sensitivity)

Gamma: 0.0153 (delta sensitivity)

Theta: $-0.0011 (negative decay per trading-day)

Vega: $0.0132 (volatility sensitivity per 1%)

ITM (In The Money) probability: **33.20%**

Profit probability: **7.94%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.20 | $3.65 | 0.60 | 0.7886 | -0.45 |
| $5 | $3.00 | $2.84 | 0.98 | 0.7886 | 0.16 |
| $8 | $2.59 | $2.31 | 1.10 | 0.7886 | 0.28 |
| $10 | $1.41 | $1.95 | 1.00 | 0.7886 | -0.54 |
| $12 | $1.85 | $1.67 | 0.93 | 0.7886 | 0.18 |
| $15 | $1.52 | $1.46 | 1.07 | 0.7886 | 0.06 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3068** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2079**

- Modal profit prediction correlation: **0.3057**

- Backtests total: **40**

- Profitable Trades (profitable trades / total trades): **47.50%**

--------------------------------------------------

