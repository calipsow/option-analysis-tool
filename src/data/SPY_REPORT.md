# SPY Option Analysis From: 02.01.2026 08:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Shares Are Bought NOT Sold on Expiration**

## Current Stock Price: $681.9199829101562

[SKIPPED]: stock option contract already expired

### Calculate Stock Option Nr. 2

Expires At: **05.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **72** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **06.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **60** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **07.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **42** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **08.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **9** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **09.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **118** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **230** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 245.000000 |     354.040000 |         87.891572 |         75.472017 |         86.028863 |   1.000000 |      0.999969 | 1.000000 | 0.000000 | -0.048486 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$245**

Market price: **$354.04**

Expected profit (USD): **87.89** [lowest: 75.47, highest: 86.03]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0485 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **100.00%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $245 | $354.04 | $437.55 | 0.00 | 0.1868 | -83.51 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 8

Expires At: **23.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **114** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 9

Expires At: **30.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **217** strikes prices..

Total of valuable options: 3

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 581.000000 |      80.650000 |         31.269955 |         11.216350 |         33.187297 |   0.999614 |      0.794492 | 0.999307 | 0.000068 | -0.116151 | 0.005366 |
| 435.000000 |     227.000000 |         30.916959 |          9.494732 |         31.471919 |   1.000000 |      0.791599 | 1.000000 | 0.000000 | -0.085848 | 0.000000 |
| 592.000000 |      74.980000 |         25.948460 |          6.044809 |         27.992354 |   0.998666 |      0.748091 | 0.997730 | 0.000200 | -0.121207 | 0.015871 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$581**

Market price: **$80.65**

Expected profit (USD): **31.27** [lowest: 11.22, highest: 33.19]

Delta: 0.9993 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.1162 (negative decay per day)

Vega: $0.0054 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.96%**

Profit probability: **79.45%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $435 | $227.00 | $249.24 | 0.00 | 0.1868 | -22.24 |
| $581 | $80.65 | $104.06 | 0.00 | 0.1868 | -23.41 |
| $592 | $74.98 | $93.19 | 0.33 | 0.1868 | -18.21 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 10

Expires At: **06.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **69** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 11

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **112** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 390.000000 |     263.910000 |         48.082896 |         11.140205 |         50.350003 |   1.000000 |      0.809832 | 1.000000 | 0.000000 | -0.076647 | 0.000000 |
| 345.000000 |     343.000000 |         13.992896 |        -23.676244 |         15.533554 |   1.000000 |      0.575453 | 1.000000 | 0.000000 | -0.067804 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$390**

Market price: **$263.91**

Expected profit (USD): **48.08** [lowest: 11.14, highest: 50.35]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0766 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **80.98%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $345 | $343.00 | $340.19 | 0.93 | 0.1868 | 2.81 |
| $390 | $263.91 | $295.62 | 0.00 | 0.1868 | -31.71 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 12

Expires At: **27.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **196** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 582.000000 |      80.810000 |         42.374076 |          2.945686 |         47.326477 |   0.990870 |      0.752421 | 0.984296 | 0.000720 | -0.131619 | 0.125490 |
| 593.000000 |      72.170000 |         40.152752 |          1.358699 |         45.302482 |   0.983282 |      0.738212 | 0.972470 | 0.001158 | -0.144034 | 0.201822 |
| 637.000000 |      46.590000 |         24.037122 |         -8.989328 |         30.368290 |   0.891454 |      0.616950 | 0.847527 | 0.004310 | -0.220678 | 0.750914 |
| 599.000000 |      88.420000 |         18.020208 |        -20.505499 |         23.108882 |   0.977319 |      0.590123 | 0.963503 | 0.001462 | -0.152215 | 0.254762 |
| 589.000000 |     107.240000 |          9.022482 |        -30.338031 |         13.787457 |   0.986489 |      0.527506 | 0.977400 | 0.000982 | -0.139137 | 0.171044 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$582**

Market price: **$80.81**

Expected profit (USD): **42.37** [lowest: 2.95, highest: 47.33]

Delta: 0.9843 (price sensitivity)

Gamma: 0.0007 (delta sensitivity)

Theta: $-0.1316 (negative decay per day)

Vega: $0.1255 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.09%**

Profit probability: **75.24%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $582 | $80.81 | $106.78 | 0.34 | 0.1868 | -25.97 |
| $589 | $107.24 | $100.09 | 0.40 | 0.1868 | 7.15 |
| $593 | $72.17 | $96.30 | 0.32 | 0.1868 | -24.13 |
| $599 | $88.42 | $90.68 | 0.31 | 0.1868 | -2.26 |
| $637 | $46.59 | $57.51 | 0.20 | 0.1868 | -10.92 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 13

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **121** strikes prices..

Total of valuable options: 10

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 295.000000 |     253.050000 |        166.229200 |        109.068376 |        171.450773 |   1.000000 |      0.995666 | 1.000000 | 0.000000 | -0.057656 | 0.000000 |
| 285.000000 |     321.900000 |        107.379200 |         49.574863 |        111.957260 |   1.000000 |      0.942339 | 1.000000 | 0.000000 | -0.055701 | 0.000000 |
| 255.000000 |     355.140000 |        104.139200 |         46.022007 |        108.404404 |   1.000000 |      0.935731 | 1.000000 | 0.000000 | -0.049838 | 0.000000 |
| 365.000000 |     281.950000 |         67.329200 |          9.901195 |         72.283592 |   1.000000 |      0.820355 | 1.000000 | 0.000000 | -0.071337 | 0.000000 |
| 260.000000 |     388.320000 |         65.959200 |          7.529527 |         69.911924 |   1.000000 |      0.814590 | 1.000000 | 0.000000 | -0.050815 | 0.000000 |
| 265.000000 |     383.680000 |         65.599200 |          7.213226 |         69.595622 |   1.000000 |      0.813058 | 1.000000 | 0.000000 | -0.051792 | 0.000000 |
| 290.000000 |     367.290000 |         56.989200 |         -1.240158 |         61.142239 |   1.000000 |      0.774410 | 1.000000 | 0.000000 | -0.056679 | 0.000000 |
| 270.000000 |     396.210000 |         48.069200 |        -10.431765 |         51.950632 |   1.000000 |      0.730607 | 1.000000 | 0.000000 | -0.052770 | 0.000000 |
| 395.000000 |     276.010000 |         43.269200 |        -14.103145 |         48.279252 |   1.000000 |      0.705652 | 1.000000 | 0.000000 | -0.077200 | 0.000000 |
| 375.000000 |     303.000000 |         36.279200 |        -21.347613 |         41.034784 |   1.000000 |      0.667861 | 1.000000 | 0.000000 | -0.073291 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$295**

