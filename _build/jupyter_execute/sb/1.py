# 1.1 Page under construction

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

bitcoin = Table.read_table('http://faculty.ung.edu/rsinn/bitcoin.csv')
bitcoin.num_rows