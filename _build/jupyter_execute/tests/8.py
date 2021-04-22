# 30. Homework 10

from datascience import *
import numpy as np

%matplotlib inline

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

from scipy import stats

I keep some data frames in CSV format accessible from my website. One of them is called personality.csv and has, as you might imagine, personality variables. We will pull different subsets of that data frame for the work below. Here's a description of the different variables you will see.

Sex
: M/F response to question about biological sex

G21
: Y/N response to "are you 21 years old or older?"

Greek
: Y/N response to "are you involved in a social Greek fraternity or sorority?"

AccDate
: Y/N response to question: "At a time in your life when you are not involved with anyone, someone asks you out. This person has a great personality, but you do not find them physically attractive. Do you accept the date?"

SitClass
: Front/middle/back response to "where do you prefer to sit in class?"

Friends
: Same/opposite/either response to "which sex do you find it easiest to make friends with."

Stress1, Stress2
: Pre-post measure of stress in the 2nd week (Stress1) and 7th week (Stress2) of the semester.

TxRel
: Toxic relationships beliefs, higher scores indicate more toxicity.

Opt
: Optimism, higher scores indicate more optimism.

SE
: Self-esteem, higher score indicate higher levels of self-esteem.

Neuro
: Neuroticism, higher scores indicate higher levels of neuroticism

Perf
: Perfectionism, higher scores indicate higher levels of perfectionism.

Narc
: Narcissism, higher scores indicate higher levels of narcissism.

You will recognize several data sets that we used in class examples and labs, too.

## Data for examples

neuroanx = Table.read_table('http://faculty.ung.edu/rsinn/neuroanx.csv')
perfnarc = Table.read_table('http://faculty.ung.edu/rsinn/perfnarc.csv')
nba = Table.read_table('http://faculty.ung.edu/rsinn/nba_salaries.csv')
assault = Table.read_table('http://faculty.ung.edu/rsinn/crime_rates.csv').select(0,1,2,3,4,7)

## Task 1

Using the `perfnarc` table, conduct an exploratory data analysis of the `Stress1` values. Be sure to find the mean, median, sample size and standard deviation, and to display a histogram of the variable.

perfnarc.show(5)

Remember, you may use the tools from [notebook 26](https://straightdraw.github.io/stats/tests/6.html).





## Task 2

Using the `perfnarc` table, conduct an A/B test on `Stress1` values using the grouping variable `Greek`. The research question is whether students involved in Greek life would be more stressed during the 2nd week of the semester. Many social Greek organizations have meetings, socials and philanthropy events early in the semester, so perhaps they experience higher levels of stess.

perfnarc.show(5)

Be sure to include your null hypothesis and a `for` loop that simulates the null hypothesis test statistic. After displaying the simulated distrubtion and calculating your $p$-value, write a sentence or two about the real world conclusions you can draw based on your results.

Remember, you may use the tools from [notebook 20](https://straightdraw.github.io/stats/tests/0.html) and [notebook 21](https://straightdraw.github.io/stats/tests/.html).





## Task 3

Using the `nba_salary` table, conduct an A/B test to determine if power forwards (PF) are paid more than shooting guards (SG).

nba.show(5)

Be sure to include your null hypothesis and a `for` loop that simulates the null hypothesis test statistic. After displaying the simulated distrubtion and calculating your $p$-value, write a sentence or two about the real world conclusions you can draw based on your results.

Remember, you may use the tools from [notebook 20](https://straightdraw.github.io/stats/tests/0.html) and [notebook 21](https://straightdraw.github.io/stats/tests/1.html)





## Task 4

Using the violent crime data set called `crime_rates`, conduct an exploratory data analysis as well as a bootstrapping confidence interval estimate of the mean `Aggravated Assault Rate` in Georgia between 1960 and 1990.

assault.show(5)

Discuss your findings. Remember, you may use the tools from [notebook 24](https://straightdraw.github.io/stats/tests/4.html) and [notebook 25](https://straightdraw.github.io/stats/tests/5.html)





## Task 5

Using the violent crime data set called `crime_rates`, conduct comparison of the Aggravated Assaults in Georgia and Alabama from 1960 to 1990. Use a 95% confidence interval for both means using a bootstrapped confidence interval with resample size of 30 and 1,000 repetitions of your `for` loop.

With the null hypothesis that the aggravated assault rate distribution will be the same in both GA and AL, we can conduct a hypothesis test. If the confidence intervals do not overlap, we have evidence of a difference in aggravated assault rates between these two states. If the confidence intervals do overlap, there is no evidence for a difference in means.

assault.show(5)





## Task 6

Using the `personality` data set, test for a significant correlation between Anxiety and Optimism. Be sure to to display descriptive statistics for regression, a scatter plot, and a simulation of the null hypothesis test statistic. Be sure to discuss your findings in terms of the $p$ calculated in your `for` loop using 2,000 to 5,000 repititions.

neuroanx.show(5)





Discuss your findings. Remember, you may use the tools from [notebook 26](https://straightdraw.github.io/stats/tests/6.html) and [notebook 27](https://straightdraw.github.io/stats/tests/7.html)





## Task 7

Conduct an investigation that interests you using one of the included data sets. Describe your null hypothesis and how you plan to test it. Have fun. Be creative. Yet try to keep it very similar to one of the investigations we have have examples for. You should finish with a hypothesis test and discussion of your calculated $p$-value.



