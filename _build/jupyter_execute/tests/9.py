# 29. Mixed Hypothesis Testing Practice

from datascience import *
import numpy as np

%matplotlib inline

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

from scipy import stats

An undergraduate statistics research project several years ago studied humor styles and personality. The data set from that study is called `personality.csv`. We will pull different subsets of that data frame for the work below. Here's a description of the different variables you will see.

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

You will likely recognize several data sets that we used in class examples and labs, too.

## Data for examples

The large table `personality.csv` is loaded below. We can use `where` and `select` to find appropriate sub-tables for analysis.

personality = Table.read_table('http://faculty.ung.edu/rsinn/personality.csv')

We should be ready and able to perform the following hypothesis tests and related statistical investigations:

1. Exploratory data analysis of single numeric and/or category variables
2. A/B Tests
3. Bootstrap confiedence interval estimates (typically of the mean)
4. Exploratory data analysis of two numeric variables (correlation)
5. Test for significant correlation
