# 1.2 Bitcoin

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

bitcoin = Table.read_table('http://faculty.ung.edu/rsinn/bitcoin.csv')
bitcoin.num_rows

bitcoin

## Investment Analysis

Suppose you were to buy $100 of bitcoin, hold for exactly 90 days, then sell it. How often would you have made money over the last four years?

dates = bitcoin.column('Date')
purchase = dates.take(np.arange(bitcoin.num_rows - 90))
sell = dates.take(np.arange(90, bitcoin.num_rows))

closing_price = bitcoin.column('Close')
purchase_price = closing_price.take(np.arange(bitcoin.num_rows - 90))
sell_price = closing_price.take(np.arange(90, bitcoin.num_rows))

invest = Table().with_columns(
    'Day', np.arange(bitcoin.num_rows - 90),
    'Purchase', purchase,
    'Bought', purchase_price,
    'Sell', sell,
    'Sold', sell_price,
    'Gain', (sell_price - purchase_price ) / sell_price * 100 )

invest

invest.hist('Gain')

invest.scatter('Bought', 'Sold')

Notice in the above scatter plot that the diagonal line from bottom-left to top-right would represent the break-even trades.

max(invest.column('Gain'))

min(invest.column('Gain'))

invest.bin('Gain', bins = np.arange(-160,100,10))

invest.hist('Gain', bins = np.arange(-100,100,10))

## Plot Price 1 vs. Price 2

If we create a table with ONLY numeric columns, then the .plot method will create multiple line plots. We specify the x-axis variable, and all others get 

When yellow (Price 2) is higher, the investor is winning. When blue is higher, the investor is losing.

price_diff = invest.select('Day', 'Bought', 'Sold')
price_diff.plot('Day')