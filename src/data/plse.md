# PLSE Option Analysis From: 05.01.2026 03:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $13.390000343322754

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4516 [-0.4778, 0.5509]**

- Stock Volatility: **0.8122 [0.7110, 0.9194]**

- Based on **2414** observations


- Garch Volatility forecast: **0.5125**

### 2. Validate Stock Option Contracts

- Analyze **18** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 10.000000 |       8.200000 |         -5.067625 |         -5.744391 |         -5.190708 |   0.999121 |      0.000308 | 0.998903 | 0.002808 | -0.002217 | 0.000098 |
| 25.000000 |       0.100000 |         -0.600000 |         -0.605169 |         -0.604739 |   0.000000 |      0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$8.20**

Expected profit (USD): **-5.07** [lowest: -5.74, highest: -5.19]

Delta: 0.9989 (price sensitivity)

Gamma: 0.0028 (delta sensitivity)

Theta: $-0.0022 (negative decay per trading-day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.91%**

Profit probability: **0.03%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $10 | $8.20 | $3.44 | 8.13 | 0.8122 | 4.76 |
| $25 | $0.10 | $0.00 | 2.11 | 0.8122 | 0.10 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2415** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.3075**

- Modal profit prediction correlation: **-0.0971**

- Backtests total: **31**

- Profitable Trades (profitable trades / total trades): **51.61%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4516 [-0.4778, 0.5509]**

- Stock Volatility: **0.8122 [0.7110, 0.9194]**

- Based on **2414** observations


- Garch Volatility forecast: **0.5125**

### 2. Validate Stock Option Contracts

- Analyze **14** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 11.000000 |       6.140000 |         -1.278672 |         -4.732828 |         -0.173031 |   0.821945 |      0.203180 | 0.788358 | 0.062709 | -0.008063 | 0.024543 |
| 14.000000 |       4.340000 |         -1.602960 |         -3.833522 |         -0.128092 |   0.588381 |      0.153582 | 0.540352 | 0.085966 | -0.010171 | 0.033645 |
| 18.000000 |       1.250000 |         -0.269687 |         -1.329711 |          1.353052 |   0.306611 |      0.123433 | 0.265151 | 0.070965 | -0.008068 | 0.027774 |
| 20.000000 |       0.800000 |         -0.329976 |         -0.967022 |          1.294660 |   0.208669 |      0.084238 | 0.175381 | 0.055910 | -0.006291 | 0.021882 |
| 19.000000 |       2.120000 |         -1.419300 |         -2.311851 |          0.153321 |   0.253894 |      0.077751 | 0.216418 | 0.063528 | -0.007182 | 0.024863 |
| 22.000000 |       0.480000 |         -0.352884 |         -0.757852 |          1.139397 |   0.138416 |      0.055100 | 0.113230 | 0.041580 | -0.004645 | 0.016273 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$11**

Market price: **$6.14**

Expected profit (USD): **-1.28** [lowest: -4.73, highest: -0.17]

Delta: 0.7884 (price sensitivity)

Gamma: 0.0627 (delta sensitivity)

Theta: $-0.0081 (negative decay per trading-day)

Vega: $0.0245 (volatility sensitivity per 1%)

ITM (In The Money) probability: **82.19%**

Profit probability: **20.32%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $11 | $6.14 | $3.97 | 2.69 | 0.8122 | 2.17 |
| $14 | $4.34 | $2.59 | 2.88 | 0.8122 | 1.75 |
| $18 | $1.25 | $1.45 | 1.39 | 0.8122 | -0.20 |
| $19 | $2.12 | $1.26 | 1.47 | 0.8122 | 0.86 |
| $20 | $0.80 | $1.09 | 0.72 | 0.8122 | -0.29 |
| $22 | $0.48 | $0.82 | 0.85 | 0.8122 | -0.34 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2415** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.3075**

- Modal profit prediction correlation: **-0.0971**

- Backtests total: **31**

- Profitable Trades (profitable trades / total trades): **51.61%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.4516 [-0.4778, 0.5509]**

- Stock Volatility: **0.8122 [0.7110, 0.9194]**

- Based on **2414** observations


- Garch Volatility forecast: **0.5125**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 14.000000 |       3.500000 |          2.156822 |         -2.947485 |          4.744549 |   0.646868 |      0.254123 | 0.590442 | 0.059966 | -0.007627 | 0.045424 |
| 17.000000 |       2.500000 |          1.455891 |         -2.352864 |          4.270634 |   0.490328 |      0.189634 | 0.431545 | 0.060646 | -0.007464 | 0.045939 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$14**

Market price: **$3.50**

Expected profit (USD): **2.16** [lowest: -2.95, highest: 4.74]

Delta: 0.5904 (price sensitivity)

Gamma: 0.0600 (delta sensitivity)

Theta: $-0.0076 (negative decay per trading-day)

Vega: $0.0454 (volatility sensitivity per 1%)

ITM (In The Money) probability: **64.69%**

Profit probability: **25.41%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $14 | $3.50 | $3.68 | 0.89 | 0.8122 | -0.18 |
| $17 | $2.50 | $2.79 | 0.96 | 0.8122 | -0.29 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **2415** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.3075**

- Modal profit prediction correlation: **-0.0971**

- Backtests total: **31**

- Profitable Trades (profitable trades / total trades): **51.61%**

--------------------------------------------------

