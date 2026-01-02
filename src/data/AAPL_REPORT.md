# AAPL Option Analysis From: 02.01.2026 07:01 UTC

> Calculates & Filters best stock option contracts based on profitability chance and estimated profit on expiry. **NOTE: Assumes Options Are Bought NOT Sold On Expiration**

## Current Stock Price: $271.8599853515625

[SKIPPED]: stock option contract already expired

### Calculate Stock Option Nr. 2

Expires At: **09.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **54** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 3

Expires At: **16.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **89** strikes prices..

Total of valuable options: 4

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 45.000000 |     197.130000 |         32.947510 |         24.750225 |         31.302983 |   1.000000 |      0.990416 | 1.000000 | 0.000000 | -0.008906 | 0.000000 |
| 70.000000 |     180.480000 |         24.597510 |         16.567871 |         23.120629 |   1.000000 |      0.955610 | 1.000000 | 0.000000 | -0.013853 | 0.000000 |
| 35.000000 |     221.720000 |         18.357510 |          9.880203 |         16.432961 |   1.000000 |      0.891972 | 1.000000 | 0.000000 | -0.006927 | 0.000000 |
| 40.000000 |     223.280000 |         11.797510 |          3.301708 |          9.854466 |   1.000000 |      0.776511 | 1.000000 | 0.000000 | -0.007916 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$45**

Market price: **$197.13**

Expected profit (USD): **32.95** [lowest: 24.75, highest: 31.30]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0089 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **99.04%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $35 | $221.72 | $236.95 | 0.00 | 0.2905 | -15.23 |
| $40 | $223.28 | $231.96 | 7.22 | 0.2905 | -8.68 |
| $45 | $197.13 | $226.98 | 0.00 | 0.2905 | -29.85 |
| $70 | $180.48 | $202.04 | 4.75 | 0.2905 | -21.56 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 4

Expires At: **23.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **34** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 5

Expires At: **30.01.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **37** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 6

Expires At: **06.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **22** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 7

Expires At: **20.02.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **64** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 8

Expires At: **20.03.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **63** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 95.000000 |     118.290000 |         80.536066 |         43.271707 |         82.251722 |   1.000000 |      0.968017 | 1.000000 | 0.000000 | -0.018567 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$95**

Market price: **$118.29**

Expected profit (USD): **80.54** [lowest: 43.27, highest: 82.25]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0186 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **96.80%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $95 | $118.29 | $178.28 | 0.00 | 0.2905 | -59.99 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 9

Expires At: **17.04.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **57** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 125.000000 |     130.760000 |         46.803175 |         -4.112330 |         49.661630 |   0.999997 |      0.755238 | 0.999990 | 0.000001 | -0.024305 | 0.000077 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$125**

Market price: **$130.76**

Expected profit (USD): **46.80** [lowest: -4.11, highest: 49.66]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0243 (negative decay per day)

Vega: $0.0001 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **75.52%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $125 | $130.76 | $149.41 | 0.00 | 0.2905 | -18.65 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 10

Expires At: **15.05.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **75** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 70.000000 |     179.250000 |         62.309619 |         -2.884766 |         65.936494 |   1.000000 |      0.790156 | 1.000000 | 0.000000 | -0.013530 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$70**

Market price: **$179.25**

Expected profit (USD): **62.31** [lowest: -2.88, highest: 65.94]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0135 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **79.02%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $70 | $179.25 | $203.67 | 1.66 | 0.2905 | -24.42 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 11

Expires At: **18.06.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **80** strikes prices..

Total of valuable options: 7

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 10.000000 |     160.950000 |        151.893678 |         70.098706 |        157.550423 |   1.000000 |      0.989701 | 1.000000 | 0.000000 | -0.001920 | 0.000000 |
| 40.000000 |     157.250000 |        125.593678 |         43.832886 |        131.284603 |   1.000000 |      0.959190 | 1.000000 | 0.000000 | -0.007679 | 0.000000 |
| 20.000000 |     178.500000 |        124.343678 |         42.320838 |        129.772555 |   1.000000 |      0.956921 | 1.000000 | 0.000000 | -0.003840 | 0.000000 |
| 15.000000 |     195.150000 |        112.693678 |         30.462592 |        117.914309 |   1.000000 |      0.931521 | 1.000000 | 0.000000 | -0.002880 | 0.000000 |
| 25.000000 |     185.350000 |        112.493678 |         30.383489 |        117.835206 |   1.000000 |      0.931016 | 1.000000 | 0.000000 | -0.004800 | 0.000000 |
| 30.000000 |     198.120000 |         94.723678 |         12.445499 |         99.897217 |   1.000000 |      0.876568 | 1.000000 | 0.000000 | -0.005760 | 0.000000 |
| 45.000000 |     209.450000 |         68.393678 |        -14.023500 |         73.428217 |   1.000000 |      0.764122 | 1.000000 | 0.000000 | -0.008639 | 0.000000 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$10**

