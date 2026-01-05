# GROY Option Analysis From: 05.01.2026 02:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $4.079999923706055

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 0.500000 |       3.000000 |          0.110367 |         -0.062292 |          0.098808 |   1.000000 |      0.569702 | 1.000000 | 0.000000 | -0.000099 | 0.000000 |
| 1.000000 |       3.000000 |         -0.389633 |         -0.565666 |         -0.404566 |   1.000000 |      0.142346 | 1.000000 | 0.000000 | -0.000198 | 0.000000 |
| 2.000000 |       2.000000 |         -0.389633 |         -0.536146 |         -0.375046 |   1.000000 |      0.142346 | 1.000000 | 0.000000 | -0.000396 | 0.000000 |
| 2.500000 |       1.510000 |         -0.399633 |         -0.539567 |         -0.378465 |   1.000000 |      0.137128 | 1.000000 | 0.000001 | -0.000495 | 0.000000 |
| 3.500000 |       0.600000 |         -0.483075 |         -0.597156 |         -0.437401 |   0.950784 |      0.096416 | 0.954452 | 0.248064 | -0.002501 | 0.000778 |
| 1.500000 |       2.650000 |         -0.539633 |         -0.703014 |         -0.541914 |   1.000000 |      0.078305 | 1.000000 | 0.000000 | -0.000297 | 0.000000 |
| 4.000000 |       0.200000 |         -0.485594 |         -0.541645 |         -0.416855 |   0.595037 |      0.063051 | 0.609364 | 0.994842 | -0.007859 | 0.003120 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$0**

Market price: **$3.00**

Expected profit (USD): **0.11** [lowest: -0.06, highest: 0.10]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0001 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **56.97%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.00 | $3.58 | 6.38 | 0.5562 | -0.58 |
| $1 | $3.00 | $3.08 | 4.25 | 0.5562 | -0.08 |
| $2 | $2.65 | $2.58 | 5.30 | 0.5562 | 0.07 |
| $2 | $2.00 | $2.08 | 3.03 | 0.5562 | -0.08 |
| $2 | $1.51 | $1.58 | 2.23 | 0.5562 | -0.07 |
| $4 | $0.60 | $0.60 | 1.22 | 0.5562 | -0.00 |
| $4 | $0.20 | $0.23 | 0.54 | 0.5562 | -0.03 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       1.120000 |         -0.382692 |         -0.852604 |         -0.159572 |   0.928857 |      0.255867 | 0.941875 | 0.131635 | -0.001678 | 0.002003 |
| 2.500000 |       1.750000 |         -0.529757 |         -1.041014 |         -0.318915 |   0.989558 |      0.216400 | 0.992099 | 0.024563 | -0.000697 | 0.000374 |
| 4.000000 |       0.450000 |         -0.476212 |         -0.741855 |         -0.257547 |   0.554721 |      0.164769 | 0.595213 | 0.439028 | -0.004202 | 0.006681 |
| 4.500000 |       0.250000 |         -0.498719 |         -0.658881 |         -0.315988 |   0.342069 |      0.106195 | 0.380775 | 0.431626 | -0.004004 | 0.006569 |
| 5.000000 |       0.100000 |         -0.477932 |         -0.564327 |         -0.342962 |   0.185708 |      0.061133 | 0.214633 | 0.330695 | -0.003017 | 0.005033 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$1.12**

Expected profit (USD): **-0.38** [lowest: -0.85, highest: -0.16]

Delta: 0.9419 (price sensitivity)

Gamma: 0.1316 (delta sensitivity)

Theta: $-0.0017 (negative decay per trading-day)

Vega: $0.0020 (volatility sensitivity per 1%)

ITM (In The Money) probability: **92.89%**

Profit probability: **25.59%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $1.75 | $1.61 | 1.52 | 0.5562 | 0.14 |
| $3 | $1.12 | $1.14 | 0.56 | 0.5562 | -0.02 |
| $4 | $0.45 | $0.44 | 0.66 | 0.5562 | 0.01 |
| $4 | $0.25 | $0.24 | 0.65 | 0.5562 | 0.01 |
| $5 | $0.10 | $0.12 | 0.63 | 0.5562 | -0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **10** strikes prices..

