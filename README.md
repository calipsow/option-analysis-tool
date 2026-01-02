## Estimate Stock Option Profitability

Tries to predict which stock options are valuable by looking at previous price movement over a long period of time to predict if the price at expiration is profitable for the given strike price.

### Setup

the setup uses real stock data from yahoo finance using the yfinance lib.

### Workflow

- Loads the last 3 years of prices (close price for each day) and currently pending stock options incl. their expiration date
- Data cleanup and validation
- Analyses the past stock prices over time by looking at **stock price volatility**, **usual price change differences**, **price drift or trend takes till turn** and more. [MORE HERE](../../../README.md)
- Reading in the stock options and apply the pasts stock change patterns to the latest stock price and estimate the stock price at stock option expiration and subtracting it from the total invest: **estimated stock price at expiry - (premium + strike price)**
- not profitable stock options will be filtered out, and profitable ones saved as csv in data

### TODO:

- further validation for prediction accuracy. **required accuracy: > 60%**
