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

The `nan` value indicates there is no value for that cell in the table. In this case, it's a survey item that went unanswered. The `numpy` function `nanmean` takes the average but ignores any `nan` values. In a clean table, we could just use `np.mean`, instead.

narc.group('Sex', np.nanmean)

integer_bins = np.arange(15)
narc.hist('Narc', group = "Sex", bins = integer_bins)
_=plots.title('Narcissism by Sex')

males_narcissism = narc.where('Sex',"M").column('Narc')

females_narcissism = narc.where('Sex',"F").column('Narc')

print('The average narcissism level for males is',
      np.round(np.nanmean(males_narcissism),2),
      "\r\n",
      'and the average narcissism level for females is', 
      np.round(np.nanmean(females_narcissism),2)
     )

from scipy import stats

stats.ttest_ind(males_narcissism, females_narcissism, axis=0, 
                equal_var=True, 
                nan_policy='omit', 
                alternative='two-sided')