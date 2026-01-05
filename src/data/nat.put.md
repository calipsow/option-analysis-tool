# Put Option. NAT Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

## Current Stock Price: $3.369999885559082

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3231 [-0.3979, 0.5245]**

- Stock Volatility: **0.4737 [0.4086, 0.5447]**

- Based on **1021** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.500000 |       0.070000 |         -0.438979 |         -0.420384 |         -0.321642 |   0.676521 |      0.006014 | 0.279171 | 1.708912 | -0.003486 | 0.002257 |
| 3.000000 |       0.390000 |         -0.889119 |         -0.894262 |         -0.871365 |   0.014516 |      0.000000 | 0.980096 | 0.245150 | -0.001055 | 0.000324 |
| 2.500000 |       0.900000 |         -1.400000 |         -1.416636 |         -1.416295 |   0.000000 |      0.000000 | 1.000000 | 0.000003 | -0.000495 | 0.000000 |
| 2.000000 |       1.850000 |         -2.350000 |         -2.381429 |         -2.381429 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000396 | 0.000000 |
| 1.500000 |       1.920000 |         -2.420000 |         -2.450443 |         -2.450443 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |
| 1.000000 |       2.400000 |         -2.900000 |         -2.933894 |         -2.933894 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 0.500000 |       2.900000 |         -3.400000 |         -3.441289 |         -3.441289 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$4**

Market price: **$0.07**

Expected profit (USD): **-0.44** [lowest: -0.42, highest: -0.32]

Delta: 0.2792 (price sensitivity)

Gamma: 1.7089 (delta sensitivity)

Theta: $-0.0035 (negative decay per trading-day)

Vega: $0.0023 (volatility sensitivity per 1%)

ITM (In The Money) probability: **67.65%**

Profit probability: **0.60%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $2.90 | $2.87 | 9.13 | 0.4737 | 0.03 |
| $1 | $2.40 | $2.37 | 4.81 | 0.4737 | 0.03 |
| $2 | $1.92 | $1.87 | 2.13 | 0.4737 | 0.05 |
| $2 | $1.85 | $1.37 | 2.59 | 0.4737 | 0.48 |
| $2 | $0.90 | $0.88 | 1.89 | 0.4737 | 0.02 |
| $3 | $0.39 | $0.39 | 1.45 | 0.4737 | -0.00 |
| $4 | $0.07 | $0.08 | 0.52 | 0.4737 | -0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1022** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0789**

- Modal profit prediction correlation: **-0.0273**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **54.55%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3231 [-0.3979, 0.5245]**

- Stock Volatility: **0.4737 [0.4086, 0.5447]**

- Based on **1021** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.500000 |       0.120000 |         -0.464063 |         -0.447126 |         -0.118125 |   0.467726 |      0.082918 | 0.440911 | 0.873189 | -0.002248 | 0.005619 |
| 3.000000 |       0.510000 |         -0.989955 |         -0.983277 |         -0.817569 |   0.109226 |      0.000017 | 0.841589 | 0.534960 | -0.001690 | 0.003442 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$4**

Market price: **$0.12**

Expected profit (USD): **-0.46** [lowest: -0.45, highest: -0.12]

Delta: 0.4409 (price sensitivity)

Gamma: 0.8732 (delta sensitivity)

Theta: $-0.0022 (negative decay per trading-day)

Vega: $0.0056 (volatility sensitivity per 1%)

ITM (In The Money) probability: **46.77%**

Profit probability: **8.29%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $0.51 | $0.50 | 0.73 | 0.4737 | 0.01 |
| $4 | $0.12 | $0.23 | 0.43 | 0.4737 | -0.11 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1022** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0789**

- Modal profit prediction correlation: **-0.0273**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **54.55%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3231 [-0.3979, 0.5245]**

- Stock Volatility: **0.4737 [0.4086, 0.5447]**

