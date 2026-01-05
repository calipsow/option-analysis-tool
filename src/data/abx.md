# ABX Option Analysis From: 05.01.2026 01:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $7.920000076293945

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0321 [-0.3423, 0.3205]**

- Stock Volatility: **0.3698 [0.3200, 0.4237]**

- Based on **1205** observations


- Garch Volatility forecast: **0.5917**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       4.300000 |          0.630089 |          0.396759 |          0.604999 |   1.000000 |      0.733604 | 1.000000 | 0.000000 | -0.000495 | 0.000000 |
|  5.000000 |       2.000000 |          0.430096 |          0.246075 |          0.454315 |   0.999946 |      0.652991 | 0.999968 | 0.000147 | -0.000996 | 0.000002 |
|  7.500000 |       0.630000 |         -0.514053 |         -0.757097 |         -0.565919 |   0.661488 |      0.211106 | 0.705378 | 0.371044 | -0.017009 | 0.005440 |
| 10.000000 |       0.360000 |         -0.850564 |         -0.868076 |         -0.867178 |   0.020920 |      0.002878 | 0.027957 | 0.069045 | -0.003024 | 0.001012 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$4.30**

Expected profit (USD): **0.63** [lowest: 0.40, highest: 0.60]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **73.36%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $4.30 | $5.42 | 4.98 | 0.3698 | -1.12 |
| $5 | $2.00 | $2.93 | 3.03 | 0.3698 | -0.93 |
| $8 | $0.63 | $0.51 | 1.34 | 0.3698 | 0.12 |
| $10 | $0.36 | $0.00 | 1.00 | 0.3698 | 0.36 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1206** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1868**

- Modal profit prediction correlation: **-0.7637**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **64.29%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0321 [-0.3423, 0.3205]**

- Stock Volatility: **0.3698 [0.3200, 0.4237]**

- Based on **1205** observations


- Garch Volatility forecast: **0.5917**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       5.230000 |         -0.264500 |         -0.926950 |          0.009235 |   0.999997 |      0.380428 | 0.999999 | 0.000002 | -0.000492 | 0.000000 |
|  5.000000 |       3.400000 |         -0.915126 |         -1.558799 |         -0.623048 |   0.958417 |      0.268745 | 0.977034 | 0.027415 | -0.002144 | 0.001821 |
|  7.500000 |       1.000000 |         -0.474021 |         -1.133048 |         -0.443345 |   0.545747 |      0.254245 | 0.647410 | 0.187086 | -0.009004 | 0.012430 |
| 10.000000 |       0.500000 |         -0.779480 |         -1.006002 |         -0.894178 |   0.150839 |      0.071897 | 0.220820 | 0.149475 | -0.006847 | 0.009931 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$5.23**

Expected profit (USD): **-0.26** [lowest: -0.93, highest: 0.01]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **38.04%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $5.23 | $5.44 | 2.52 | 0.3698 | -0.21 |
| $5 | $3.40 | $2.96 | 1.40 | 0.3698 | 0.44 |
| $8 | $1.00 | $0.76 | 0.96 | 0.3698 | 0.24 |
| $10 | $0.50 | $0.05 | 0.69 | 0.3698 | 0.45 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1206** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1868**

- Modal profit prediction correlation: **-0.7637**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **64.29%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0321 [-0.3423, 0.3205]**

- Stock Volatility: **0.3698 [0.3200, 0.4237]**

- Based on **1205** observations


- Garch Volatility forecast: **0.5917**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  5.000000 |       3.340000 |         -0.611953 |         -2.199345 |          0.413024 |   0.816903 |      0.303463 | 0.911757 | 0.047372 | -0.002891 | 0.009068 |
|  7.500000 |       1.560000 |         -0.453502 |         -1.769368 |          0.031755 |   0.481253 |      0.242574 | 0.655797 | 0.108974 | -0.005530 | 0.020860 |
| 10.000000 |       0.600000 |         -0.361335 |         -1.079618 |         -0.315560 |   0.235303 |      0.147268 | 0.392248 | 0.113764 | -0.005500 | 0.021777 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$3.34**

Expected profit (USD): **-0.61** [lowest: -2.20, highest: 0.41]

Delta: 0.9118 (price sensitivity)

Gamma: 0.0474 (delta sensitivity)

