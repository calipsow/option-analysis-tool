# INNV Option Analysis From: 02.01.2026 19:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $5.190000057220459

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2288 [-0.6492, 0.6545]**

- Stock Volatility: **0.6632 [0.5718, 0.7629]**

- Based on **1002** observations


- Garch Volatility forecast: **0.6831**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       0.470000 |         -0.522124 |         -0.700972 |         -0.431852 |   0.599934 |      0.156921 | 0.633539 | 0.484496 | -0.011816 | 0.004437 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$0.47**

Expected profit (USD): **-0.52** [lowest: -0.70, highest: -0.43]

Delta: 0.6335 (price sensitivity)

Gamma: 0.4845 (delta sensitivity)

Theta: $-0.0118 (negative decay per trading-day)

Vega: $0.0044 (volatility sensitivity per 1%)

ITM (In The Money) probability: **59.99%**

Profit probability: **15.69%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $0.47 | $0.42 | 0.76 | 0.6632 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1003** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1490**

- Modal profit prediction correlation: **-0.3113**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **36.36%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2288 [-0.6492, 0.6545]**

- Stock Volatility: **0.6632 [0.5718, 0.7629]**

- Based on **1002** observations


- Garch Volatility forecast: **0.6831**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       3.010000 |         -0.586792 |         -1.514742 |         -0.224343 |   0.991250 |      0.265394 | 0.994927 | 0.009222 | -0.000728 | 0.000332 |
| 5.000000 |       1.000000 |         -0.633884 |         -1.210184 |         -0.327290 |   0.544279 |      0.188647 | 0.620200 | 0.239670 | -0.006790 | 0.008623 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.01**

Expected profit (USD): **-0.59** [lowest: -1.51, highest: -0.22]

Delta: 0.9949 (price sensitivity)

Gamma: 0.0092 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0003 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.12%**

Profit probability: **26.54%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.01 | $2.72 | 1.38 | 0.6632 | 0.29 |
| $5 | $1.00 | $0.71 | 0.69 | 0.6632 | 0.29 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1003** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1490**

- Modal profit prediction correlation: **-0.3113**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **36.36%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2288 [-0.6492, 0.6545]**

- Stock Volatility: **0.6632 [0.5718, 0.7629]**

- Based on **1002** observations


- Garch Volatility forecast: **0.6831**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       3.200000 |         -0.304068 |         -2.472176 |          1.027037 |   0.910140 |      0.276991 | 0.954872 | 0.034581 | -0.001413 | 0.003569 |
| 5.000000 |       1.600000 |         -0.493879 |         -1.873561 |          0.590675 |   0.512833 |      0.198256 | 0.649735 | 0.134860 | -0.004283 | 0.013917 |
| 7.500000 |       0.650000 |         -0.435057 |         -1.120902 |          0.261941 |   0.231534 |      0.111061 | 0.351464 | 0.135027 | -0.004123 | 0.013934 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.20**

Expected profit (USD): **-0.30** [lowest: -2.47, highest: 1.03]

Delta: 0.9549 (price sensitivity)

Gamma: 0.0346 (delta sensitivity)

Theta: $-0.0014 (negative decay per trading-day)

Vega: $0.0036 (volatility sensitivity per 1%)

ITM (In The Money) probability: **91.01%**

Profit probability: **27.70%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.20 | $2.80 | 0.84 | 0.6632 | 0.40 |
| $5 | $1.60 | $1.12 | 0.84 | 0.6632 | 0.48 |
| $8 | $0.65 | $0.41 | 0.80 | 0.6632 | 0.24 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1003** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1490**

- Modal profit prediction correlation: **-0.3113**

- Backtests total: **11**

- Profitable Trades (profitable trades / total trades): **36.36%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2288 [-0.6492, 0.6545]**

- Stock Volatility: **0.6632 [0.5718, 0.7629]**

- Based on **1002** observations


- Garch Volatility forecast: **0.6831**

### 2. Validate Stock Option Contracts

- Analyze **1** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

