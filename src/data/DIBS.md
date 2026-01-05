# DIBS Option Analysis From: 05.01.2026 01:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $5.900000095367432

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.1761 [-0.6402, 0.4324]**

- Stock Volatility: **0.5835 [0.5045, 0.6693]**

- Based on **1146** observations


- Garch Volatility forecast: **0.4522**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       1.370000 |         -1.005462 |         -1.123863 |         -0.876121 |   0.965563 |      0.023206 | 0.977772 | 0.105392 | -0.002293 | 0.000622 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$1.37**

Expected profit (USD): **-1.01** [lowest: -1.12, highest: -0.88]

Delta: 0.9778 (price sensitivity)

Gamma: 0.1054 (delta sensitivity)

Theta: $-0.0023 (negative decay per trading-day)

Vega: $0.0006 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.56%**

Profit probability: **2.32%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $1.37 | $0.93 | 1.11 | 0.5835 | 0.44 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1147** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1865**

- Modal profit prediction correlation: **-0.0765**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **76.92%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.1761 [-0.6402, 0.4324]**

- Stock Volatility: **0.5835 [0.5045, 0.6693]**

- Based on **1146** observations


- Garch Volatility forecast: **0.4522**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       3.200000 |         -0.593161 |         -1.367986 |          0.415317 |   0.998674 |      0.238650 | 0.999782 | 0.000540 | -0.000497 | 0.000026 |
| 5.000000 |       1.250000 |         -0.850568 |         -1.260660 |          0.122743 |   0.623825 |      0.149056 | 0.795988 | 0.186350 | -0.003650 | 0.008997 |
| 7.500000 |       0.250000 |         -0.642384 |         -0.710879 |         -0.156695 |   0.104200 |      0.034437 | 0.227790 | 0.198648 | -0.003376 | 0.009590 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.20**

Expected profit (USD): **-0.59** [lowest: -1.37, highest: 0.42]

Delta: 0.9998 (price sensitivity)

Gamma: 0.0005 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.87%**

Profit probability: **23.87%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.20 | $3.44 | 1.20 | 0.5835 | -0.24 |
| $5 | $1.25 | $1.27 | 0.87 | 0.5835 | -0.02 |
| $8 | $0.25 | $0.29 | 0.84 | 0.5835 | -0.04 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1147** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1865**

- Modal profit prediction correlation: **-0.0765**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **76.92%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.1761 [-0.6402, 0.4324]**

- Stock Volatility: **0.5835 [0.5045, 0.6693]**

- Based on **1146** observations


- Garch Volatility forecast: **0.4522**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       3.650000 |         -1.368180 |         -2.728067 |          1.082228 |   0.952804 |      0.143975 | 0.992617 | 0.008699 | -0.000617 | 0.000969 |
|  5.000000 |       1.500000 |         -1.051402 |         -1.712626 |          1.093547 |   0.472404 |      0.116723 | 0.756842 | 0.133355 | -0.002848 | 0.014856 |
|  7.500000 |       0.600000 |         -0.846939 |         -1.057995 |          0.574321 |   0.138260 |      0.043740 | 0.373437 | 0.161299 | -0.003067 | 0.017969 |
| 10.000000 |       0.200000 |         -0.635739 |         -0.692233 |          0.191481 |   0.035061 |      0.011976 | 0.147846 | 0.098356 | -0.001806 | 0.010957 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.65**

Expected profit (USD): **-1.37** [lowest: -2.73, highest: 1.08]

Delta: 0.9926 (price sensitivity)

Gamma: 0.0087 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0010 (volatility sensitivity per 1%)

ITM (In The Money) probability: **95.28%**

Profit probability: **14.40%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.65 | $3.50 | 0.81 | 0.5835 | 0.15 |
| $5 | $1.50 | $1.61 | 0.63 | 0.5835 | -0.11 |
| $8 | $0.60 | $0.66 | 0.60 | 0.5835 | -0.06 |
| $10 | $0.20 | $0.26 | 0.62 | 0.5835 | -0.06 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1147** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1865**

- Modal profit prediction correlation: **-0.0765**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **76.92%**

--------------------------------------------------

