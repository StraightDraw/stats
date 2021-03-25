# 1.8 Caffeine and Sleep

from datascience import *
import numpy as np
from scipy.stats import t

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

I keep some data frames in CSV format accessible from my website. One of them is called `personality.csv` and has, as you might imagine, personality variables. In this case, we will compare and contrast sleep and caffeine consumption levels based upon the grouping variables of biological sex and whether the students are at least 21 years old (Y/N response).

pers = Table.read_table('http://faculty.ung.edu/rsinn/personality.csv')
pers.num_rows

pers

## Sleep and Caffeine Data

sleep = pers.select('Sex','Age','G21', 'Caff','Sleep')
sleep

### Data Analysis

#### Pivot tables with third variable averaging

sleep.pivot('Sex','G21')

sleep.pivot('Sex','G21','Sleep',np.average)

sleep.pivot('Sex','G21','Caff',np.average)

From the pivot tables with averaging for Sleep and Caffeine, we see very little difference based on gender but more pronounced differences based on the "older than 21 years" variable (Y/N response).

### Histograms with grouping

sleep.hist('Sleep',group='Sex')

sleep.hist('Sleep',group='G21')

sleep.hist('Caff',group='Sex')

sleep.hist('Caff',group='G21')

## Applied Statistics

In the case of demographic grouping variables and a single numeric variables, resesearchers use a t-test which is calculated as

$$t = \frac{\bar x_1 - \bar x_2}{SE}$$

where the standard error is

$$SE = \sqrt{\frac{s_1^2}{n_1-1}+\frac{s_2^2}{n_2-2}}$$

We can create a couple simple functions for the standard error and degrees of freedom.

# Standard error for two sample t-test.
def se_t2(array1,array2):
    s1 = np.std(array1)
    s2 = np.std(array2)
    n1 = len(array1)
    n2 = len(array2)
    return np.sqrt(s1**2 / n1 + s2**2 / n2)

# The simplest calculation of degrees of freedom for two sample t-test.
def df_t2(array1,array2):
    n1 = len(array1)
    n2 = len(array2)
    return n1 + n2 - 2

# The t-test.
def t2(array1,array2):
    se = se_t2(array1, array2)
    df = df_t2(array1, array2)
    t_stat = ( np.average(array1) - np.average(array2) ) / se_t2(array1,array2)
    p_val = t.pdf(t_stat, df)
    print('t = ',t_stat)
    print('p = ', p_val)

### Creating arrays for Caff variable using G21 grouping and Sex grouping

caff_older = sleep.where('G21',"Y").column('Caff')
caff_younger = sleep.where('G21',"N").column('Caff')
caff_males =  sleep.where('Sex','M').column('Caff')
caff_females =  sleep.where('Sex','F').column('Caff')

#### $t$-tests for Caffeine differences

t2(caff_older,caff_younger)

t2(caff_males,caff_females)

We find a significant difference based on age ($\alpha = 0.05$) but not based on gender.

### Creating arrays for Sleep variable using G21 grouping and Sex grouping

sleep_older = sleep.where('G21',"Y").column('Sleep')
sleep_younger = sleep.where('G21',"N").column('Sleep')
sleep_males =  sleep.where('Sex','M').column('Sleep')
sleep_females =  sleep.where('Sex','F').column('Sleep')

t2(sleep_older,sleep_younger)

t2(sleep_males,sleep_females)

As with caffeine, we find a significant difference in sleep based on age ($\alpha = 0.05$) but not based on gender.