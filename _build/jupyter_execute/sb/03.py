# 1.3 Functions and Cubes

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

Let's start out by creating a table of integers and their cubes. Then we can see how the `.apply` method works.

ints = np.arange(1,21)
ints

cubes = ints ** 3
cubes

digits = Table().with_columns('Integers', ints,
                             'Cubes', cubes)
digits

def cube_root(x):
    return x ** (1/3)

cube_root(8)

cube_root(1000)

digits.apply(cube_root,'Cubes')

This can also be accomplished with the `.column` method.


cube_root(digits.column('Cubes'))