Market price: **$160.95**

Expected profit (USD): **151.89** [lowest: 70.10, highest: 157.55]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0019 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **98.97%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $10 | $160.95 | $262.18 | 0.00 | 0.2905 | -101.23 |
| $15 | $195.15 | $257.35 | 0.00 | 0.2905 | -62.20 |
| $20 | $178.50 | $252.51 | 0.00 | 0.2905 | -74.01 |
| $25 | $185.35 | $247.67 | 0.00 | 0.2905 | -62.32 |
| $30 | $198.12 | $242.83 | 0.00 | 0.2905 | -44.71 |
| $40 | $157.25 | $233.16 | 0.00 | 0.2905 | -75.91 |
| $45 | $209.45 | $228.32 | 0.00 | 0.2905 | -18.87 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 12

Expires At: **17.07.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **43** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 13

Expires At: **21.08.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **58** strikes prices..

Total of valuable options: 2

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 115.000000 |     118.750000 |        111.454387 |         -2.217775 |        121.412489 |   0.999815 |      0.849339 | 0.999317 | 0.000029 | -0.022175 | 0.006154 |
| 130.000000 |     131.020000 |         84.190964 |        -29.514891 |         93.981142 |   0.999178 |      0.746157 | 0.997354 | 0.000101 | -0.025919 | 0.021218 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$115**

Market price: **$118.75**

Expected profit (USD): **111.45** [lowest: -2.22, highest: 121.41]

Delta: 0.9993 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0222 (negative decay per day)

Vega: $0.0062 (volatility sensitivity per 1%)

ITM (In The Money) probability: **99.98%**

Profit probability: **84.93%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $115 | $118.75 | $162.00 | 0.00 | 0.2905 | -43.25 |
| $130 | $131.02 | $147.69 | 0.88 | 0.2905 | -16.67 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 14

Expires At: **18.09.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **79** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|     strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|-----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
|  65.000000 |     164.780000 |        125.685151 |         -3.168850 |        136.854200 |   1.000000 |      0.861288 | 0.999999 | 0.000000 | -0.012254 | 0.000008 |
| 115.000000 |     117.500000 |        122.967805 |         -5.201474 |        134.738032 |   0.999692 |      0.852888 | 0.998847 | 0.000045 | -0.022248 | 0.010557 |
|  85.000000 |     158.770000 |        111.695181 |        -17.075713 |        122.945611 |   0.999994 |      0.815713 | 0.999969 | 0.000002 | -0.016043 | 0.000360 |
|  50.000000 |     213.000000 |         92.465151 |        -37.017934 |        103.005144 |   1.000000 |      0.745022 | 1.000000 | 0.000000 | -0.009426 | 0.000000 |
| 110.000000 |     154.150000 |         91.316604 |        -37.364169 |        102.608990 |   0.999818 |      0.740569 | 0.999285 | 0.000029 | -0.021105 | 0.006803 |
|  60.000000 |     204.300000 |         91.165151 |        -38.206624 |        101.816448 |   1.000000 |      0.739986 | 1.000000 | 0.000000 | -0.011311 | 0.000002 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$65**

Market price: **$164.78**

Expected profit (USD): **125.69** [lowest: -3.17, highest: 136.85]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0123 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **86.13%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $50 | $213.00 | $224.36 | 1.58 | 0.2905 | -11.36 |
| $60 | $204.30 | $214.85 | 1.43 | 0.2905 | -10.55 |
| $65 | $164.78 | $210.10 | 0.00 | 0.2905 | -45.32 |
| $85 | $158.77 | $191.10 | 0.00 | 0.2905 | -32.33 |
| $110 | $154.15 | $167.36 | 0.96 | 0.2905 | -13.21 |
| $115 | $117.50 | $162.61 | 0.00 | 0.2905 | -45.11 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 15

