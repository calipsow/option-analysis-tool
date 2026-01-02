# META Option Analysis From: 02.01.2026 07:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Options Are Bought NOT Sold On Expiration**

## Current Stock Price: $660.0900268554688

[SKIPPED]: stock option contract already expired

### Calculate Stock Option Nr. 2

Expires At: **09.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **107** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **213** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 30.000000 |     556.000000 |         82.958536 |         57.743822 |         79.689834 |   1.000000 |      0.971266 | 1.000000 | 0.000000 | -0.005937 | 0.000000 |
| 15.000000 |     607.980000 |         45.978536 |         20.183613 |         42.129626 |   1.000000 |      0.835842 | 1.000000 | 0.000000 | -0.002969 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$30**

Market price: **$556.00**

Expected profit (USD): **82.96** [lowest: 57.74, highest: 79.69]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0059 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **97.13%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $15 | $607.98 | $645.13 | 0.00 | 0.4008 | -37.15 |
| $30 | $556.00 | $630.17 | 0.00 | 0.4008 | -74.17 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **23.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **90** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **30.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **84** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **06.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **32** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **178** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |     733.350000 |        -53.502359 |       -130.907492 |        -49.175065 |   1.000000 |      0.244962 | 1.000000 | 0.000000 | -0.002948 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$15**

Market price: **$733.35**

Expected profit (USD): **-53.50** [lowest: -130.91, highest: -49.18]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0029 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **24.50%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $15 | $733.35 | $645.23 | 0.00 | 0.4008 | 88.12 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 8

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **140** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 80.000000 |     658.040000 |        -21.762066 |       -137.927614 |         -7.560870 |   1.000000 |      0.351925 | 1.000000 | 0.000000 | -0.015635 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$80**

Market price: **$658.04**

Expected profit (USD): **-21.76** [lowest: -137.93, highest: -7.56]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0156 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **35.19%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $80 | $658.04 | $581.29 | 0.00 | 0.4008 | 76.75 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 9

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **77** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 380.000000 |     298.450000 |         59.977604 |        -89.659688 |         89.024266 |   0.997555 |      0.544916 | 0.995802 | 0.000083 | -0.082182 | 0.052456 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$380**

Market price: **$298.45**

Expected profit (USD): **59.98** [lowest: -89.66, highest: 89.02]

Delta: 0.9958 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0822 (negative decay per day)

Vega: $0.0525 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.76%**

Profit probability: **54.49%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $380 | $298.45 | $288.43 | 0.00 | 0.4008 | 10.02 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 10

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **126** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 200.000000 |     479.820000 |         81.320293 |       -112.094280 |        117.984740 |   1.000000 |      0.556992 | 0.999999 | 0.000000 | -0.038659 | 0.000016 |
| 320.000000 |     438.380000 |          2.774026 |       -189.413317 |         40.141066 |   0.999344 |      0.390534 | 0.998744 | 0.000024 | -0.064364 | 0.019822 |
| 100.000000 |     679.730000 |        -18.589709 |       -214.786091 |         15.294151 |   1.000000 |      0.350161 | 1.000000 | 0.000000 | -0.019328 | 0.000000 |
| 380.000000 |     402.600000 |        -21.303111 |       -210.422235 |         16.859702 |   0.994624 |      0.344932 | 0.990848 | 0.000144 | -0.088134 | 0.117836 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$200**

Market price: **$479.82**

