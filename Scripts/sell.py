from scrape import scr

# data needed to make a sell decision
'''
Stock symbol
current price
purchase price
date of purchase
current date
'''
# Assigns an array containing all the database info to a variable
DBarray = scr()
print("Here are the stocks you have available:")
print(DBarray[0],DBarray[3])


def timecheck():
  
  # Function that checks if it's been four weeks or not.

if (current_price / purchase_price >= .20):
  timecheck()