Expires At: **18.12.2026**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **85** strikes prices..

Total of valuable options: 8

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 15.000000 |     186.060000 |        189.908535 |         11.882528 |        207.407223 |   1.000000 |      0.926769 | 1.000000 | 0.000000 | -0.002777 | 0.000000 |
| 45.000000 |     156.530000 |        189.438535 |         11.785744 |        207.310433 |   1.000000 |      0.925890 | 1.000000 | 0.000000 | -0.008331 | 0.000001 |
| 40.000000 |     161.680000 |        189.288535 |         11.567602 |        207.092296 |   1.000000 |      0.925608 | 1.000000 | 0.000000 | -0.007406 | 0.000000 |
| 25.000000 |     184.650000 |        181.318535 |          3.310655 |        198.835350 |   1.000000 |      0.909761 | 1.000000 | 0.000000 | -0.004628 | 0.000000 |
| 30.000000 |     199.100000 |        161.868535 |        -16.322543 |        179.202152 |   1.000000 |      0.864318 | 1.000000 | 0.000000 | -0.005554 | 0.000000 |
| 10.000000 |     245.230000 |        135.738535 |        -43.053946 |        152.470749 |   1.000000 |      0.790589 | 1.000000 | 0.000000 | -0.001851 | 0.000000 |
| 20.000000 |     240.800000 |        130.168535 |        -48.567637 |        146.957058 |   1.000000 |      0.773433 | 1.000000 | 0.000000 | -0.003703 | 0.000000 |
| 70.000000 |     203.000000 |        117.968554 |        -60.275927 |        135.246251 |   0.999996 |      0.734606 | 0.999973 | 0.000001 | -0.012974 | 0.000363 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$15**

Market price: **$186.06**

Expected profit (USD): **189.91** [lowest: 11.88, highest: 207.41]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0028 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **92.68%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $10 | $245.23 | $262.53 | 0.00 | 0.2905 | -17.30 |
| $15 | $186.06 | $257.86 | 0.00 | 0.2905 | -71.80 |
| $20 | $240.80 | $253.20 | 2.17 | 0.2905 | -12.40 |
| $25 | $184.65 | $248.53 | 0.00 | 0.2905 | -63.88 |
| $30 | $199.10 | $243.87 | 0.00 | 0.2905 | -44.77 |
| $40 | $161.68 | $234.54 | 0.00 | 0.2905 | -72.86 |
| $45 | $156.53 | $229.87 | 0.00 | 0.2905 | -73.34 |
| $70 | $203.00 | $206.54 | 1.51 | 0.2905 | -3.54 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 16

Expires At: **15.01.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **72** strikes prices..

Total of valuable options: 6

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 25.000000 |     172.100000 |        205.489313 |         12.057158 |        225.442534 |   1.000000 |      0.932583 | 1.000000 | 0.000000 | -0.004603 | 0.000000 |
| 35.000000 |     165.980000 |        201.609313 |          8.255274 |        221.640650 |   1.000000 |      0.925743 | 1.000000 | 0.000000 | -0.006444 | 0.000000 |
| 30.000000 |     192.400000 |        180.189313 |        -13.502154 |        199.883222 |   1.000000 |      0.881471 | 1.000000 | 0.000000 | -0.005523 | 0.000000 |
| 80.000000 |     172.800000 |        149.789509 |        -43.623339 |        169.740149 |   0.999969 |      0.802417 | 0.999817 | 0.000007 | -0.014815 | 0.002314 |
| 45.000000 |     213.400000 |        144.189313 |        -49.774960 |        163.610397 |   1.000000 |      0.786253 | 1.000000 | 0.000000 | -0.008285 | 0.000004 |
| 60.000000 |     203.250000 |        139.339318 |        -54.492219 |        158.892310 |   0.999999 |      0.771948 | 0.999992 | 0.000000 | -0.011051 | 0.000122 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$25**

Market price: **$172.10**

Expected profit (USD): **205.49** [lowest: 12.06, highest: 225.44]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0046 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **93.26%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $25 | $172.10 | $248.66 | 0.00 | 0.2905 | -76.56 |
| $30 | $192.40 | $244.02 | 0.00 | 0.2905 | -51.62 |
| $35 | $165.98 | $239.38 | 0.00 | 0.2905 | -73.40 |
| $45 | $213.40 | $230.10 | 0.61 | 0.2905 | -16.70 |
| $60 | $203.25 | $216.18 | 1.22 | 0.2905 | -12.93 |
| $80 | $172.80 | $197.63 | 0.98 | 0.2905 | -24.83 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 17

