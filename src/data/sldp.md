# SLDP Option Analysis From: 05.01.2026 03:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $4.650000095367432

### Calculate Stock Option Nr. 1

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1486 [-0.7713, 0.6738]**

- Stock Volatility: **0.7889 [0.6822, 0.9047]**

- Based on **1154** observations


- Garch Volatility forecast: **0.9834**

### 2. Validate Stock Option Contracts

- Analyze **7** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 2.500000 |       2.050000 |         -0.372448 |         -0.617193 |         -0.351010 |   0.999558 |      0.281993 | 0.999756 | 0.001071 | -0.000534 | 0.000008 |
| 4.000000 |       0.650000 |         -0.386030 |         -0.598185 |         -0.343720 |   0.776883 |      0.247027 | 0.822184 | 0.305414 | -0.011711 | 0.002412 |
| 4.500000 |       0.390000 |         -0.458655 |         -0.639502 |         -0.430740 |   0.547489 |      0.175591 | 0.610773 | 0.449765 | -0.016827 | 0.003552 |
| 5.000000 |       0.150000 |         -0.434767 |         -0.561296 |         -0.423025 |   0.324441 |      0.117173 | 0.384645 | 0.448220 | -0.016604 | 0.003540 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.05**

Expected profit (USD): **-0.37** [lowest: -0.62, highest: -0.35]

Delta: 0.9998 (price sensitivity)

Gamma: 0.0011 (delta sensitivity)

Theta: $-0.0005 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.96%**

Profit probability: **28.20%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $2.05 | $2.15 | 2.88 | 0.7889 | -0.10 |
| $4 | $0.65 | $0.72 | 1.36 | 0.7889 | -0.07 |
| $4 | $0.39 | $0.37 | 0.81 | 0.7889 | 0.02 |
| $5 | $0.15 | $0.16 | 0.84 | 0.7889 | -0.01 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1155** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2261**

- Modal profit prediction correlation: **0.3537**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **46.15%**

--------------------------------------------------

### Calculate Stock Option Nr. 2

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1486 [-0.7713, 0.6738]**

- Stock Volatility: **0.7889 [0.6822, 0.9047]**

- Based on **1154** observations


- Garch Volatility forecast: **0.9834**

### 2. Validate Stock Option Contracts

- Analyze **15** strikes prices..

Total of valuable options: 12

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 1.000000 |       3.300000 |         -0.024929 |         -0.879062 |          0.313768 |   0.999693 |      0.360825 | 0.999932 | 0.000138 | -0.000203 | 0.000005 |
| 2.500000 |       1.880000 |         -0.062857 |         -0.871668 |          0.307094 |   0.901842 |      0.346516 | 0.953577 | 0.048669 | -0.002596 | 0.001910 |
| 4.000000 |       0.650000 |          0.044872 |         -0.662606 |          0.283268 |   0.578354 |      0.301483 | 0.721107 | 0.168246 | -0.007897 | 0.006602 |
| 3.500000 |       1.280000 |         -0.267034 |         -1.047480 |          0.013690 |   0.694491 |      0.281568 | 0.815160 | 0.133598 | -0.006388 | 0.005242 |
| 4.500000 |       0.600000 |         -0.166626 |         -0.802478 |          0.005527 |   0.469478 |      0.237241 | 0.622430 | 0.190295 | -0.008833 | 0.007467 |
| 3.000000 |       2.100000 |         -0.711186 |         -1.548889 |         -0.409321 |   0.807186 |      0.237241 | 0.895446 | 0.090777 | -0.004492 | 0.003562 |
| 2.000000 |       3.100000 |         -0.814654 |         -1.668005 |         -0.477023 |   0.964986 |      0.237241 | 0.986103 | 0.017758 | -0.001165 | 0.000697 |
| 0.500000 |       4.620000 |         -0.844959 |         -1.739199 |         -0.546370 |   1.000000 |      0.234684 | 1.000000 | 0.000000 | -0.000098 | 0.000000 |
| 5.000000 |       0.470000 |         -0.246820 |         -0.788186 |         -0.123118 |   0.373756 |      0.193742 | 0.526522 | 0.199336 | -0.009185 | 0.007822 |
| 5.500000 |       0.350000 |         -0.292935 |         -0.741208 |         -0.210192 |   0.293270 |      0.156756 | 0.438250 | 0.197379 | -0.009048 | 0.007745 |
| 1.500000 |       4.380000 |         -1.603750 |         -2.491738 |         -1.298976 |   0.993461 |      0.154136 | 0.997948 | 0.003250 | -0.000437 | 0.000128 |
| 7.500000 |       0.070000 |         -0.378875 |         -0.558903 |         -0.379930 |   0.102743 |      0.058670 | 0.190074 | 0.135923 | -0.006164 | 0.005334 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$1**