Expected profit (USD): **81.32** [lowest: -112.09, highest: 117.98]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0387 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **55.70%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $100 | $679.73 | $562.68 | 4.42 | 0.4008 | 117.05 |
| $200 | $479.82 | $465.26 | 0.00 | 0.4008 | 14.56 |
| $320 | $438.38 | $348.56 | 2.10 | 0.4008 | 89.82 |
| $380 | $402.60 | $291.14 | 1.47 | 0.4008 | 111.46 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 11

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **179** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  60.000000 |     423.810000 |        305.927079 |         64.638237 |        357.048472 |   1.000000 |      0.909628 | 1.000000 | 0.000000 | -0.011519 | 0.000000 |
|  30.000000 |     455.050000 |        304.687079 |         62.924015 |        355.334250 |   1.000000 |      0.908203 | 1.000000 | 0.000000 | -0.005760 | 0.000000 |
|  70.000000 |     441.110000 |        278.627079 |         37.070486 |        329.480721 |   1.000000 |      0.875325 | 1.000000 | 0.000000 | -0.013439 | 0.000000 |
|  90.000000 |     448.350000 |        251.387079 |          9.735754 |        302.145989 |   1.000000 |      0.835337 | 1.000000 | 0.000000 | -0.017279 | 0.000000 |
| 130.000000 |     513.750000 |        145.987079 |        -96.586236 |        195.823972 |   1.000000 |      0.643477 | 1.000000 | 0.000000 | -0.024958 | 0.000000 |
|  50.000000 |     616.500000 |        123.237079 |       -120.831738 |        171.578497 |   1.000000 |      0.598599 | 1.000000 | 0.000000 | -0.009599 | 0.000000 |
|  20.000000 |     699.580000 |         70.157079 |       -175.062577 |        117.347658 |   1.000000 |      0.495711 | 1.000000 | 0.000000 | -0.003840 | 0.000000 |
| 165.000000 |     556.420000 |         68.317080 |       -174.846575 |        117.562758 |   1.000000 |      0.492249 | 1.000000 | 0.000000 | -0.031678 | 0.000009 |
| 120.000000 |     601.450000 |         68.287079 |       -175.511168 |        116.899060 |   1.000000 |      0.492192 | 1.000000 | 0.000000 | -0.023038 | 0.000000 |
| 100.000000 |     630.200000 |         59.537079 |       -184.664560 |        107.745675 |   1.000000 |      0.475858 | 1.000000 | 0.000000 | -0.019198 | 0.000000 |
|  80.000000 |     656.420000 |         53.317079 |       -191.298766 |        101.111469 |   1.000000 |      0.464388 | 1.000000 | 0.000000 | -0.015359 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$60**

Market price: **$423.81**

Expected profit (USD): **305.93** [lowest: 64.64, highest: 357.05]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0115 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **90.96%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $20 | $699.58 | $640.74 | 0.00 | 0.4008 | 58.84 |
| $30 | $455.05 | $631.06 | 0.00 | 0.4008 | -176.01 |
| $50 | $616.50 | $611.71 | 0.00 | 0.4008 | 4.79 |
| $60 | $423.81 | $602.03 | 0.00 | 0.4008 | -178.22 |
| $70 | $441.11 | $592.36 | 0.00 | 0.4008 | -151.25 |
| $80 | $656.42 | $582.68 | 0.00 | 0.4008 | 73.74 |
| $90 | $448.35 | $573.01 | 1.52 | 0.4008 | -124.66 |
| $100 | $630.20 | $563.33 | 5.63 | 0.4008 | 66.87 |
| $120 | $601.45 | $543.98 | 4.48 | 0.4008 | 57.47 |
| $130 | $513.75 | $534.30 | 2.64 | 0.4008 | -20.55 |
| $165 | $556.42 | $500.44 | 3.35 | 0.4008 | 55.98 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 12

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **73** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 13

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **86** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 14

