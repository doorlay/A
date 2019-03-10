# Imports TimeSeries function which gets real time data
from alpha_vantage.timeseries import TimeSeries

# Imports json, to parse the api output
import json

# This function will be imported to the 'sell.py' file within the Scripts folder.
def scr():
	database1 = open("Database/database.txt")
	database2 = database1.read()
	DBarray = database2.splitlines()
	# Returns an array of all purchased stocks from the database.txt file
	return DBarray

def getPrice(stock):
	# Enter your personal api key here! Required to make api calls
	ts = TimeSeries(key='52UIN9CWN6RNDHXJ')
	
	# Entire json output is assigned to 'data'
	data = ts.get_intraday(symbol=stock, outputsize='compact', interval = '1min')
	
	# The following three assignments isolate the most current info on the specific stock
	dataone = data[0]
	datatwo = list(dataone.items())[0]
	datathree = datatwo[1]
	
	# Gets just the current price of the stock, assigns it to 'datafour', returns to user
	datafour = datathree['1. open']
	return datafour


# Parameters must be entered within the quotes. I'll figure out a way around this soon.
getPrice('MSFT')

# parameter accepted will be the stock symbol 
'''def getDataFrom(nameofstock):
	
	# will create a list containing the below info
	data = [stockSymbol, currentPrice, currentData]
	# returns the data
	return data '''
