# YEXT Option Analysis From: 05.01.2026 00:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $7.849999904632568

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0530 [-0.3365, 0.2996]**

- Stock Volatility: **0.4786 [0.4184, 0.5425]**

- Based on **2192** observations


- Garch Volatility forecast: **0.3420**

### 2. Validate Stock Option Contracts

- Analyze **13** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 6.000000 |       2.000000 |         -0.633483 |         -0.793683 |         -0.595286 |   0.999991 |      0.090747 | 0.999993 | 0.000066 | -0.001189 | 0.000001 |
| 1.000000 |       7.150000 |         -0.783483 |         -1.015604 |         -0.817592 |   1.000000 |      0.053207 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 5.000000 |       3.170000 |         -0.803483 |         -0.972071 |         -0.774059 |   1.000000 |      0.049341 | 1.000000 | 0.000000 | -0.000990 | 0.000000 |
| 2.500000 |       5.700000 |         -0.833483 |         -1.043052 |         -0.845040 |   1.000000 |      0.043982 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |
| 7.500000 |       0.850000 |         -0.921188 |         -0.955484 |         -0.776854 |   0.766631 |      0.023950 | 0.784876 | 0.592485 | -0.008347 | 0.004571 |
| 4.000000 |       5.010000 |         -1.643483 |         -1.832561 |         -1.634550 |   1.000000 |      0.000896 | 1.000000 | 0.000000 | -0.000792 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$6**

Market price: **$2.00**

Expected profit (USD): **-0.63** [lowest: -0.79, highest: -0.60]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0012 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **9.07%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $7.15 | $6.85 | 10.31 | 0.4786 | 0.30 |
| $2 | $5.70 | $5.35 | 5.26 | 0.4786 | 0.35 |
| $4 | $5.01 | $3.86 | 4.68 | 0.4786 | 1.15 |
| $5 | $3.17 | $2.86 | 2.45 | 0.4786 | 0.31 |
| $6 | $2.00 | $1.86 | 1.24 | 0.4786 | 0.14 |
| $8 | $0.85 | $0.51 | 0.55 | 0.4786 | 0.34 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2193** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1071**

- Modal profit prediction correlation: **-0.1339**

- Backtests total: **28**

- Profitable Trades (profitable trades / total trades): **53.57%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0530 [-0.3365, 0.2996]**

- Stock Volatility: **0.4786 [0.4184, 0.5425]**

- Based on **2192** observations


- Garch Volatility forecast: **0.3420**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 8.000000 |       0.450000 |         -0.509793 |         -0.639270 |         -0.101455 |   0.445059 |      0.153665 | 0.503437 | 0.338127 | -0.005928 | 0.013233 |
| 7.000000 |       1.500000 |         -0.946990 |         -1.272399 |         -0.534992 |   0.773465 |      0.145048 | 0.815161 | 0.226124 | -0.004561 | 0.008850 |
| 9.000000 |       0.150000 |         -0.509821 |         -0.537430 |         -0.206745 |   0.178307 |      0.064019 | 0.219151 | 0.250409 | -0.004187 | 0.009800 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$0.45**

Expected profit (USD): **-0.51** [lowest: -0.64, highest: -0.10]

Delta: 0.5034 (price sensitivity)

Gamma: 0.3381 (delta sensitivity)

Theta: $-0.0059 (negative decay per trading-day)

Vega: $0.0132 (volatility sensitivity per 1%)

ITM (In The Money) probability: **44.51%**

Profit probability: **15.37%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $7 | $1.50 | $1.16 | 0.70 | 0.4786 | 0.34 |
| $8 | $0.45 | $0.60 | 0.54 | 0.4786 | -0.15 |
| $9 | $0.15 | $0.27 | 0.45 | 0.4786 | -0.12 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2193** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1071**

- Modal profit prediction correlation: **-0.1339**

- Backtests total: **28**

- Profitable Trades (profitable trades / total trades): **53.57%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0530 [-0.3365, 0.2996]**

- Stock Volatility: **0.4786 [0.4184, 0.5425]**

- Based on **2192** observations


