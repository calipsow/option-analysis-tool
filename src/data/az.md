# AZ Option Analysis From: 05.01.2026 01:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $6.829999923706055

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4978 [-0.7621, 0.8188]**

- Stock Volatility: **0.8982 [0.7779, 1.0283]**

- Based on **1250** observations


- Garch Volatility forecast: **0.6479**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 6.000000 |       0.960000 |         -0.445718 |         -0.684793 |         -0.286226 |   0.867515 |      0.232721 | 0.864608 | 0.251304 | -0.010409 | 0.002960 |
| 7.000000 |       0.700000 |         -0.863744 |         -0.933136 |         -0.635653 |   0.459584 |      0.069957 | 0.454245 | 0.457806 | -0.017715 | 0.005392 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$6**

Market price: **$0.96**

Expected profit (USD): **-0.45** [lowest: -0.68, highest: -0.29]

Delta: 0.8646 (price sensitivity)

Gamma: 0.2513 (delta sensitivity)

Theta: $-0.0104 (negative decay per trading-day)

Vega: $0.0030 (volatility sensitivity per 1%)

ITM (In The Money) probability: **86.75%**

Profit probability: **23.27%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $6 | $0.96 | $1.00 | 1.47 | 0.8982 | -0.04 |
| $7 | $0.70 | $0.42 | 1.52 | 0.8982 | 0.28 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1251** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2525**

- Modal profit prediction correlation: **-0.0164**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **28.57%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4978 [-0.7621, 0.8188]**

- Stock Volatility: **0.8982 [0.7779, 1.0283]**

- Based on **1250** observations


- Garch Volatility forecast: **0.6479**

### 2. Validate Stock Option Contracts

- Analyze **14** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       2.150000 |         -0.129953 |         -1.378691 |          0.366726 |   0.905175 |      0.313004 | 0.902987 | 0.090911 | -0.004433 | 0.004954 |
|  6.000000 |       1.380000 |         -0.190057 |         -1.135544 |          0.384446 |   0.742823 |      0.276085 | 0.738659 | 0.172254 | -0.007580 | 0.009387 |
|  7.000000 |       1.300000 |         -0.751150 |         -1.363169 |         -0.111717 |   0.537618 |      0.160119 | 0.532509 | 0.210596 | -0.008923 | 0.011476 |
|  8.000000 |       0.970000 |         -0.861132 |         -1.227806 |         -0.242242 |   0.348782 |      0.103942 | 0.344038 | 0.194938 | -0.008113 | 0.010623 |
|  9.000000 |       0.720000 |         -0.884954 |         -1.087992 |         -0.336683 |   0.207625 |      0.062377 | 0.203964 | 0.150033 | -0.006181 | 0.008176 |
| 10.000000 |       0.600000 |         -0.922995 |         -1.031668 |         -0.468534 |   0.115882 |      0.033333 | 0.113392 | 0.101780 | -0.004167 | 0.005546 |
| 16.000000 |       0.660000 |         -1.157375 |         -1.174450 |         -1.083936 |   0.001889 |      0.000325 | 0.001813 | 0.003072 | -0.000124 | 0.000167 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.15**

Expected profit (USD): **-0.13** [lowest: -1.38, highest: 0.37]

Delta: 0.9030 (price sensitivity)

Gamma: 0.0909 (delta sensitivity)

Theta: $-0.0044 (negative decay per trading-day)

Vega: $0.0050 (volatility sensitivity per 1%)

ITM (In The Money) probability: **90.52%**

Profit probability: **31.30%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $2.15 | $2.12 | 0.61 | 0.8982 | 0.03 |
| $6 | $1.38 | $1.47 | 0.74 | 0.8982 | -0.09 |
| $7 | $1.30 | $0.98 | 1.41 | 0.8982 | 0.32 |
| $8 | $0.97 | $0.64 | 1.45 | 0.8982 | 0.33 |
| $9 | $0.72 | $0.42 | 1.39 | 0.8982 | 0.30 |
| $10 | $0.60 | $0.27 | 1.43 | 0.8982 | 0.33 |
| $16 | $0.66 | $0.02 | 1.59 | 0.8982 | 0.64 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1251** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2525**

- Modal profit prediction correlation: **-0.0164**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **28.57%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4978 [-0.7621, 0.8188]**

- Stock Volatility: **0.8982 [0.7779, 1.0283]**

- Based on **1250** observations


- Garch Volatility forecast: **0.6479**

### 2. Validate Stock Option Contracts

