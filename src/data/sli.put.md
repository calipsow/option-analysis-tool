# Put Option. SLI Option Analysis From: 05.01.2026 03:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

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
| 5.000000 |       0.240000 |         -0.401754 |         -0.411749 |         -0.234144 |   0.607112 |      0.204776 | 0.400526 | 0.600257 | -0.012788 | 0.003680 |
| 2.500000 |       2.180000 |         -2.680000 |         -2.732132 |         -2.732104 |   0.000001 |      0.000000 | 1.000000 | 0.000004 | -0.000495 | 0.000000 |
| 2.000000 |       2.650000 |         -3.150000 |         -3.213522 |         -3.213522 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000396 | 0.000000 |
| 1.000000 |       3.200000 |         -3.700000 |         -3.783236 |         -3.783236 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 1.500000 |       3.200000 |         -3.700000 |         -3.791998 |         -3.791998 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |
| 0.500000 |       4.100000 |         -4.600000 |         -4.702950 |         -4.702950 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$0.24**

Expected profit (USD): **-0.40** [lowest: -0.41, highest: -0.23]

Delta: 0.4005 (price sensitivity)

Gamma: 0.6003 (delta sensitivity)

Theta: $-0.0128 (negative decay per trading-day)

Vega: $0.0037 (volatility sensitivity per 1%)

ITM (In The Money) probability: **60.71%**

Profit probability: **20.48%**

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
| 7.500000 |       0.150000 |          1.775377 |          1.659059 |          2.547348 |   0.917574 |      0.898666 | 0.093300 | 0.116228 | -0.002737 | 0.003369 |
| 5.000000 |       0.650000 |         -0.624827 |         -0.694718 |         -0.130073 |   0.515271 |      0.259359 | 0.511947 | 0.277893 | -0.006745 | 0.008055 |
| 2.500000 |       2.100000 |         -2.597268 |         -2.657309 |         -2.626441 |   0.011584 |      0.000000 | 0.990330 | 0.018037 | -0.000894 | 0.000523 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$0.15**

Expected profit (USD): **1.78** [lowest: 1.66, highest: 2.55]

Delta: 0.0933 (price sensitivity)

Gamma: 0.1162 (delta sensitivity)

Theta: $-0.0027 (negative decay per trading-day)

Vega: $0.0034 (volatility sensitivity per 1%)

ITM (In The Money) probability: **91.76%**

Profit probability: **89.87%**

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
| 10.000000 |       0.300000 |          3.684675 |          3.378127 |          5.360314 |   0.925964 |      0.938048 | 0.093064 | 0.075330 | -0.001893 | 0.005038 |
|  7.500000 |       0.450000 |          1.356733 |          1.122676 |          2.810969 |   0.795062 |      0.789223 | 0.242008 | 0.141314 | -0.003595 | 0.009450 |
|  5.000000 |       0.850000 |         -0.684248 |         -0.818521 |          0.231659 |   0.478897 |      0.322372 | 0.570314 | 0.177717 | -0.004673 | 0.011885 |
|  2.500000 |       2.300000 |         -2.774544 |         -2.848409 |         -2.668324 |   0.060305 |      0.000000 | 0.953177 | 0.044283 | -0.001502 | 0.002961 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$0.30**

Expected profit (USD): **3.68** [lowest: 3.38, highest: 5.36]

Delta: 0.0931 (price sensitivity)

Gamma: 0.0753 (delta sensitivity)

Theta: $-0.0019 (negative decay per trading-day)

Vega: $0.0050 (volatility sensitivity per 1%)

ITM (In The Money) probability: **92.60%**

Profit probability: **93.80%**

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
| 10.000000 |       0.520000 |          3.129525 |          2.597427 |          5.849695 |   0.828112 |      0.875134 | 0.223451 | 0.096740 | -0.002555 | 0.012464 |
|  7.500000 |       0.780000 |          0.952211 |          0.572355 |          3.207416 |   0.691964 |      0.719907 | 0.376272 | 0.122925 | -0.003294 | 0.015838 |
|  5.000000 |       1.300000 |         -1.021357 |         -1.238684 |          0.438431 |   0.449789 |      0.327726 | 0.622607 | 0.123039 | -0.003408 | 0.015853 |
|  2.500000 |       2.420000 |         -2.849163 |         -2.941504 |         -2.463391 |   0.115241 |      0.000000 | 0.917013 | 0.049492 | -0.001597 | 0.006377 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$0.52**

Expected profit (USD): **3.13** [lowest: 2.60, highest: 5.85]

Delta: 0.2235 (price sensitivity)

Gamma: 0.0967 (delta sensitivity)

Theta: $-0.0026 (negative decay per trading-day)

Vega: $0.0125 (volatility sensitivity per 1%)

ITM (In The Money) probability: **82.81%**

Profit probability: **87.51%**

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