Market price: **$253.05**

Expected profit (USD): **166.23** [lowest: 109.07, highest: 171.45]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0577 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **99.57%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $255 | $355.14 | $430.74 | 0.00 | 0.1868 | -75.60 |
| $260 | $388.32 | $425.81 | 0.00 | 0.1868 | -37.49 |
| $265 | $383.68 | $420.89 | 0.00 | 0.1868 | -37.21 |
| $270 | $396.21 | $415.96 | 0.00 | 0.1868 | -19.75 |
| $285 | $321.90 | $401.19 | 0.00 | 0.1868 | -79.29 |
| $290 | $367.29 | $396.26 | 0.00 | 0.1868 | -28.97 |
| $295 | $253.05 | $391.34 | 0.00 | 0.1868 | -138.29 |
| $365 | $281.95 | $322.38 | 0.00 | 0.1868 | -40.43 |
| $375 | $303.00 | $312.53 | 0.00 | 0.1868 | -9.53 |
| $395 | $276.01 | $292.83 | 0.00 | 0.1868 | -16.82 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 14

Expires At: **31.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **195** strikes prices..

Total of valuable options: 42

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 534.000000 |      60.980000 |        124.227230 |         61.336507 |        132.528021 |   0.997374 |      0.954985 | 0.994570 | 0.000217 | -0.109779 | 0.062350 |
| 536.000000 |      61.220000 |        121.992781 |         59.129956 |        130.284597 |   0.997070 |      0.951488 | 0.993990 | 0.000238 | -0.110691 | 0.068230 |
| 532.000000 |      81.590000 |        105.612258 |         42.482872 |        113.708262 |   0.997650 |      0.919538 | 0.995102 | 0.000198 | -0.108902 | 0.056886 |
| 533.000000 |      87.070000 |         99.134675 |         35.980674 |        107.189488 |   0.997515 |      0.903531 | 0.994842 | 0.000208 | -0.109336 | 0.059568 |
| 528.000000 |      95.160000 |         96.033843 |         32.688868 |        103.973797 |   0.998127 |      0.895188 | 0.996033 | 0.000164 | -0.107251 | 0.047120 |
| 526.000000 |      97.730000 |         95.460306 |         32.060008 |        103.370972 |   0.998332 |      0.893599 | 0.996438 | 0.000149 | -0.106472 | 0.042778 |
| 350.000000 |     276.190000 |         92.974547 |         27.593752 |         99.142452 |   1.000000 |      0.886556 | 1.000000 | 0.000000 | -0.068256 | 0.000000 |
| 360.000000 |     266.820000 |         92.344547 |         27.052342 |         98.601042 |   1.000000 |      0.884705 | 1.000000 | 0.000000 | -0.070206 | 0.000000 |
| 542.000000 |      85.010000 |         92.223515 |         29.282447 |        100.306371 |   0.995968 |      0.884143 | 0.991924 | 0.000309 | -0.113657 | 0.088561 |
| 541.000000 |      86.130000 |         92.099587 |         29.142286 |        100.190250 |   0.996174 |      0.883787 | 0.992305 | 0.000296 | -0.113137 | 0.084877 |
| 531.000000 |      96.530000 |         91.669972 |         28.386646 |         99.627911 |   0.997778 |      0.882595 | 0.995350 | 0.000189 | -0.108477 | 0.054303 |
| 544.000000 |      84.780000 |         90.462010 |         27.582556 |         98.555462 |   0.995530 |      0.878820 | 0.991115 | 0.000336 | -0.114728 | 0.096304 |
| 514.000000 |     117.350000 |         87.826037 |         24.103379 |         95.528522 |   0.999197 |      0.870819 | 0.998198 | 0.000081 | -0.102359 | 0.023104 |
| 527.000000 |     107.690000 |         84.502023 |         21.026593 |         92.324833 |   0.998232 |      0.859935 | 0.996240 | 0.000157 | -0.106857 | 0.044906 |
| 370.000000 |     270.750000 |         78.414547 |         13.085146 |         84.633846 |   1.000000 |      0.838800 | 1.000000 | 0.000000 | -0.072156 | 0.000000 |
| 543.000000 |     103.080000 |         73.157653 |         10.077931 |         81.076845 |   0.995754 |      0.818762 | 0.991527 | 0.000322 | -0.114187 | 0.092369 |
| 390.000000 |     256.540000 |         72.624547 |          7.429644 |         78.978342 |   1.000000 |      0.816970 | 1.000000 | 0.000000 | -0.076057 | 0.000000 |
| 546.000000 |     100.600000 |         72.651423 |          9.689143 |         80.606914 |   0.995051 |      0.816736 | 0.990238 | 0.000365 | -0.115842 | 0.104563 |
| 556.000000 |      95.000000 |         68.315383 |          5.805761 |         76.377139 |   0.991944 |      0.799101 | 0.984707 | 0.000538 | -0.122115 | 0.154279 |
| 415.000000 |     236.850000 |         67.314548 |          2.306265 |         73.854920 |   1.000000 |      0.795595 | 1.000000 | 0.000000 | -0.080933 | 0.000008 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$534**

