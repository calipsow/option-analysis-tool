# Put Option. RC Option Analysis From: 05.01.2026 04:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Sold NOT Bought on Expiration**

## Current Stock Price: $2.140000104904175

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0037 [-0.2012, 0.1652]**

- Stock Volatility: **0.3353 [0.2946, 0.3781]**

- Based on **3244** observations


- Garch Volatility forecast: **0.4610**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 1.000000 |       1.290000 |         -1.790000 |         -1.822526 |         -1.822526 |   0.000000 |      0.000000 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$1**

Market price: **$1.29**

Expected profit (USD): **-1.79** [lowest: -1.82, highest: -1.82]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **0.00%**

Profit probability: **0.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $1.29 | $1.14 | 4.13 | 0.3353 | 0.15 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3245** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0829**

- Modal profit prediction correlation: **-0.1393**

- Backtests total: **43**

- Profitable Trades (profitable trades / total trades): **55.81%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0037 [-0.2012, 0.1652]**

- Stock Volatility: **0.3353 [0.2946, 0.3781]**

- Based on **3244** observations


- Garch Volatility forecast: **0.4610**

### 2. Validate Stock Option Contracts

- Analyze **4** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.000000 |       0.500000 |         -0.895359 |         -0.979097 |         -0.922009 |   0.407081 |      0.000131 | 0.685446 | 0.829628 | -0.001929 | 0.003211 |
| 1.500000 |       0.850000 |         -1.344559 |         -1.376833 |         -1.374970 |   0.047094 |      0.000000 | 0.972674 | 0.147125 | -0.000582 | 0.000569 |
| 1.000000 |       1.220000 |         -1.719995 |         -1.753156 |         -1.753155 |   0.000107 |      0.000000 | 0.999961 | 0.000383 | -0.000197 | 0.000001 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$2**

Market price: **$0.50**

Expected profit (USD): **-0.90** [lowest: -0.98, highest: -0.92]

Delta: 0.6854 (price sensitivity)

Gamma: 0.8296 (delta sensitivity)

Theta: $-0.0019 (negative decay per trading-day)

Vega: $0.0032 (volatility sensitivity per 1%)

ITM (In The Money) probability: **40.71%**

Profit probability: **0.01%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $1.22 | $1.15 | 2.09 | 0.3353 | 0.07 |
| $2 | $0.85 | $0.65 | 1.19 | 0.3353 | 0.20 |
| $2 | $0.50 | $0.21 | 0.66 | 0.3353 | 0.29 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3245** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0829**

- Modal profit prediction correlation: **-0.1393**

- Backtests total: **43**

- Profitable Trades (profitable trades / total trades): **55.81%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0037 [-0.2012, 0.1652]**

- Stock Volatility: **0.3353 [0.2946, 0.3781]**

- Based on **3244** observations


- Garch Volatility forecast: **0.4610**

### 2. Validate Stock Option Contracts

- Analyze **8** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       0.080000 |          0.338479 |          0.151249 |          0.451054 |   0.892971 |      0.734593 | 0.194553 | 0.411923 | -0.000981 | 0.003730 |
| 2.000000 |       0.350000 |         -0.656038 |         -0.798252 |         -0.666449 |   0.477787 |      0.039600 | 0.668927 | 0.542528 | -0.001414 | 0.004913 |
| 1.000000 |       1.350000 |         -1.848881 |         -1.886400 |         -1.886240 |   0.011453 |      0.000000 | 0.996049 | 0.017530 | -0.000231 | 0.000159 |
| 0.500000 |       1.710000 |         -2.210000 |         -2.252641 |         -2.252641 |   0.000003 |      0.000000 | 0.999999 | 0.000004 | -0.000097 | 0.000000 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$3**

Market price: **$0.08**

Expected profit (USD): **0.34** [lowest: 0.15, highest: 0.45]

Delta: 0.1946 (price sensitivity)

Gamma: 0.4119 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0037 (volatility sensitivity per 1%)

ITM (In The Money) probability: **89.30%**

