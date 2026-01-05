# DAO Option Analysis From: 05.01.2026 00:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $11.220000267028809

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3149 [-0.6490, 0.6385]**

- Stock Volatility: **0.8154 [0.7089, 0.9297]**

- Based on **1553** observations


- Garch Volatility forecast: **0.6963**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 10.000000 |       1.240000 |         -0.228109 |         -0.577187 |         -0.041187 |   0.796993 |      0.346129 | 0.815452 | 0.167848 | -0.022696 | 0.005957 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$1.24**

Expected profit (USD): **-0.23** [lowest: -0.58, highest: -0.04]

Delta: 0.8155 (price sensitivity)

Gamma: 0.1678 (delta sensitivity)

Theta: $-0.0227 (negative decay per trading-day)

Vega: $0.0060 (volatility sensitivity per 1%)

ITM (In The Money) probability: **79.70%**

Profit probability: **34.61%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $10 | $1.24 | $1.48 | 0.76 | 0.8154 | -0.24 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1554** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1573**

- Modal profit prediction correlation: **0.0201**

- Backtests total: **19**

- Profitable Trades (profitable trades / total trades): **42.11%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3149 [-0.6490, 0.6385]**

- Stock Volatility: **0.8154 [0.7089, 0.9297]**

- Based on **1553** observations


- Garch Volatility forecast: **0.6963**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       4.210000 |          2.159979 |          0.165507 |          2.743150 |   0.997642 |      0.633281 | 0.998432 | 0.001556 | -0.001164 | 0.000241 |
|  7.500000 |       2.200000 |          1.735754 |         -0.025313 |          2.422348 |   0.923959 |      0.568025 | 0.940688 | 0.036163 | -0.005606 | 0.005597 |
| 10.000000 |       1.700000 |          0.210312 |         -1.003940 |          0.999757 |   0.671280 |      0.328506 | 0.716274 | 0.103776 | -0.013489 | 0.016062 |
| 12.500000 |       0.580000 |          0.035945 |         -0.618060 |          0.776804 |   0.373160 |      0.208293 | 0.422642 | 0.119903 | -0.014968 | 0.018558 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$4.21**

Expected profit (USD): **2.16** [lowest: 0.17, highest: 2.74]

Delta: 0.9984 (price sensitivity)

Gamma: 0.0016 (delta sensitivity)

Theta: $-0.0012 (negative decay per trading-day)

Vega: $0.0002 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.76%**

Profit probability: **63.33%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $4.21 | $6.27 | 0.00 | 0.8154 | -2.06 |
| $8 | $2.20 | $3.96 | 0.76 | 0.8154 | -1.76 |
| $10 | $1.70 | $2.19 | 0.80 | 0.8154 | -0.49 |
| $12 | $0.58 | $1.10 | 0.71 | 0.8154 | -0.52 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1554** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1573**

- Modal profit prediction correlation: **0.0201**

- Backtests total: **19**

- Profitable Trades (profitable trades / total trades): **42.11%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3149 [-0.6490, 0.6385]**

- Stock Volatility: **0.8154 [0.7089, 0.9297]**

- Based on **1553** observations


- Garch Volatility forecast: **0.6963**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  7.500000 |       2.450000 |          3.010449 |         -1.115884 |          5.417165 |   0.824587 |      0.455766 | 0.871088 | 0.038996 | -0.005473 | 0.016883 |
| 10.000000 |       1.800000 |          1.837534 |         -1.283117 |          4.287932 |   0.631001 |      0.326283 | 0.703006 | 0.064173 | -0.008242 | 0.027784 |
| 20.000000 |       0.300000 |          0.017788 |         -0.687532 |          1.706290 |   0.134041 |      0.061400 | 0.181694 | 0.048939 | -0.005836 | 0.021189 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$2.45**

Expected profit (USD): **3.01** [lowest: -1.12, highest: 5.42]

Delta: 0.8711 (price sensitivity)

Gamma: 0.0390 (delta sensitivity)

Theta: $-0.0055 (negative decay per trading-day)

Vega: $0.0169 (volatility sensitivity per 1%)

ITM (In The Money) probability: **82.46%**

Profit probability: **45.58%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $8 | $2.45 | $4.60 | 1.10 | 0.8154 | -2.15 |
| $10 | $1.80 | $3.21 | 0.77 | 0.8154 | -1.41 |
| $20 | $0.30 | $0.77 | 0.77 | 0.8154 | -0.47 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1554** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1573**

- Modal profit prediction correlation: **0.0201**

- Backtests total: **19**

- Profitable Trades (profitable trades / total trades): **42.11%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3149 [-0.6490, 0.6385]**

- Stock Volatility: **0.8154 [0.7089, 0.9297]**

- Based on **1553** observations


- Garch Volatility forecast: **0.6963**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  7.500000 |       2.750000 |          4.608013 |         -2.036230 |          9.642219 |   0.778882 |      0.392147 | 0.847107 | 0.033259 | -0.004621 | 0.025146 |
|  5.000000 |       5.290000 |          4.200553 |         -3.691872 |          9.150546 |   0.920608 |      0.389893 | 0.952029 | 0.014053 | -0.002366 | 0.010625 |
| 12.500000 |       2.000000 |          2.227354 |         -2.024624 |          7.171031 |   0.484514 |      0.211800 | 0.585839 | 0.054883 | -0.006897 | 0.041496 |
| 17.500000 |       0.930000 |          1.417213 |         -1.222994 |          5.910881 |   0.284152 |      0.121419 | 0.376431 | 0.053472 | -0.006507 | 0.040428 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$8**

Market price: **$2.75**

Expected profit (USD): **4.61** [lowest: -2.04, highest: 9.64]

Delta: 0.8471 (price sensitivity)

Gamma: 0.0333 (delta sensitivity)

Theta: $-0.0046 (negative decay per trading-day)

Vega: $0.0251 (volatility sensitivity per 1%)

ITM (In The Money) probability: **77.89%**

Profit probability: **39.21%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $5.29 | $6.81 | 1.02 | 0.8154 | -1.52 |
| $8 | $2.75 | $5.22 | 1.26 | 0.8154 | -2.47 |
| $12 | $2.00 | $3.14 | 0.64 | 0.8154 | -1.14 |
| $18 | $0.93 | $1.97 | 0.66 | 0.8154 | -1.04 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1554** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1573**

- Modal profit prediction correlation: **0.0201**

- Backtests total: **19**

- Profitable Trades (profitable trades / total trades): **42.11%**

--------------------------------------------------