Theta: $-0.0029 (negative decay per trading-day)

Vega: $0.0091 (volatility sensitivity per 1%)

ITM (In The Money) probability: **81.69%**

Profit probability: **30.35%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $3.34 | $3.07 | 1.19 | 0.3698 | 0.27 |
| $8 | $1.56 | $1.14 | 0.69 | 0.3698 | 0.42 |
| $10 | $0.60 | $0.29 | 0.65 | 0.3698 | 0.31 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1206** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1868**

- Modal profit prediction correlation: **-0.7637**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **64.29%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.0321 [-0.3423, 0.3205]**

- Stock Volatility: **0.3698 [0.3200, 0.4237]**

- Based on **1205** observations


- Garch Volatility forecast: **0.5917**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 5.000000 |       3.900000 |         -0.868258 |         -3.356442 |          1.064678 |   0.718833 |      0.260001 | 0.879906 | 0.044598 | -0.002669 | 0.015045 |
| 7.500000 |       2.400000 |         -0.809758 |         -2.744525 |          0.404990 |   0.445843 |      0.205609 | 0.676871 | 0.080007 | -0.004200 | 0.026990 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$5**

Market price: **$3.90**

Expected profit (USD): **-0.87** [lowest: -3.36, highest: 1.06]

Delta: 0.8799 (price sensitivity)

Gamma: 0.0446 (delta sensitivity)

Theta: $-0.0027 (negative decay per trading-day)

Vega: $0.0150 (volatility sensitivity per 1%)

ITM (In The Money) probability: **71.88%**

Profit probability: **26.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $5 | $3.90 | $3.21 | 0.69 | 0.3698 | 0.69 |
| $8 | $2.40 | $1.47 | 0.63 | 0.3698 | 0.93 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1206** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1868**

- Modal profit prediction correlation: **-0.7637**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **64.29%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.0321 [-0.3423, 0.3205]**

- Stock Volatility: **0.3698 [0.3200, 0.4237]**

- Based on **1205** observations


- Garch Volatility forecast: **0.5917**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.500000 |       5.720000 |         -0.348567 |         -4.039614 |          3.903048 |   0.900703 |      0.284293 | 0.979819 | 0.008463 | -0.000794 | 0.004708 |
|  5.000000 |       3.900000 |         -0.445091 |         -3.838799 |          3.260076 |   0.630557 |      0.250380 | 0.863850 | 0.037881 | -0.002277 | 0.021071 |
|  7.500000 |       2.450000 |         -0.280485 |         -2.835182 |          2.575053 |   0.411497 |      0.206460 | 0.705662 | 0.059787 | -0.003245 | 0.033256 |
| 10.000000 |       1.500000 |         -0.166290 |         -1.994885 |          1.793185 |   0.267988 |      0.156543 | 0.557858 | 0.068471 | -0.003558 | 0.038087 |
| 15.000000 |       0.500000 |         -0.080458 |         -1.078238 |          0.618883 |   0.119811 |      0.080162 | 0.340360 | 0.063583 | -0.003177 | 0.035367 |
| 20.000000 |       0.300000 |         -0.303992 |         -0.812558 |         -0.066136 |   0.058074 |      0.038831 | 0.209921 | 0.049980 | -0.002451 | 0.027801 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$5.72**

Expected profit (USD): **-0.35** [lowest: -4.04, highest: 3.90]

Delta: 0.9798 (price sensitivity)

Gamma: 0.0085 (delta sensitivity)

Theta: $-0.0008 (negative decay per trading-day)

Vega: $0.0047 (volatility sensitivity per 1%)

ITM (In The Money) probability: **90.07%**

Profit probability: **28.43%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $5.72 | $5.60 | 1.02 | 0.3698 | 0.12 |
| $5 | $3.90 | $3.43 | 1.33 | 0.3698 | 0.47 |
| $8 | $2.45 | $1.86 | 0.72 | 0.3698 | 0.59 |
| $10 | $1.50 | $0.94 | 0.68 | 0.3698 | 0.56 |
| $15 | $0.50 | $0.23 | 1.11 | 0.3698 | 0.27 |
| $20 | $0.30 | $0.06 | 0.67 | 0.3698 | 0.24 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1206** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1868**

- Modal profit prediction correlation: **-0.7637**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **64.29%**

--------------------------------------------------

