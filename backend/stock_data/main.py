# getData function returns stock symbol, current price, and and current date in a list.
import funcs as f
# Current version gets declared as a global var up here
version = 1.0

# This will act as the main file that everything flows through.

# This function gets a list of all stock symbols in the database
def getSymbolsDatabase():
    dataList = f.scr()
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
    dataList = f.scr()
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
    dataList = f.scr()
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
        price = f.getData(stock)
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
        price = f.getData(stock)
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



def main():
    # Some formatting to make stuff look pretty.
    print("-----------------------------------")
    print("Welcome to StockScrape, version 1.2")
    print("-----------------------------------")

    print("Would you like to... \n\n 1. Review portfolio \n 2. Check current prices \n 3. Compare\n")
    q = input(" Type a number from above: ")
    # Creates a flag for the while loop
    flag = False
    # While loop iterate until user types a correct response
    while not flag:
        if q == "1":
            print("-----------------------------")
            review()
            flag = True
            break
        if q == "2":
            print("--------------------------")
            current()
            flag = True
            break
        if q == "3":
            print("-----------------------------")
            compareTotal()
            flag = True
            break
        # if q == "3":
        #     print("exiting")
        #     flag = True
        #     break
        else:
            q = input("You typed neither. Type a number from above: ")

        



main()
