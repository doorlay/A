# scr function gets the database from the text file in a list.
from scrape import scr

# getData function returns stock symbol, current price, and and current date in a list.
from scrape import getData

'''
data needed to make a sell decision:

Stock symbol (done)
current price (done)
purchase price
date of purchase
current date (done)
'''

# just need purchase price and date of purchase, which is stored in my database. Perfect!



def timecheck():
  
  # Function that checks if it's been four weeks or not.

if (current_price / purchase_price >= .20):
  timecheck()
