# SIGA Option Analysis From: 05.01.2026 03:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $6.269999980926514

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3299 [-0.2626, 0.3017]**

- Stock Volatility: **0.7278 [0.6439, 0.8146]**

- Based on **6441** observations


- Garch Volatility forecast: **0.4218**

### 2. Validate Stock Option Contracts

- Analyze **20** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.400000 |       3.700000 |         -0.247390 |         -0.487460 |         -0.339842 |   1.000000 |      0.251291 | 1.000000 | 0.000000 | -0.000475 | 0.000000 |
| 4.400000 |       2.100000 |         -0.647390 |         -0.853090 |         -0.704178 |   0.999999 |      0.075830 | 0.999998 | 0.000016 | -0.000871 | 0.000000 |
| 4.000000 |       3.500000 |         -1.647390 |         -1.855045 |         -1.707187 |   1.000000 |      0.000773 | 1.000000 | 0.000000 | -0.000792 | 0.000000 |
| 3.400000 |       5.790000 |         -3.337390 |         -3.613999 |         -3.466376 |   1.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000673 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.70**

Expected profit (USD): **-0.25** [lowest: -0.49, highest: -0.34]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **25.13%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.70 | $3.87 | 6.77 | 0.7278 | -0.17 |
| $3 | $5.79 | $2.88 | 6.39 | 0.7278 | 2.91 |
| $4 | $3.50 | $2.28 | 13.07 | 0.7278 | 1.22 |
| $4 | $2.10 | $1.88 | 3.64 | 0.7278 | 0.22 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6442** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1555**

- Modal profit prediction correlation: **-0.0428**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **44.94%**

--------------------------------------------------

[SKIPPED]: Empty options data found

### Calculate Stock Option Nr. 3

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3299 [-0.2626, 0.3017]**

- Stock Volatility: **0.7278 [0.6439, 0.8146]**

- Based on **6441** observations


- Garch Volatility forecast: **0.4218**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       3.400000 |         -0.001222 |         -1.192122 |         -0.108325 |   0.999430 |      0.331719 | 0.999241 | 0.001690 | -0.000613 | 0.000088 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$3.40**

Expected profit (USD): **-0.00** [lowest: -1.19, highest: -0.11]

Delta: 0.9992 (price sensitivity)

Gamma: 0.0017 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.94%**

Profit probability: **33.17%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $3.40 | $3.33 | 5.30 | 0.7278 | 0.07 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6442** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1555**

- Modal profit prediction correlation: **-0.0428**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **44.94%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.3299 [-0.2626, 0.3017]**

- Stock Volatility: **0.7278 [0.6439, 0.8146]**

- Based on **6441** observations


- Garch Volatility forecast: **0.4218**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.000000 |       1.000000 |          0.049183 |         -0.933778 |          0.696397 |   0.529754 |      0.191439 | 0.496515 | 0.164915 | -0.003426 | 0.020117 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$7**

Market price: **$1.00**

Expected profit (USD): **0.05** [lowest: -0.93, highest: 0.70]

Delta: 0.4965 (price sensitivity)

Gamma: 0.1649 (delta sensitivity)

Theta: $-0.0034 (negative decay per trading-day)

Vega: $0.0201 (volatility sensitivity per 1%)

ITM (In The Money) probability: **52.98%**

Profit probability: **19.14%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $7 | $1.00 | $1.26 | 1.01 | 0.7278 | -0.26 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6442** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1555**

- Modal profit prediction correlation: **-0.0428**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **44.94%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.3299 [-0.2626, 0.3017]**

- Stock Volatility: **0.7278 [0.6439, 0.8146]**

- Based on **6441** observations


- Garch Volatility forecast: **0.4218**

### 2. Validate Stock Option Contracts

- Analyze **13** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.400000 |       4.000000 |          3.337076 |         -2.427362 |          3.313356 |   0.983393 |      0.383119 | 0.978875 | 0.013546 | -0.000662 | 0.003874 |
| 4.400000 |       2.750000 |          2.718262 |         -2.049196 |          3.085304 |   0.867447 |      0.319141 | 0.845177 | 0.063598 | -0.001729 | 0.018188 |
| 9.400000 |       0.700000 |          1.541195 |         -0.777285 |          2.819420 |   0.437675 |      0.154743 | 0.399244 | 0.103139 | -0.002274 | 0.029496 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$4.00**

Expected profit (USD): **3.34** [lowest: -2.43, highest: 3.31]

Delta: 0.9789 (price sensitivity)

Gamma: 0.0135 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0039 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.34%**

Profit probability: **38.31%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $4.00 | $4.23 | 0.53 | 0.7278 | -0.23 |
| $4 | $2.75 | $3.05 | 0.92 | 0.7278 | -0.30 |
| $9 | $0.70 | $1.50 | 0.63 | 0.7278 | -0.80 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **6442** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1555**

- Modal profit prediction correlation: **-0.0428**

- Backtests total: **89**

- Profitable Trades (profitable trades / total trades): **44.94%**

--------------------------------------------------

