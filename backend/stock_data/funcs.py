# Imports TimeSeries function which gets real time data
from alpha_vantage.timeseries import TimeSeries

# Imports module to get current date
import datetime

# Imports json, to parse the api output
import json

# Function to return the current date
# none -> 
def getDate():
	currentDT = datetime.datetime.now()
	# outputs the date in format of month/day/year
	currentDate = currentDT.strftime("%m/%d/%Y")
	return currentDate

# This function will be imported to sell.py, as it scrapes the database for all purchased stocks.
def scr():
	database1 = open("database.txt")
	database2 = database1.read()
	DBarray = database2.splitlines()
	# Returns an array of all purchased stocks from the database.txt file
	return DBarray


# Quick note, the price seems to have 0% error on NYSE traded, but 0.08% error on NASDAQ. Weird.
def getPrice(stock):
	# Enter your personal api key here! Required to make api calls
	ts = TimeSeries(key='52UIN9CWN6RNDHXJ')
	
	# Entire json output is assigned to 'data'
	data = ts.get_intraday(symbol=stock, outputsize='compact', interval = '1min')
	
	# The following three assignments isolate the most current price of the specific stock
	dataone = data[0]
	datatwo = list(dataone.items())[0]
	datathree = datatwo[1]
	
	# Gets just the current price of the stock, assigns it to 'datafour', returns to user
	datafour = datathree['1. open']
	return datafour

# Enter the stock with 'quotes' around it.
def getData(stock):
	price = getPrice(stock)
	date = getDate()
	stockData = [stock, price, date]
	return stockData
