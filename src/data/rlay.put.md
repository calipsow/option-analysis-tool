# Put Option. RLAY Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

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
| 9.000000 |       0.300000 |          0.152961 |          0.035026 |          0.389307 |   0.798042 |      0.566443 | 0.243353 | 0.309988 | -0.016192 | 0.005104 |
| 8.000000 |       1.000000 |         -1.185346 |         -1.244526 |         -1.002026 |   0.452692 |      0.043309 | 0.601779 | 0.381901 | -0.020373 | 0.006288 |
| 6.000000 |       1.410000 |         -1.908319 |         -2.035733 |         -2.018711 |   0.007187 |      0.000000 | 0.995158 | 0.013908 | -0.001890 | 0.000229 |
| 4.000000 |       3.800000 |         -4.300000 |         -4.470169 |         -4.470166 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000792 | 0.000000 |
| 3.000000 |       4.010000 |         -4.510000 |         -4.684475 |         -4.684475 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000594 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$9**

Market price: **$0.30**

Expected profit (USD): **0.15** [lowest: 0.04, highest: 0.39]

Delta: 0.2434 (price sensitivity)

Gamma: 0.3100 (delta sensitivity)

Theta: $-0.0162 (negative decay per trading-day)

Vega: $0.0051 (volatility sensitivity per 1%)

ITM (In The Money) probability: **79.80%**

Profit probability: **56.64%**

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
| 8.000000 |       1.230000 |         -0.888861 |         -1.239563 |         -0.333573 |   0.526517 |      0.270678 | 0.599626 | 0.163495 | -0.010912 | 0.013358 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$1.23**

Expected profit (USD): **-0.89** [lowest: -1.24, highest: -0.33]

Delta: 0.5996 (price sensitivity)

Gamma: 0.1635 (delta sensitivity)

Theta: $-0.0109 (negative decay per trading-day)

Vega: $0.0134 (volatility sensitivity per 1%)

ITM (In The Money) probability: **52.65%**

Profit probability: **27.07%**

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
| 13.000000 |       0.500000 |          4.026341 |          2.835864 |          5.361615 |   0.920291 |      0.919417 | 0.161138 | 0.078571 | -0.005426 | 0.010762 |
|  6.000000 |       3.130000 |         -3.321939 |         -3.669837 |         -3.034877 |   0.265686 |      0.002094 | 0.851561 | 0.074422 | -0.005809 | 0.010194 |
|  5.000000 |       3.640000 |         -4.029548 |         -4.292774 |         -3.968639 |   0.134517 |      0.000000 | 0.936062 | 0.040237 | -0.003521 | 0.005511 |
|  2.500000 |       4.000000 |         -4.499576 |         -4.685810 |         -4.679002 |   0.001707 |      0.000000 | 0.999589 | 0.000477 | -0.000520 | 0.000065 |
|  4.000000 |       4.250000 |         -4.725158 |         -4.938128 |         -4.821310 |   0.045323 |      0.000000 | 0.982538 | 0.013865 | -0.001669 | 0.001899 |
|  1.000000 |       6.850000 |         -7.350000 |         -7.607260 |         -7.607258 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000196 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$13**

Market price: **$0.50**

Expected profit (USD): **4.03** [lowest: 2.84, highest: 5.36]

Delta: 0.1611 (price sensitivity)

Gamma: 0.0786 (delta sensitivity)

Theta: $-0.0054 (negative decay per trading-day)

Vega: $0.0108 (volatility sensitivity per 1%)

ITM (In The Money) probability: **92.03%**

Profit probability: **91.94%**

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
| 12.000000 |       1.100000 |          3.101667 |          1.106460 |          5.371960 |   0.827143 |      0.840104 | 0.382097 | 0.079050 | -0.006075 | 0.025091 |
|  9.000000 |       2.200000 |         -0.276011 |         -1.665380 |          1.444775 |   0.675513 |      0.557658 | 0.574472 | 0.081243 | -0.006395 | 0.025787 |
|  7.000000 |       3.800000 |         -3.072806 |         -4.033774 |         -1.915818 |   0.511607 |      0.098263 | 0.730346 | 0.068488 | -0.005576 | 0.021739 |
|  5.000000 |       3.500000 |         -3.585546 |         -4.076672 |         -3.008939 |   0.294126 |      0.001462 | 0.881859 | 0.041007 | -0.003623 | 0.013016 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$12**

Market price: **$1.10**

Expected profit (USD): **3.10** [lowest: 1.11, highest: 5.37]

Delta: 0.3821 (price sensitivity)

Gamma: 0.0790 (delta sensitivity)

Theta: $-0.0061 (negative decay per trading-day)

Vega: $0.0251 (volatility sensitivity per 1%)

ITM (In The Money) probability: **82.71%**

Profit probability: **84.01%**

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

