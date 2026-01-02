# GNW Option Analysis From: 02.01.2026 13:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $9.029999732971191

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2184 [-0.3176, 0.3901]**

- Stock Volatility: **0.4415 [0.3837, 0.5036]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2184 [-0.3176, 0.3901]**

- Stock Volatility: **0.4415 [0.3837, 0.5036]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2184 [-0.3176, 0.3901]**

- Stock Volatility: **0.4415 [0.3837, 0.5036]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       2.900000 |          1.244940 |         -0.238328 |          1.708974 |   0.999963 |      0.721751 | 0.999931 | 0.000191 | -0.000980 | 0.000014 |
| 1.000000 |       7.500000 |          0.644933 |         -0.906299 |          1.045936 |   1.000000 |      0.564993 | 1.000000 | 0.000000 | -0.000195 | 0.000000 |
| 4.000000 |       4.880000 |          0.264933 |         -1.252270 |          0.699776 |   1.000000 |      0.463843 | 1.000000 | 0.000000 | -0.000782 | 0.000000 |
| 2.000000 |       7.150000 |         -0.005067 |         -1.551958 |          0.400276 |   1.000000 |      0.395380 | 1.000000 | 0.000000 | -0.000391 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.90**

Expected profit (USD): **1.24** [lowest: -0.24, highest: 1.71]

Delta: 0.9999 (price sensitivity)

Gamma: 0.0002 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **72.18%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $7.50 | $8.04 | 2.31 | 0.4415 | -0.54 |
| $2 | $7.15 | $7.06 | 3.04 | 0.4415 | 0.09 |
| $4 | $4.88 | $5.09 | 1.73 | 0.4415 | -0.21 |
| $5 | $2.90 | $4.11 | 1.20 | 0.4415 | -1.21 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1508** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0693**

- Modal profit prediction correlation: **0.3637**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **38.89%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2184 [-0.3176, 0.3901]**

- Stock Volatility: **0.4415 [0.3837, 0.5036]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2184 [-0.3176, 0.3901]**

- Stock Volatility: **0.4415 [0.3837, 0.5036]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       4.260000 |          2.770152 |         -3.473858 |          6.380151 |   0.984135 |      0.527029 | 0.971024 | 0.018692 | -0.001170 | 0.007302 |
| 15.000000 |       0.140000 |          0.476366 |         -0.635410 |          3.536090 |   0.255530 |      0.127949 | 0.181692 | 0.074630 | -0.001505 | 0.029152 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$4.26**

Expected profit (USD): **2.77** [lowest: -3.47, highest: 6.38]

Delta: 0.9710 (price sensitivity)

Gamma: 0.0187 (delta sensitivity)

Theta: $-0.0012 (negative decay per trading-day)

Vega: $0.0073 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.41%**

Profit probability: **52.70%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $4.26 | $4.57 | 1.13 | 0.4415 | -0.31 |
| $15 | $0.14 | $0.71 | 0.79 | 0.4415 | -0.57 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1508** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0693**

- Modal profit prediction correlation: **0.3637**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **38.89%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.2184 [-0.3176, 0.3901]**

- Stock Volatility: **0.4415 [0.3837, 0.5036]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2656**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  7.000000 |       3.100000 |          6.801218 |         -3.400616 |         18.258541 |   0.910334 |      0.531264 | 0.841859 | 0.048007 | -0.001616 | 0.037564 |
| 12.000000 |       1.000000 |          4.981865 |         -1.480821 |         16.280149 |   0.646211 |      0.361017 | 0.513731 | 0.079272 | -0.001958 | 0.062028 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$7**

Market price: **$3.10**

Expected profit (USD): **6.80** [lowest: -3.40, highest: 18.26]

Delta: 0.8419 (price sensitivity)

Gamma: 0.0480 (delta sensitivity)

Theta: $-0.0016 (negative decay per trading-day)

Vega: $0.0376 (volatility sensitivity per 1%)

ITM (In The Money) probability: **91.03%**

Profit probability: **53.13%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $7 | $3.10 | $4.02 | 0.76 | 0.4415 | -0.92 |
| $12 | $1.00 | $2.26 | 0.53 | 0.4415 | -1.26 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1508** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0693**

- Modal profit prediction correlation: **0.3637**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **38.89%**

--------------------------------------------------

