from pandas_datareader import data
from collections import OrderedDict
from datetime import date, timedelta
from IPython import embed

# COMPILE REQUEST PARAMS

symbols = ['AAPL', 'MSFT']
data_source = 'google'
start = str(date.today() - timedelta(days=15))
end = str(date.today())

# ISSUE REQUEST

response = data.DataReader(symbols, data_source, start, end)

# PARSE RESPONSE

daily_closing_prices = response.ix["Close"]

daily_closing_prices = daily_closing_prices.to_dict('index')

daily_closing_prices = OrderedDict(sorted(daily_closing_prices.items(), reverse=True)) # h/t https://stackoverflow.com/a/15743140/670433

print("---------------------------------------")
print("DAILY STOCK PRICES:")
print("---------------------------------------")
print("")
print("date       | Apple (AAPL)     | Microsoft (MSFT)")
print("---------- | ---------------- | -----------------")


for beginning_of_day in daily_closing_prices:
    symbol_prices = daily_closing_prices[beginning_of_day]
    date = str(beginning_of_day.date())
    aapl_usd = '${0:.2f}'.format(symbol_prices["AAPL"])
    msft_usd = '${0:.2f}'.format(symbol_prices["MSFT"])
    print(date, "|", aapl_usd, "         |", msft_usd)
