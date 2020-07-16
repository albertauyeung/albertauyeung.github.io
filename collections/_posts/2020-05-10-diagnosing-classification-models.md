---
layout: article
title:  "Diagnosing Problems in Machine Learning Classification Models"
tags: [machine learning, supervised learning, classification]
key: 'p20200510dpcm'
---

This post aims at describing different ways to investigate how a classification model (classifier) can be improved. Although numerous research papers, courses, tutorials and blog posts on this topic can easily be found online, I would still like to write an article for two reasons. The first is to give myself a chance to summarize my foundings and understanding of the topic in a systematic way. The second is to add my own opinions on the topic based on some of my experience in applying machine learning in various applications.

## The Scenario

We start the discussion with a scenario or a motivating example:

- **We trained a model to perform a classification task, and it achieved 70% accuracy on the test dataset. What shall we do next?**

(Andrew Ng mentioned a similar but more specific example in his ["Advice for applying Machine Learning"](http://cs229.stanford.edu/materials/ML-advice.pdf) slides for his CS229 lectures at Stanford.)

This scenario is common enough that every machine learning practitioner would have experienced. It is also likely to be discussed in an interview for a mahcine learning position, as it can effectively reveal how much a candidate knows about the fundamentals of machine learning, and what are the important things to consider when applying machine learning to solve real world problems.

We can approach this question from many different angels, and surely there are a lot of things you can do to improve a classification model. However, I will first discuss about what **further questions** we should ask before taking actions to improve the model.

## Asking Questions

The scenario mentioned above does not provide details of the machine learning task, the algorithm(s) used to train the model, the parameters involved, the dataset used in training and evaluation, or even the actual performance of the model. Hence, it seems natural that we should try to have a better understanding of the situation.

In particular, the following questions are some of the most important ones:

1. Is it **binary**, **multi-class**, or **multi-label**?
    - The variety of the outputs of the classifier will determine what further questions we should ask, and what further investigations we should make
    - If it is a multi-class or a multi-label classifier, we would like to know the performance of the model on different classes. For example, it may do good on the majority classes, and do badly on the minority classes.
2. How does the **dataset** look like?
    - Do we have a **balanced** dataset?
    - How much data do we have? Is the amount of data enough for the type of algorithm chosen to train the model?
3. What about **precision** and **recall**?
    - Accuracy alone does not give us a full picture of the performance of the model
    - Accuracy can be misleading if the distribution of the difference classes is skewed (consider a classifier that tries to predict whether a test of cancer is positive)
4. Is precision or recall more important in the application?
    - Do we want the model to be more **precise** (higher precision)?
    - Or do we want to **avoid missing any positive cases**, at the cost of having some false positives (more sensitive, or in other words higher recall)?
5. What is a **"good"** model in this application?
    - Do we have a target? (e.g. should we aim at achieving 90% precision, or 80% recall?)
    - Do we know what is the **optimal error rate** of the tast? (Refer to Chapter 22 of Andrew Ng's *Machine Learning Yearning*)
6. How does this compared with a **baseline** model?
    - Have we tried to use some common algorithm to build a model that can be used as a baseline?
    - How different is the current model's performance compared to the baseline model?

## Identifying Problems



### Bias and Variance Analysis

(Refer to Andrew Ng's definition of bias and variance)

Overfitting
Underfitting


### Error Analysis

Error analysis refers to the process of examining the 
A largely overlooked step in debugging a machine learning model 

What kind of errors does the model usually made?
Which class is more likely to have errors?


## Actions to be Taken


### On the Dataset

Collect more samples?
Generate synthetic data samples using data augmentation?


### On the Features

Feature selection

### On the Learning Algorithms

Changing the learning rate?



## References

- Pedro Domingos. 2012. [A few useful things to Know about machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf). Communications of the ACM.
- Andrew Ng's [slides](https://media.nips.cc/Conferences/2016/Slides/6203-Slides.pdf) at NIPS 2016
- Andrew Ng. 2018. [Machine Learning Yearning](https://d2wvfoqc9gyqzf.cloudfront.net/content/uploads/2018/09/Ng-MLY01-13.pdf)
- Andrew Ng. [Advice for applying Machine Learning](http://cs229.stanford.edu/materials/ML-advice.pdf)


