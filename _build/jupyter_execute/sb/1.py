# 1.1 Narcissism

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

I keep some data frames in CSV format accessible from my website. One of them is called `personality.csv` and has, as you might imagine, personality variables. In this case, we will compare the narcissism levels based upon the grouping variable of biological sex.

pers = Table.read_table('http://faculty.ung.edu/rsinn/personality.csv')
pers.num_rows

pers.labels

pers

narc = pers.select('Sex','Narc')

narc

integer_bins = np.arange(15)
narc.hist('Narc', group = "Sex", bins = integer_bins)
plots.title('Narcissism by Sex')

males_narcissism = narc.where('Sex',"M").column('Narc')

females_narcissism = narc.where('Sex',"F").column('Narc')

print('The average narcissism level for males is ', np.nanmean(males_narcissism),
      "\r\n",
      'and the average narcissism level for females is ' , np.nanmean(females_narcissism))

from scipy import stats

stats.ttest_ind(males_narcissism, females_narcissism, axis=0, 
                equal_var=True, 
                nan_policy='omit', 
                alternative='two-sided')