from scrape import scr

# data needed to make a sell decision

# stock symbol 
# current price
# purchase price
# date of purchase price

DBarray = scr()
print("Here are the stocks you have available:")
print(DBarray)


def timecheck():
  
  # Function that checks if it's been four weeks or not.

if (current_price / purchase_price >= .20):
  timecheck()
