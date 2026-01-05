# RLAY Option Analysis From: 05.01.2026 03:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $8.180000305175781

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0015 [-0.6956, 0.5353]**

- Stock Volatility: **0.7329 [0.6359, 0.8376]**

- Based on **1373** observations


- Garch Volatility forecast: **0.6620**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       4.010000 |          0.670501 |          0.272832 |          0.671151 |   1.000000 |      0.706868 | 1.000000 | 0.000000 | -0.000594 | 0.000000 |
| 6.000000 |       1.410000 |          0.272182 |         -0.073577 |          0.326214 |   0.992813 |      0.549407 | 0.995158 | 0.013908 | -0.001890 | 0.000229 |
| 4.000000 |       3.800000 |         -0.119499 |         -0.512863 |         -0.114542 |   1.000000 |      0.395330 | 1.000000 | 0.000000 | -0.000792 | 0.000000 |
| 8.000000 |       1.000000 |         -1.004846 |         -1.121201 |         -0.813904 |   0.547308 |      0.087130 | 0.601779 | 0.381901 | -0.020373 | 0.006288 |
| 9.000000 |       0.300000 |         -0.666538 |         -0.710187 |         -0.534155 |   0.201958 |      0.053663 | 0.243353 | 0.309988 | -0.016192 | 0.005104 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$4.01**

Expected profit (USD): **0.67** [lowest: 0.27, highest: 0.67]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **70.69%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $4.01 | $5.19 | 3.47 | 0.7329 | -1.18 |
| $4 | $3.80 | $4.19 | 2.56 | 0.7329 | -0.39 |
| $6 | $1.41 | $2.20 | 2.13 | 0.7329 | -0.79 |
| $8 | $1.00 | $0.57 | 1.08 | 0.7329 | 0.43 |
| $9 | $0.30 | $0.20 | 1.32 | 0.7329 | 0.10 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1374** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1736**

- Modal profit prediction correlation: **-0.1821**

- Backtests total: **16**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0015 [-0.6956, 0.5353]**

- Stock Volatility: **0.7329 [0.6359, 0.8376]**

- Based on **1373** observations


- Garch Volatility forecast: **0.6620**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 8.000000 |       1.230000 |         -0.706609 |         -1.254114 |         -0.080013 |   0.473483 |      0.181398 | 0.599626 | 0.163495 | -0.010912 | 0.013358 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$1.23**

Expected profit (USD): **-0.71** [lowest: -1.25, highest: -0.08]

Delta: 0.5996 (price sensitivity)

Gamma: 0.1635 (delta sensitivity)

Theta: $-0.0109 (negative decay per trading-day)

Vega: $0.0134 (volatility sensitivity per 1%)

ITM (In The Money) probability: **47.35%**

Profit probability: **18.14%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $1.23 | $1.12 | 1.09 | 0.7329 | 0.11 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1374** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1736**

- Modal profit prediction correlation: **-0.1821**

- Backtests total: **16**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0015 [-0.6956, 0.5353]**

- Stock Volatility: **0.7329 [0.6359, 0.8376]**

- Based on **1373** observations


- Garch Volatility forecast: **0.6620**

### 2. Validate Stock Option Contracts

- Analyze **10** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       4.000000 |          1.184078 |         -0.496843 |          2.366890 |   0.998293 |      0.506390 | 0.999589 | 0.000477 | -0.000520 | 0.000065 |
|  1.000000 |       6.850000 |         -0.166346 |         -1.920026 |          0.944883 |   1.000000 |      0.327199 | 1.000000 | 0.000000 | -0.000196 | 0.000000 |
|  4.000000 |       4.250000 |         -0.541504 |         -2.190561 |          0.628536 |   0.954677 |      0.284104 | 0.982538 | 0.013865 | -0.001669 | 0.001899 |
|  5.000000 |       3.640000 |         -0.845895 |         -2.393517 |          0.305672 |   0.865483 |      0.246563 | 0.936062 | 0.040237 | -0.003521 | 0.005511 |
|  6.000000 |       3.130000 |         -1.138285 |         -2.502998 |         -0.021421 |   0.734314 |      0.205352 | 0.851561 | 0.074422 | -0.005809 | 0.010194 |
| 13.000000 |       0.500000 |         -0.790005 |         -1.009305 |         -0.403073 |   0.079709 |      0.035423 | 0.161138 | 0.078571 | -0.005426 | 0.010762 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$4.00**

Expected profit (USD): **1.18** [lowest: -0.50, highest: 2.37]

Delta: 0.9996 (price sensitivity)

Gamma: 0.0005 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.83%**

Profit probability: **50.64%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $6.85 | $7.19 | 2.86 | 0.7329 | -0.34 |
| $2 | $4.00 | $5.72 | 5.27 | 0.7329 | -1.72 |
| $4 | $4.25 | $4.27 | 1.23 | 0.7329 | -0.02 |
| $5 | $3.64 | $3.37 | 1.31 | 0.7329 | 0.27 |
| $6 | $3.13 | $2.58 | 1.06 | 0.7329 | 0.55 |
| $13 | $0.50 | $0.25 | 1.52 | 0.7329 | 0.25 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1374** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1736**

- Modal profit prediction correlation: **-0.1821**

- Backtests total: **16**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0015 [-0.6956, 0.5353]**

- Stock Volatility: **0.7329 [0.6359, 0.8376]**

- Based on **1373** observations


- Garch Volatility forecast: **0.6620**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       3.500000 |         -0.397386 |         -2.981914 |          2.591019 |   0.705874 |      0.226701 | 0.881859 | 0.041007 | -0.003623 | 0.013016 |
|  7.000000 |       3.800000 |         -1.884646 |         -3.897573 |          0.763047 |   0.488393 |      0.128061 | 0.730346 | 0.068488 | -0.005576 | 0.021739 |
|  9.000000 |       2.200000 |         -1.087851 |         -2.504563 |          1.245269 |   0.324487 |      0.116125 | 0.574472 | 0.081243 | -0.006395 | 0.025787 |
| 12.000000 |       1.100000 |         -0.710173 |         -1.520355 |          1.107937 |   0.172857 |      0.073569 | 0.382097 | 0.079050 | -0.006075 | 0.025091 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$3.50**

Expected profit (USD): **-0.40** [lowest: -2.98, highest: 2.59]

Delta: 0.8819 (price sensitivity)

Gamma: 0.0410 (delta sensitivity)

Theta: $-0.0036 (negative decay per trading-day)

Vega: $0.0130 (volatility sensitivity per 1%)

ITM (In The Money) probability: **70.59%**

Profit probability: **22.67%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $3.50 | $3.71 | 1.03 | 0.7329 | -0.21 |
| $7 | $3.80 | $2.52 | 1.01 | 0.7329 | 1.28 |
| $9 | $2.20 | $1.70 | 1.26 | 0.7329 | 0.50 |
| $12 | $1.10 | $0.95 | 0.99 | 0.7329 | 0.15 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1374** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1736**

- Modal profit prediction correlation: **-0.1821**

- Backtests total: **16**

- Profitable Trades (profitable trades / total trades): **50.00%**

--------------------------------------------------

