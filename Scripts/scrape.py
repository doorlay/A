# Imports TimeSeries function which gets real time data
from alpha_vantage.timeseries import TimeSeries
# Imports json, to parse the api output
import json

# This first function creates an array from the database of purchased stocks.
# This function will be imported to the 'sell.py' file within the Scripts folder.
def scr():
	database1 = open("Database/database.txt")
	database2 = database1.read()
	DBarray = database2.splitlines()
	return DBarray


# This will handle gathering the stock data from the internet.

# Assigns ts to an api call that uses the user's api key
ts = TimeSeries(key='52UIN9CWN6RNDHXJ')

# Assings data to the json output from the api call
data = ts.get_intraday(symbol='MSFT', outputsize='compact')

# Creates jsonParsed, a dictionary, from the parsed json data
jsonParsed = json.loads(data)

# prints data to test out the corresponding parts the dictionary needs
print(data)

# The info will then be sent through the other files to be analyzed.

# below is a psuedo-code example of how I want my data fetching function to run.
# This function will be imported to both the sell.py file and the buy.py file, in order to fetch real time prices on command.

# parameter accepted will be the stock symbol 
def getDataFrom(nameofstock):
	
	# will create a list containing the below info
	data = [stockSymbol, purchasePrice, purchaseDate]
	# returns the data
	return data