- Garch Volatility forecast: **0.3420**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       3.350000 |         -0.756080 |         -2.135156 |          0.273700 |   0.946259 |      0.245120 | 0.969800 | 0.031832 | -0.001484 | 0.003843 |
| 8.000000 |       0.850000 |         -0.442045 |         -0.982342 |          0.549041 |   0.457394 |      0.186557 | 0.564051 | 0.183217 | -0.003985 | 0.022117 |
| 6.000000 |       3.120000 |         -1.419284 |         -2.575411 |         -0.384743 |   0.827342 |      0.159958 | 0.887237 | 0.089054 | -0.002553 | 0.010750 |
| 9.000000 |       0.280000 |         -0.245078 |         -0.574609 |          0.621356 |   0.295570 |      0.145741 | 0.393990 | 0.179022 | -0.003717 | 0.021611 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$3.35**

Expected profit (USD): **-0.76** [lowest: -2.14, highest: 0.27]

Delta: 0.9698 (price sensitivity)

Gamma: 0.0318 (delta sensitivity)

Theta: $-0.0015 (negative decay per trading-day)

Vega: $0.0038 (volatility sensitivity per 1%)

ITM (In The Money) probability: **94.63%**

Profit probability: **24.51%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $3.35 | $3.05 | 1.06 | 0.4786 | 0.30 |
| $6 | $3.12 | $2.25 | 1.34 | 0.4786 | 0.87 |
| $8 | $0.85 | $1.09 | 0.49 | 0.4786 | -0.24 |
| $9 | $0.28 | $0.73 | 0.45 | 0.4786 | -0.45 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2193** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1071**

- Modal profit prediction correlation: **-0.1339**

- Backtests total: **28**

- Profitable Trades (profitable trades / total trades): **53.57%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0530 [-0.3365, 0.2996]**

- Stock Volatility: **0.4786 [0.4184, 0.5425]**

- Based on **2192** observations


- Garch Volatility forecast: **0.3420**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       2.020000 |         -0.679303 |         -1.987638 |          1.234795 |   0.599754 |      0.196161 | 0.731080 | 0.113432 | -0.002907 | 0.024585 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$7**

Market price: **$2.02**

Expected profit (USD): **-0.68** [lowest: -1.99, highest: 1.23]

Delta: 0.7311 (price sensitivity)

Gamma: 0.1134 (delta sensitivity)

Theta: $-0.0029 (negative decay per trading-day)

Vega: $0.0246 (volatility sensitivity per 1%)

ITM (In The Money) probability: **59.98%**

Profit probability: **19.62%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $7 | $2.02 | $1.96 | 0.55 | 0.4786 | 0.06 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2193** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1071**

- Modal profit prediction correlation: **-0.1339**

- Backtests total: **28**

- Profitable Trades (profitable trades / total trades): **53.57%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.0530 [-0.3365, 0.2996]**

- Stock Volatility: **0.4786 [0.4184, 0.5425]**

- Based on **2192** observations


- Garch Volatility forecast: **0.3420**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  3.000000 |       3.300000 |          1.704761 |         -1.890502 |          5.391209 |   0.972882 |      0.447650 | 0.991720 | 0.005989 | -0.000651 | 0.002161 |
|  5.000000 |       3.700000 |         -0.498099 |         -3.395029 |          3.095545 |   0.805644 |      0.223441 | 0.908791 | 0.043476 | -0.001567 | 0.015684 |
|  7.000000 |       2.510000 |         -0.678540 |         -2.652177 |          2.749421 |   0.564261 |      0.174581 | 0.736691 | 0.086545 | -0.002370 | 0.031222 |
| 10.000000 |       0.150000 |          0.450073 |         -0.520890 |          3.344037 |   0.280812 |      0.143397 | 0.456587 | 0.105127 | -0.002512 | 0.037926 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$3.30**

Expected profit (USD): **1.70** [lowest: -1.89, highest: 5.39]

Delta: 0.9917 (price sensitivity)

Gamma: 0.0060 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0022 (volatility sensitivity per 1%)

ITM (In The Money) probability: **97.29%**

Profit probability: **44.77%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $3.30 | $5.10 | 0.00 | 0.4786 | -1.80 |
| $5 | $3.70 | $3.55 | 0.72 | 0.4786 | 0.15 |
| $7 | $2.51 | $2.40 | 0.61 | 0.4786 | 0.11 |
| $10 | $0.15 | $1.33 | 0.48 | 0.4786 | -1.18 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2193** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1071**

- Modal profit prediction correlation: **-0.1339**

- Backtests total: **28**

- Profitable Trades (profitable trades / total trades): **53.57%**

--------------------------------------------------

