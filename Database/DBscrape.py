# This file will scrape the data from the database to be turned into an array.

database1 = open(Database/database.txt)
database2 = database1.read()
DBarray = database2.splitlines()
