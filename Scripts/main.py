# getData function returns stock symbol, current price, and and current date in a list.
from scrape import getData

stockdata = getData('AMD')
print(stockdata)