Market price: **$60.98**

Expected profit (USD): **124.23** [lowest: 61.34, highest: 132.53]

Delta: 0.9946 (price sensitivity)

Gamma: 0.0002 (delta sensitivity)

Theta: $-0.1098 (negative decay per day)

Vega: $0.0624 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.74%**

Profit probability: **95.50%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $350 | $276.19 | $337.91 | 0.00 | 0.1868 | -61.72 |
| $355 | $323.00 | $333.00 | 0.00 | 0.1868 | -10.00 |
| $360 | $266.82 | $328.08 | 0.00 | 0.1868 | -61.26 |
| $370 | $270.75 | $318.25 | 0.00 | 0.1868 | -47.50 |
| $375 | $313.62 | $313.34 | 0.71 | 0.1868 | 0.28 |
| $390 | $256.54 | $298.59 | 0.00 | 0.1868 | -42.05 |
| $405 | $267.00 | $283.85 | 0.00 | 0.1868 | -16.85 |
| $415 | $236.85 | $274.02 | 0.00 | 0.1868 | -37.17 |
| $420 | $233.30 | $269.11 | 0.00 | 0.1868 | -35.81 |
| $425 | $251.47 | $264.19 | 0.00 | 0.1868 | -12.72 |
| $440 | $241.27 | $249.45 | 0.00 | 0.1868 | -8.18 |
| $445 | $210.46 | $244.54 | 0.00 | 0.1868 | -34.08 |
| $511 | $184.74 | $179.72 | 0.49 | 0.1868 | 5.02 |
| $513 | $185.40 | $177.76 | 0.49 | 0.1868 | 7.64 |
| $514 | $117.35 | $176.78 | 0.00 | 0.1868 | -59.43 |
| $516 | $163.83 | $174.82 | 0.37 | 0.1868 | -10.99 |
| $518 | $144.94 | $172.86 | 0.00 | 0.1868 | -27.92 |
| $521 | $152.78 | $169.93 | 0.00 | 0.1868 | -17.15 |
| $524 | $158.60 | $167.00 | 0.00 | 0.1868 | -8.40 |
| $526 | $97.73 | $165.04 | 0.00 | 0.1868 | -67.31 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 15

Expires At: **30.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **154** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 16

Expires At: **29.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **110** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 17

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **126** strikes prices..

Total of valuable options: 11

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 280.000000 |     314.930000 |        160.315170 |         36.529873 |        175.001871 |   1.000000 |      0.924129 | 1.000000 | 0.000000 | -0.053756 | 0.000000 |
| 265.000000 |     349.370000 |        140.875170 |         16.763689 |        155.235687 |   1.000000 |      0.888734 | 1.000000 | 0.000000 | -0.050876 | 0.000000 |
| 295.000000 |     325.100000 |        135.145170 |         11.267298 |        149.739295 |   1.000000 |      0.876600 | 1.000000 | 0.000000 | -0.056635 | 0.000000 |
| 260.000000 |     368.980000 |        126.265170 |          1.964779 |        140.436778 |   1.000000 |      0.856269 | 1.000000 | 0.000000 | -0.049916 | 0.000000 |
| 290.000000 |     356.090000 |        109.155170 |        -15.021239 |        123.450758 |   1.000000 |      0.812034 | 1.000000 | 0.000000 | -0.055675 | 0.000000 |
| 365.000000 |     284.640000 |        105.605179 |        -17.882008 |        120.589046 |   0.999999 |      0.802064 | 0.999996 | 0.000000 | -0.070080 | 0.000111 |
| 325.000000 |     325.600000 |        104.645170 |        -19.235564 |        119.236407 |   1.000000 |      0.799324 | 1.000000 | 0.000000 | -0.062395 | 0.000003 |
| 285.000000 |     379.600000 |         90.645170 |        -33.754732 |        104.717266 |   1.000000 |      0.757342 | 1.000000 | 0.000000 | -0.054715 | 0.000000 |
| 320.000000 |     350.080000 |         85.165170 |        -38.952362 |         99.519620 |   1.000000 |      0.739961 | 1.000000 | 0.000000 | -0.061435 | 0.000002 |
| 360.000000 |     312.840000 |         82.405176 |        -41.352944 |         97.118419 |   0.999999 |      0.731026 | 0.999997 | 0.000000 | -0.069118 | 0.000073 |
| 375.000000 |     297.950000 |         82.295195 |        -41.317524 |         97.152462 |   0.999998 |      0.730668 | 0.999990 | 0.000000 | -0.072006 | 0.000243 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$280**

Market price: **$314.93**

Expected profit (USD): **160.32** [lowest: 36.53, highest: 175.00]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0538 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **92.41%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $260 | $368.98 | $430.34 | 0.00 | 0.1868 | -61.36 |
| $265 | $349.37 | $425.51 | 0.00 | 0.1868 | -76.14 |
| $280 | $314.93 | $410.99 | 0.00 | 0.1868 | -96.06 |
| $285 | $379.60 | $406.15 | 0.00 | 0.1868 | -26.55 |
| $290 | $356.09 | $401.32 | 0.00 | 0.1868 | -45.23 |
| $295 | $325.10 | $396.48 | 0.00 | 0.1868 | -71.38 |
| $320 | $350.08 | $372.29 | 0.48 | 0.1868 | -22.21 |
| $325 | $325.60 | $367.45 | 0.00 | 0.1868 | -41.85 |
| $360 | $312.84 | $333.58 | 0.00 | 0.1868 | -20.74 |
| $365 | $284.64 | $328.75 | 0.00 | 0.1868 | -44.11 |
| $375 | $297.95 | $319.07 | 0.00 | 0.1868 | -21.12 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 18

Expires At: **30.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **158** strikes prices..

