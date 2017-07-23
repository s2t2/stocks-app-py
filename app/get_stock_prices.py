from pandas_datareader import data
from IPython import embed

# COMPILE REQUEST PARAMS

symbols = ['AAPL', 'MSFT']
data_source = 'google'
start = '2017-01-01'
end = '2017-12-31'

# ISSUE REQUEST

response = data.DataReader(symbols, data_source, start, end)

# PARSE RESPONSE

daily_closing_prices = response.ix["Close"]

daily_closing_prices = daily_closing_prices.to_dict('index')

print("---------------------------------------")
print("DAILY STOCK PRICES:")
print("---------------------------------------")
for beginning_of_day in daily_closing_prices:
    symbol_prices = daily_closing_prices[beginning_of_day]
    date = str(beginning_of_day.date())
    print(" + ", date, symbol_prices)