- Based on **1021** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **10** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 4.000000 |       0.070000 |         -0.154467 |         -0.200025 |          0.645230 |   0.619670 |      0.415142 | 0.268538 | 0.466824 | -0.001312 | 0.007035 |
| 3.500000 |       0.220000 |         -0.553136 |         -0.555227 |          0.075338 |   0.369773 |      0.111849 | 0.507910 | 0.564674 | -0.001684 | 0.008510 |
| 3.000000 |       0.540000 |         -0.997978 |         -0.994783 |         -0.603252 |   0.142783 |      0.001962 | 0.774957 | 0.424634 | -0.001462 | 0.006399 |
| 2.500000 |       1.120000 |         -1.615107 |         -1.632403 |         -1.450433 |   0.026327 |      0.000000 | 0.947931 | 0.150799 | -0.000821 | 0.002273 |
| 2.000000 |       1.780000 |         -2.279850 |         -2.312745 |         -2.260714 |   0.001340 |      0.000000 | 0.996424 | 0.015168 | -0.000424 | 0.000229 |
| 0.500000 |       3.360000 |         -3.860000 |         -3.917224 |         -3.917224 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000097 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$4**

Market price: **$0.07**

Expected profit (USD): **-0.15** [lowest: -0.20, highest: 0.65]

Delta: 0.2685 (price sensitivity)

Gamma: 0.4668 (delta sensitivity)

Theta: $-0.0013 (negative decay per trading-day)

Vega: $0.0070 (volatility sensitivity per 1%)

ITM (In The Money) probability: **61.97%**

Profit probability: **41.51%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.36 | $2.88 | 2.56 | 0.4737 | 0.48 |
| $2 | $1.78 | $1.42 | 0.96 | 0.4737 | 0.36 |
| $2 | $1.12 | $0.98 | 0.65 | 0.4737 | 0.14 |
| $3 | $0.54 | $0.63 | 0.58 | 0.4737 | -0.09 |
| $4 | $0.22 | $0.38 | 0.50 | 0.4737 | -0.16 |
| $4 | $0.07 | $0.21 | 0.41 | 0.4737 | -0.14 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1022** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0789**

- Modal profit prediction correlation: **-0.0273**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **54.55%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3231 [-0.3979, 0.5245]**

- Stock Volatility: **0.4737 [0.4086, 0.5447]**

- Based on **1021** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 4.500000 |       0.100000 |          0.016522 |         -0.118424 |          1.475744 |   0.615320 |      0.538952 | 0.240748 | 0.313332 | -0.000943 | 0.009160 |
| 4.000000 |       0.250000 |         -0.402757 |         -0.471530 |          0.862014 |   0.457721 |      0.301378 | 0.380371 | 0.383231 | -0.001195 | 0.011204 |
| 3.500000 |       0.370000 |         -0.709100 |         -0.731669 |          0.306118 |   0.288091 |      0.107821 | 0.558941 | 0.397028 | -0.001316 | 0.011607 |
| 3.000000 |       0.550000 |         -0.994383 |         -1.005473 |         -0.279108 |   0.139698 |      0.012142 | 0.748888 | 0.320500 | -0.001195 | 0.009370 |
| 2.500000 |       1.050000 |         -1.537846 |         -1.553558 |         -1.121187 |   0.044574 |      0.000001 | 0.901341 | 0.174853 | -0.000851 | 0.005112 |
| 2.000000 |       1.500000 |         -1.998760 |         -2.028933 |         -1.831173 |   0.007013 |      0.000000 | 0.979616 | 0.049510 | -0.000494 | 0.001447 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$4**

Market price: **$0.10**

Expected profit (USD): **0.02** [lowest: -0.12, highest: 1.48]

Delta: 0.2407 (price sensitivity)

Gamma: 0.3133 (delta sensitivity)

Theta: $-0.0009 (negative decay per trading-day)

Vega: $0.0092 (volatility sensitivity per 1%)

ITM (In The Money) probability: **61.53%**

