# 1.5 Airports

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

#airports = Table.read_table('http://faculty.ung.edu/rsinn/airports.csv')
#airports.num_rows

airports = Table.read_table('airports.csv')

airports.num_rows

airports.labels

airports

us = airports.where('country', "US")
us

# Do NOT execute this code block unless you're prepared to wait 2+ minutes for it to load.
#Circle.map_table(us.select('lat', 'long', 'code'), radius=2)

milehigh = us.where('elevation_ft',are.above(5280))
milehigh

Circle.map_table(milehigh.select('lat', 'long', 'code'), radius=1)

ga = us.where('region', are.containing('GA'))
ga

Circle.map_table(ga.select('lat', 'long', 'code'), radius=2)

ga.group('type')

heliports = ga.where('type',"heliport")
heliports

Circle.map_table(heliports.select('lat', 'long', 'code'), radius=2)


ga_big = ga.where('type',"large_airport")
ga_big

Marker.map_table(ga_big.select('lat', 'long', 'code'))