# This file will handle all of the scraping of the program. 

# This first function creates an array from the database of purchased stocks.
# This function will be imported to the 'sell.py' file within the Scripts folder.
def scr():
	database1 = open("Database/database.txt")
	database2 = database1.read()
	DBarray = database2.splitlines()
	return DBarray


# This will handle gathering the stock data from the internet.

from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='52UIN9CWN6RNDHXJ', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))

# The info will then be sent through the other files to be analyzed.

# below is a psuedo-code example of how I want my data fetching function to run.
# This function will be imported to both the sell.py file and the buy.py file, in order to fetch real time prices on command.

# parameter accepted will be the stock symbol 
function getDataFrom(nameofstock):
	
	# will create a list containing the below info
	data = [stockSymbol, purchasePrice, purchaseDate]
	# returns the data
	return data
