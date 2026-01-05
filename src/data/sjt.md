# SJT Option Analysis From: 05.01.2026 03:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $5.75

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1239 [-0.1283, 0.1605]**

- Stock Volatility: **0.3744 [0.3313, 0.4191]**

- Based on **6508** observations


- Garch Volatility forecast: **0.4115**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       3.200000 |         -0.421668 |         -0.544236 |         -0.478292 |   1.000000 |      0.163960 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |
| 5.000000 |       0.730000 |         -0.446485 |         -0.523521 |         -0.455566 |   0.965407 |      0.149114 | 0.968383 | 0.158564 | -0.002545 | 0.000814 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.20**

Expected profit (USD): **-0.42** [lowest: -0.54, highest: -0.48]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **16.40%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.20 | $3.25 | 5.22 | 0.3744 | -0.05 |
| $5 | $0.73 | $0.76 | 1.25 | 0.3744 | -0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6509** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1010**

- Modal profit prediction correlation: **0.3174**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **52.81%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1239 [-0.1283, 0.1605]**

- Stock Volatility: **0.3744 [0.3313, 0.4191]**

- Based on **6508** observations


- Garch Volatility forecast: **0.4115**

### 2. Validate Stock Option Contracts

- Analyze **1** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       0.900000 |         -0.425811 |         -0.714713 |         -0.434371 |   0.793382 |      0.262482 | 0.821912 | 0.254090 | -0.003729 | 0.006333 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$0.90**

Expected profit (USD): **-0.43** [lowest: -0.71, highest: -0.43]

Delta: 0.8219 (price sensitivity)

Gamma: 0.2541 (delta sensitivity)

Theta: $-0.0037 (negative decay per trading-day)

Vega: $0.0063 (volatility sensitivity per 1%)

ITM (In The Money) probability: **79.34%**

Profit probability: **26.25%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $0.90 | $0.87 | 1.22 | 0.3744 | 0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6509** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1010**

- Modal profit prediction correlation: **0.3174**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **52.81%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1239 [-0.1283, 0.1605]**

- Stock Volatility: **0.3744 [0.3313, 0.4191]**

- Based on **6508** observations


- Garch Volatility forecast: **0.4115**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       3.320000 |         -0.277118 |         -0.927195 |         -0.256892 |   0.998781 |      0.344096 | 0.999320 | 0.001475 | -0.000504 | 0.000086 |
| 5.000000 |       1.000000 |         -0.232560 |         -0.792435 |         -0.219458 |   0.705802 |      0.307769 | 0.762143 | 0.193254 | -0.003101 | 0.011261 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.32**

Expected profit (USD): **-0.28** [lowest: -0.93, highest: -0.26]

Delta: 0.9993 (price sensitivity)

Gamma: 0.0015 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.88%**

Profit probability: **34.41%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.32 | $3.30 | 1.98 | 0.3744 | 0.02 |
| $5 | $1.00 | $1.04 | 0.58 | 0.3744 | -0.04 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6509** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1010**

- Modal profit prediction correlation: **0.3174**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **52.81%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1239 [-0.1283, 0.1605]**

- Stock Volatility: **0.3744 [0.3313, 0.4191]**

- Based on **6508** observations


- Garch Volatility forecast: **0.4115**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       3.060000 |          0.263647 |         -0.911380 |          0.370577 |   0.985130 |      0.410915 | 0.992264 | 0.009457 | -0.000592 | 0.001068 |
| 5.000000 |       1.140000 |          0.047418 |         -0.934320 |          0.093930 |   0.656353 |      0.323215 | 0.742193 | 0.143502 | -0.002468 | 0.016209 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.06**

Expected profit (USD): **0.26** [lowest: -0.91, highest: 0.37]

Delta: 0.9923 (price sensitivity)

Gamma: 0.0095 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0011 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.51%**

Profit probability: **41.09%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.06 | $3.34 | 1.45 | 0.3744 | -0.28 |
| $5 | $1.14 | $1.25 | 0.56 | 0.3744 | -0.11 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6509** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1010**

- Modal profit prediction correlation: **0.3174**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **52.81%**

--------------------------------------------------