Expires At: **18.09.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **86** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  70.000000 |     582.010000 |        220.605700 |       -156.812080 |        312.263655 |   1.000000 |      0.646608 | 1.000000 | 0.000000 | -0.013196 | 0.000000 |
|  10.000000 |     722.590000 |        140.025700 |       -239.380060 |        229.695678 |   1.000000 |      0.525119 | 1.000000 | 0.000000 | -0.001885 | 0.000000 |
| 120.000000 |     618.500000 |        134.115701 |       -243.759360 |        225.314208 |   1.000000 |      0.516516 | 1.000000 | 0.000000 | -0.022622 | 0.000016 |
| 140.000000 |     643.000000 |         89.615710 |       -288.598853 |        180.466179 |   0.999999 |      0.453885 | 0.999997 | 0.000000 | -0.026399 | 0.000110 |
| 130.000000 |     654.700000 |         87.915703 |       -290.533802 |        178.536893 |   1.000000 |      0.451576 | 0.999999 | 0.000000 | -0.024509 | 0.000044 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$70**

Market price: **$582.01**

Expected profit (USD): **220.61** [lowest: -156.81, highest: 312.26]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0132 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **64.66%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $10 | $722.59 | $650.59 | 0.00 | 0.4008 | 72.00 |
| $70 | $582.01 | $593.58 | 0.00 | 0.4008 | -11.57 |
| $120 | $618.50 | $546.08 | 3.65 | 0.4008 | 72.42 |
| $130 | $654.70 | $536.58 | 3.00 | 0.4008 | 118.12 |
| $140 | $643.00 | $527.08 | 3.14 | 0.4008 | 115.92 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 15

Expires At: **18.12.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **158** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  30.000000 |     452.920000 |        480.221251 |        -31.610668 |        625.978804 |   1.000000 |      0.866794 | 1.000000 | 0.000000 | -0.005554 | 0.000000 |
|  70.000000 |     416.710000 |        476.431251 |        -34.879486 |        622.709715 |   1.000000 |      0.862897 | 1.000000 | 0.000000 | -0.012960 | 0.000001 |
|  55.000000 |     488.880000 |        419.261251 |        -93.078020 |        564.511431 |   1.000000 |      0.799142 | 1.000000 | 0.000000 | -0.010183 | 0.000000 |
| 210.000000 |     511.500000 |        241.652471 |       -269.052685 |        386.589228 |   0.999485 |      0.575312 | 0.998683 | 0.000015 | -0.040466 | 0.033659 |
|  75.000000 |     662.670000 |        225.471251 |       -289.387126 |        368.201808 |   1.000000 |      0.555289 | 1.000000 | 0.000000 | -0.013885 | 0.000002 |
|  95.000000 |     676.000000 |        192.141252 |       -322.946066 |        334.638469 |   1.000000 |      0.514993 | 0.999999 | 0.000000 | -0.017589 | 0.000027 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$30**

Market price: **$452.92**

Expected profit (USD): **480.22** [lowest: -31.61, highest: 625.98]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0056 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **86.68%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $30 | $452.92 | $632.10 | 0.00 | 0.4008 | -179.18 |
| $55 | $488.88 | $608.77 | 1.13 | 0.4008 | -119.89 |
| $70 | $416.71 | $594.77 | 0.00 | 0.4008 | -178.06 |
| $75 | $662.67 | $590.11 | 0.00 | 0.4008 | 72.56 |
| $95 | $676.00 | $571.45 | 2.91 | 0.4008 | 104.55 |
| $210 | $511.50 | $464.40 | 0.00 | 0.4008 | 47.10 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 16

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **137** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 310.000000 |     384.280000 |        298.956266 |       -235.343628 |        464.278800 |   0.990450 |      0.616833 | 0.980288 | 0.000160 | -0.072959 | 0.386124 |
| 140.000000 |     587.490000 |        265.350496 |       -291.101773 |        427.511219 |   0.999979 |      0.576959 | 0.999932 | 0.000001 | -0.025875 | 0.002233 |
| 110.000000 |     645.290000 |        237.550246 |       -319.902124 |        398.884061 |   0.999998 |      0.544354 | 0.999993 | 0.000000 | -0.020264 | 0.000255 |
| 130.000000 |     636.650000 |        226.190347 |       -331.065319 |        387.633326 |   0.999990 |      0.531277 | 0.999965 | 0.000000 | -0.023988 | 0.001181 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$310**

