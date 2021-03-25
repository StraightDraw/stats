# 1.7 National Parks

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

parks = Table.read_table('http://faculty.ung.edu/rsinn/nationalparks.csv')
parks.num_rows

parks.labels

parks

parks.group('state').sort('count', descending = True)

parks.group('state').sort('count', descending = True).barh('state','count')

visit = parks.select('title','acres','visitors', 'lat','long').relabel(0,'name')
visit

visit.sort('visitors', descending = True)

````{warning}
The values in the acres and visitors columns are strings, not numbers. I will attempt to repair and repost soon.
````

Circle.map_table(visit.select('lat', 'long', 'name'), area=2)