Total of valuable options: 21

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 460.000000 |     198.060000 |        102.837330 |        -28.313133 |        120.111317 |   0.999178 |      0.779888 | 0.997633 | 0.000069 | -0.089977 | 0.042327 |
| 577.000000 |      87.460000 |         97.990643 |        -19.958193 |        116.540727 |   0.955168 |      0.761117 | 0.915251 | 0.001458 | -0.144624 | 0.889847 |
| 562.000000 |     108.000000 |         91.886365 |        -29.580669 |        110.212458 |   0.968966 |      0.744339 | 0.938518 | 0.001140 | -0.135050 | 0.695865 |
| 558.000000 |     115.550000 |         88.218443 |        -34.093505 |        106.463219 |   0.972032 |      0.733349 | 0.943877 | 0.001061 | -0.132560 | 0.647795 |
| 586.000000 |      90.120000 |         86.778812 |        -28.856746 |        105.329445 |   0.944988 |      0.725284 | 0.898797 | 0.001662 | -0.150426 | 1.014622 |
| 564.000000 |     115.680000 |         82.270048 |        -38.869244 |        100.524286 |   0.967340 |      0.713968 | 0.935708 | 0.001180 | -0.136308 | 0.720523 |
| 584.000000 |     102.720000 |         76.071194 |        -40.243493 |         94.478721 |   0.947381 |      0.691142 | 0.902618 | 0.001616 | -0.149139 | 0.986468 |
| 515.000000 |     174.260000 |         71.815523 |        -56.684863 |         89.415670 |   0.992345 |      0.682775 | 0.982205 | 0.000412 | -0.109202 | 0.251239 |
| 589.000000 |     100.330000 |         73.739405 |        -41.166801 |         92.191654 |   0.941255 |      0.682543 | 0.892888 | 0.001732 | -0.152348 | 1.057233 |
| 587.000000 |     102.900000 |         73.054435 |        -42.454940 |         91.458499 |   0.943763 |      0.680656 | 0.896851 | 0.001685 | -0.151067 | 1.028778 |
| 576.000000 |     113.950000 |         72.456332 |        -46.007365 |         90.732797 |   0.956208 |      0.680491 | 0.916962 | 0.001436 | -0.143979 | 0.876320 |
| 581.000000 |     111.960000 |         69.678551 |        -47.484666 |         88.017896 |   0.950829 |      0.670474 | 0.908173 | 0.001547 | -0.147205 | 0.944669 |
| 588.000000 |     107.070000 |         67.941293 |        -47.331105 |         86.306422 |   0.942518 |      0.663404 | 0.894881 | 0.001709 | -0.151708 | 1.042982 |
| 603.000000 |      92.520000 |         68.505738 |        -42.139551 |         86.982308 |   0.921466 |      0.661891 | 0.862505 | 0.002064 | -0.161086 | 1.260036 |
| 566.000000 |     132.890000 |         63.127045 |        -57.739899 |         81.242012 |   0.965651 |      0.650514 | 0.932809 | 0.001221 | -0.137573 | 0.745579 |
| 591.000000 |     107.990000 |         64.199469 |        -50.236986 |         82.553855 |   0.938668 |      0.650175 | 0.888831 | 0.001779 | -0.153622 | 1.085863 |
| 613.000000 |      93.750000 |         58.142396 |        -49.110954 |         76.616218 |   0.904851 |      0.623679 | 0.838017 | 0.002303 | -0.166932 | 1.405716 |
| 609.000000 |     101.010000 |         54.515712 |        -54.210695 |         72.910280 |   0.911750 |      0.612452 | 0.848085 | 0.002208 | -0.164645 | 1.347604 |
| 612.000000 |      99.800000 |         52.998128 |        -54.688977 |         71.391068 |   0.906608 |      0.606269 | 0.840568 | 0.002279 | -0.166367 | 1.391222 |
| 614.000000 |     100.110000 |         50.878432 |        -56.107650 |         69.263730 |   0.903073 |      0.598273 | 0.835444 | 0.002326 | -0.167491 | 1.420182 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$460**

Market price: **$198.06**

Expected profit (USD): **102.84** [lowest: -28.31, highest: 120.11]

Delta: 0.9976 (price sensitivity)

Gamma: 0.0001 (delta sensitivity)

Theta: $-0.0900 (negative decay per day)

Vega: $0.0423 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.92%**

Profit probability: **77.99%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $460 | $198.06 | $237.96 | 0.00 | 0.1868 | -39.90 |
| $515 | $174.26 | $185.54 | 0.34 | 0.1868 | -11.28 |
| $558 | $115.55 | $146.05 | 0.25 | 0.1868 | -30.50 |
| $562 | $108.00 | $142.50 | 0.25 | 0.1868 | -34.50 |
| $564 | $115.68 | $140.74 | 0.14 | 0.1868 | -25.06 |
| $566 | $132.89 | $138.98 | 0.30 | 0.1868 | -6.09 |
| $576 | $113.95 | $130.30 | 0.40 | 0.1868 | -16.35 |
| $577 | $87.46 | $129.44 | 0.24 | 0.1868 | -41.98 |
| $581 | $111.96 | $126.03 | 0.25 | 0.1868 | -14.07 |
| $584 | $102.72 | $123.50 | 0.18 | 0.1868 | -20.78 |
| $586 | $90.12 | $121.82 | 0.29 | 0.1868 | -31.70 |
| $587 | $102.90 | $120.99 | 0.25 | 0.1868 | -18.09 |
| $588 | $107.07 | $120.15 | 0.28 | 0.1868 | -13.08 |
| $589 | $100.33 | $119.32 | 0.25 | 0.1868 | -18.99 |
| $591 | $107.99 | $117.67 | 0.29 | 0.1868 | -9.68 |
| $603 | $92.52 | $107.94 | 0.37 | 0.1868 | -15.42 |
| $609 | $101.01 | $103.22 | 0.30 | 0.1868 | -2.21 |
| $612 | $99.80 | $100.89 | 0.30 | 0.1868 | -1.09 |
| $613 | $93.75 | $100.12 | 0.26 | 0.1868 | -6.37 |
| $614 | $100.11 | $99.36 | 0.29 | 0.1868 | 0.75 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 19

