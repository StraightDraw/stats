# 1.11 Narcissism, Perfectionism and A/B Testing

from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

from scipy import stats

I keep some data frames in CSV format accessible from my website. One of them is called `personality.csv` and has, as you might imagine, personality variables. In this case, we are using a subset of the personality data with variables like perfectionsism, narcissism with grouping variables like biological sex and the `AccDate` variable which has Yes/No responses to the following question:

"At a time in your life when you are not involved with anyone, a person asks you out. This person has a great personality, but you do not find this person physically attractive. Do you accept the date?"

pers = Table.read_table('http://faculty.ung.edu/rsinn/perfnarc.csv')
pers.num_rows

pers.labels

pers

narc = pers.select('Sex','Narc')

The `nan` value indicates there is no value for that cell in the table. In this case, it's a survey item that went unanswered. The `numpy` function `nanmean` takes the average but ignores any `nan` values. In a clean table, we could just use `np.mean`, instead.

narc.group('Sex', np.average)

a_mean = narc.group(0,np.average).column(1).item(0)
a_mean

b_mean = narc.group(0,np.average).column(1).item(1)
b_mean

observed_difference = a_mean - b_mean
observed_difference

integer_bins = np.arange(15)
narc.hist('Narc', group = "Sex", bins = integer_bins)
_=plots.title('Narcissism by Sex')

## An A/B Test for differences in narcissism based on biological sex.

Notice that we simplify to the `narc` table which has only two columns, a grouping variable (Male/Female) and a numeric variable (narcissism score).

narc

## Let's shuffle the labels in the grouping variable column

shuffle_sex = narc.sample(with_replacement = False).column(0)
shuffle_sex

shuffled_narc = narc.with_column("Shuffled Grouping",shuffle_sex).select(2,1)
shuffled_narc

shuffled_narc.group('Shuffled Grouping',np.average)

### Create a function that produces a random shuffle of the grouping variable column

We're copy-pasting the code from the previous 3-4 code blocks to make our function, and using the generic name `tab` for our data table.

def ab_shuffle(tab):
    shuffle_group = tab.sample(with_replacement = False).column(0)
    shuffled_tab = tab.with_column("Shuffled Grouping",shuffle_group).select(2,1)
    return shuffled_tab

ab_shuffle(narc)

### Function that calculates difference in means between shuffled A/B groups

From above, we were using the `.group` method to find our group means.

shuffled_narc.group('Shuffled Grouping',np.average)

a_mean = shuffled_narc.group('Shuffled Grouping',np.average).column(1).item(0)
a_mean

b_mean = shuffled_narc.group('Shuffled Grouping',np.average).column(1).item(1)
b_mean

diff = a_mean - b_mean
diff

We can see that we need to accept a generic two-column table where the grouping variable is listed first. Then we can use the above 3-4 to create our function.

def ab_diff(tab):
    tab.group(0,np.average)
    a_mean = tab.group(0,np.average).column(1).item(0)
    b_mean = tab.group(0,np.average).column(1).item(1)
    return a_mean - b_mean

ab_diff(shuffled_narc)

### Run simulation 5,000 times

diffs = make_array()

reps = 5000

for i in range(reps):
    shuffled_tab = ab_shuffle(narc)
    new_diff = ab_diff(shuffled_tab)
    diffs = np.append(diffs, new_diff)
    
diffs

def ab_hist(myArray, obs_diff):
    tab = Table().with_column('A/B Differencs',myArray)
    tab.hist(0)
    _ = plots.plot([obs_diff, obs_diff], [0, 1], color='red', lw=2)

ab_hist(diffs,observed_difference)