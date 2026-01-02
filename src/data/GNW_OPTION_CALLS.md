# GNW Option Analysis From: 02.01.2026 19:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $9.029999732971191

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1351 [-0.2542, 0.2347]**

- Stock Volatility: **0.5792 [0.5117, 0.6493]**

- Based on **5435** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 8.000000 |       1.070000 |         -0.475236 |         -0.569873 |         -0.337652 |   0.989176 |      0.133075 | 0.988454 | 0.060694 | -0.002140 | 0.000619 |
| 9.000000 |       0.200000 |         -0.451083 |         -0.309420 |         -0.108366 |   0.563285 |      0.087422 | 0.553592 | 0.794398 | -0.008514 | 0.008108 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$1.07**

Expected profit (USD): **-0.48** [lowest: -0.57, highest: -0.34]

Delta: 0.9885 (price sensitivity)

Gamma: 0.0607 (delta sensitivity)

Theta: $-0.0021 (negative decay per trading-day)

Vega: $0.0006 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.92%**

Profit probability: **13.31%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $1.07 | $1.15 | 0.57 | 0.5792 | -0.08 |
| $9 | $0.20 | $0.50 | 0.37 | 0.5792 | -0.30 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5436** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1526**

- Modal profit prediction correlation: **0.0516**

- Backtests total: **74**

- Profitable Trades (profitable trades / total trades): **41.89%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1351 [-0.2542, 0.2347]**

- Stock Volatility: **0.5792 [0.5117, 0.6493]**

- Based on **5435** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 8.000000 |       1.350000 |         -0.524269 |         -0.758955 |         -0.042712 |   0.870968 |      0.206706 | 0.869165 | 0.191094 | -0.003784 | 0.008374 |
| 9.000000 |       0.500000 |         -0.406518 |         -0.374815 |          0.216937 |   0.569249 |      0.173444 | 0.565896 | 0.353877 | -0.005472 | 0.015507 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$1.35**

Expected profit (USD): **-0.52** [lowest: -0.76, highest: -0.04]

Delta: 0.8692 (price sensitivity)

Gamma: 0.1911 (delta sensitivity)

Theta: $-0.0038 (negative decay per trading-day)

Vega: $0.0084 (volatility sensitivity per 1%)

ITM (In The Money) probability: **87.10%**

Profit probability: **20.67%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $1.35 | $1.52 | 0.50 | 0.5792 | -0.17 |
| $9 | $0.50 | $0.96 | 0.62 | 0.5792 | -0.46 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5436** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1526**

- Modal profit prediction correlation: **0.0516**

- Backtests total: **74**

- Profitable Trades (profitable trades / total trades): **41.89%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1351 [-0.2542, 0.2347]**

- Stock Volatility: **0.5792 [0.5117, 0.6493]**

- Based on **5435** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       2.900000 |          1.005579 |         -0.054851 |          1.265560 |   0.999929 |      0.619084 | 0.999931 | 0.000191 | -0.000980 | 0.000014 |
|  1.000000 |       7.500000 |          0.405566 |         -0.748086 |          0.580605 |   1.000000 |      0.451713 | 1.000000 | 0.000000 | -0.000195 | 0.000000 |
|  4.000000 |       4.880000 |          0.025566 |         -1.090527 |          0.237754 |   1.000000 |      0.353558 | 1.000000 | 0.000000 | -0.000782 | 0.000000 |
|  2.000000 |       7.150000 |         -0.244434 |         -1.393746 |         -0.065054 |   1.000000 |      0.291057 | 1.000000 | 0.000000 | -0.000391 | 0.000000 |
|  7.000000 |       2.290000 |         -0.366445 |         -1.081425 |          0.122383 |   0.958703 |      0.261443 | 0.959112 | 0.059760 | -0.002137 | 0.004350 |
|  8.000000 |       1.300000 |         -0.276229 |         -0.664000 |          0.408406 |   0.819748 |      0.259404 | 0.820967 | 0.178151 | -0.003738 | 0.012968 |
|  6.000000 |       3.300000 |         -0.393393 |         -1.354789 |         -0.069174 |   0.996364 |      0.259404 | 0.996414 | 0.007318 | -0.001270 | 0.000533 |
| 10.000000 |       0.200000 |         -0.324629 |         -0.253138 |          0.480997 |   0.323380 |      0.117877 | 0.325053 | 0.245202 | -0.004002 | 0.017849 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.90**

Expected profit (USD): **1.01** [lowest: -0.05, highest: 1.27]

Delta: 0.9999 (price sensitivity)

Gamma: 0.0002 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.99%**

Profit probability: **61.91%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $7.50 | $8.04 | 3.00 | 0.5792 | -0.54 |
| $2 | $7.15 | $7.06 | 3.22 | 0.5792 | 0.09 |
| $4 | $4.88 | $5.09 | 1.83 | 0.5792 | -0.21 |
| $5 | $2.90 | $4.13 | 1.29 | 0.5792 | -1.23 |
| $6 | $3.30 | $3.22 | 0.72 | 0.5792 | 0.08 |
| $7 | $2.29 | $2.41 | 0.64 | 0.5792 | -0.12 |
| $8 | $1.30 | $1.74 | 0.46 | 0.5792 | -0.44 |
| $10 | $0.20 | $0.83 | 0.33 | 0.5792 | -0.63 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5436** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1526**

- Modal profit prediction correlation: **0.0516**

- Backtests total: **74**

- Profitable Trades (profitable trades / total trades): **41.89%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1351 [-0.2542, 0.2347]**

- Stock Volatility: **0.5792 [0.5117, 0.6493]**