Total of valuable options: 9

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       1.660000 |         -0.241076 |         -1.247928 |          0.322581 |   0.933745 |      0.300019 | 0.953452 | 0.070726 | -0.001107 | 0.002516 |
| 1.000000 |       3.300000 |         -0.402694 |         -1.523110 |          0.120393 |   0.999988 |      0.270254 | 0.999994 | 0.000019 | -0.000195 | 0.000001 |
| 3.500000 |       0.850000 |         -0.257309 |         -1.007048 |          0.270796 |   0.694067 |      0.260195 | 0.752513 | 0.229516 | -0.002587 | 0.008164 |
| 3.000000 |       1.400000 |         -0.424636 |         -1.328874 |          0.122721 |   0.832505 |      0.250431 | 0.872674 | 0.151415 | -0.001882 | 0.005386 |
| 4.000000 |       0.580000 |         -0.296877 |         -0.877972 |          0.197744 |   0.544508 |      0.217691 | 0.612869 | 0.278020 | -0.002983 | 0.009889 |
| 4.500000 |       0.500000 |         -0.453766 |         -0.895650 |         -0.022700 |   0.406266 |      0.154966 | 0.475221 | 0.289134 | -0.003016 | 0.010285 |
| 5.000000 |       0.200000 |         -0.327091 |         -0.637373 |          0.051279 |   0.291396 |      0.131104 | 0.354090 | 0.270094 | -0.002767 | 0.009607 |
| 6.000000 |       0.160000 |         -0.493858 |         -0.643047 |         -0.238251 |   0.137972 |      0.056786 | 0.180236 | 0.190699 | -0.001913 | 0.006783 |
| 7.500000 |       0.100000 |         -0.553471 |         -0.599814 |         -0.430230 |   0.040009 |      0.015299 | 0.057562 | 0.083730 | -0.000827 | 0.002978 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$1.66**

Expected profit (USD): **-0.24** [lowest: -1.25, highest: 0.32]

Delta: 0.9535 (price sensitivity)

Gamma: 0.0707 (delta sensitivity)

Theta: $-0.0011 (negative decay per trading-day)

Vega: $0.0025 (volatility sensitivity per 1%)

ITM (In The Money) probability: **93.37%**

Profit probability: **30.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $3.30 | $3.10 | 1.45 | 0.5562 | 0.20 |
| $2 | $1.66 | $1.67 | 0.76 | 0.5562 | -0.01 |
| $3 | $1.40 | $1.25 | 0.79 | 0.5562 | 0.15 |
| $4 | $0.85 | $0.91 | 0.60 | 0.5562 | -0.06 |
| $4 | $0.58 | $0.64 | 0.54 | 0.5562 | -0.06 |
| $4 | $0.50 | $0.44 | 0.94 | 0.5562 | 0.06 |
| $5 | $0.20 | $0.30 | 0.69 | 0.5562 | -0.10 |
| $6 | $0.16 | $0.13 | 0.71 | 0.5562 | 0.03 |
| $8 | $0.10 | $0.04 | 0.85 | 0.5562 | 0.06 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.000000 |       2.250000 |         -0.025527 |         -1.861809 |          1.206836 |   0.941260 |      0.306424 | 0.965631 | 0.039324 | -0.000732 | 0.002711 |
| 1.000000 |       3.300000 |         -0.095579 |         -2.063232 |          1.123714 |   0.998762 |      0.298722 | 0.999483 | 0.000947 | -0.000200 | 0.000065 |
| 3.000000 |       1.350000 |          0.015198 |         -1.463610 |          1.212407 |   0.761421 |      0.291187 | 0.832872 | 0.129295 | -0.001656 | 0.008914 |
| 2.500000 |       1.850000 |         -0.077941 |         -1.759814 |          1.142807 |   0.863272 |      0.291187 | 0.911466 | 0.082867 | -0.001195 | 0.005713 |
| 3.500000 |       1.050000 |         -0.037827 |         -1.300228 |          1.114908 |   0.650250 |      0.262686 | 0.739139 | 0.167842 | -0.002016 | 0.011571 |
| 4.000000 |       0.850000 |         -0.135506 |         -1.197980 |          0.946289 |   0.541640 |      0.224611 | 0.640301 | 0.193201 | -0.002232 | 0.013320 |
| 4.500000 |       0.720000 |         -0.251131 |         -1.118322 |          0.762556 |   0.442879 |      0.184685 | 0.544201 | 0.204814 | -0.002307 | 0.014120 |
| 5.000000 |       0.650000 |         -0.380594 |         -1.089650 |          0.545898 |   0.357283 |      0.146763 | 0.455795 | 0.204814 | -0.002265 | 0.014120 |
| 5.500000 |       0.330000 |         -0.220723 |         -0.798476 |          0.615090 |   0.285491 |      0.133237 | 0.377556 | 0.196296 | -0.002142 | 0.013533 |
| 7.000000 |       0.250000 |         -0.448971 |         -0.750981 |          0.144099 |   0.141215 |      0.062051 | 0.206057 | 0.147219 | -0.001567 | 0.010150 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.25**