Expires At: **18.09.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **120** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 305.000000 |     313.600000 |        180.949228 |        -11.731504 |        207.276284 |   1.000000 |      0.876652 | 0.999998 | 0.000000 | -0.057498 | 0.000072 |
| 345.000000 |     276.530000 |        178.019327 |        -14.287651 |        204.706278 |   0.999992 |      0.871518 | 0.999960 | 0.000001 | -0.065073 | 0.001150 |
| 435.000000 |     204.150000 |        160.419781 |        -30.293318 |        187.822070 |   0.999055 |      0.838132 | 0.996801 | 0.000075 | -0.083981 | 0.066886 |
| 390.000000 |     252.740000 |        156.811221 |        -35.126415 |        183.731307 |   0.999884 |      0.830817 | 0.999517 | 0.000013 | -0.073883 | 0.011866 |
| 365.000000 |     292.840000 |        141.709644 |        -50.724883 |        168.238899 |   0.999972 |      0.798271 | 0.999868 | 0.000004 | -0.068917 | 0.003539 |
| 445.000000 |     220.630000 |        133.951408 |        -56.552463 |        161.207268 |   0.998594 |      0.780429 | 0.995436 | 0.000103 | -0.086583 | 0.091975 |
| 370.000000 |     299.260000 |        130.289808 |        -62.193113 |        156.757493 |   0.999962 |      0.771890 | 0.999826 | 0.000005 | -0.069892 | 0.004583 |
| 475.000000 |     232.720000 |         91.937920 |        -96.863717 |        119.090070 |   0.995911 |      0.674245 | 0.988225 | 0.000237 | -0.095565 | 0.212007 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$305**

Market price: **$313.60**

