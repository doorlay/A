from DBscrape import scrape

# data needed to make a sell decision

# stock symbol
# current price
# purchase price
# date of purchase price
# current date

DBarray = scrape()
print("Here are the stocks you have available:")
print(DBarray)


def timecheck():
  
  # Function that checks if it's been four weeks or not.

if (current_price / purchase_price >= .20):
  timecheck()
