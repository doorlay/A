# Stock Scrape
A bare-bones stock data scraper, written in Python.

---
**Description**   
Stock Scrape is a lightweight stock data scraper written in python. The program utilizes the Alpha Vantage API to get current prices from NYSE and NASDAQ stocks. The programs intakes a stock symbol, and then outputs an array containing the stock symbol, current stock price, and current date. This program can be used as a great starting point for a more complex stock data scraper.


**Getting started**  
1. Register an API key [here](https://www.alphavantage.co/), for free.
2. Ensure that you are running a current version of python. If not, head [here](https://www.python.org/downloads/) to download.
3. Head to your terminal and use the pip installer to install the alpha vantage module, with the following command:  
` pip install alpha_vantage`. If you're having difficulty with the pip installer, head [here](https://www.makeuseof.com/tag/install-pip-for-python/) to troubleshoot.
4. Head over to the 'scrape.py' file within the scripts folder. On line 26, enter your personal API key from step one inside the parameter titled 'key'.
5. You're ready to start!

**How to Run**  

To run, head to the main.py file. Within the file, change the stock symbol inside of the 'getData()' function. Execute the program to see the current data, outputted in an array. Change the program as you see fit, and enjoy!