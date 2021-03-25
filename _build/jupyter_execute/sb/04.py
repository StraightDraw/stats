# 1.4 Historical Stock Prices

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

## Warning!! Do not execute code block below unless you have a good bandwidth connection and are prepared to wait 60+ seconds.

The file `stocks.csv` includes thousands of historical stock prices from 1970 to 2018. The file is 2GB of data which, given time, Python can read into this notebook. I have created some subsets of the table, however, which you may want to work with first before downloading the big daddy table.

#stocks =  Table.read_table('http://faculty.ung.edu/rsinn/stocks.csv')

### The following subsets are much smaller files

microsoft = Table.read_table('http://faculty.ung.edu/rsinn/msft.csv')
microsoft

### To create a CSV file from a table and store in current directory

# microsoft.to_csv('msft.csv')

faang = Table.read_table('http://faculty.ung.edu/rsinn/faang.csv')
faang

facebook = faang.where('ticker','FB')
apple = faang.where('ticker','AAPL')
amazon = faang.where('ticker','AMZN')
netflix = faang.where('ticker','NFLX')
google = faang.where('ticker','GOOGL')

facebook

apple

amazon

netflix

google

faang.sort('date', descending = True)

### To create a CSV file from a table and store in current directory

# faang.to_csv('faang.csv')