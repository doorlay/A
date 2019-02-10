# This file will handle gathering the stock data from the internet.

from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='52UIN9CWN6RNDHXJ', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))

# The info will then be sent through the other files to be analyzed.
