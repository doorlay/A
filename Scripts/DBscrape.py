# This file contains a function to scrape the database and create an array of stock info.
# This function will be imported to the 'scrape.py' file within the Scripts folder.

def DBscrape():
	database1 = open(Database/database.txt)
	database2 = database1.read()
	DBarray = database2.splitlines()
	

