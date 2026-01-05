# SLI Option Analysis From: 05.01.2026 03:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $4.78000020980835

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4400 [-0.5188, 0.5941]**

- Stock Volatility: **0.7930 [0.6921, 0.9004]**

- Based on **1966** observations


- Garch Volatility forecast: **0.6985**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 1.000000 |       3.200000 |          0.164185 |         -0.100634 |          0.110794 |   1.000000 |      0.537820 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 0.500000 |       4.100000 |         -0.235815 |         -0.520348 |         -0.308919 |   1.000000 |      0.304520 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |
| 2.000000 |       2.650000 |         -0.285815 |         -0.530920 |         -0.319492 |   1.000000 |      0.279653 | 1.000000 | 0.000000 | -0.000396 | 0.000000 |
| 2.500000 |       2.180000 |         -0.315815 |         -0.549528 |         -0.338093 |   0.999999 |      0.265331 | 1.000000 | 0.000004 | -0.000495 | 0.000000 |
| 1.500000 |       3.200000 |         -0.335815 |         -0.609395 |         -0.397967 |   1.000000 |      0.256039 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |
| 5.000000 |       0.240000 |         -0.537569 |         -0.595480 |         -0.449043 |   0.392888 |      0.082400 | 0.400526 | 0.600257 | -0.012788 | 0.003680 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$3.20**

Expected profit (USD): **0.16** [lowest: -0.10, highest: 0.11]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **53.78%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $4.10 | $4.28 | 10.31 | 0.7930 | -0.18 |
| $1 | $3.20 | $3.78 | 6.88 | 0.7930 | -0.58 |
| $2 | $3.20 | $3.28 | 6.27 | 0.7930 | -0.08 |
| $2 | $2.65 | $2.78 | 3.45 | 0.7930 | -0.13 |
| $2 | $2.18 | $2.28 | 2.69 | 0.7930 | -0.10 |
| $5 | $0.24 | $0.21 | 0.91 | 0.7930 | 0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1967** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2310**

- Modal profit prediction correlation: **0.3687**

- Backtests total: **25**

- Profitable Trades (profitable trades / total trades): **52.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4400 [-0.5188, 0.5941]**

- Stock Volatility: **0.7930 [0.6921, 0.9004]**

- Based on **1966** observations


- Garch Volatility forecast: **0.6985**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       2.100000 |          0.073411 |         -0.786876 |          0.165160 |   0.988416 |      0.385419 | 0.990330 | 0.018037 | -0.000894 | 0.000523 |
| 5.000000 |       0.650000 |         -0.454148 |         -0.862079 |         -0.262027 |   0.484729 |      0.180122 | 0.511947 | 0.277893 | -0.006745 | 0.008055 |
| 7.500000 |       0.150000 |         -0.553944 |         -0.627762 |         -0.433486 |   0.082426 |      0.031953 | 0.093300 | 0.116228 | -0.002737 | 0.003369 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.10**

Expected profit (USD): **0.07** [lowest: -0.79, highest: 0.17]

Delta: 0.9903 (price sensitivity)

Gamma: 0.0180 (delta sensitivity)

Theta: $-0.0009 (negative decay per trading-day)

Vega: $0.0005 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.84%**

Profit probability: **38.54%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.10 | $2.31 | 1.58 | 0.7930 | -0.21 |
| $5 | $0.65 | $0.56 | 1.16 | 0.7930 | 0.09 |
| $8 | $0.15 | $0.09 | 1.16 | 0.7930 | 0.06 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1967** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2310**

- Modal profit prediction correlation: **0.3687**

- Backtests total: **25**

- Profitable Trades (profitable trades / total trades): **52.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4400 [-0.5188, 0.5941]**

- Stock Volatility: **0.7930 [0.6921, 0.9004]**

- Based on **1966** observations


- Garch Volatility forecast: **0.6985**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       2.300000 |          0.427199 |         -1.350421 |          0.746463 |   0.939695 |      0.364788 | 0.953177 | 0.044283 | -0.001502 | 0.002961 |
|  5.000000 |       0.850000 |          0.017495 |         -1.004270 |          0.412725 |   0.521103 |      0.230667 | 0.570314 | 0.177717 | -0.004673 | 0.011885 |
|  7.500000 |       0.450000 |         -0.441524 |         -0.876243 |         -0.122963 |   0.204938 |      0.087764 | 0.242008 | 0.141314 | -0.003595 | 0.009450 |
| 10.000000 |       0.300000 |         -0.613582 |         -0.789930 |         -0.396969 |   0.074036 |      0.029687 | 0.093064 | 0.075330 | -0.001893 | 0.005038 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.30**

Expected profit (USD): **0.43** [lowest: -1.35, highest: 0.75]

Delta: 0.9532 (price sensitivity)

Gamma: 0.0443 (delta sensitivity)

Theta: $-0.0015 (negative decay per trading-day)

Vega: $0.0030 (volatility sensitivity per 1%)

ITM (In The Money) probability: **93.97%**

Profit probability: **36.48%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.30 | $2.40 | 1.25 | 0.7930 | -0.10 |
| $5 | $0.85 | $0.90 | 1.06 | 0.7930 | -0.05 |
| $8 | $0.45 | $0.32 | 1.09 | 0.7930 | 0.13 |
| $10 | $0.30 | $0.12 | 1.07 | 0.7930 | 0.18 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1967** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2310**

- Modal profit prediction correlation: **0.3687**

- Backtests total: **25**

- Profitable Trades (profitable trades / total trades): **52.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4400 [-0.5188, 0.5941]**

- Stock Volatility: **0.7930 [0.6921, 0.9004]**

- Based on **1966** observations


- Garch Volatility forecast: **0.6985**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       2.420000 |          1.334356 |         -1.852712 |          2.131888 |   0.884759 |      0.355892 | 0.917013 | 0.049492 | -0.001597 | 0.006377 |
|  5.000000 |       1.300000 |          0.662162 |         -1.476289 |          1.492591 |   0.550211 |      0.235588 | 0.622607 | 0.123039 | -0.003408 | 0.015853 |
|  7.500000 |       0.780000 |          0.135730 |         -1.168556 |          0.896447 |   0.308036 |      0.132181 | 0.376272 | 0.122925 | -0.003294 | 0.015838 |
| 10.000000 |       0.520000 |         -0.186956 |         -0.992206 |          0.439884 |   0.171888 |      0.071069 | 0.223451 | 0.096740 | -0.002555 | 0.012464 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.42**

Expected profit (USD): **1.33** [lowest: -1.85, highest: 2.13]

Delta: 0.9170 (price sensitivity)

Gamma: 0.0495 (delta sensitivity)

Theta: $-0.0016 (negative decay per trading-day)

Vega: $0.0064 (volatility sensitivity per 1%)

ITM (In The Money) probability: **88.48%**

Profit probability: **35.59%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.42 | $2.56 | 1.07 | 0.7930 | -0.14 |
| $5 | $1.30 | $1.28 | 1.09 | 0.7930 | 0.02 |
| $8 | $0.78 | $0.67 | 1.10 | 0.7930 | 0.11 |
| $10 | $0.52 | $0.37 | 1.15 | 0.7930 | 0.15 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1967** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2310**

- Modal profit prediction correlation: **0.3687**

- Backtests total: **25**

- Profitable Trades (profitable trades / total trades): **52.00%**

--------------------------------------------------

