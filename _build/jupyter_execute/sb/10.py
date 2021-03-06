# 10. Nighthawks Version of Lab 6

We are creating a Nighthawks version of Lab 6. You should work on the official Lab 06 from the course schedule but use the hints and suggestions from this notebook to clarify your work.

from datascience import *
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

## What is the Therapeutic Touch

**The following paragraphs are copied directly from Berkeley's Data8 Lab06 materials.**

The Therapeutic Touch (TT) is the idea that everyone can feel the Human Energy Field (HEF) around individuals. Those who practice TT have described different people's HEFs as "warm as Jell-O" and "tactile as taffy."

TT was a popular technique used throughout the 20th century that was toted as a great way to bring balance to a person's health. Certain practitioners claim they have the ability to feel the HEF and can massage it in order to promote health and relaxation in individuals.

Emily Rosa
Emily Rosa was a 4th grade student who was very familiar with the world of TT, thanks to her parents, who were both medical practitioners and skeptics of TT.

For her 4th grade science fair project, Emily decided to test whether or not TT practitioners could truly interact with a person's HEF. She later went on to publish her work in TT, becoming the youngest person to have a research paper published in a peer reviewed medical journal.

Emily's Experiment
Emily's experiment was clean, simple, and effective. Due to her parents' occupations in the medical field, she had wide access to people who claimed to be TT practitioners.

