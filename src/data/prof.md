# PROF Option Analysis From: 05.01.2026 02:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $7.659999847412109

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1613 [-0.5109, 0.4878]**

- Stock Volatility: **0.6321 [0.5496, 0.7207]**

- Based on **1551** observations


- Garch Volatility forecast: **0.6195**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       3.230000 |          1.479186 |          1.180801 |          1.484273 |   1.000000 |      0.951525 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |
| 5.000000 |       2.530000 |         -0.320788 |         -0.594174 |         -0.290608 |   0.999822 |      0.319928 | 0.999870 | 0.000554 | -0.001013 | 0.000008 |
| 7.500000 |       0.500000 |         -0.524168 |         -0.677639 |         -0.438341 |   0.567878 |      0.172393 | 0.599957 | 0.422830 | -0.018473 | 0.005895 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$3.23**

Expected profit (USD): **1.48** [lowest: 1.18, highest: 1.48]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **95.15%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.23 | $5.16 | 0.00 | 0.6321 | -1.93 |
| $5 | $2.53 | $2.67 | 2.78 | 0.6321 | -0.14 |
| $8 | $0.50 | $0.47 | 0.85 | 0.6321 | 0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1552** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1758**

- Modal profit prediction correlation: **-0.4142**

- Backtests total: **19**

- Profitable Trades (profitable trades / total trades): **31.58%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1613 [-0.5109, 0.4878]**

- Stock Volatility: **0.6321 [0.5496, 0.7207]**

- Based on **1551** observations


- Garch Volatility forecast: **0.6195**

### 2. Validate Stock Option Contracts

- Analyze **1** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       2.500000 |         -0.086426 |         -1.044779 |          0.290955 |   0.942455 |      0.373725 | 0.961436 | 0.040981 | -0.002815 | 0.002708 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.50**

Expected profit (USD): **-0.09** [lowest: -1.04, highest: 0.29]

Delta: 0.9614 (price sensitivity)

Gamma: 0.0410 (delta sensitivity)

Theta: $-0.0028 (negative decay per trading-day)

Vega: $0.0027 (volatility sensitivity per 1%)

ITM (In The Money) probability: **94.25%**

Profit probability: **37.37%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $2.50 | $2.74 | 0.91 | 0.6321 | -0.24 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1552** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1758**

- Modal profit prediction correlation: **-0.4142**

- Backtests total: **19**

- Profitable Trades (profitable trades / total trades): **31.58%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1613 [-0.5109, 0.4878]**

- Stock Volatility: **0.6321 [0.5496, 0.7207]**

- Based on **1551** observations


- Garch Volatility forecast: **0.6195**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       2.980000 |         -0.161881 |         -1.980882 |          0.848225 |   0.838961 |      0.311892 | 0.901903 | 0.054987 | -0.003485 | 0.008392 |
| 10.000000 |       0.250000 |         -0.013506 |         -0.625566 |          0.572317 |   0.242930 |      0.142800 | 0.346557 | 0.117268 | -0.006159 | 0.017897 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$2.98**

Expected profit (USD): **-0.16** [lowest: -1.98, highest: 0.85]

Delta: 0.9019 (price sensitivity)

Gamma: 0.0550 (delta sensitivity)

Theta: $-0.0035 (negative decay per trading-day)

Vega: $0.0084 (volatility sensitivity per 1%)

ITM (In The Money) probability: **83.90%**

Profit probability: **31.19%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $2.98 | $2.92 | 1.01 | 0.6321 | 0.06 |
| $10 | $0.25 | $0.56 | 0.65 | 0.6321 | -0.31 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1552** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1758**

- Modal profit prediction correlation: **-0.4142**

- Backtests total: **19**

- Profitable Trades (profitable trades / total trades): **31.58%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1613 [-0.5109, 0.4878]**

- Stock Volatility: **0.6321 [0.5496, 0.7207]**

- Based on **1551** observations


- Garch Volatility forecast: **0.6195**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       4.980000 |          0.695673 |         -2.901574 |          2.961853 |   0.969671 |      0.341086 | 0.989355 | 0.006396 | -0.000780 | 0.001882 |
| 5.000000 |       2.800000 |          0.694857 |         -2.282837 |          2.890465 |   0.748353 |      0.316344 | 0.863490 | 0.049721 | -0.003175 | 0.014628 |
| 7.500000 |       1.850000 |          0.112955 |         -1.994713 |          2.005000 |   0.485429 |      0.218873 | 0.651836 | 0.084016 | -0.004848 | 0.024718 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$4.98**

Expected profit (USD): **0.70** [lowest: -2.90, highest: 2.96]

Delta: 0.9894 (price sensitivity)

Gamma: 0.0064 (delta sensitivity)

Theta: $-0.0008 (negative decay per trading-day)

Vega: $0.0019 (volatility sensitivity per 1%)

ITM (In The Money) probability: **96.97%**

Profit probability: **34.11%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $4.98 | $5.27 | 2.34 | 0.6321 | -0.29 |
| $5 | $2.80 | $3.21 | 0.77 | 0.6321 | -0.41 |
| $8 | $1.85 | $1.85 | 0.52 | 0.6321 | 0.00 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1552** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1758**

- Modal profit prediction correlation: **-0.4142**

- Backtests total: **19**

- Profitable Trades (profitable trades / total trades): **31.58%**

--------------------------------------------------

