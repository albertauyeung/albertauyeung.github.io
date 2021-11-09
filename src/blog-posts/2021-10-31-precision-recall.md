---
layout: default
route: /2021/10/31/precision-recall.html
date: 2021-10-31
tags:
  - machine learninng
  - evaluation metrics
  - statistics
icon: dot
order: 20211031
visibility: hidden
---

# Understanding Precision and Recall

A machine learning pipeline involves several major components, such as data clearning and preprocessing, modelling, model evaluation, and deployment. Obviously, each of these steps are very important to the overall outcome. However, I always think that **model evaluation** is the most important part, because:
1. It allows us to understand quantitatively **how good** the current method is doing
2. It informs us **how we can further improve** the outcome (e.g. by adding more data or by using a more sophisticated model)

This is why when I am an interviewer of a machine learning or data science role, I usually like to spend more time on discussing how one would evaluate a certain model, and what one can do when the metrics of interests have been computed. As many applications are classification tasks, naturally the discussion would involve talking about **precision** and **recall** (and other relatd classification metrics).

At times, I was surprised to learn that some candidates who claimed to have several years of data science or machine learning experience failed to correctly describe what precision and recall are and how they can be used to understand the performance of a model. Even when a candidate was able to give the definitions of these metrics, he or she was not always able to explain what they can do to improve the model given the results.

Indeed, while the definitions of precision and recall are straight-forward, they can be confusing sometimes when discussed together with other similar terms such as accuracy, specificity, sensitivity and F1 scores. Having a good understanding of these evaluation metrics not only would let you do better in interviews, but more importantly it will allow you to achieve better results in practical machine learning projects. I hope the follow discussion and explanations would help people understand more about these concepts.

## How Good is a Model?

Metrics are primarily used to understand how "good" a model is doing on the task it was trained to do. Before really dive into the definitions, let's consider a simple binary classification task and different models trained on the task.

In a binary classification task, an input is expected to be classified into either a positive (1) or a negative (0). Let's assume that we have 100 samples in our **test set**, in which 50 are positives and another 50 are negatives. (In practice, though, it is likely that we won't get equal amount of samples in every class.)

### Accuracy

When we apply a model on this test set, ideally we want the model to be able to label all positives as positives, and all negatives as negatives, which translates into **100% accuracy**, as illustrated in the figure below.

![](/assets/images/precision-recall-ideal-model.png)

Of course, in reality it is very difficult, if not impossible, to achieve 100% accuracy. It is more likely that we will have a model that makes mistakes by either labelling a positive as a negative or vice versa. For example, we can imagine that there is a Model A that wrongly labels 10 negatives as positives, and labels 10 positives as negatives, as illustrated in the figure below.

![](/assets/images/precision-recall-model-a.png)

**Accuracy** is defined as the ratio of correct predictions to the total number of predictions. Let's try to compute the accuracy of Model A. Firstly, let's further annotate the above figure to identify different types of predictions output by Model A:

![](/assets/images/precision-recall-model-a-annotated.png)

From this figure, we can easily identify the follow four types of predictions:
- **<span style="color: #dd8830">True positives (TP)</span>**: **40** positive samples are correctly labelled as positives
- **<span style="color: #990000">True negatives (TN)</span>**: **40** negative samples are correctly labelled as negative
- **<span style="color: #4285f4">False positives (FP)</span>**: **10** negative samples are wrongly labelled as positives
- **<span style="color: #0097a7">False negatives (FN)</style>**: **10** positive samples are wrongly labelled as negatives

Hence, the accuracy of **Model A** is:

$$
\frac{(TP + TN)}{(TP + TN + FP + FN)} = \frac{(40 + 40)}{(40 + 40 + 10 + 10)}  = 80\%
$$

Now consider another model (**Model B**) that outputs also 50 positive predictions, but it wrongly labels 20 negatives as positives, as illustrated in the figure below. Similarly, we can compute its accuracy by using the formula above:

$$
\frac{(30 + 30)}{(30 + 30 + 20 + 20)} = 60\%
$$

![](/assets/images/precision-recall-model-b.png)

Hence, we can conclude that Model A performs better than Model B in terms of accuracy on the test set.


### Accuracy's Limitations

While accuracy is useful, it has its limitation. For instance, we cannot understand a model's capability to identify **as many positives as possible**. We can illustrate this concept by consider another model as follows. Let's say we have another model (**Model C**) that, when applied to the test set, outputs 30 positive predictions, and labelled the rest as negatives (see figure below).

![](/assets/images/precision-recall-model-c.png)

Based on the figure above, we can count the number of true/false positives/negatives:

|||TP
20
|||TN
40
|||FP
10
|||FN
30
|||

Again, we can compute the **Model C**'s accuracy by using the formula:

$$
\frac{(20 + 40)}{(20 + 40 + 10 + 30)} = 60\%
$$

We can see that although Model C's output is quite different from Model B's output, they both achieve $60\%$ accuracy. In other words, the two models' performance is indistinguisable from each other in terms of accuracy.

However, we can see that Model B's output may be more desirable in that it was able to return **more true positives**. For example, if this is a classifier for identifying photos showing a certain person's face, we will be able to retrieve more photos of interests by using Model B (30 photos) instead of using Model C (20 photos).

### Imbalanced Datasets

In addition to the scenario described above, accuracy is also not a good metric when we have an **imbalanced dataset**. In the examples above, we considered a test set with **equal numbers of positives and negatives**. In practice, the number of positives available can be much smaller than that of negatives (or vice versa). For instance, consider a blood test that is used to identify a rare disease. We can imagine that out of, say, a hundred patients, only a handful of them actually are positives.

To illustrate the problem of an imbalanced dataset, consider the example below. Let's say instead of having equal number of positives and negatives, we now have 90 negatives and only 10 positives in the test set.

![](/assets/images/precision-recall-imbalanced-dataset.png)

A model can easily achieve **90% accuracy** by simply label **everything as negatives** in the test set. Obviously, such a model is useless as it won't help us identify any positive.


## Classification Evaluation Metrics and Their Relations


## Precision and Recall in Multi-class Classification


## The Precision-Recall Curve

Given a trained model, we can still 


## Debugging ML Models with Precision and Recall


## Summary


## Refereces

1. Marina Sokolova & Guy Lapalme. [A systematic analysis of performance measures for classification tasks](http://rali.iro.umontreal.ca/rali/sites/default/files/publis/SokolovaLapalme-JIPM09.pdf). Information Processing and Management 45 (2009) 427–437.
