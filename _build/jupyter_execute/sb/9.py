# 1.9 Chatahoochee

from datascience import *
import numpy as np
from scipy.stats import t

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

I keep some data frames in CSV format accessible from my website. One of them has recreation locations for the Chatahoochee National Forest.

chat = Table.read_table('http://faculty.ung.edu/rsinn/chattahoochee.csv')
chat.num_rows

chat

## Exploring category data

### `.group` Method

We have two obvious category variables: 'county' and 'type' of recreation area. While it looks numeric, the 'ranger station' ID number describes only handful of station.

#### Grouping by County

chat.group('county').sort('count',descending = True)

chat.group('county').sort('count',descending = True).barh('county')

#### Recreation areas grouped by type

# Create a grouping table by type of recreation area.



# Create a bar chart showing for the grouping by type of recreation area sorted for most to least.



#### Recreation areas grouped by ranger station

# While the Ranger Station data may look numeric, it's not. 
# There are only a handful of them, so we can treat them like a category variables. 
# Create a grouping table by type of recreation area.



### `.pivot` method

The best data display for two category variables is often a pivot table

chat.pivot('type','county').show()

Suppose Mina and Jo were interested in hiking and picnic areas. Recall that grouping tables and pivot tables are still tables, so table methods can be used on them. We can select three columns of the pivot table and sort by number of picnic sites.

chat.pivot('type','county').select('county','PICNIC SITE','TRAILHEAD')

We can use parentheses to allow a "text wrapping" effect so we can add returns and indents for clarity when using multiple methods.

(chat.pivot('type','county')
     .select('county','PICNIC SITE','TRAILHEAD')
     .sort('PICNIC SITE', descending = True))

If we sort twice, we can find which of the counties with the most picnic areas have the most trailheads. Notice how the two sorts are run by priority.

(chat.pivot('type','county')
     .select('county','PICNIC SITE','TRAILHEAD')
     .sort('TRAILHEAD', descending = True)
     .sort('PICNIC SITE', descending = True))

## Cleaning Data

The latitude and longitude columns are in deg-min-sec format rather than decimal format. We can use several approaches to create arrays of latitude and longitude in decimal form:

1. The `.column` method used six times with formula implemented manually
2. A user-defined function using `.apply` method (still need `.column` method)
3. A user-defined function using full power of the `.apply` method


### 1. The `.column` method

We take the 3 latitude columns and perform the arithmetic ourselves.

latd = chat.column('lat deg')
latm = chat.column('lat min')
lats = chat.column('lat sec')

lat = latd + latm / 60 + lats / 3600

chat_lat = chat.with_column('lat', lat).drop('lat deg','lat min','lat sec')

#Complete the work by doing the same steps for longitude







# Create a table called chat_lat_lon that contains two columns "lat" and "lon" which have
# the decimal values for latitude and longitude.

chat_lat_lon





### 2. User-defined functions

def dms_to_dec(d,m,s):
    return d + m / 60 + s / 3600

# Use the function defined above to create two arrays, one for latitudes and one for longitudes 












### 3. User-defined function with `.apply` method

The `.apply` method, if a column is not specified, just works row by row. For this reason, we do not have to use the `.column` method first. We can just feed the function a table with the proper three columns.

def deg_2_dec(my_row):
    d = my_row.item(0)
    m = my_row.item(1)
    s = my_row.item(2)
    return d + m/60 + s/3600

lat = chat.select('lat deg','lat min','lat sec').apply(deg_2_dec)
lat

lon = chat.select('lon deg','lon min','lon sec').apply(deg_2_dec)
lon

chattahoochee = (chat.select('name','type','county')
                 .with_columns(
                     'lat',lat,
                     'lon',lon))
chattahoochee

## Maps using lat-lon coordinates

Marker.map_table(chattahoochee.select('lat','lon','name'))

Circle.map_table(chattahoochee.select('lat','lon','name'))

### Recreation areas near Dahlonega

#### Miles per degree of latitude
The distance between latitude lines are consistent, or would be if the earth were a sphere. Taking the radius of a spherical earth as 4,000 miles, we can chop the circumference of the earth into 360 equally sized pieces, one for each of the $360^\circ$, using the formula for the circumference of circule based on its radius.

$$C = 2\pi r \approx 25133 \text{ mi}$$

The distance between latitude lines that are one degree apart is approximately 70 miles which a bit of basic geometry will demonstrate.

r = 4000
circumference = 2 * np.pi * r
circumference

mile_per_degree_lat = circumference / 360 
mile_per_degree_lat

This is why we round to 70 miles per degree of latitude to make life simpler.

#### Miles per degree of longitude

The distance between lines of longitude varies from a maximum at the equator to near-zero at the north or south pole. Within a hudred yards of the north pole, the distance between degrees of longitude would be one or two footsteps. At the equator, assuming the eath is spherical, the distance would the same as for latitude, or about 70 miles.

We can find the radius around the earth at $34.5^\circ$ latitude, a good approximation based on UNG's Dahlonega campus coordinates:

$$(34.5279^\circ N, 83.9844^\circ W)$$

If we call $x$ the new radius, the one specific to the latitude, then:

$$\cos L = \frac{x}{r}$$
 
where 

$$\begin{align*}
L &= \text{ degrees latitude} \\
R &= \text{ radius}
\end{align*}$$

The `numpy` package expects radians, not degrees, so the value for $x$ will be as follows.

x = np.cos(34.5 * np.pi / 180) * r
x

With the new radius $x$, we do the same as before. Determine the circumference and divide it by 360.

x_circumference = 2 * np.pi * x
x_circumference

mile_per_degree_long = x_circumference / 360
mile_per_degree_long

This means that near Dahlonega, GA, there about 70 miles between each degree of latitude and about 57.5 miles between each degree of longitude. Suppose that we want to find all the recreation areas that are within 30 miles east or west of the UNG Dahlonega campus and within 30 miles north and south.


lat_adj = 30/70
round(lat_adj,2)

lon_adj = 30 / 57.5
round(lon_adj,2)

chat_near_dahlonega = (chattahoochee.where('lat',are.between(34.5 - lat_adj,34.5+lat_adj))
                       .where('lon',are.between(-84 - lon_adj, -84+lon_adj)))
chat_near_dahlonega

Circle.map_table(chat_near_dahlonega.select('lat','lon','name'))

# Create a map of all recreation areas in White County.



# Create a map of all trailheads in Rabun County.

