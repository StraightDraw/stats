# 1.5 Airports

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

````{warning}
The `airports.csv` file takes 10 - 15 seconds to load on residential wifi and has 57,420 rows.
````

airports = Table.read_table('http://faculty.ung.edu/rsinn/airports.csv')
airports.num_rows

airports.labels

airports

us = airports.where('country', "US")
us

# Do NOT execute this code block unless you're prepared to wait 2+ minutes for it to load.
#Circle.map_table(us.select('lat', 'long', 'code'), radius=2)

## What airports are north of $65^\circ$?

north65 = us.where('lat', are.above(65)).sort('lat', descending = True)
north65

Marker.map_table(north65.select('lat', 'long', 'name'))

## What airports are at least 1 mile above sea level?

milehigh = us.where('elevation_ft',are.above(5280))
milehigh

Circle.map_table(milehigh.select('lat', 'long', 'name'), area=2)

## Airports and heliports in Georgia

ga = us.where('region', are.containing('GA'))
ga

Circle.map_table(ga.select('lat', 'long', 'code'), area=2)

ga.group('type')

heliports = ga.where('type',"heliport")
heliports

Circle.map_table(heliports.select('lat', 'long', 'code'), radius=2)


ga_big = ga.where('type',"large_airport")
ga_big

Marker.map_table(ga_big.select('lat', 'long', 'code'))