Expires At: **17.06.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **68** strikes prices..

Total of valuable options: 5

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 70.000000 |     116.000000 |        286.457533 |          3.565777 |        321.953366 |   0.999958 |      0.945605 | 0.999679 | 0.000009 | -0.012622 | 0.004644 |
| 90.000000 |     124.800000 |        257.660680 |        -24.892954 |        293.053525 |   0.999642 |      0.901638 | 0.997921 | 0.000053 | -0.016719 | 0.025887 |
| 75.000000 |     143.000000 |        254.457827 |        -28.714662 |        289.616470 |   0.999922 |      0.895951 | 0.999449 | 0.000016 | -0.013591 | 0.007668 |
| 65.000000 |     193.000000 |        214.457379 |        -69.456941 |        248.965818 |   0.999979 |      0.813997 | 0.999825 | 0.000005 | -0.011678 | 0.002642 |
| 80.000000 |     184.620000 |        207.838352 |        -75.787277 |        242.457985 |   0.999864 |      0.798888 | 0.999103 | 0.000024 | -0.014592 | 0.012010 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$70**

Market price: **$116.00**

Expected profit (USD): **286.46** [lowest: 3.57, highest: 321.95]

Delta: 0.9997 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0126 (negative decay per day)

Vega: $0.0046 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **94.56%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $65 | $193.00 | $213.35 | 0.62 | 0.2905 | -20.35 |
| $70 | $116.00 | $208.85 | 0.00 | 0.2905 | -92.85 |
| $75 | $143.00 | $204.35 | 0.00 | 0.2905 | -61.35 |
| $80 | $184.62 | $199.86 | 0.90 | 0.2905 | -15.24 |
| $90 | $124.80 | $190.88 | 0.00 | 0.2905 | -66.08 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 18

Expires At: **17.12.2027**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **93** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

### Calculate Stock Option Nr. 19

Expires At: **21.01.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **64** strikes prices..

Total of valuable options: 1

### 3. Stock Option Contract Analysis

- **Top 20 Valuable Option Strikes**

|    strike |   market_price |   expected_profit |   profit_ci_lower |   profit_ci_upper |   prob_ITM |   prob_profit |    delta |    gamma |     theta |     vega |
|----------:|---------------:|------------------:|------------------:|------------------:|-----------:|--------------:|---------:|---------:|----------:|---------:|
| 25.000000 |     247.400000 |        321.029508 |       -110.314135 |        384.473629 |   1.000000 |      0.820422 | 1.000000 | 0.000000 | -0.004276 | 0.000011 |

### 4. Option Call (Buy): Risk Assessment

Best strike price: **$25**

Market price: **$247.40**

Expected profit (USD): **321.03** [lowest: -110.31, highest: 384.47]

Delta: 1.0000 (price sensitivity)

Gamma: 0.0000 (delta sensitivity)

Theta: $-0.0043 (negative decay per day)

Vega: $0.0000 (volatility sensitivity per 1%)

ITM (In The Money) probability: **100.00%**

Profit probability: **82.04%**

### 5. Model VS Market Comparison

| Strike Price | Market Price | Model Biased Market Price | Market Implied Volatility | Model Volatility | Market Price - Model Price USD |
|--------|--------|----------|----|-----------|----- |
| $25 | $247.40 | $250.31 | 2.06 | 0.2905 | -2.91 |

### 6. Backtest Stock Option Strategies

- Average model prediction error: **0.0871**

- Model prediction correlation: **0.2150**

- Run backtests total: **11**

- Model Win Rate: **63.64%**

--------------------------------------------------

### Calculate Stock Option Nr. 20

Expires At: **17.03.2028**

### 1. Black-School Analysis

- Stock Price Drift: **0.2633 [-0.1665, 0.2991]**

- Stock Volatility: **0.2905 [0.2524, 0.3314]**

- Based on **1507** observations


- Garch Volatility forecast: **0.2571**

### 2. Validate Stock Option Contracts

- Analyze **56** strikes prices..

**No valuable option strikes found**

--------------------------------------------------

