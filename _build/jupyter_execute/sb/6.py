# 1.6 World Cities

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

## This data is from [simplemaps.com/data/world-cities](https://simplemaps.com/data/world-cities)

````{warning}
Getting an error when table loads. Will repair and repost.
````

citie = Table.read_table('http://faculty.ung.edu/rsinn/worldcities.csv')
cities