Market price: **$384.28**

Expected profit (USD): **298.96** [lowest: -235.34, highest: 464.28]

Delta: 0.9803 (price sensitivity)

Gamma: 0.0002 (delta sensitivity)

Theta: $-0.0730 (negative decay per day)

Vega: $0.3861 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.05%**

Profit probability: **61.68%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $110 | $645.29 | $558.02 | 3.38 | 0.4008 | 87.27 |
| $130 | $636.65 | $539.47 | 2.18 | 0.4008 | 97.18 |
| $140 | $587.49 | $530.20 | 2.64 | 0.4008 | 57.29 |
| $310 | $384.28 | $376.31 | 0.53 | 0.4008 | 7.97 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 17

Expires At: **17.06.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **74** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 430.000000 |     284.450000 |        462.192986 |       -226.705090 |        751.045909 |   0.943866 |      0.630594 | 0.895905 | 0.000507 | -0.119415 | 1.729801 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$430**

Market price: **$284.45**

Expected profit (USD): **462.19** [lowest: -226.71, highest: 751.05]

Delta: 0.8959 (price sensitivity)

Gamma: 0.0005 (delta sensitivity)

Theta: $-0.1194 (negative decay per day)

Vega: $1.7298 (volatility sensitivity per 1%)

ITM (In The Money) probability: **94.39%**

Profit probability: **63.06%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $430 | $284.45 | $300.82 | 0.48 | 0.4008 | -16.37 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 18

Expires At: **17.09.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **78** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 19

Expires At: **17.12.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **139** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 230.000000 |     470.020000 |        729.508917 |       -361.772567 |       1222.454476 |   0.995267 |      0.677210 | 0.986711 | 0.000082 | -0.047318 | 0.378812 |
| 240.000000 |     462.480000 |        727.101229 |       -359.737430 |       1220.169189 |   0.994248 |      0.675205 | 0.984219 | 0.000095 | -0.050193 | 0.439218 |
|  80.000000 |     651.500000 |        697.847603 |       -427.685625 |       1188.089304 |   0.999990 |      0.651707 | 0.999952 | 0.000000 | -0.013830 | 0.002216 |
| 260.000000 |     511.410000 |        658.309861 |       -419.797462 |       1150.711858 |   0.991793 |      0.619978 | 0.978437 | 0.000124 | -0.056132 | 0.572964 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$230**

Market price: **$470.02**

Expected profit (USD): **729.51** [lowest: -361.77, highest: 1222.45]

Delta: 0.9867 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0473 (negative decay per day)

Vega: $0.3788 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.53%**

Profit probability: **67.72%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $80 | $651.50 | $590.66 | 0.00 | 0.4008 | 60.84 |
| $230 | $470.02 | $464.01 | 0.54 | 0.4008 | 6.01 |
| $240 | $462.48 | $456.02 | 0.53 | 0.4008 | 6.46 |
| $260 | $511.41 | $440.30 | 1.23 | 0.4008 | 71.11 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 20

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.2732 [-0.2634, 0.3791]**

- Stock Volatility: **0.4008 [0.3483, 0.4573]**

- Based on **1507** observations


- Garch Volatility forecast: **0.3148**

### 2. Validate Stock Option Contracts

- Analyze **142** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 230.000000 |     501.170000 |        753.668593 |       -400.821395 |       1295.178471 |   0.995001 |      0.658193 | 0.985751 | 0.000085 | -0.047233 | 0.412070 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$230**

Market price: **$501.17**

Expected profit (USD): **753.67** [lowest: -400.82, highest: 1295.18]

Delta: 0.9858 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0472 (negative decay per day)

Vega: $0.4121 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.50%**

Profit probability: **65.82%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $230 | $501.17 | $465.76 | 0.46 | 0.4008 | 35.41 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.1022**

- Model prediction correlation: **-0.7985**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

