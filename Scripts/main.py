# getData function returns stock symbol, current price, and and current date in a list.
from scrape import getData

# Currently getting data for Microsoft, but can scrape for any symbol. Just make sure to enter in quotes!
stockdata = getData('MSFT')
print(stockdata)