Expected profit (USD): **-0.03** [lowest: -1.86, highest: 1.21]

Delta: 0.9656 (price sensitivity)

Gamma: 0.0393 (delta sensitivity)

Theta: $-0.0007 (negative decay per trading-day)

Vega: $0.0027 (volatility sensitivity per 1%)

ITM (In The Money) probability: **94.13%**

Profit probability: **30.64%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $3.30 | $3.12 | 1.06 | 0.5562 | 0.18 |
| $2 | $2.25 | $2.19 | 0.67 | 0.5562 | 0.06 |
| $2 | $1.85 | $1.78 | 0.70 | 0.5562 | 0.07 |
| $3 | $1.35 | $1.42 | 0.82 | 0.5562 | -0.07 |
| $4 | $1.05 | $1.12 | 0.62 | 0.5562 | -0.07 |
| $4 | $0.85 | $0.88 | 0.81 | 0.5562 | -0.03 |
| $4 | $0.72 | $0.69 | 0.73 | 0.5562 | 0.03 |
| $5 | $0.65 | $0.53 | 0.68 | 0.5562 | 0.12 |
| $6 | $0.33 | $0.41 | 0.76 | 0.5562 | -0.08 |
| $7 | $0.25 | $0.20 | 0.88 | 0.5562 | 0.05 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 1.000000 |       2.850000 |          1.036826 |         -2.384253 |          4.236968 |   0.985407 |      0.359805 | 0.994562 | 0.005707 | -0.000236 | 0.000775 |
| 2.000000 |       2.150000 |          0.798718 |         -2.233280 |          3.975615 |   0.873934 |      0.323247 | 0.934588 | 0.046667 | -0.000760 | 0.006333 |
| 1.500000 |       2.730000 |          0.673625 |         -2.593560 |          3.867846 |   0.942380 |      0.314148 | 0.973855 | 0.022223 | -0.000470 | 0.003016 |
| 2.500000 |       2.050000 |          0.482004 |         -2.283438 |          3.614229 |   0.791530 |      0.280300 | 0.880484 | 0.073057 | -0.001048 | 0.009915 |
| 3.000000 |       1.700000 |          0.457828 |         -2.024681 |          3.532697 |   0.705159 |      0.265760 | 0.817259 | 0.097018 | -0.001295 | 0.013166 |
| 3.500000 |       1.400000 |          0.426406 |         -1.786127 |          3.422505 |   0.621320 |      0.247593 | 0.750041 | 0.116376 | -0.001484 | 0.015794 |
| 4.000000 |       1.150000 |          0.385484 |         -1.574828 |          3.289652 |   0.543562 |      0.226714 | 0.682635 | 0.130521 | -0.001613 | 0.017713 |
| 4.500000 |       1.000000 |          0.281563 |         -1.442691 |          3.090009 |   0.473453 |      0.200587 | 0.617559 | 0.139723 | -0.001687 | 0.018962 |
| 5.000000 |       0.900000 |          0.160691 |         -1.367951 |          2.849661 |   0.411365 |      0.174645 | 0.556316 | 0.144655 | -0.001717 | 0.019631 |
| 5.500000 |       0.850000 |          0.018907 |         -1.341537 |          2.579795 |   0.357012 |      0.149750 | 0.499686 | 0.146114 | -0.001711 | 0.019829 |
| 7.000000 |       0.650000 |         -0.217361 |         -1.162190 |          1.986544 |   0.233666 |      0.097286 | 0.358991 | 0.136888 | -0.001560 | 0.018577 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$2.85**

Expected profit (USD): **1.04** [lowest: -2.38, highest: 4.24]

Delta: 0.9946 (price sensitivity)

Gamma: 0.0057 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0008 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.54%**

Profit probability: **35.98%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $2.85 | $3.16 | 1.93 | 0.5562 | -0.31 |
| $2 | $2.73 | $2.72 | 0.73 | 0.5562 | 0.01 |
| $2 | $2.15 | $2.33 | 0.98 | 0.5562 | -0.18 |
| $2 | $2.05 | $1.99 | 0.90 | 0.5562 | 0.06 |
| $3 | $1.70 | $1.69 | 0.75 | 0.5562 | 0.01 |
| $4 | $1.40 | $1.44 | 0.74 | 0.5562 | -0.04 |
| $4 | $1.15 | $1.23 | 0.84 | 0.5562 | -0.08 |
| $4 | $1.00 | $1.05 | 0.67 | 0.5562 | -0.05 |
| $5 | $0.90 | $0.90 | 0.76 | 0.5562 | 0.00 |
| $6 | $0.85 | $0.77 | 0.83 | 0.5562 | 0.08 |
| $7 | $0.65 | $0.49 | 0.75 | 0.5562 | 0.16 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.1869 [-0.4876, 0.5069]**

