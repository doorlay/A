# This file will handle all of the scraping of the program. 

# This first function creates an array from the database of purchased stocks.
# This function will be imported to the 'sell.py' file within the Scripts folder.
def scr():
	database1 = open(Database/database.txt)
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