- Analyze **14** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 4.000000 |       2.900000 |          1.469061 |         -2.204549 |          3.011473 |   0.921652 |      0.380078 | 0.921209 | 0.045082 | -0.002495 | 0.007182 |
| 6.000000 |       1.600000 |          1.118825 |         -1.525221 |          2.858096 |   0.714560 |      0.310426 | 0.713532 | 0.104400 | -0.004920 | 0.016631 |
| 5.000000 |       2.850000 |          0.641417 |         -2.485413 |          2.332273 |   0.828626 |      0.288309 | 0.827856 | 0.078251 | -0.003881 | 0.012465 |
| 7.000000 |       1.950000 |          0.113630 |         -2.032594 |          1.915522 |   0.596302 |      0.206788 | 0.595129 | 0.118883 | -0.005447 | 0.018938 |
| 8.000000 |       1.380000 |          0.143621 |         -1.586206 |          1.947047 |   0.485647 |      0.181188 | 0.484441 | 0.122286 | -0.005505 | 0.019480 |
| 9.000000 |       1.100000 |         -0.012273 |         -1.389312 |          1.760356 |   0.388680 |      0.144977 | 0.387521 | 0.117482 | -0.005227 | 0.018715 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$4**

Market price: **$2.90**

Expected profit (USD): **1.47** [lowest: -2.20, highest: 3.01]

Delta: 0.9212 (price sensitivity)

Gamma: 0.0451 (delta sensitivity)

Theta: $-0.0025 (negative decay per trading-day)

Vega: $0.0072 (volatility sensitivity per 1%)

ITM (In The Money) probability: **92.17%**

Profit probability: **38.01%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $4 | $2.90 | $3.27 | 1.13 | 0.8982 | -0.37 |
| $5 | $2.85 | $2.64 | 1.27 | 0.8982 | 0.21 |
| $6 | $1.60 | $2.13 | 1.70 | 0.8982 | -0.53 |
| $7 | $1.95 | $1.72 | 1.29 | 0.8982 | 0.23 |
| $8 | $1.38 | $1.40 | 1.34 | 0.8982 | -0.02 |
| $9 | $1.10 | $1.14 | 1.33 | 0.8982 | -0.04 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1251** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2525**

- Modal profit prediction correlation: **-0.0164**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **28.57%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4978 [-0.7621, 0.8188]**

- Stock Volatility: **0.8982 [0.7779, 1.0283]**

- Based on **1250** observations


- Garch Volatility forecast: **0.6479**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       2.500000 |          1.505923 |         -2.698911 |          5.321976 |   0.635788 |      0.216667 | 0.637025 | 0.086261 | -0.004108 | 0.024320 |
| 8.000000 |       2.000000 |          1.411242 |         -2.341337 |          5.169358 |   0.554694 |      0.194862 | 0.555995 | 0.090821 | -0.004254 | 0.025606 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$7**

Market price: **$2.50**

Expected profit (USD): **1.51** [lowest: -2.70, highest: 5.32]

Delta: 0.6370 (price sensitivity)

Gamma: 0.0863 (delta sensitivity)

Theta: $-0.0041 (negative decay per trading-day)

Vega: $0.0243 (volatility sensitivity per 1%)

ITM (In The Money) probability: **63.58%**

Profit probability: **21.67%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $7 | $2.50 | $2.30 | 1.24 | 0.8982 | 0.20 |
| $8 | $2.00 | $2.00 | 1.39 | 0.8982 | -0.00 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1251** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2525**

- Modal profit prediction correlation: **-0.0164**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **28.57%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **18.12.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4978 [-0.7621, 0.8188]**

- Stock Volatility: **0.8982 [0.7779, 1.0283]**

- Based on **1250** observations


- Garch Volatility forecast: **0.6479**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       2.880000 |          5.452088 |         -3.095190 |         13.049888 |   0.807501 |      0.312402 | 0.809726 | 0.050450 | -0.002609 | 0.021737 |
|  7.000000 |       2.800000 |          4.055234 |         -3.121238 |         11.776321 |   0.670704 |      0.226395 | 0.673653 | 0.066966 | -0.003282 | 0.028853 |
| 10.000000 |       2.500000 |          2.616932 |         -2.971139 |         10.271469 |   0.495756 |      0.147753 | 0.499013 | 0.074102 | -0.003501 | 0.031928 |
| 12.000000 |       1.050000 |          3.169983 |         -1.487937 |         10.796317 |   0.404413 |      0.135952 | 0.407579 | 0.072105 | -0.003361 | 0.031067 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.88**

Expected profit (USD): **5.45** [lowest: -3.10, highest: 13.05]

Delta: 0.8097 (price sensitivity)

Gamma: 0.0504 (delta sensitivity)

Theta: $-0.0026 (negative decay per trading-day)

Vega: $0.0217 (volatility sensitivity per 1%)

ITM (In The Money) probability: **80.75%**

Profit probability: **31.24%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $2.88 | $3.52 | 0.87 | 0.8982 | -0.64 |
| $7 | $2.80 | $2.83 | 1.19 | 0.8982 | -0.03 |
| $10 | $2.50 | $2.12 | 1.10 | 0.8982 | 0.38 |
| $12 | $1.05 | $1.78 | 0.81 | 0.8982 | -0.73 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1251** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2525**

- Modal profit prediction correlation: **-0.0164**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **28.57%**

--------------------------------------------------