- Stock Volatility: **0.5562 [0.4814, 0.6372]**

- Based on **1211** observations


- Garch Volatility forecast: **0.4991**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 0.500000 |       3.500000 |          2.590239 |         -3.543343 |         13.677425 |   0.989761 |      0.316394 | 0.997752 | 0.001820 | -0.000101 | 0.000495 |
| 1.000000 |       3.190000 |          2.415557 |         -3.452320 |         13.496569 |   0.943808 |      0.301060 | 0.982620 | 0.011089 | -0.000262 | 0.003014 |
| 1.500000 |       2.800000 |          2.349844 |         -3.172693 |         13.404667 |   0.877098 |      0.292613 | 0.953925 | 0.024933 | -0.000449 | 0.006777 |
| 2.000000 |       2.400000 |          2.329403 |         -2.831826 |         13.333803 |   0.804462 |      0.285194 | 0.916396 | 0.039666 | -0.000628 | 0.010781 |
| 3.000000 |       2.160000 |          1.835368 |         -2.652521 |         12.662974 |   0.666658 |      0.235974 | 0.830026 | 0.065305 | -0.000916 | 0.017750 |
| 3.500000 |       1.750000 |          1.927502 |         -2.239767 |         12.656994 |   0.605796 |      0.230888 | 0.785803 | 0.075249 | -0.001020 | 0.020453 |
| 4.500000 |       1.420000 |          1.705732 |         -1.933239 |         12.157753 |   0.501491 |      0.197110 | 0.701008 | 0.089601 | -0.001162 | 0.024354 |
| 4.000000 |       2.000000 |          1.388587 |         -2.519489 |         11.968490 |   0.550833 |      0.193511 | 0.742584 | 0.083285 | -0.001101 | 0.022637 |
| 5.000000 |       1.400000 |          1.486236 |         -1.922751 |         11.783943 |   0.457311 |      0.176726 | 0.661425 | 0.094416 | -0.001205 | 0.025663 |
| 5.500000 |       1.270000 |          1.397645 |         -1.794858 |         11.540571 |   0.417781 |      0.162824 | 0.623995 | 0.097950 | -0.001235 | 0.026624 |
| 7.000000 |       1.000000 |          1.116544 |         -1.513829 |         10.785197 |   0.322212 |      0.125584 | 0.524735 | 0.102767 | -0.001260 | 0.027933 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$0**

Market price: **$3.50**

Expected profit (USD): **2.59** [lowest: -3.54, highest: 13.68]

Delta: 0.9978 (price sensitivity)

Gamma: 0.0018 (delta sensitivity)

Theta: $-0.0001 (negative decay per trading-day)

Vega: $0.0005 (volatility sensitivity per 1%)

ITM (In The Money) probability: **98.98%**

Profit probability: **31.64%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $3.50 | $3.65 | 1.27 | 0.5562 | -0.15 |
| $1 | $3.19 | $3.25 | 1.02 | 0.5562 | -0.06 |
| $2 | $2.80 | $2.90 | 0.86 | 0.5562 | -0.10 |
| $2 | $2.40 | $2.59 | 0.74 | 0.5562 | -0.19 |
| $3 | $2.16 | $2.09 | 0.83 | 0.5562 | 0.07 |
| $4 | $1.75 | $1.89 | 0.75 | 0.5562 | -0.14 |
| $4 | $2.00 | $1.72 | 0.73 | 0.5562 | 0.28 |
| $4 | $1.42 | $1.56 | 0.68 | 0.5562 | -0.14 |
| $5 | $1.40 | $1.43 | 0.65 | 0.5562 | -0.03 |
| $6 | $1.27 | $1.31 | 0.66 | 0.5562 | -0.04 |
| $7 | $1.00 | $1.02 | 0.72 | 0.5562 | -0.02 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1212** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.1233**

- Modal profit prediction correlation: **0.5624**

- Backtests total: **14**

- Profitable Trades (profitable trades / total trades): **71.43%**

--------------------------------------------------