Profit probability: **73.46%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $1.71 | $1.65 | 2.53 | 0.3353 | 0.06 |
| $1 | $1.35 | $1.16 | 1.41 | 0.3353 | 0.19 |
| $2 | $0.35 | $0.28 | 0.80 | 0.3353 | 0.07 |
| $3 | $0.08 | $0.02 | 0.65 | 0.3353 | 0.06 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3245** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0829**

- Modal profit prediction correlation: **-0.1393**

- Backtests total: **43**

- Profitable Trades (profitable trades / total trades): **55.81%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0037 [-0.2012, 0.1652]**

- Stock Volatility: **0.3353 [0.2946, 0.3781]**

- Based on **3244** observations


- Garch Volatility forecast: **0.4610**

### 2. Validate Stock Option Contracts

- Analyze **5** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       0.150000 |          0.353568 |          0.009345 |          0.528830 |   0.840148 |      0.704258 | 0.321809 | 0.381312 | -0.000983 | 0.006696 |
| 2.000000 |       0.500000 |         -0.703804 |         -0.927248 |         -0.679643 |   0.528713 |      0.079511 | 0.677380 | 0.381710 | -0.001073 | 0.006703 |
| 1.000000 |       1.240000 |         -1.729174 |         -1.774907 |         -1.770481 |   0.066047 |      0.000000 | 0.979241 | 0.053158 | -0.000303 | 0.000933 |
| 0.500000 |       1.710000 |         -2.209944 |         -2.253250 |         -2.253248 |   0.001022 |      0.000000 | 0.999851 | 0.000614 | -0.000097 | 0.000011 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$3**

Market price: **$0.15**

Expected profit (USD): **0.35** [lowest: 0.01, highest: 0.53]

Delta: 0.3218 (price sensitivity)

Gamma: 0.3813 (delta sensitivity)

Theta: $-0.0010 (negative decay per trading-day)

Vega: $0.0067 (volatility sensitivity per 1%)

ITM (In The Money) probability: **84.01%**

Profit probability: **70.43%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $1.71 | $1.66 | 1.84 | 0.3353 | 0.05 |
| $1 | $1.24 | $1.18 | 1.03 | 0.3353 | 0.06 |
| $2 | $0.50 | $0.36 | 0.71 | 0.3353 | 0.14 |
| $3 | $0.15 | $0.06 | 0.62 | 0.3353 | 0.09 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3245** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0829**

- Modal profit prediction correlation: **-0.1393**

- Backtests total: **43**

- Profitable Trades (profitable trades / total trades): **55.81%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **18.12.2026**

### 1. Black-School Analysis

- Stock Price Drift: **-0.0037 [-0.2012, 0.1652]**

- Stock Volatility: **0.3353 [0.2946, 0.3781]**

- Based on **3244** observations


- Garch Volatility forecast: **0.4610**

### 2. Validate Stock Option Contracts

- Analyze **2** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       0.250000 |          0.378737 |         -0.169055 |          0.650768 |   0.808814 |      0.698506 | 0.438730 | 0.309334 | -0.000852 | 0.009886 |
| 2.000000 |       0.600000 |         -0.678633 |         -1.013952 |         -0.586017 |   0.576400 |      0.154221 | 0.700783 | 0.272497 | -0.000815 | 0.008708 |

### 4. Option Call (Sell): Risk Assessment

Best strike price: **$3**

Market price: **$0.25**

Expected profit (USD): **0.38** [lowest: -0.17, highest: 0.65]

Delta: 0.4387 (price sensitivity)

Gamma: 0.3093 (delta sensitivity)

Theta: $-0.0009 (negative decay per trading-day)

Vega: $0.0099 (volatility sensitivity per 1%)

ITM (In The Money) probability: **80.88%**

Profit probability: **69.85%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $0.60 | $0.47 | 0.63 | 0.3353 | 0.13 |
| $3 | $0.25 | $0.14 | 0.59 | 0.3353 | 0.11 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **3245** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.0829**

- Modal profit prediction correlation: **-0.1393**

- Backtests total: **43**

- Profitable Trades (profitable trades / total trades): **55.81%**

--------------------------------------------------

