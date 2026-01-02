# SIFY Option Analysis From: 02.01.2026 19:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $12.1899995803833

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1815 [-0.8174, 0.7384]**

- Stock Volatility: **0.7914 [0.6824, 0.9105]**

- Based on **1002** observations


- Garch Volatility forecast: **0.6797**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       3.900000 |          5.404656 |          4.673330 |          5.649979 |   1.000000 |      0.999927 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |
|  5.000000 |       6.800000 |          0.004656 |         -0.808512 |          0.168137 |   1.000000 |      0.428083 | 1.000000 | 0.000000 | -0.000990 | 0.000000 |
|  7.500000 |       4.400000 |         -0.095227 |         -0.854026 |          0.123137 |   0.999576 |      0.406324 | 0.999704 | 0.000618 | -0.001558 | 0.000030 |
| 10.000000 |       2.800000 |         -0.939934 |         -1.556020 |         -0.621251 |   0.912362 |      0.235922 | 0.927022 | 0.078308 | -0.011230 | 0.003838 |
| 12.500000 |       0.700000 |         -0.575535 |         -0.778113 |         -0.165579 |   0.428156 |      0.177869 | 0.467106 | 0.224584 | -0.028085 | 0.011008 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.90**

Expected profit (USD): **5.40** [lowest: 4.67, highest: 5.65]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **99.99%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.90 | $9.70 | 6.21 | 0.7914 | -5.80 |
| $5 | $6.80 | $7.20 | 6.00 | 0.7914 | -0.40 |
| $8 | $4.40 | $4.71 | 1.42 | 0.7914 | -0.31 |
| $10 | $2.80 | $2.35 | 1.15 | 0.7914 | 0.45 |
| $12 | $0.70 | $0.75 | 1.17 | 0.7914 | -0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1003** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2693**

- Modal profit prediction correlation: **-0.1153**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1815 [-0.8174, 0.7384]**

- Stock Volatility: **0.7914 [0.6824, 0.9105]**

- Based on **1002** observations


- Garch Volatility forecast: **0.6797**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.500000 |       1.810000 |         -0.704631 |         -1.783794 |          0.417732 |   0.450543 |      0.193633 | 0.541605 | 0.105117 | -0.016629 | 0.021109 |
| 15.000000 |       1.400000 |         -1.136284 |         -1.739819 |         -0.271741 |   0.237892 |      0.098366 | 0.314075 | 0.093995 | -0.014580 | 0.018875 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$1.81**

Expected profit (USD): **-0.70** [lowest: -1.78, highest: 0.42]

Delta: 0.5416 (price sensitivity)

Gamma: 0.1051 (delta sensitivity)

Theta: $-0.0166 (negative decay per trading-day)

Vega: $0.0211 (volatility sensitivity per 1%)

ITM (In The Money) probability: **45.05%**

Profit probability: **19.36%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $12 | $1.81 | $1.59 | 1.10 | 0.7914 | 0.22 |
| $15 | $1.40 | $0.81 | 1.22 | 0.7914 | 0.59 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1003** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2693**

- Modal profit prediction correlation: **-0.1153**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1815 [-0.8174, 0.7384]**

- Stock Volatility: **0.7914 [0.6824, 0.9105]**

- Based on **1002** observations


- Garch Volatility forecast: **0.6797**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       6.510000 |          1.159747 |         -3.386242 |          4.300022 |   0.961379 |      0.373479 | 0.983635 | 0.006956 | -0.002075 | 0.003196 |
|  7.500000 |       5.500000 |         -0.079647 |         -4.063248 |          3.014534 |   0.822348 |      0.285806 | 0.901963 | 0.029486 | -0.006032 | 0.013545 |
| 10.000000 |       3.570000 |          0.034199 |         -3.105575 |          2.971905 |   0.627991 |      0.257324 | 0.756475 | 0.053416 | -0.009973 | 0.024538 |
| 12.500000 |       2.470000 |         -0.200751 |         -2.524859 |          2.443047 |   0.445451 |      0.198014 | 0.591462 | 0.066213 | -0.011929 | 0.030417 |
| 15.000000 |       2.250000 |         -0.907133 |         -2.508982 |          1.434136 |   0.302915 |      0.128307 | 0.441343 | 0.067271 | -0.011901 | 0.030903 |
| 17.500000 |       2.300000 |         -1.579805 |         -2.768615 |          0.311493 |   0.201475 |      0.078773 | 0.319930 | 0.060957 | -0.010667 | 0.028002 |
| 20.000000 |       1.070000 |         -0.761713 |         -1.576661 |          0.811177 |   0.132672 |      0.061844 | 0.228022 | 0.051513 | -0.008950 | 0.023664 |
| 22.500000 |       0.050000 |         -0.012497 |         -0.566231 |          1.280467 |   0.087136 |      0.046734 | 0.161054 | 0.041656 | -0.007200 | 0.019136 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$6.51**