- Based on **5435** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  7.000000 |       1.960000 |          0.495093 |         -0.884805 |          1.546527 |   0.890550 |      0.346387 | 0.896452 | 0.078669 | -0.002374 | 0.013193 |
|  6.000000 |       3.200000 |          0.188655 |         -1.585650 |          1.045073 |   0.966954 |      0.310666 | 0.969253 | 0.030349 | -0.001569 | 0.005089 |
|  8.000000 |       1.500000 |          0.126365 |         -0.849662 |          1.348079 |   0.758815 |      0.269553 | 0.768716 | 0.133116 | -0.003151 | 0.022324 |
|  9.000000 |       0.840000 |          0.108635 |         -0.502799 |          1.447193 |   0.593935 |      0.227800 | 0.606347 | 0.168117 | -0.003527 | 0.028193 |
| 10.000000 |       0.400000 |          0.038288 |         -0.287562 |          1.416995 |   0.429318 |      0.169977 | 0.441969 | 0.172501 | -0.003382 | 0.028928 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$7**

Market price: **$1.96**

Expected profit (USD): **0.50** [lowest: -0.88, highest: 1.55]

Delta: 0.8965 (price sensitivity)

Gamma: 0.0787 (delta sensitivity)

Theta: $-0.0024 (negative decay per trading-day)

Vega: $0.0132 (volatility sensitivity per 1%)

ITM (In The Money) probability: **89.06%**

Profit probability: **34.64%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $6 | $3.20 | $3.54 | 0.59 | 0.5792 | -0.34 |
| $7 | $1.96 | $2.86 | 0.69 | 0.5792 | -0.90 |
| $8 | $1.50 | $2.28 | 0.55 | 0.5792 | -0.78 |
| $9 | $0.84 | $1.81 | 0.46 | 0.5792 | -0.97 |
| $10 | $0.40 | $1.43 | 0.34 | 0.5792 | -1.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5436** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1526**

- Modal profit prediction correlation: **0.0516**

- Backtests total: **74**

- Profitable Trades (profitable trades / total trades): **41.89%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1351 [-0.2542, 0.2347]**

- Stock Volatility: **0.5792 [0.5117, 0.6493]**

- Based on **5435** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       4.260000 |          1.315618 |         -2.752694 |          3.277568 |   0.966339 |      0.301904 | 0.971024 | 0.018692 | -0.001170 | 0.007302 |
|  7.000000 |       2.610000 |          1.147279 |         -1.863151 |          3.483488 |   0.834084 |      0.271299 | 0.850126 | 0.065888 | -0.002048 | 0.025738 |
| 10.000000 |       0.850000 |          0.863110 |         -0.686868 |          3.595761 |   0.523826 |      0.182924 | 0.550254 | 0.111904 | -0.002584 | 0.043712 |
| 15.000000 |       0.140000 |         -0.018743 |         -0.424154 |          2.436483 |   0.164661 |      0.042456 | 0.181692 | 0.074630 | -0.001505 | 0.029152 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$4.26**

Expected profit (USD): **1.32** [lowest: -2.75, highest: 3.28]

Delta: 0.9710 (price sensitivity)

Gamma: 0.0187 (delta sensitivity)

Theta: $-0.0012 (negative decay per trading-day)

Vega: $0.0073 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.63%**

Profit probability: **30.19%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $4.26 | $4.80 | 1.15 | 0.5792 | -0.54 |
| $7 | $2.61 | $3.63 | 0.94 | 0.5792 | -1.02 |
| $10 | $0.85 | $2.41 | 0.38 | 0.5792 | -1.56 |
| $15 | $0.14 | $1.27 | 0.80 | 0.5792 | -1.13 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5436** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1526**

- Modal profit prediction correlation: **0.0516**

- Backtests total: **74**

- Profitable Trades (profitable trades / total trades): **41.89%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.1351 [-0.2542, 0.2347]**

- Stock Volatility: **0.5792 [0.5117, 0.6493]**

- Based on **5435** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       3.850000 |          4.201884 |         -3.167565 |          9.174508 |   0.933559 |      0.303321 | 0.945888 | 0.021835 | -0.001099 | 0.017085 |
|  7.000000 |       3.100000 |          3.195363 |         -2.770700 |          8.595201 |   0.815605 |      0.229604 | 0.841859 | 0.048007 | -0.001616 | 0.037564 |
| 10.000000 |       1.550000 |          2.618707 |         -1.585321 |          8.413205 |   0.601941 |      0.165939 | 0.641235 | 0.074295 | -0.001979 | 0.058134 |
| 12.000000 |       1.000000 |          2.097529 |         -1.143720 |          8.043887 |   0.472510 |      0.120129 | 0.513731 | 0.079272 | -0.001958 | 0.062028 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$3.85**

Expected profit (USD): **4.20** [lowest: -3.17, highest: 9.17]

Delta: 0.9459 (price sensitivity)

Gamma: 0.0218 (delta sensitivity)

Theta: $-0.0011 (negative decay per trading-day)

Vega: $0.0171 (volatility sensitivity per 1%)

ITM (In The Money) probability: **93.36%**

Profit probability: **30.33%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $3.85 | $5.49 | 1.45 | 0.5792 | -1.64 |
| $7 | $3.10 | $4.59 | 0.56 | 0.5792 | -1.49 |
| $10 | $1.55 | $3.58 | 0.60 | 0.5792 | -2.03 |
| $12 | $1.00 | $3.08 | 0.54 | 0.5792 | -2.08 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5436** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1526**

- Modal profit prediction correlation: **0.0516**

- Backtests total: **74**

- Profitable Trades (profitable trades / total trades): **41.89%**

--------------------------------------------------