Market price: **$3.30**

Expected profit (USD): **-0.02** [lowest: -0.88, highest: 0.31]

Delta: 0.9999 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0002 (negative decay per trading-day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.97%**

Profit probability: **36.08%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $0 | $4.62 | $4.15 | 7.03 | 0.7889 | 0.47 |
| $1 | $3.30 | $3.66 | 3.69 | 0.7889 | -0.36 |
| $2 | $4.38 | $3.16 | 3.28 | 0.7889 | 1.22 |
| $2 | $3.10 | $2.67 | 2.73 | 0.7889 | 0.43 |
| $2 | $1.88 | $2.18 | 1.45 | 0.7889 | -0.30 |
| $3 | $2.10 | $1.73 | 1.93 | 0.7889 | 0.37 |
| $4 | $1.28 | $1.32 | 1.28 | 0.7889 | -0.04 |
| $4 | $0.65 | $0.98 | 1.01 | 0.7889 | -0.33 |
| $4 | $0.60 | $0.70 | 1.07 | 0.7889 | -0.10 |
| $5 | $0.47 | $0.49 | 0.92 | 0.7889 | -0.02 |
| $6 | $0.35 | $0.34 | 0.92 | 0.7889 | 0.01 |
| $8 | $0.07 | $0.07 | 0.96 | 0.7889 | -0.00 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1155** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2261**

- Modal profit prediction correlation: **0.3537**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **46.15%**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1486 [-0.7713, 0.6738]**

- Stock Volatility: **0.7889 [0.6822, 0.9047]**

- Based on **1154** observations


- Garch Volatility forecast: **0.9834**

### 2. Validate Stock Option Contracts

- Analyze **12** strikes prices..

Total of valuable options: 12

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  3.000000 |       1.750000 |          0.204381 |         -1.627660 |          1.369609 |   0.609343 |      0.257424 | 0.838010 | 0.068158 | -0.003760 | 0.008160 |
|  4.500000 |       1.200000 |          0.005612 |         -1.479956 |          0.846949 |   0.402724 |      0.193186 | 0.678103 | 0.099616 | -0.005329 | 0.011927 |
|  3.500000 |       2.400000 |         -0.730382 |         -2.477970 |          0.305663 |   0.531255 |      0.182140 | 0.784397 | 0.081325 | -0.004424 | 0.009737 |
|  4.000000 |       1.950000 |         -0.528437 |         -2.156341 |          0.399672 |   0.462510 |      0.179494 | 0.730588 | 0.091778 | -0.004945 | 0.010988 |
|  5.000000 |       1.050000 |         -0.032516 |         -1.395579 |          0.709366 |   0.351067 |      0.174335 | 0.627887 | 0.105110 | -0.005593 | 0.012585 |
|  1.500000 |       4.600000 |         -1.531199 |         -3.607034 |         -0.208832 |   0.879650 |      0.171820 | 0.970078 | 0.018866 | -0.001198 | 0.002259 |
|  5.500000 |       0.740000 |          0.113352 |         -1.121560 |          0.773938 |   0.306571 |      0.164998 | 0.580476 | 0.108593 | -0.005753 | 0.013002 |
|  2.500000 |       3.800000 |         -1.519584 |         -3.495721 |         -0.314773 |   0.696090 |      0.162171 | 0.889126 | 0.052548 | -0.002963 | 0.006291 |
|  7.500000 |       0.410000 |         -0.033367 |         -0.884352 |          0.334405 |   0.182375 |      0.103808 | 0.421660 | 0.108712 | -0.005697 | 0.013016 |
| 10.000000 |       0.220000 |         -0.185353 |         -0.718271 |         -0.020583 |   0.100612 |      0.057775 | 0.284553 | 0.094268 | -0.004905 | 0.011287 |
| 12.500000 |       0.170000 |         -0.328891 |         -0.677466 |         -0.269481 |   0.058627 |      0.032907 | 0.195530 | 0.076739 | -0.003976 | 0.009188 |
| 15.000000 |       0.080000 |         -0.354147 |         -0.598596 |         -0.353030 |   0.035774 |      0.019851 | 0.137136 | 0.060984 | -0.003151 | 0.007301 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$1.75**

Expected profit (USD): **0.20** [lowest: -1.63, highest: 1.37]

Delta: 0.8380 (price sensitivity)

Gamma: 0.0682 (delta sensitivity)

Theta: $-0.0038 (negative decay per trading-day)

Vega: $0.0082 (volatility sensitivity per 1%)

ITM (In The Money) probability: **60.93%**

Profit probability: **25.74%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $4.60 | $3.20 | 2.53 | 0.7889 | 1.40 |
| $2 | $3.80 | $2.33 | 1.10 | 0.7889 | 1.47 |
| $3 | $1.75 | $1.96 | 1.12 | 0.7889 | -0.21 |
| $4 | $2.40 | $1.64 | 1.05 | 0.7889 | 0.76 |
| $4 | $1.95 | $1.37 | 0.95 | 0.7889 | 0.58 |
| $4 | $1.20 | $1.14 | 1.00 | 0.7889 | 0.06 |
| $5 | $1.05 | $0.95 | 1.10 | 0.7889 | 0.10 |
| $6 | $0.74 | $0.79 | 1.01 | 0.7889 | -0.05 |
| $8 | $0.41 | $0.39 | 1.08 | 0.7889 | 0.02 |
| $10 | $0.22 | $0.16 | 1.05 | 0.7889 | 0.06 |
| $12 | $0.17 | $0.07 | 1.12 | 0.7889 | 0.10 |
| $15 | $0.08 | $0.04 | 1.51 | 0.7889 | 0.04 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1155** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2261**

- Modal profit prediction correlation: **0.3537**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **46.15%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1486 [-0.7713, 0.6738]**

- Stock Volatility: **0.7889 [0.6822, 0.9047]**

- Based on **1154** observations


- Garch Volatility forecast: **0.9834**

### 2. Validate Stock Option Contracts

- Analyze **6** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|   strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|---------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 3.000000 |       2.150000 |          0.379127 |         -2.327131 |          2.966912 |   0.510114 |      0.197949 | 0.837679 | 0.050563 | -0.002899 | 0.010840 |
| 4.000000 |       1.630000 |          0.446318 |         -1.951262 |          2.764096 |   0.401280 |      0.176956 | 0.761014 | 0.063851 | -0.003598 | 0.013688 |
| 4.500000 |       1.750000 |          0.136675 |         -2.128736 |          2.304902 |   0.358382 |      0.154040 | 0.724686 | 0.068730 | -0.003851 | 0.014734 |
| 5.500000 |       1.000000 |          0.564398 |         -1.425512 |          2.481348 |   0.289487 |      0.145925 | 0.657159 | 0.075671 | -0.004205 | 0.016222 |
| 5.000000 |       1.700000 |          0.016943 |         -2.116886 |          2.046504 |   0.321450 |      0.139840 | 0.690038 | 0.072624 | -0.004051 | 0.015569 |
| 7.500000 |       0.850000 |          0.235711 |         -1.329441 |          1.699135 |   0.197165 |      0.100526 | 0.542929 | 0.081653 | -0.004492 | 0.017505 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$2.15**

Expected profit (USD): **0.38** [lowest: -2.33, highest: 2.97]

Delta: 0.8377 (price sensitivity)

Gamma: 0.0506 (delta sensitivity)

Theta: $-0.0029 (negative decay per trading-day)

Vega: $0.0108 (volatility sensitivity per 1%)

ITM (In The Money) probability: **51.01%**

Profit probability: **19.79%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $3 | $2.15 | $2.19 | 1.12 | 0.7889 | -0.04 |
| $4 | $1.63 | $1.69 | 1.10 | 0.7889 | -0.06 |
| $4 | $1.75 | $1.49 | 1.07 | 0.7889 | 0.26 |
| $5 | $1.70 | $1.31 | 1.06 | 0.7889 | 0.39 |
| $6 | $1.00 | $1.16 | 1.05 | 0.7889 | -0.16 |
| $8 | $0.85 | $0.73 | 1.03 | 0.7889 | 0.12 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1155** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2261**

- Modal profit prediction correlation: **0.3537**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **46.15%**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1486 [-0.7713, 0.6738]**

- Stock Volatility: **0.7889 [0.6822, 0.9047]**

- Based on **1154** observations


- Garch Volatility forecast: **0.9834**

### 2. Validate Stock Option Contracts

- Analyze **13** strikes prices..

Total of valuable options: 13

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  2.000000 |       2.850000 |          0.943754 |         -3.110812 |          7.239948 |   0.543918 |      0.168926 | 0.912281 | 0.025326 | -0.001524 | 0.009025 |
|  1.000000 |       3.900000 |          0.524362 |         -3.859545 |          7.088088 |   0.733256 |      0.167199 | 0.969071 | 0.011093 | -0.000715 | 0.003953 |
|  2.500000 |       2.800000 |          0.738819 |         -3.149435 |          6.856971 |   0.478213 |      0.154312 | 0.882975 | 0.031241 | -0.001853 | 0.011133 |
|  4.000000 |       1.830000 |          1.101501 |         -2.282026 |          6.694431 |   0.343816 |      0.139459 | 0.800262 | 0.044470 | -0.002577 | 0.015847 |
|  3.000000 |       2.850000 |          0.463486 |         -3.264355 |          6.392915 |   0.424885 |      0.138942 | 0.854336 | 0.036344 | -0.002134 | 0.012951 |
|  3.500000 |       2.750000 |          0.362398 |         -3.206691 |          6.105618 |   0.380807 |      0.129187 | 0.826715 | 0.040723 | -0.002374 | 0.014511 |
|  4.500000 |       1.800000 |          0.967659 |         -2.284592 |          6.367748 |   0.312373 |      0.128042 | 0.775023 | 0.047674 | -0.002750 | 0.016989 |
|  5.000000 |       1.720000 |          0.898394 |         -2.203396 |          6.137843 |   0.285350 |      0.119000 | 0.750990 | 0.050410 | -0.002897 | 0.017964 |
|  5.500000 |       1.600000 |          0.881714 |         -2.091329 |          5.952301 |   0.261908 |      0.111628 | 0.728125 | 0.052744 | -0.003021 | 0.018795 |
|  7.500000 |       1.050000 |          0.982291 |         -1.557175 |          5.427324 |   0.193041 |      0.088991 | 0.647242 | 0.059050 | -0.003352 | 0.021042 |
| 10.000000 |       1.000000 |          0.621166 |         -1.530721 |          4.386752 |   0.140205 |      0.063742 | 0.565617 | 0.062560 | -0.003526 | 0.022293 |
| 12.500000 |       0.900000 |          0.415446 |         -1.440587 |          3.630912 |   0.106685 |      0.048036 | 0.500111 | 0.063420 | -0.003558 | 0.022599 |
| 15.000000 |       0.650000 |          0.428880 |         -1.197968 |          3.193178 |   0.083928 |      0.037940 | 0.446505 | 0.062849 | -0.003514 | 0.022396 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$2**

Market price: **$2.85**

Expected profit (USD): **0.94** [lowest: -3.11, highest: 7.24]

Delta: 0.9123 (price sensitivity)

Gamma: 0.0253 (delta sensitivity)

Theta: $-0.0015 (negative decay per trading-day)

Vega: $0.0090 (volatility sensitivity per 1%)

ITM (In The Money) probability: **54.39%**

Profit probability: **16.89%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $1 | $3.90 | $3.76 | 1.30 | 0.7889 | 0.14 |
| $2 | $2.85 | $3.03 | 1.16 | 0.7889 | -0.18 |
| $2 | $2.80 | $2.74 | 1.11 | 0.7889 | 0.06 |
| $3 | $2.85 | $2.48 | 0.97 | 0.7889 | 0.37 |
| $4 | $2.75 | $2.25 | 0.96 | 0.7889 | 0.50 |
| $4 | $1.83 | $2.05 | 1.07 | 0.7889 | -0.22 |
| $4 | $1.80 | $1.87 | 0.97 | 0.7889 | -0.07 |
| $5 | $1.72 | $1.72 | 1.01 | 0.7889 | 0.00 |
| $6 | $1.60 | $1.58 | 1.03 | 0.7889 | 0.02 |
| $8 | $1.05 | $1.16 | 1.05 | 0.7889 | -0.11 |
| $10 | $1.00 | $0.82 | 1.06 | 0.7889 | 0.18 |
| $12 | $0.90 | $0.60 | 1.17 | 0.7889 | 0.30 |
| $15 | $0.65 | $0.45 | 1.22 | 0.7889 | 0.20 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1155** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2261**

- Modal profit prediction correlation: **0.3537**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **46.15%**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.1486 [-0.7713, 0.6738]**

- Stock Volatility: **0.7889 [0.6822, 0.9047]**

- Based on **1154** observations


- Garch Volatility forecast: **0.9834**

### 2. Validate Stock Option Contracts

- Analyze **11** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  3.000000 |       2.150000 |          3.080390 |         -2.701596 |         28.598845 |   0.306945 |      0.094682 | 0.897240 | 0.020028 | -0.001205 | 0.014313 |
|  2.000000 |       3.700000 |          1.872973 |         -4.281737 |         27.840555 |   0.384537 |      0.086790 | 0.930152 | 0.014997 | -0.000916 | 0.010717 |
|  3.500000 |       2.500000 |          2.584040 |         -3.078932 |         27.827744 |   0.279366 |      0.082969 | 0.882147 | 0.022097 | -0.001323 | 0.015791 |
|  2.500000 |       3.500000 |          1.892062 |         -4.085550 |         27.620403 |   0.341021 |      0.082969 | 0.913217 | 0.017682 | -0.001071 | 0.012636 |
|  4.000000 |       2.400000 |          2.550243 |         -2.984569 |         27.540205 |   0.256493 |      0.078323 | 0.867857 | 0.023937 | -0.001427 | 0.017106 |
|  4.500000 |       2.700000 |          2.126959 |         -3.298774 |         26.855722 |   0.237159 |      0.070306 | 0.854296 | 0.025583 | -0.001520 | 0.018282 |
|  5.000000 |       2.370000 |          2.342629 |         -2.946462 |         26.848971 |   0.220565 |      0.068788 | 0.841400 | 0.027066 | -0.001604 | 0.019342 |
|  5.500000 |       2.200000 |          2.406033 |         -2.775214 |         26.671898 |   0.206145 |      0.066002 | 0.829107 | 0.028407 | -0.001679 | 0.020300 |
|  7.500000 |       1.830000 |          2.409898 |         -2.399801 |         25.751693 |   0.163240 |      0.054736 | 0.785027 | 0.032688 | -0.001918 | 0.023360 |
| 10.000000 |       1.700000 |          2.177705 |         -2.282782 |         24.436191 |   0.129050 |      0.043362 | 0.738789 | 0.036377 | -0.002121 | 0.025996 |
| 12.500000 |       1.500000 |          2.085358 |         -2.068420 |         23.385070 |   0.106202 |      0.035710 | 0.699696 | 0.038918 | -0.002260 | 0.027812 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$3**

Market price: **$2.15**

Expected profit (USD): **3.08** [lowest: -2.70, highest: 28.60]

Delta: 0.8972 (price sensitivity)

Gamma: 0.0200 (delta sensitivity)

Theta: $-0.0012 (negative decay per trading-day)

Vega: $0.0143 (volatility sensitivity per 1%)

ITM (In The Money) probability: **30.69%**

Profit probability: **9.47%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Optimal Market Price | Implied Volatility | Model Volatility | Market Price - Optimal Market Price |
|--------|--------|----------|----|-----------|----- |
| $2 | $3.70 | $3.38 | 0.91 | 0.7889 | 0.32 |
| $2 | $3.50 | $3.17 | 0.91 | 0.7889 | 0.33 |
| $3 | $2.15 | $2.99 | 0.91 | 0.7889 | -0.84 |
| $4 | $2.50 | $2.82 | 0.94 | 0.7889 | -0.32 |
| $4 | $2.40 | $2.68 | 1.00 | 0.7889 | -0.28 |
| $4 | $2.70 | $2.54 | 0.89 | 0.7889 | 0.16 |
| $5 | $2.37 | $2.42 | 1.05 | 0.7889 | -0.05 |
| $6 | $2.20 | $2.31 | 1.02 | 0.7889 | -0.11 |
| $8 | $1.83 | $1.95 | 1.04 | 0.7889 | -0.12 |
| $10 | $1.70 | $1.63 | 1.06 | 0.7889 | 0.07 |
| $12 | $1.50 | $1.39 | 1.07 | 0.7889 | 0.11 |

### 6. Backtest Stock Option Strategies

- Config: Look Back Interval **252 Days**. **1155** Historical Prices **Last 5 Years**

- Average modal profit prediction error (actual price - predicted price): **0.2261**

- Modal profit prediction correlation: **0.3537**

- Backtests total: **13**

- Profitable Trades (profitable trades / total trades): **46.15%**

--------------------------------------------------

