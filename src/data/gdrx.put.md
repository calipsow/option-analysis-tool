# Put Option. GDRX Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

## Current Stock Price: $2.75

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.3322 [-0.7347, 0.4026]**

- Stock Volatility: **0.6653 [0.5768, 0.7608]**

- Based on **1325** observations


- Garch Volatility forecast: **0.5466**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       0.350000 |         -0.822156 |         -0.825947 |         -0.777339 |   0.212056 |      0.000000 | 0.853769 | 0.860395 | -0.003464 | 0.001256 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$2**

Market price: **$0.35**

Expected profit (USD): **-0.82** [lowest: -0.83, highest: -0.78]

Delta: 0.8538 (price sensitivity)

Gamma: 0.8604 (delta sensitivity)

Theta: $-0.0035 (negative decay per trading-day)

Vega: $0.0013 (volatility sensitivity per 1%)

ITM (In The Money) probability: **21.21%**

Profit probability: **0.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $0.35 | $0.30 | 1.06 | 0.6653 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1326** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1646**

- Modal profit prediction correlation: **-0.2251**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.3322 [-0.7347, 0.4026]**

- Stock Volatility: **0.6653 [0.5768, 0.7608]**

- Based on **1325** observations


- Garch Volatility forecast: **0.5466**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       0.500000 |         -0.796132 |         -0.902012 |         -0.667515 |   0.489741 |      0.025065 | 0.708653 | 0.511659 | -0.002860 | 0.003987 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$2**

Market price: **$0.50**

Expected profit (USD): **-0.80** [lowest: -0.90, highest: -0.67]

Delta: 0.7087 (price sensitivity)

Gamma: 0.5117 (delta sensitivity)

Theta: $-0.0029 (negative decay per trading-day)

Vega: $0.0040 (volatility sensitivity per 1%)

ITM (In The Money) probability: **48.97%**

Profit probability: **2.51%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $0.50 | $0.45 | 0.97 | 0.6653 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1326** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1646**

- Modal profit prediction correlation: **-0.2251**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.3322 [-0.7347, 0.4026]**

- Stock Volatility: **0.6653 [0.5768, 0.7608]**

- Based on **1325** observations


- Garch Volatility forecast: **0.5466**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.500000 |       0.060000 |          4.533799 |          3.716921 |          4.890583 |   0.998926 |      0.999022 | 0.011125 | 0.026866 | -0.000163 | 0.000509 |
| 5.000000 |       0.150000 |          1.959966 |          1.215527 |          2.311904 |   0.979552 |      0.972372 | 0.103517 | 0.165330 | -0.001017 | 0.003133 |
| 2.500000 |       0.600000 |         -0.666913 |         -0.947093 |         -0.438507 |   0.615426 |      0.171769 | 0.687694 | 0.325137 | -0.002168 | 0.006162 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$0.06**

Expected profit (USD): **4.53** [lowest: 3.72, highest: 4.89]

Delta: 0.0111 (price sensitivity)

Gamma: 0.0269 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0005 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.89%**

Profit probability: **99.90%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $0.60 | $0.60 | 0.98 | 0.6653 | 0.00 |
| $5 | $0.15 | $0.06 | 1.00 | 0.6653 | 0.09 |
| $8 | $0.06 | $0.01 | 1.22 | 0.6653 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1326** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1646**

- Modal profit prediction correlation: **-0.2251**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.3322 [-0.7347, 0.4026]**

- Stock Volatility: **0.6653 [0.5768, 0.7608]**

- Based on **1325** observations


- Garch Volatility forecast: **0.5466**

### 2. Validate Stock Option Contracts

- Analyze **3** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.500000 |       0.100000 |          4.775047 |          3.284019 |          5.328489 |   0.993842 |      0.996018 | 0.077443 | 0.093199 | -0.000621 | 0.003482 |
| 5.000000 |       0.270000 |          2.147147 |          0.903289 |          2.674086 |   0.962993 |      0.963192 | 0.240078 | 0.199778 | -0.001357 | 0.007464 |
| 2.500000 |       0.800000 |         -0.581817 |         -1.110556 |         -0.227789 |   0.712867 |      0.331006 | 0.698013 | 0.224066 | -0.001643 | 0.008371 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$0.10**

