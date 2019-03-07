# This file will manage the purchasing of stocks.

from scrape import getDataFrom
# This is the most critical part of the process, and if purchases are made at the right time, everything else should go smoothly.

# If a stock is on the way down, do not purchase. Only purchase on the way up.

# Must identify proper buy points. This can include...
# - cup with handle
# - double bottom
# - flat base 

stock = input("What stock do you want to get data from? Enter with 'quotes':")
getDataFrom(stock)