Profit probability: **53.90%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.50 | $1.49 | 1.40 | 0.4737 | 0.01 |
| $2 | $1.05 | $1.10 | 0.81 | 0.4737 | -0.05 |
| $3 | $0.55 | $0.79 | 0.71 | 0.4737 | -0.24 |
| $4 | $0.37 | $0.55 | 0.41 | 0.4737 | -0.18 |
| $4 | $0.25 | $0.38 | 0.42 | 0.4737 | -0.13 |
| $4 | $0.10 | $0.26 | 0.47 | 0.4737 | -0.16 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1022** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0789**

- Modal profit prediction correlation: **-0.0273**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **54.55%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.3231 [-0.3979, 0.5245]**

- Stock Volatility: **0.4737 [0.4086, 0.5447]**

- Based on **1021** observations


- Garch Volatility forecast: **0.3089**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       0.170000 |         -0.013518 |         -0.242742 |          2.506457 |   0.501507 |      0.523178 | 0.287166 | 0.242963 | -0.000790 | 0.013988 |
| 4.500000 |       0.160000 |         -0.229585 |         -0.376517 |          2.034661 |   0.401522 |      0.408865 | 0.378853 | 0.271257 | -0.000907 | 0.015617 |
| 4.000000 |       0.260000 |         -0.504300 |         -0.587690 |          1.460222 |   0.297207 |      0.261494 | 0.489847 | 0.284385 | -0.000990 | 0.016373 |
| 3.500000 |       0.420000 |         -0.787419 |         -0.830181 |          0.835422 |   0.196736 |      0.117786 | 0.616169 | 0.272329 | -0.001007 | 0.015679 |
| 3.000000 |       0.610000 |         -1.053414 |         -1.077953 |          0.196866 |   0.110519 |      0.026557 | 0.747252 | 0.227913 | -0.000930 | 0.013122 |
| 2.500000 |       1.000000 |         -1.481964 |         -1.500657 |         -0.608633 |   0.048266 |      0.000266 | 0.865204 | 0.154662 | -0.000754 | 0.008905 |
| 2.000000 |       1.400000 |         -1.896399 |         -1.917183 |         -1.375900 |   0.013970 |      0.000000 | 0.949521 | 0.074104 | -0.000523 | 0.004267 |
| 1.500000 |       1.830000 |         -2.329685 |         -2.366794 |         -2.111580 |   0.001930 |      0.000000 | 0.990138 | 0.018776 | -0.000318 | 0.001081 |
| 1.000000 |       1.890000 |         -2.389995 |         -2.479182 |         -2.408441 |   0.000056 |      0.000000 | 0.999527 | 0.001205 | -0.000187 | 0.000069 |
| 0.500000 |       3.000000 |         -3.500000 |         -3.553481 |         -3.549400 |   0.000000 |      0.000000 | 1.000000 | 0.000001 | -0.000092 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$5**

Market price: **$0.17**

Expected profit (USD): **-0.01** [lowest: -0.24, highest: 2.51]

Delta: 0.2872 (price sensitivity)

Gamma: 0.2430 (delta sensitivity)

Theta: $-0.0008 (negative decay per trading-day)

Vega: $0.0140 (volatility sensitivity per 1%)

ITM (In The Money) probability: **50.15%**

Profit probability: **52.32%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.00 | $2.91 | 1.34 | 0.4737 | 0.09 |
| $1 | $1.89 | $2.45 | 1.49 | 0.4737 | -0.56 |
| $2 | $1.83 | $2.01 | 0.59 | 0.4737 | -0.18 |
| $2 | $1.40 | $1.62 | 0.62 | 0.4737 | -0.22 |
| $2 | $1.00 | $1.30 | 0.58 | 0.4737 | -0.30 |
| $3 | $0.61 | $1.03 | 0.47 | 0.4737 | -0.42 |
| $4 | $0.42 | $0.81 | 0.41 | 0.4737 | -0.39 |
| $4 | $0.26 | $0.64 | 0.38 | 0.4737 | -0.38 |
| $4 | $0.16 | $0.51 | 0.43 | 0.4737 | -0.35 |
| $5 | $0.17 | $0.40 | 0.50 | 0.4737 | -0.23 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1022** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0789**

- Modal profit prediction correlation: **-0.0273**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **54.55%**

--------------------------------------------------