Expected profit (USD): **180.95** [lowest: -11.73, highest: 207.28]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0575 (negative decay per day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **87.67%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $305 | $313.60 | $392.14 | 0.00 | 0.1868 | -78.54 |
| $345 | $276.53 | $354.14 | 0.00 | 0.1868 | -77.61 |
| $365 | $292.84 | $335.14 | 0.00 | 0.1868 | -42.30 |
| $370 | $299.26 | $330.39 | 0.00 | 0.1868 | -31.13 |
| $390 | $252.74 | $311.40 | 0.00 | 0.1868 | -58.66 |
| $435 | $204.15 | $268.75 | 0.19 | 0.1868 | -64.60 |
| $445 | $220.63 | $259.31 | 0.33 | 0.1868 | -38.68 |
| $475 | $232.72 | $231.16 | 0.43 | 0.1868 | 1.56 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 20

Expires At: **30.09.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **155** strikes prices..

Total of valuable options: 14

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 470.000000 |     208.780000 |        126.837682 |        -70.764751 |        155.842940 |   0.996208 |      0.753137 | 0.988755 | 0.000222 | -0.094025 | 0.208374 |
| 515.000000 |     177.250000 |        113.726508 |        -77.617403 |        143.057319 |   0.986129 |      0.720269 | 0.965071 | 0.000580 | -0.110721 | 0.544504 |
| 598.000000 |     105.100000 |        106.091325 |        -59.034670 |        135.905872 |   0.924247 |      0.692835 | 0.852251 | 0.001737 | -0.147078 | 1.629218 |
| 604.000000 |     101.000000 |        104.668344 |        -57.820997 |        134.469972 |   0.916668 |      0.687956 | 0.840110 | 0.001830 | -0.149381 | 1.716653 |
| 607.000000 |      98.560000 |        104.364259 |        -56.770948 |        134.159498 |   0.912702 |      0.686514 | 0.833849 | 0.001876 | -0.150490 | 1.760057 |
| 601.000000 |     106.840000 |        101.584151 |        -62.299999 |        131.327835 |   0.920516 |      0.680626 | 0.846245 | 0.001783 | -0.148243 | 1.673022 |
| 603.000000 |     107.740000 |         98.845662 |        -64.177198 |        128.562047 |   0.917964 |      0.673099 | 0.842169 | 0.001814 | -0.149005 | 1.702132 |
| 633.000000 |      77.860000 |        101.826264 |        -46.760428 |        131.471898 |   0.873352 |      0.672787 | 0.774661 | 0.002259 | -0.158641 | 2.118751 |
| 611.000000 |     100.190000 |         99.094328 |        -60.250939 |        128.829575 |   0.907229 |      0.671927 | 0.825309 | 0.001937 | -0.151920 | 1.817481 |
| 623.000000 |      89.860000 |         98.641812 |        -54.971682 |        128.325621 |   0.889540 |      0.667571 | 0.798420 | 0.002117 | -0.155844 | 1.985478 |
| 634.000000 |      82.850000 |         95.963756 |        -52.199961 |        125.514616 |   0.871661 |      0.657113 | 0.772222 | 0.002272 | -0.158895 | 2.131665 |
| 629.000000 |      89.660000 |         93.533004 |        -57.154269 |        123.129104 |   0.879984 |      0.652348 | 0.784304 | 0.002203 | -0.157578 | 2.066309 |
| 614.000000 |     105.690000 |         90.878977 |        -67.169361 |        120.497490 |   0.902985 |      0.649630 | 0.818762 | 0.001983 | -0.152955 | 1.860143 |
| 651.000000 |      70.760000 |         93.491134 |        -45.812133 |        122.825215 |   0.840984 |      0.644158 | 0.729207 | 0.002492 | -0.162436 | 2.337300 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$470**

Market price: **$208.78**

Expected profit (USD): **126.84** [lowest: -70.76, highest: 155.84]

Delta: 0.9888 (price sensitivity)

Gamma: 0.0002 (delta sensitivity)

Theta: $-0.0940 (negative decay per day)

Vega: $0.2084 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.62%**

Profit probability: **75.31%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $470 | $208.78 | $236.95 | 0.32 | 0.1868 | -28.17 |
| $515 | $177.25 | $195.68 | 0.33 | 0.1868 | -18.43 |
| $598 | $105.10 | $125.96 | 0.27 | 0.1868 | -20.86 |
| $601 | $106.84 | $123.68 | 0.28 | 0.1868 | -16.84 |
| $603 | $107.74 | $122.17 | 0.27 | 0.1868 | -14.43 |
| $604 | $101.00 | $121.42 | 0.27 | 0.1868 | -20.42 |
| $607 | $98.56 | $119.19 | 0.27 | 0.1868 | -20.63 |
| $611 | $100.19 | $116.24 | 0.26 | 0.1868 | -16.05 |
| $614 | $105.69 | $114.05 | 0.29 | 0.1868 | -8.36 |
| $623 | $89.86 | $107.62 | 0.26 | 0.1868 | -17.76 |
| $629 | $89.66 | $103.45 | 0.25 | 0.1868 | -13.79 |
| $633 | $77.86 | $100.73 | 0.23 | 0.1868 | -22.87 |
| $634 | $82.85 | $100.05 | 0.25 | 0.1868 | -17.20 |
| $651 | $70.76 | $88.98 | 0.24 | 0.1868 | -18.22 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 21

Expires At: **18.12.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **145** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 285.000000 |     353.650000 |        207.276235 |        -55.556963 |        246.152078 |   0.999999 |      0.850993 | 0.999993 | 0.000000 | -0.052771 | 0.000263 |
| 430.000000 |     231.240000 |        184.730660 |        -74.161700 |        224.811316 |   0.998294 |      0.811874 | 0.993642 | 0.000118 | -0.082579 | 0.143628 |
| 245.000000 |     422.000000 |        178.926224 |        -84.577604 |        217.136745 |   1.000000 |      0.801204 | 1.000000 | 0.000000 | -0.045359 | 0.000011 |
| 305.000000 |     365.000000 |        175.926276 |        -87.004066 |        214.691729 |   0.999996 |      0.795542 | 0.999972 | 0.000001 | -0.056489 | 0.000940 |
| 325.000000 |     346.060000 |        174.866439 |        -87.843267 |        213.816479 |   0.999986 |      0.793525 | 0.999911 | 0.000002 | -0.060235 | 0.002850 |
| 405.000000 |     275.150000 |        165.792233 |        -94.955938 |        205.430121 |   0.999305 |      0.775887 | 0.997114 | 0.000058 | -0.076486 | 0.070903 |
| 320.000000 |     362.810000 |        163.116377 |        -99.766852 |        201.905246 |   0.999989 |      0.770614 | 0.999933 | 0.000002 | -0.059294 | 0.002191 |
| 270.000000 |     414.310000 |        161.616227 |       -101.806924 |        199.905698 |   1.000000 |      0.767620 | 0.999998 | 0.000000 | -0.049989 | 0.000089 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$285**

Market price: **$353.65**

Expected profit (USD): **207.28** [lowest: -55.56, highest: 246.15]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0528 (negative decay per day)

Vega: $0.0003 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **85.10%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $245 | $422.00 | $453.31 | 0.00 | 0.1868 | -31.31 |
| $270 | $414.31 | $429.98 | 0.49 | 0.1868 | -15.67 |
| $285 | $353.65 | $415.99 | 0.00 | 0.1868 | -62.34 |
| $305 | $365.00 | $397.33 | 0.00 | 0.1868 | -32.33 |
| $320 | $362.81 | $383.33 | 0.48 | 0.1868 | -20.52 |
| $325 | $346.06 | $378.67 | 0.00 | 0.1868 | -32.61 |
| $405 | $275.15 | $304.14 | 0.46 | 0.1868 | -28.99 |
| $430 | $231.24 | $280.99 | 0.29 | 0.1868 | -49.75 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 22

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **199** strikes prices..

Total of valuable options: 15

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 215.000000 |     408.800000 |        236.929862 |        -48.263411 |        279.557329 |   1.000000 |      0.876720 | 1.000000 | 0.000000 | -0.039584 | 0.000001 |
| 205.000000 |     436.750000 |        218.979862 |        -66.484905 |        261.335868 |   1.000000 |      0.850020 | 1.000000 | 0.000000 | -0.037743 | 0.000000 |
| 270.000000 |     376.330000 |        214.399868 |        -70.473406 |        257.342939 |   0.999999 |      0.842763 | 0.999995 | 0.000000 | -0.049714 | 0.000179 |
| 320.000000 |     335.000000 |        205.730116 |        -78.668824 |        249.076002 |   0.999984 |      0.828554 | 0.999893 | 0.000003 | -0.058989 | 0.003532 |
| 375.000000 |     280.110000 |        205.625306 |        -77.589942 |        249.508784 |   0.999739 |      0.828370 | 0.998723 | 0.000027 | -0.069741 | 0.035128 |
| 285.000000 |     372.000000 |        203.729882 |        -81.093446 |        246.715844 |   0.999998 |      0.825191 | 0.999987 | 0.000000 | -0.052483 | 0.000491 |
| 305.000000 |     375.150000 |        180.579954 |       -104.249546 |        223.535643 |   0.999993 |      0.784103 | 0.999953 | 0.000001 | -0.056188 | 0.001607 |
| 240.000000 |     440.190000 |        180.539862 |       -104.958336 |        222.861974 |   1.000000 |      0.784029 | 1.000000 | 0.000000 | -0.044187 | 0.000017 |
| 275.000000 |     407.120000 |        178.609871 |       -106.560503 |        221.254119 |   0.999999 |      0.780435 | 0.999993 | 0.000000 | -0.050636 | 0.000254 |
| 435.000000 |     247.940000 |        177.855255 |       -101.610558 |        222.062546 |   0.997666 |      0.778901 | 0.991272 | 0.000150 | -0.083772 | 0.197349 |
| 365.000000 |     320.040000 |        175.693190 |       -108.128125 |        219.186898 |   0.999832 |      0.774953 | 0.999136 | 0.000019 | -0.067694 | 0.024547 |
| 455.000000 |     232.110000 |        173.749124 |       -103.135719 |        218.113990 |   0.995797 |      0.771035 | 0.985487 | 0.000233 | -0.089354 | 0.307017 |
| 335.000000 |     357.260000 |        168.470505 |       -116.066029 |        211.603252 |   0.999962 |      0.761174 | 0.999770 | 0.000005 | -0.061826 | 0.007195 |
| 295.000000 |     398.000000 |        167.729906 |       -117.335862 |        210.464321 |   0.999997 |      0.759744 | 0.999975 | 0.000001 | -0.054332 | 0.000907 |
| 380.000000 |     318.910000 |        161.826760 |       -121.631630 |        205.333069 |   0.999678 |      0.748217 | 0.998461 | 0.000032 | -0.070788 | 0.041666 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$215**

Market price: **$408.80**

Expected profit (USD): **236.93** [lowest: -48.26, highest: 279.56]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0396 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **87.67%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $205 | $436.75 | $491.69 | 0.00 | 0.1868 | -54.94 |
| $215 | $408.80 | $482.42 | 0.00 | 0.1868 | -73.62 |
| $240 | $440.19 | $459.22 | 0.00 | 0.1868 | -19.03 |
| $270 | $376.33 | $431.38 | 0.00 | 0.1868 | -55.05 |
| $275 | $407.12 | $426.74 | 0.00 | 0.1868 | -19.62 |
| $285 | $372.00 | $417.46 | 0.00 | 0.1868 | -45.46 |
| $295 | $398.00 | $408.18 | 0.56 | 0.1868 | -10.18 |
| $305 | $375.15 | $398.90 | 0.40 | 0.1868 | -23.75 |
| $320 | $335.00 | $384.99 | 0.00 | 0.1868 | -49.99 |
| $335 | $357.26 | $371.07 | 0.46 | 0.1868 | -13.81 |
| $365 | $320.04 | $343.26 | 0.44 | 0.1868 | -23.22 |
| $375 | $280.11 | $334.00 | 0.00 | 0.1868 | -53.89 |
| $380 | $318.91 | $329.37 | 0.49 | 0.1868 | -10.46 |
| $435 | $247.94 | $278.71 | 0.30 | 0.1868 | -30.77 |
| $455 | $232.11 | $260.51 | 0.33 | 0.1868 | -28.40 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 23

Expires At: **19.03.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **135** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 24

Expires At: **17.06.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **149** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 280.000000 |     408.660000 |        257.654838 |       -149.867609 |        326.493695 |   0.999990 |      0.810113 | 0.999908 | 0.000002 | -0.050062 | 0.003628 |
| 250.000000 |     448.320000 |        247.994704 |       -160.017931 |        316.451060 |   0.999999 |      0.796149 | 0.999983 | 0.000000 | -0.044662 | 0.000720 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$280**

Market price: **$408.66**

Expected profit (USD): **257.65** [lowest: -149.87, highest: 326.49]

Delta: 0.9999 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0501 (negative decay per day)

Vega: $0.0036 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **81.01%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $250 | $448.32 | $456.88 | 0.55 | 0.1868 | -8.56 |
| $280 | $408.66 | $429.87 | 0.47 | 0.1868 | -21.21 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 25

Expires At: **17.12.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **198** strikes prices..

Total of valuable options: 15

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 265.000000 |     348.500000 |        446.422255 |       -114.746925 |        554.206281 |   0.999983 |      0.916963 | 0.999800 | 0.000003 | -0.045730 | 0.008696 |
| 285.000000 |     353.090000 |        421.832816 |       -138.825647 |        529.577492 |   0.999957 |      0.896673 | 0.999540 | 0.000008 | -0.049273 | 0.018882 |
| 215.000000 |     423.440000 |        421.481976 |       -140.899178 |        528.540418 |   0.999999 |      0.896366 | 0.999986 | 0.000000 | -0.037039 | 0.000704 |
| 255.000000 |     395.000000 |        409.922126 |       -151.869365 |        517.258398 |   0.999990 |      0.885967 | 0.999874 | 0.000002 | -0.043978 | 0.005653 |
| 275.000000 |     375.700000 |        409.222469 |       -151.976682 |        516.739882 |   0.999973 |      0.885320 | 0.999692 | 0.000005 | -0.047494 | 0.012988 |
| 230.000000 |     439.500000 |        390.421997 |       -172.050430 |        497.323401 |   0.999998 |      0.867254 | 0.999966 | 0.000001 | -0.039632 | 0.001659 |
| 260.000000 |     415.800000 |        384.122182 |       -177.794375 |        491.253013 |   0.999987 |      0.860906 | 0.999840 | 0.000003 | -0.044853 | 0.007039 |
| 205.000000 |     476.000000 |        378.921971 |       -183.999679 |        485.464543 |   1.000000 |      0.855560 | 0.999993 | 0.000000 | -0.035313 | 0.000375 |
| 270.000000 |     413.990000 |        375.932349 |       -185.765029 |        483.078498 |   0.999979 |      0.852443 | 0.999751 | 0.000004 | -0.046611 | 0.010665 |
| 240.000000 |     444.970000 |        374.952028 |       -187.504231 |        481.797026 |   0.999996 |      0.851414 | 0.999940 | 0.000001 | -0.041366 | 0.002786 |
| 305.000000 |     382.910000 |        372.014197 |       -188.012639 |        479.467459 |   0.999898 |      0.848309 | 0.999042 | 0.000015 | -0.052889 | 0.037147 |
| 310.000000 |     378.050000 |        371.874761 |       -187.799615 |        479.375112 |   0.999876 |      0.848161 | 0.998864 | 0.000017 | -0.053807 | 0.043402 |
| 280.000000 |     418.760000 |        361.162623 |       -200.304508 |        468.265920 |   0.999966 |      0.836600 | 0.999622 | 0.000006 | -0.048382 | 0.015710 |
| 415.000000 |     289.000000 |        356.029587 |       -185.036552 |        464.381063 |   0.997080 |      0.830808 | 0.984028 | 0.000182 | -0.075187 | 0.458441 |
| 385.000000 |     325.990000 |        348.977102 |       -200.193965 |        456.983078 |   0.998605 |      0.822949 | 0.991307 | 0.000108 | -0.068621 | 0.270445 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$265**

Market price: **$348.50**

Expected profit (USD): **446.42** [lowest: -114.75, highest: 554.21]

Delta: 0.9998 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0457 (negative decay per day)

Vega: $0.0087 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **91.70%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $205 | $476.00 | $503.96 | 0.00 | 0.1868 | -27.96 |
| $215 | $423.44 | $495.28 | 0.00 | 0.1868 | -71.84 |
| $230 | $439.50 | $482.26 | 0.00 | 0.1868 | -42.76 |
| $240 | $444.97 | $473.58 | 0.00 | 0.1868 | -28.61 |
| $255 | $395.00 | $460.56 | 0.00 | 0.1868 | -65.56 |
| $260 | $415.80 | $456.23 | 0.32 | 0.1868 | -40.43 |
| $265 | $348.50 | $451.89 | 0.00 | 0.1868 | -103.39 |
| $270 | $413.99 | $447.55 | 0.44 | 0.1868 | -33.56 |
| $275 | $375.70 | $443.21 | 0.43 | 0.1868 | -67.51 |
| $280 | $418.76 | $438.87 | 0.51 | 0.1868 | -20.11 |
| $285 | $353.09 | $434.54 | 0.26 | 0.1868 | -81.45 |
| $305 | $382.91 | $417.20 | 0.43 | 0.1868 | -34.29 |
| $310 | $378.05 | $412.87 | 0.43 | 0.1868 | -34.82 |
| $385 | $325.99 | $348.30 | 0.43 | 0.1868 | -22.31 |
| $415 | $289.00 | $322.87 | 0.38 | 0.1868 | -33.87 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 26

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **192** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 255.000000 |     417.830000 |        410.325547 |       -182.277610 |        525.749979 |   0.999988 |      0.869112 | 0.999841 | 0.000003 | -0.043685 | 0.007180 |
| 240.000000 |     445.030000 |        398.125425 |       -194.973991 |        513.282377 |   0.999995 |      0.857174 | 0.999923 | 0.000001 | -0.041086 | 0.003640 |
|  60.000000 |     627.360000 |        395.795345 |       -199.363629 |        509.167711 |   1.000000 |      0.854838 | 1.000000 | 0.000000 | -0.010263 | 0.000000 |
| 330.000000 |     358.770000 |        394.392703 |       -193.356869 |        510.394375 |   0.999713 |      0.853416 | 0.997583 | 0.000034 | -0.057214 | 0.088439 |
| 335.000000 |     360.270000 |        387.894266 |       -199.285128 |        503.883922 |   0.999661 |      0.846778 | 0.997216 | 0.000038 | -0.058168 | 0.100472 |
| 250.000000 |     448.730000 |        384.425495 |       -208.569301 |        499.547365 |   0.999991 |      0.843191 | 0.999874 | 0.000002 | -0.042817 | 0.005773 |
| 465.000000 |     248.300000 |        370.230483 |       -178.654392 |        487.225349 |   0.991866 |      0.827689 | 0.962225 | 0.000366 | -0.086016 | 0.966310 |
| 435.000000 |     282.590000 |        365.753502 |       -196.225251 |        482.461446 |   0.995410 |      0.823007 | 0.976120 | 0.000250 | -0.079171 | 0.660716 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$255**

Market price: **$417.83**

Expected profit (USD): **410.33** [lowest: -182.28, highest: 525.75]

Delta: 0.9998 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0437 (negative decay per day)

Vega: $0.0072 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **86.91%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $60 | $627.36 | $630.20 | 0.87 | 0.1868 | -2.84 |
| $240 | $445.03 | $475.02 | 0.00 | 0.1868 | -29.99 |
| $250 | $448.73 | $466.41 | 0.52 | 0.1868 | -17.68 |
| $255 | $417.83 | $462.10 | 0.49 | 0.1868 | -44.27 |
| $330 | $358.77 | $397.58 | 0.41 | 0.1868 | -38.81 |
| $335 | $360.27 | $393.29 | 0.40 | 0.1868 | -33.02 |
| $435 | $282.59 | $308.90 | 0.39 | 0.1868 | -26.31 |
| $465 | $248.30 | $284.49 | 0.34 | 0.1868 | -36.19 |

### 6. Backtest Stock Option Strategies

- **Backtesting Setup**: Look Back **Interval 252 Days**. **1508 Historical Prices** (2020-01-01 - 2026-01-02)

- Average modal profit prediction error (actual price - predicted price): **0.0327**

- Modal profit prediction correlation: **0.3436**

- Backtests total: **18**

- Profitable Trades (profitable trades / total trades): **44.44%**

--------------------------------------------------

### Calculate Stock Option Nr. 27

Expires At: **16.06.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.1560 [-0.1081, 0.1913]**

- Stock Volatility: **0.1868 [0.1623, 0.2131]**

- Based on **1507** observations


- Garch Volatility forecast: **0.1607**

### 2. Validate Stock Option Contracts

- Analyze **146** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

