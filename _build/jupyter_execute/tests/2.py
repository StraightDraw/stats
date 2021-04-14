# 22. Matched Pairs Testing

from datascience import *
import numpy as np

%matplotlib inline

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

from scipy import stats

We will continue to work with a subset of the `personality` table called `pers` but the use pretest vs. posttest data in the `Stress1` and `Stress2` variables. They are the same measure, but one was conducted in the second week of the academic semester while the other was conducted in the seventh week. The **research question** asks whether stress levels are higher during midterms than early in the semester.

pers = Table.read_table('http://faculty.ung.edu/rsinn/perfnarc.csv')
pers.show(5)

## Matched Pairs

The exact same students were surveyed in what researchers call a pre-post format. This is **not** an A/B test because we don't have two groups of subjects A and B, we have one group only. Let's gather the columns we need.

stress = pers.select('Stress1','Stress2')
stress

The null hypothesis is that there is no change in stress between the pretest measure (2nd week) and the posttest measure (7th week). We are primarily interested in how individual stress scores changed, either increasing or decreasing, so we produce a third column called `Gain` to measure the increase from pre to post.

$$\text{Gain} = \text{Post} - \text{Pre}$$

pre = stress.column(0)
post = stress.column(1)
gain = post - pre
gain

stress = stress.with_column('Gain',gain)
stress

We first want to determine the observed gain value to see if stress scores increased.

obs_gain = np.average(gain)
obs_gain

The null hypothesis is that there is no difference between pretest and posttest scores. In that case, the gain would be zero, and it would not matter if we switched the pre and post scores. That's exactly how we will randomize the test statistic: randomly change the signs of the gain scores.

sign = make_array(-1,1)

n = len(gain)
n

ones = np.random.choice(sign,n)
ones

Now we have a random assortment of postive and negative ones. We can multiply this array times the gain array. The result will be a random choice of sign for the gain scores. The absolute value of the gain scores will remain fixed.

rand_gain = ones * gain
rand_gain

Like before, we can simulate the statistic thousands of times to determine what the test statistic distribution looks like.

avg_gains = make_array()

# Set reps to 2k or less especially if working in the cloud
reps = 25000

for i in range(reps):
    ones = np.random.choice(sign,n)
    new_avg_gain = np.average(ones * gain)
    avg_gains = np.append(avg_gains, new_avg_gain)
    
# Remove hashtag comment below to see the gains array   
# gains

def ab_hist(myArray, observed_value):
    tab = Table().with_column('Average Gains',myArray)
    tab.hist(0)
    _ = plots.plot([observed_value, observed_value], [0, 0.1], color='red', lw=2)

ab_hist(avg_gains,obs_gain)

I changed the $x$-axis title in the `ab_hist` fucntion, but everything else is identical the previous two notebooks. We can calculate a $p$-value using a truth array. The observed average gain in stress appears to be atypical given the conditions of the null hypothesis.

p = sum( avg_gains >= obs_gain ) / reps
p

Reject the null hypothesis. There appears to be a significant increase in stress at midterms compared to the second week of the semester.

murder = Table.read_table('http://faculty.ung.edu/rsinn/crime_rates.csv').select('State', 'Year', 'Population', 'Murder Rate')
murder.set_format("Population", NumberFormatter)

non_death_penalty_states = make_array('Alaska', 'Hawaii', 'Maine', 'Michigan', 'Wisconsin', 'Minnesota')
non_death_penalty_states

murder_1971 = murder.where('State',are.not_contained_in(non_death_penalty_states)).where('Year', 1971)
murder_1971

murder_1973 = murder.where('State',are.not_contained_in(non_death_penalty_states)).where('Year', 1973)
murder_1973

ab_murder = murder_1971.append(murder_1973).select('Year','Murder Rate')
ab_murder

def ab_diff(tab):
    tab.group(0,np.average)
    a_mean = tab.group(0,np.average).column(1).item(0)
    b_mean = tab.group(0,np.average).column(1).item(1)
    return a_mean - b_mean

observed_diff = ab_diff(ab_murder)
observed_diff

def ab_shuffle(tab):
    shuffle_group = tab.sample(with_replacement = False).column(0)
    shuffled_tab = tab.with_column("Shuffled Grouping",shuffle_group).select(2,1)
    return shuffled_tab

diffs = make_array()

# Set repetititions to 1,000 or less, especially if you're working in the cloud.
repetitions = 5000

for i in range(repetitions):
    new_diff = ab_diff(ab_shuffle(ab_murder))
    diffs = np.append(diffs, new_diff)

# Remove hashtag comment below to see results array
#diffs

ab_hist(diffs, observed_diff)

p_value = sum( diffs <= observed_diff) / repetitions
p_value

The result of the A/B test is to fail to reject the null. There is no evidence for a difference in murder rates between 1971 and 1973, so there is no evidence that the death penalty served as a detterent. However, this should not be an A/B test at all. We have matched pairs data with each state have a pretest score (murder rate in '71) and posttest score (murder rate in '73).


prepost_murder = murder_1971.join('State', murder_1973).select(0,3,6)
prepost_murder

pre = prepost_murder.column(1)
post = prepost_murder.column(2)
gain_m = post - pre

obs_gain_murder = np.average(gain_m)
obs_gain_murder

avg_gain_murder = make_array()

# Set reps to 2k or less especially if working in the cloud
reps = 25000

for i in range(reps):
    ones = np.random.choice(sign,44)
    new_avg_gain = np.average(ones * gain)
    avg_gain_murder = np.append(avg_gain_murder, new_avg_gain)
    
# Remove hashtag comment below to see the gains array   
# avg_gain_murder

ab_hist(avg_gain_murder, obs_gain_murder)

p_val_prepost = sum( avg_gain_murder >= obs_gain_murder ) / repetitions
p_val_prepost

In fact, we get quite the wrong results if we use A/B testing on paired data. When the appropriate testing method is used, we reject the null and find a signficant positive difference between the prestest (1971 murder rates) and the posttest (1973 murder rates). In contrast to the conclusion above, the evidence suggests the death penalty may be a deterant.

