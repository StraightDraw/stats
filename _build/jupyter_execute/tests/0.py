# 20. A/B Testing Tools

from datascience import *
import numpy as np

%matplotlib inline

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

from scipy import stats

I keep some data frames in CSV format accessible from my website. One of them is called `personality.csv` and has, as you might imagine, personality variables. In this case, we are using a subset of the personality data with variables like perfectionsism, narcissism with grouping variables like biological sex and the `AccDate` variable which has Yes/No responses to the following question:

"At a time in your life when you are not involved with anyone, a person asks you out. This person has a great personality, but you do not find this person physically attractive. Do you accept the date?"

The Stress1 and Stress2 variables are pre-post data collected from the 2nd week and 7th week of the semester respectively to see if college students experience more stress during midterms.

pers = Table.read_table('http://faculty.ung.edu/rsinn/perfnarc.csv')
pers

## Tools for A/B Testing

As we walk through an example with narcissism, we will build three functions that will help us conduct A/B tests.

1. `ab_shuffle`
2. `ab_diff`
3. `ab_hist`

All three expect an input of a 2-column table with the grouping variable in the first column and a numeric variable in the second.

### Creating a 2-column table for A/B Testing

We will use the grouping variable of biological sex and numeric variable of narcissism scores.

narc = pers.select('Sex','Narc')

narc.group('Sex')

narc.group('Sex', np.average)

### Calculating observed difference in means for A/B groups

a_mean = narc.group(0,np.average).column(1).item(0)
a_mean

b_mean = narc.group(0,np.average).column(1).item(1)
b_mean

observed_difference = a_mean - b_mean
observed_difference

integer_bins = np.arange(15)
narc.hist('Narc', group = "Sex", bins = integer_bins)
_= plots.title('Narcissism by Sex')

### The A/B hypothesis test for differences in narcissism based on biological sex

The null hypothesis is that the male and female groups are drawn from the same distribution. If so, then randomly shuffling the grouping labels should not matter. The observed difference in A/B means should fall well within the distribution of shuffled differences in A/B means which we can simulate.

### Creating `ab_shuffle`: a function for shuffling the grouping labels

Let's first demonstrate step by step what we need the function to do. Then we can create the function. The first code block below demonstrates our "shuffle" command which uses the `sample` method and draws without replacement.

shuffle_sex = narc.sample(with_replacement = False)
shuffle_sex.show(5)

shuffle_sex = narc.sample(with_replacement = False).column(0)
shuffle_sex

After creating an array of shuffled labels, we need to include that array as column in our table. We can add the shuffled labels as a third column, then use the `select` method to create a two-column table with the columns in the correct order.

shuffled_narc = narc.with_column("Shuffled Grouping",shuffle_sex)
shuffled_narc.show(5)

shuffled_narc = narc.with_column("Shuffled Grouping",shuffle_sex).select(2,1)
shuffled_narc.show(5)

shuffled_narc.group('Shuffled Grouping',np.average)

#### The `ab_shuffle` function

Our function just combines the previous several code blocks. Notice that the expected input is a two-column table with the grouping variable be in the first column.

def ab_shuffle(tab):
    shuffle_group = tab.sample(with_replacement = False).column(0)
    shuffled_tab = tab.with_column("Shuffled Grouping",shuffle_group).select(2,1)
    return shuffled_tab

ab_shuffle(narc)

### Creating `ab_diff`: a function that calculates the difference in A/B group means

We can add a function to the `.group` method to find the A/B group means.

shuffled_narc.group('Shuffled Grouping',np.average)

a_mean = shuffled_narc.group('Shuffled Grouping',np.average).column(1).item(0)
a_mean

b_mean = shuffled_narc.group('Shuffled Grouping',np.average).column(1).item(1)
b_mean

diff = a_mean - b_mean
diff

#### The `ab_diff` function

Using the above code blocks as a template, we can write a function that grabs the means from the grouping table. Again, the expected input is a two-column table with the grouping variable first.

def ab_diff(tab):
    tab.group(0,np.average)
    a_mean = tab.group(0,np.average).column(1).item(0)
    b_mean = tab.group(0,np.average).column(1).item(1)
    return a_mean - b_mean

ab_diff(shuffled_narc)

## Simulating the statistic

The statistic we need is the difference in shuffled A/B group means. Our plan is to use a `for` loop to repeatedly reshuffle the labels and calculate this statistic. The output will be an array representing a random sampling of this statistic.

The engine in the `for` loop is quite simple. We shuffle the data table and calculate the difference in A/B means in one line using the two functions we created above.

diffs = make_array()

# Reduce reps to 1,000 or less, especially if running in cloud.
reps = 5000

for i in range(reps):
    new_diff = ab_diff(ab_shuffle(narc))
    diffs = np.append(diffs, new_diff)

# Remove the hashtag/comment symbol to see the array output
# diffs

## Displaying the distribution of the null hypothesis statistic

Let's create a third function, one that will take an array of simulated statistics along with an observed value and plot a histogram showing both.

def ab_hist(myArray, observed_value):
    tab = Table().with_column('A/B Differencs',myArray)
    tab.hist(0)
    _ = plots.plot([observed_value, observed_value], [0, 0.1], color='red', lw=2)

ab_hist(diffs,observed_difference)

Conside what the above visualization means.

1. The blue histogram represents the null hypothesis statistic
2. The red line indicates the observed value of the statistic

To calculate a $p$-value, we first creat a truth array for the number of randomized A/B differences in means that were less than the `observed_difference`. Then we can sum the truth array which counts all simulated values at least as extreme as the observed value.

sum(diffs <= observed_difference)

p_val = sum(diffs <= observed_difference) / reps
p_val

## Results of Example A/B Test

Because `p_val` is far less than $0.05$, we reject the null. In real world terms, we conclude that there is strong evidence that a significant difference exists in Narcissism levels based upon biological sex.