## MODEL VS MARKET COMPARISON

**Data Source**: Apple Stock Options and Past 3 Years Stock Prices (close price for each day)

| Strike | Market | BS_Price | IV   | Model_Vol | Diff   |
| ------ | ------ | -------- | ---- | --------- | ------ |
| 50     | 207.30 | 207.76   | 0.75 | 0.2907    | -0.46  |
| 80     | 181.15 | 181.07   | 0.62 | 0.2907    | 0.08   |
| 110    | 151.34 | 154.70   | 0.54 | 0.2907    | -3.36  |
| 120    | 147.67 | 146.10   | 0.51 | 0.2907    | 1.57   |
| 135    | 134.52 | 133.49   | 0.50 | 0.2907    | 1.03   |
| 150    | 122.00 | 121.35   | 0.46 | 0.2907    | 0.65   |
| 155    | 114.07 | 117.43   | 0.45 | 0.2907    | -3.36  |
| 160    | 113.19 | 113.57   | 0.44 | 0.2907    | -0.38  |
| 170    | 105.14 | 106.07   | 0.42 | 0.2907    | -0.93  |
| 175    | 85.11  | 102.44   | 0.41 | 0.2907    | -17.33 |

### Column Explanations:

**Strike** - The strike price of the call option (the price at which you can buy the stock if you exercise the option)

**Market** - The actual market price (premium) that traders are currently paying for this option

**BS_Price** - The theoretical fair value calculated by your Black-Scholes model using your estimated volatility (0.2907 or ~29%)

**IV** - Implied Volatility from the market price. This is the volatility that, when plugged into Black-Scholes, would produce the current market price

**Model_Vol** - Your model's estimated volatility (0.2907 for all options, derived from historical stock price movements)

**Diff** - The difference between Market price and BS_Price (Market - BS_Price)

### What it Means:

**Volatility Smile/Skew**: Notice how the Implied Volatility (IV) varies significantly across strikes (0.41 to 0.75), but your model uses a constant 0.2907. This creates pricing discrepancies.

**Deep ITM Options (strikes 50-80)**: Very high IV (~0.62-0.75) suggests these options are expensive relative to your model, possibly due to early exercise premiums or liquidity issues.

**ATM/Near-the-Money (around current stock price)**: More reasonable IV (~0.44-0.51), closer to your model's volatility.

**Large Discrepancies**: The -17.33 difference at strike 175 suggests either:

    Your model significantly overvalues this option, or
    The market price is stale/illiquid

### Implications:

**Positive Diff values**: Market is more expensive than your model predicts

**Negative Diff values**: **Model thinks the option should be worth more** than the market price

**Large negative diffs**: Indicate potential buying opportunities (if you trust your model)

**Large positive diffs**: Suggest overpriced options to avoid or potentially sell

#### NOTE:

The best stocks to use this on are those **WITHOUT** upcoming events like: earning reports, negative company news
or anything else what can affects the stock price directly