Expected profit (USD): **1.16** [lowest: -3.39, highest: 4.30]

Delta: 0.9836 (price sensitivity)

Gamma: 0.0070 (delta sensitivity)

Theta: $-0.0021 (negative decay per trading-day)

Vega: $0.0032 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.14%**

Profit probability: **37.35%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $6.51 | $7.35 | 1.37 | 0.7914 | -0.84 |
| $8 | $5.50 | $5.24 | 1.11 | 0.7914 | 0.26 |
| $10 | $3.57 | $3.60 | 1.16 | 0.7914 | -0.03 |
| $12 | $2.47 | $2.42 | 1.13 | 0.7914 | 0.05 |
| $15 | $2.25 | $1.62 | 1.02 | 0.7914 | 0.63 |
| $18 | $2.30 | $1.08 | 1.26 | 0.7914 | 1.22 |
| $20 | $1.07 | $0.73 | 1.34 | 0.7914 | 0.34 |
| $22 | $0.05 | $0.49 | 1.42 | 0.7914 | -0.44 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1003** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2693**

- Modal profit prediction correlation: **-0.1153**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1815 [-0.8174, 0.7384]**

- Stock Volatility: **0.7914 [0.6824, 0.9105]**

- Based on **1002** observations


- Garch Volatility forecast: **0.6797**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       6.790000 |          1.888037 |         -5.264079 |          9.114159 |   0.882461 |      0.308215 | 0.956660 | 0.011155 | -0.002755 | 0.009861 |
|  7.500000 |       5.400000 |          1.268960 |         -4.857006 |          8.292857 |   0.721664 |      0.264746 | 0.867272 | 0.026033 | -0.005494 | 0.023012 |
| 10.000000 |       4.320000 |          0.745507 |         -4.293158 |          7.422298 |   0.564496 |      0.218365 | 0.754329 | 0.038191 | -0.007618 | 0.033759 |
| 12.500000 |       3.560000 |          0.264196 |         -3.815432 |          6.485376 |   0.433450 |      0.173125 | 0.639903 | 0.045388 | -0.008804 | 0.040121 |
| 15.000000 |       2.570000 |          0.304288 |         -2.969068 |          6.034675 |   0.330980 |      0.142101 | 0.535296 | 0.048206 | -0.009196 | 0.042611 |
| 17.500000 |       2.490000 |         -0.341113 |         -2.996888 |          4.858125 |   0.252974 |      0.104416 | 0.444582 | 0.047928 | -0.009044 | 0.042366 |
| 20.000000 |       1.800000 |         -0.206567 |         -2.349984 |          4.504930 |   0.194173 |      0.083492 | 0.368125 | 0.045727 | -0.008561 | 0.040420 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$6.79**

Expected profit (USD): **1.89** [lowest: -5.26, highest: 9.11]

Delta: 0.9567 (price sensitivity)

Gamma: 0.0112 (delta sensitivity)

Theta: $-0.0028 (negative decay per trading-day)

Vega: $0.0099 (volatility sensitivity per 1%)

ITM (In The Money) probability: **88.25%**

Profit probability: **30.82%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $6.79 | $7.60 | 1.14 | 0.7914 | -0.81 |
| $8 | $5.40 | $5.80 | 1.13 | 0.7914 | -0.40 |
| $10 | $4.32 | $4.42 | 1.12 | 0.7914 | -0.10 |
| $12 | $3.56 | $3.38 | 1.09 | 0.7914 | 0.18 |
| $15 | $2.57 | $2.60 | 1.02 | 0.7914 | -0.03 |
| $18 | $2.49 | $2.02 | 1.12 | 0.7914 | 0.47 |
| $20 | $1.80 | $1.59 | 1.24 | 0.7914 | 0.21 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1003** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2693**

- Modal profit prediction correlation: **-0.1153**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **63.64%**

--------------------------------------------------

