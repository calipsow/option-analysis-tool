# Put Option. FDMT Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

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
| 6.000000 |       2.850000 |         -3.265686 |         -3.465619 |         -3.381169 |   0.158882 |      0.000000 | 0.883458 | 0.146785 | -0.014081 | 0.002857 |
| 5.000000 |       2.260000 |         -2.752688 |         -2.876689 |         -2.865596 |   0.022814 |      0.000000 | 0.985817 | 0.027033 | -0.003377 | 0.000526 |
| 2.500000 |       8.850000 |         -9.350000 |         -9.716713 |         -9.716713 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$6**

Market price: **$2.85**

Expected profit (USD): **-3.27** [lowest: -3.47, highest: -3.38]

Delta: 0.8835 (price sensitivity)

Gamma: 0.1468 (delta sensitivity)

Theta: $-0.0141 (negative decay per trading-day)

Vega: $0.0029 (volatility sensitivity per 1%)

ITM (In The Money) probability: **15.89%**

Profit probability: **0.00%**

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
| 20.000000 |       0.600000 |         11.724789 |          9.596525 |         13.562226 |   0.975143 |      0.981841 | 0.092906 | 0.037491 | -0.003755 | 0.007705 |
| 11.000000 |       1.520000 |          2.454589 |          0.713735 |          3.792934 |   0.835373 |      0.806487 | 0.368332 | 0.085014 | -0.008647 | 0.017471 |
|  9.000000 |       1.150000 |          1.241473 |         -0.264175 |          2.262157 |   0.740338 |      0.703470 | 0.497988 | 0.089958 | -0.009232 | 0.018487 |
|  7.500000 |       1.450000 |         -0.093935 |         -1.184409 |          0.786641 |   0.634369 |      0.528200 | 0.616346 | 0.086106 | -0.008935 | 0.017696 |
|  5.000000 |       2.840000 |         -2.764805 |         -3.392448 |         -2.521943 |   0.372281 |      0.027334 | 0.832768 | 0.056463 | -0.006120 | 0.011604 |
|  6.000000 |       5.700000 |         -5.192351 |         -6.166590 |         -4.848752 |   0.490077 |      0.000000 | 0.746726 | 0.072151 | -0.007635 | 0.014828 |
|  2.500000 |       9.150000 |         -9.611759 |        -10.033740 |         -9.946857 |   0.070790 |      0.000000 | 0.982540 | 0.009726 | -0.001401 | 0.001999 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$20**

Market price: **$0.60**

Expected profit (USD): **11.72** [lowest: 9.60, highest: 13.56]

Delta: 0.0929 (price sensitivity)

Gamma: 0.0375 (delta sensitivity)

Theta: $-0.0038 (negative decay per trading-day)

Vega: $0.0077 (volatility sensitivity per 1%)

ITM (In The Money) probability: **97.51%**

Profit probability: **98.18%**

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
| 8.000000 |       1.650000 |          0.703579 |         -1.216211 |          2.188047 |   0.700939 |      0.678023 | 0.640862 | 0.060647 | -0.006482 | 0.023884 |
| 4.000000 |       4.150000 |         -4.048766 |         -4.798025 |         -3.651072 |   0.383585 |      0.000000 | 0.881783 | 0.032114 | -0.003661 | 0.012647 |
| 3.000000 |       4.900000 |         -5.122780 |         -5.644777 |         -5.023729 |   0.261824 |      0.000000 | 0.936445 | 0.020215 | -0.002431 | 0.007961 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$1.65**

Expected profit (USD): **0.70** [lowest: -1.22, highest: 2.19]

Delta: 0.6409 (price sensitivity)

Gamma: 0.0606 (delta sensitivity)

Theta: $-0.0065 (negative decay per trading-day)

Vega: $0.0239 (volatility sensitivity per 1%)

ITM (In The Money) probability: **70.09%**

Profit probability: **67.80%**

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

