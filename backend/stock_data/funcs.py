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

# This function gets a list of all stock symbols in the database
def getSymbolsDatabase():
    dataList = scr()
    symbols = []
    # I'm going to try and do a flag while loop here
    flag = False
    initial = 0
    while not flag:
        lastIndex = len(dataList) - 1
        symbols.append(dataList[initial])
        if initial == lastIndex - 2:
            flag = True
            break
        initial = initial + 3
    return symbols

# This function gets a list of all prices in the database
def getPricesDatabase():
    dataList = scr()
    prices = []
    # I'm going to try and do a flag while loop here
    flag = False
    initial = 1
    while not flag:
        lastIndex = len(dataList) - 1
        prices.append(dataList[initial])
        if initial == lastIndex - 1:
            flag = True
            break
        initial = initial + 3
    return prices

# This function gets a list of all dates in the database 
def getDatesDatabase():
    dataList = scr()
    dates = []
    # I'm going to try and do a flag while loop here
    flag = False
    initial = 2
    while not flag:
        lastIndex = len(dataList) - 1
        dates.append(dataList[initial])
        if initial == lastIndex:
            flag = True
            break
        initial = initial + 3
    return dates
    

def review():
    symbols = getSymbolsDatabase()
    numberOfStocks = len(symbols)
    prices = getPricesDatabase()
    newPrices = []
    for price in prices:
        newPrices.append(float(price))
    totalPrice = sum(newPrices)
    dates = getDatesDatabase()
    print("You have purchased {} stocks, for an initial investment of ${}  \n" .format(numberOfStocks, totalPrice))
    initial = 0
    for stock in symbols:
        print("{} for ${} on {} \n".format(stock, prices[initial], dates[initial]))
        initial = initial + 1

def returnReview():
    prices = getPricesDatabase()
    newPrices = []
    for price in prices:
        newPrices.append(float(price))
    totalPrice = sum(newPrices)
    return totalPrice
    

def current():
    print("Checking current prices...\n")
    # Make sure to enter data in quotes
    stockSymbols = getSymbolsDatabase()
    totalPrice = []
    # Loops through all stocks, printing out their current prices
    for stock in stockSymbols:
        price = getData(stock)
        converted = float(price[1])
        totalPrice.append(converted)
        print("{} is valued at ${} \n" .format(stock, price[1]))
    newTotalPrice = sum(totalPrice)
    print("Your portfolio is currently valued at ${}" .format(round(newTotalPrice, 2)))


# This function will return the current portfolio value
def returnCurrent():
    stockSymbols = getSymbolsDatabase()
    totalPrice = []
    # Loops through all stocks, printing out their current prices
    for stock in stockSymbols:
        price = getData(stock)
        converted = float(price[1])
        totalPrice.append(converted)
    newTotalPrice = sum(totalPrice)
    return round(newTotalPrice,2)

    # I can tell this is going to be the hardest function here to write. yikes
def compareTotal():
    symbols = getSymbolsDatabase()
    prices = getPricesDatabase()
    dates = getDatesDatabase()
    # This var is the current value of portfolio
    totalCurrentValue = returnCurrent()
    # This var is initial amount invested
    totalInitialValue = returnReview()
    if totalCurrentValue > totalInitialValue:
        totalReturn = totalCurrentValue - totalInitialValue 
        percentChange = (totalReturn / totalInitialValue) * 100
        print("Your portfolio has made ${}, a {}% increase " .format(totalReturn, percentChange))
    if totalInitialValue > totalCurrentValue:
        totalReturn = totalInitialValue - totalCurrentValue
        percentChange = (totalReturn / totalInitialValue) * 100
        print("Your portfolio has lost ${}, a {}% drop " .format(round(totalReturn, 2), round(percentChange,2)))