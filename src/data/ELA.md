# ELA Option Analysis From: 04.01.2026 19:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $11.989999771118164

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3019 [-0.2993, 0.3185]**

- Stock Volatility: **0.7349 [0.6492, 0.8238]**

- Based on **5479** observations


- Garch Volatility forecast: **0.7594**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  7.500000 |       5.170000 |         -1.019683 |         -1.519356 |         -1.195330 |   0.996600 |      0.267033 | 0.997565 | 0.003659 | -0.002192 | 0.000190 |
| 10.000000 |       2.830000 |         -1.057495 |         -1.511396 |         -1.161467 |   0.851008 |      0.244553 | 0.874891 | 0.099469 | -0.021043 | 0.005160 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$5.17**

Expected profit (USD): **-1.02** [lowest: -1.52, highest: -1.20]

Delta: 0.9976 (price sensitivity)

Gamma: 0.0037 (delta sensitivity)

Theta: $-0.0022 (negative decay per trading-day)

Vega: $0.0002 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.66%**

Profit probability: **26.70%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $5.17 | $4.51 | 2.09 | 0.7349 | 0.66 |
| $10 | $2.83 | $2.11 | 1.75 | 0.7349 | 0.72 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5480** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1945**

- Modal profit prediction correlation: **0.2670**

- Backtests total: **75**

- Profitable Trades (profitable trades / total trades): **37.33%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3019 [-0.2993, 0.3185]**

- Stock Volatility: **0.7349 [0.6492, 0.8238]**

- Based on **5479** observations


- Garch Volatility forecast: **0.7594**

### 2. Validate Stock Option Contracts

- Analyze **1** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 12.500000 |       1.500000 |         -0.386471 |         -1.197439 |         -0.224963 |   0.456727 |      0.224820 | 0.518428 | 0.108824 | -0.016840 | 0.020415 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$12**

Market price: **$1.50**

Expected profit (USD): **-0.39** [lowest: -1.20, highest: -0.22]

Delta: 0.5184 (price sensitivity)

Gamma: 0.1088 (delta sensitivity)

Theta: $-0.0168 (negative decay per trading-day)

Vega: $0.0204 (volatility sensitivity per 1%)

ITM (In The Money) probability: **45.67%**

Profit probability: **22.48%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $12 | $1.50 | $1.33 | 0.84 | 0.7349 | 0.17 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5480** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1945**

- Modal profit prediction correlation: **0.2670**

- Backtests total: **75**

- Profitable Trades (profitable trades / total trades): **37.33%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3019 [-0.2993, 0.3185]**

- Stock Volatility: **0.7349 [0.6492, 0.8238]**

- Based on **5479** observations


- Garch Volatility forecast: **0.7594**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       6.800000 |          1.255773 |         -1.829367 |          1.169747 |   0.987903 |      0.407488 | 0.991990 | 0.004511 | -0.001473 | 0.001674 |
| 10.000000 |       2.200000 |          1.462011 |         -0.690881 |          1.843574 |   0.707332 |      0.377182 | 0.758055 | 0.064186 | -0.008643 | 0.023818 |
| 12.500000 |       1.930000 |          0.228377 |         -1.341571 |          0.755772 |   0.498253 |      0.238354 | 0.559647 | 0.081090 | -0.010377 | 0.030091 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$6.80**

Expected profit (USD): **1.26** [lowest: -1.83, highest: 1.17]

Delta: 0.9920 (price sensitivity)

Gamma: 0.0045 (delta sensitivity)

Theta: $-0.0015 (negative decay per trading-day)

Vega: $0.0017 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.79%**

Profit probability: **40.75%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $6.80 | $7.13 | 1.93 | 0.7349 | -0.33 |
| $10 | $2.20 | $3.29 | 0.88 | 0.7349 | -1.09 |
| $12 | $1.93 | $2.11 | 0.84 | 0.7349 | -0.18 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **5480** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1945**

- Modal profit prediction correlation: **0.2670**

- Backtests total: **75**

- Profitable Trades (profitable trades / total trades): **37.33%**

--------------------------------------------------

[SKIPPED]: Empty options data found