Expected profit (USD): **4.78** [lowest: 3.28, highest: 5.33]

Delta: 0.0774 (price sensitivity)

Gamma: 0.0932 (delta sensitivity)

Theta: $-0.0006 (negative decay per trading-day)

Vega: $0.0035 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.38%**

Profit probability: **99.60%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $0.80 | $0.78 | 0.93 | 0.6653 | 0.02 |
| $5 | $0.27 | $0.18 | 0.93 | 0.6653 | 0.09 |
| $8 | $0.10 | $0.05 | 1.01 | 0.6653 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1326** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1646**

- Modal profit prediction correlation: **-0.2251**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **-0.3322 [-0.7347, 0.4026]**

- Stock Volatility: **0.6653 [0.5768, 0.7608]**

- Based on **1325** observations


- Garch Volatility forecast: **0.5466**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 10.000000 |       0.200000 |          7.634798 |          4.777479 |          8.372295 |   0.995580 |      0.998338 | 0.133808 | 0.097459 | -0.000690 | 0.007230 |
|  7.500000 |       0.300000 |          5.053402 |          2.497595 |          5.765372 |   0.988118 |      0.994277 | 0.226240 | 0.135867 | -0.000973 | 0.010079 |
|  5.000000 |       0.500000 |          2.409599 |          0.439988 |          3.081150 |   0.960573 |      0.970500 | 0.402175 | 0.174724 | -0.001280 | 0.012961 |
|  2.500000 |       1.050000 |         -0.413406 |         -1.335303 |          0.080608 |   0.815013 |      0.540936 | 0.730103 | 0.149296 | -0.001174 | 0.011075 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$10**

Market price: **$0.20**

Expected profit (USD): **7.63** [lowest: 4.78, highest: 8.37]

Delta: 0.1338 (price sensitivity)

Gamma: 0.0975 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0072 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.56%**

Profit probability: **99.83%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.05 | $1.03 | 0.95 | 0.6653 | 0.02 |
| $5 | $0.50 | $0.43 | 0.88 | 0.6653 | 0.07 |
| $8 | $0.30 | $0.21 | 1.09 | 0.6653 | 0.09 |
| $10 | $0.20 | $0.11 | 0.96 | 0.6653 | 0.09 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1326** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1646**

- Modal profit prediction correlation: **-0.2251**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **-0.3322 [-0.7347, 0.4026]**

- Stock Volatility: **0.6653 [0.5768, 0.7608]**

- Based on **1325** observations


- Garch Volatility forecast: **0.5466**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 7.500000 |       0.710000 |          5.307923 |          1.363169 |          5.958898 |   0.989383 |      0.996742 | 0.431864 | 0.124561 | -0.000953 | 0.018588 |
| 5.000000 |       0.940000 |          2.619590 |         -0.285567 |          3.228349 |   0.974442 |      0.986948 | 0.572082 | 0.124340 | -0.000974 | 0.018555 |
| 2.500000 |       1.400000 |         -0.218842 |         -1.689653 |          0.268943 |   0.910931 |      0.749565 | 0.783968 | 0.092841 | -0.000774 | 0.013854 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$8**

Market price: **$0.71**

Expected profit (USD): **5.31** [lowest: 1.36, highest: 5.96]

Delta: 0.4319 (price sensitivity)

Gamma: 0.1246 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0186 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.94%**

Profit probability: **99.67%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.40 | $1.38 | 0.91 | 0.6653 | 0.02 |
| $5 | $0.94 | $0.85 | 0.90 | 0.6653 | 0.09 |
| $8 | $0.71 | $0.58 | 0.89 | 0.6653 | 0.13 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1326** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1646**

- Modal profit prediction correlation: **-0.2251**

- Backtests total: **15**

- Profitable Trades (profitable trades / total trades): **46.67%**

--------------------------------------------------

