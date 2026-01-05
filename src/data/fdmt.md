# FDMT Option Analysis From: 05.01.2026 01:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $7.320000171661377

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0007 [-0.8211, 0.6173]**

- Stock Volatility: **0.8235 [0.7134, 0.9425]**

- Based on **1269** observations


- Garch Volatility forecast: **0.9324**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       2.260000 |         -0.432877 |         -0.788560 |         -0.371243 |   0.977186 |      0.313773 | 0.985817 | 0.027033 | -0.003377 | 0.000526 |
| 6.000000 |       2.850000 |         -1.945874 |         -2.340535 |         -1.931381 |   0.841118 |      0.065872 | 0.883458 | 0.146785 | -0.014081 | 0.002857 |
| 2.500000 |       8.850000 |         -4.530189 |         -5.131393 |         -4.715181 |   1.000000 |      0.002504 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.26**

Expected profit (USD): **-0.43** [lowest: -0.79, highest: -0.37]

Delta: 0.9858 (price sensitivity)

Gamma: 0.0270 (delta sensitivity)

Theta: $-0.0034 (negative decay per trading-day)

Vega: $0.0005 (volatility sensitivity per 1%)

ITM (In The Money) probability: **97.72%**

Profit probability: **31.38%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $8.85 | $4.82 | 3.19 | 0.8235 | 4.03 |
| $5 | $2.26 | $2.33 | 2.91 | 0.8235 | -0.07 |
| $6 | $2.85 | $1.39 | 3.39 | 0.8235 | 1.46 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1270** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.4578**

- Modal profit prediction correlation: **-0.4243**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **40.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0007 [-0.8211, 0.6173]**

- Stock Volatility: **0.8235 [0.7134, 0.9425]**

- Based on **1269** observations


- Garch Volatility forecast: **0.9324**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0007 [-0.8211, 0.6173]**

- Stock Volatility: **0.8235 [0.7134, 0.9425]**

- Based on **1269** observations


- Garch Volatility forecast: **0.9324**

### 2. Validate Stock Option Contracts

- Analyze **15** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       2.840000 |         -0.446714 |         -2.426023 |          1.093415 |   0.627719 |      0.228746 | 0.832768 | 0.056463 | -0.006120 | 0.011604 |
|  7.500000 |       1.450000 |         -0.275843 |         -1.613466 |          0.946892 |   0.365631 |      0.171252 | 0.616346 | 0.086106 | -0.008935 | 0.017696 |
|  9.000000 |       1.150000 |         -0.440435 |         -1.606679 |          0.417831 |   0.259662 |      0.125783 | 0.497988 | 0.089958 | -0.009232 | 0.018487 |
|  2.500000 |       9.150000 |         -4.793667 |         -7.223652 |         -3.151709 |   0.929210 |      0.086276 | 0.982540 | 0.009726 | -0.001401 | 0.001999 |
|  6.000000 |       5.700000 |         -3.874260 |         -5.764280 |         -2.617643 |   0.509923 |      0.085214 | 0.746726 | 0.072151 | -0.007635 | 0.014828 |
| 11.000000 |       1.520000 |         -1.227320 |         -2.034356 |         -0.586568 |   0.164627 |      0.069677 | 0.368332 | 0.085014 | -0.008647 | 0.017471 |
| 20.000000 |       0.600000 |         -0.957120 |         -1.184979 |         -0.868168 |   0.024857 |      0.011450 | 0.092906 | 0.037491 | -0.003755 | 0.007705 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.84**

Expected profit (USD): **-0.45** [lowest: -2.43, highest: 1.09]

Delta: 0.8328 (price sensitivity)

Gamma: 0.0565 (delta sensitivity)

Theta: $-0.0061 (negative decay per trading-day)

Vega: $0.0116 (volatility sensitivity per 1%)

ITM (In The Money) probability: **62.77%**

Profit probability: **22.87%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $9.15 | $4.88 | 1.33 | 0.8235 | 4.27 |
| $5 | $2.84 | $2.81 | 0.83 | 0.8235 | 0.03 |
| $6 | $5.70 | $2.19 | 1.28 | 0.8235 | 3.51 |
| $8 | $1.45 | $1.49 | 0.86 | 0.8235 | -0.04 |
| $9 | $1.15 | $1.01 | 1.97 | 0.8235 | 0.14 |
| $11 | $1.52 | $0.60 | 1.48 | 0.8235 | 0.92 |
| $20 | $0.60 | $0.07 | 2.15 | 0.8235 | 0.53 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1270** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.4578**

- Modal profit prediction correlation: **-0.4243**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **40.00%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0007 [-0.8211, 0.6173]**

- Stock Volatility: **0.8235 [0.7134, 0.9425]**

- Based on **1269** observations


- Garch Volatility forecast: **0.9324**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       4.900000 |         -0.806408 |         -4.251485 |          3.116306 |   0.738176 |      0.186239 | 0.936445 | 0.020215 | -0.002431 | 0.007961 |
| 4.000000 |       4.150000 |         -0.732393 |         -3.912809 |          3.018788 |   0.616415 |      0.177049 | 0.881783 | 0.032114 | -0.003661 | 0.012647 |
| 8.000000 |       1.650000 |          0.019951 |         -2.049165 |          2.876314 |   0.299061 |      0.132086 | 0.640862 | 0.060647 | -0.006482 | 0.023884 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$4.90**

Expected profit (USD): **-0.81** [lowest: -4.25, highest: 3.12]

Delta: 0.9364 (price sensitivity)

Gamma: 0.0202 (delta sensitivity)

Theta: $-0.0024 (negative decay per trading-day)

Vega: $0.0080 (volatility sensitivity per 1%)

ITM (In The Money) probability: **73.82%**

Profit probability: **18.62%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $4.90 | $4.58 | 1.36 | 0.8235 | 0.32 |
| $4 | $4.15 | $3.84 | 1.09 | 0.8235 | 0.31 |
| $8 | $1.65 | $1.92 | 1.60 | 0.8235 | -0.27 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1270** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.4578**

- Modal profit prediction correlation: **-0.4243**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **40.00%**

--------------------------------------------------