Emily took 21 TT practitioners and used them for her science experiment. She would take a TT practitioner and ask them to extend their hands through a screen (which they can't see through). Emily would be on the other side and would flip a fair coin. Depending on how the coin landed, she would put out either her left hand or her right hand. The TT practitioner would then have to answer which hand Emily put out. If a pracitioner could truly interact with a person's HEF, it would be expected that they answered correctly.

Overall, through 210 samples, the practitioner picked the correct hand 44% of the time.

Emily's main goal here was to test whether or not the TT practicioners' guesses were random, like the flip of a coin. In most medical experiments, this is the norm. We want to test whether or not the treatment has an effect, not whether or not the treatment actually works.

We will now begin to formulate this experiment in terms of the terminology we learned in this course.

### Question 1

Describe Emily’s model for how likely the TT practitioners are to choose the correct hand. What alternative model is her model meant to discredit?

#### Nighthawks:
Answer question as asked.

### Question 2
Remember that the practitioner got the correct answer 44% (0.44) of the time. According to Emily's model, on average, what proportion of times do we expect the practitioner to guess the correct hand? Make sure your answer is between 0 and 1.

#### Nighthawks
Answer question as asked.

### Question 3
We usually use a statistic to help determine which model the evidence points towards. What is a statistic that we can use to compare outcomes under Emily’s model to what was observed? Assign valid_stat to an array of integer(s) representing test statistics that Emily can use:

1. The difference between the expected percent correct and the actual percent correct
2. The absolute difference between the expected percent correct and the actual percent correct
3. The sum of the expected percent correct and the actual percent correct

#### Nighthawks

This is a multiple choice question asking for an array that lists the items 1, 2, or 3 that *could be used* as a valid statistic for this scenario. Our suggestion is to choose item 1 only as the correct answer:

```
valid_stat = make_array(1)
```

However, we plan to use a variation of item 1 in our version of the lab: the difference between the actual **number** of correct choices minus the expected number of correct choices.

### Question 4

Why is the statistic from Question 3 the best choice for comparing outcomes in Emily's experiment? How does it relate to the models you defined in question 1?

#### Nighthawks
Answer question as asked.

### Question 5
Define the function statistic which takes in an expected proportion and an actual proportion, and returns the value of the statistic chosen in Question 3. Assume that the argument takes in proportions, but return your answer as a percentage.

**Hint:** Remember we are asking for a percentage, not a proportion.

#### Nighthawks

Ignore above directions. Instead, use the function `np.random.choice` to generate a random sample from the array called `choice_array`. The value of `simulated_outcome` should be a whole number between 0 and 210 representing the number of correct choices made out of 210 attempts. Think about this: while any whole number in this range is possible, what values are probable?

**Hint:** If we think of the **zeros** as errors and the **ones** as times when the simulated TT practitioners made the correct choice, then we can use the function `sum` to determine the total number of correct choices out of 210 attempts.


choice_array = make_array(0,1)

simulated_outcome = ...


### Question 6
Use your newly defined function to calculate the observed statistic from Emily's experiment.

#### Nighthawks

Ignore above directions. Instead, answer: "What value, on average, do expect your statistic `simulated_outcome` to produce? If we repeatedly used `simulated_outcome`, what would be the "typical" or "average" value?

### Question 7

To begin simulating, we should start by creating a representation of Emily's model to use for our simulation. This will be an array with two items in it. The first item should be the proportion of times, assuming that Emily’s model was correct, a TT practictioner picks the correct hand. The second item should be the proportion of times, under the same assumption, that the TT practitioner picks the incorrect hand. Assign `model_proportions` to this array. 

After this, we can simulate 210 hand choices, as Emily evaluated in real life, and find a single statistic to summarize this instance of the simulation. Use the `sample_proportions` function and assign the proportion of correct hand choices (out of 210) to `simulation_proportion_correct`. Lastly, use your statistic function to assign `one_statistic`  to the value of the statistic for this one simulation.



#### Nighthawks

Ignore above directions because *there is no reason to simulate random outcomes and compare them to Emily's data*. **Why?**

The TT practitioners only got 44% of their attempts correct. They would have been better off flipping a coin and guessing. The TT practitioners clearly produced data that would suggest to anyone, scientist or not, that they could not predict at a rate that was better than random chance. No statistical analysis is needed for this claim.

Let's change the observed data, however, so we can use a simulation to test this scenario. Suppose Emily had found that the TT practitioners chose correctly 55% of the time. What is the expected number of correct choices out of 210 attempts if the TT practitioners were to choose correctly 55% of the time? Also, what total number of correct outcomes out of 210 would be expected to be correct if a coin flip were "choosing"?

expected_correct_if_55 = ...
expected_correct_if_50 = ...

**Note:** the value of `expected_correct_if_55` will **not** be an integer, it will have a decimal part equal to 0.5. However, the value of `expected_correct_if_50` will be an integer and should have the property that, when the value of `simulated_outcome` is greater than `expected_correct_if_50`, the difference 

```
simulated_outcome - expected_correct_if_50
```
will be a **positive integer**.

### Question 8

Let's now see what the distribution of statistics is actually like under Emily's model.

Define the function simulation_and_statistic to take in the model_proportions array and the expected proportion of times a TT practitioner would guess a hand correctly under Emily's model. The function should simulate Emily running through the experiment 210 times and return the statistic of this one simulation.

Hint: This should follow the same pattern as the code you did in the previous problem.

#### Nighthawks

Ignore above directions because our statistic produces a whole number. What we need is a `for` loop that runs our simulation 10000 times and creates an array in which the outcomes are stored. You should base your answer on your response to **Question 5**.

We will create a blank array called `results` and use the `np.append` method to add the result of each simulation to the end of the `results` array. Be sure that your `for` loop runs ten thousand times and that the length of the final `results` array is also ten thousand.

results = make_array()

for ... in ... :
    new_simulated_outcome = ...

    


# Remove the hashtag in the line below to test your for loop.
#results

**Question 8** includes a histogram which will produce an error due to the changes we have made. Replace the code block at the end of question 8 with the code block below. You will see a histogram of `results` with a red line at `expected_correct_if_55`. The p-value is the proportion of observations in `results` that lie above the red line and will be calculated in **Question 9**.

# Do not change this code block, just run it.
t = Table().with_column('Results', results)
t.hist(bins = np.arange(80,130))
_ = plots.plot([115.5, 115.5], [0, 0.06], color='red', lw=2)

### Question 9

Calculate the proportion of simulated statistics greater than or equal to the observed statistic.

#### Nighthawks
Calculate the proportion `p` of simulated statistics greater than or equal to `expected_correct_if_55`.


p = ...