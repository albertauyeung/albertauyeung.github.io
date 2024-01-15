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

One can imagine that a model can easily achieve **90% accuracy** by simply label **everything as negatives** in the test set. Obviously, such a model is useless as it won't help us identify any positive, even though the accuracy looks impressive.

### Precision and Recall

As we can see from the discussion above, accuracy alone does not give us a full picture of **how good** our models are. We need some other measures that would allow us to understand how good a model is in identifying true postives and avoiding false positives. This is where **precision** and **recall** come into the scene.

**Precision**, by definition, is the **ratio of true positives to all the samples that are labelled positives by the model**. For example, if a model labels 10 samples as positives, and out of which 8 of them are true positives, then the model's precision would be 80%. In other words, it's the **percentage of attempts that hit the target**. It can be computed by the following formula:

$$
Precision = \frac{TP}{TP + FP}
$$

On the other hannd, **recall** is defined as the percentage of all positives that are correctly identified by the model. It measures the ability of the model to pick up positives. For example, if there are 10 positives in the test set, and the model is able to correctly label 8 of them as positives, then the model has 80% recall. It's formula is given by:

$$
Recall = \frac{TP}{TP + FN}
$$

In the field of [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval), precision is used to measure how relevant the search results are, and recall is used to measure how many truly relevant results are retrieved.

Given their definitions, we can now apply them to the examples we discussed above and see how they help us to better understand the performance of the models (Models B and C in particular) we discussed above:

Model  | Precision  | Recall
---    | ---        | ---
Model B | 30 / (30 + 20) = 60% | 30 / (30 + 20) = 60%
Model C | 20 / (20 + 10) = 67% | 20 / (20 + 30) = 40%

We can see that even though the two models' accuracy scores are the same, they have different precision and recall scores. Model C is more **precise**, but is **not able to recall** as many positives as Model B. Depending on the requirements on the final output, we can then determine which model to use. For example, if we have to decide on whether to put Model B or Model C into production:

- If we want a model that **makes fewer mistakes** when trying to identify a positive, we would prefer **Model C**
- If we want a model that is able to **identify as many positives as possible**, we would prefer **Model B**

For imbalance datasets such as the one we mentioned above (with 10 positives and 90 negatives), precision and recall are much more useful than accuracy. For example, for a model that labels everything as **negatives**, its performance metrics will be:
- **Accuracy**: **90%**
- **Precision**: This is **undefined**, as the model does not output any positive samples (there are no true positives or false positives), and thus the denominator is zero.
- **Recall**: **0%**, as there isn't any sample labelled as positive.

As a result, we can see that even though such a model achieves high accuracy, both the precision and recall scores are problematic, suggesting that something is wrong about the model.

## Trade-off and the Precision-Recall Curve

For many classification models, the prediction usually comes with a score. Take [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) as an example, the output of the model is given by the formula:

$$
score = \sigma(w^TX + b)
$$

where $b$ is the bias term, $w$ is the vector of parameters or weights of the features, $X$ is the input feature vector, and $\sigma$ is the sigmoid function given by

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

The output of the sigmoid function is always between 0 and 1. Usually, the final label of input $X$ is determined by the following rule:

$$
\hat{y} = 
\begin{cases}
1 \quad \text{if } score >= 0.5\\
0 \quad \text{otherwise}
\end{cases}
$$

We can imagine that if the threshold of 0.5 is changed to another value, the output of the model on the same test set will be different:
- If we **increase** the threshold, we would expect the model to output **fewer positive labels**
- If we **decrease** the threshold, we would expect the model to output **more positive labels**

In other words, the value of the threshold is closely related to the precision and recall scores of the model on a test set. In general:
- With a higher threshold, the model will achieve higher precision and lower recall
- With a lower threshold, the model will achieve lower precision and higher recall

This is what is commonly referred to as the **precision-recall tradeoff**. 

### An Example

The **precision-recall tradeoff** can be easily explained by plotting the precision and recall scores against the threshold value. Let's take a look at the example below.

We take the [Titanic dataset](https://www.kaggle.com/c/titanic) and build a simple classification model using the decision tree algorithm to predict whether a passenger survived in the end based on his or her gender and age.

The following figure shows how precision and recall of the trained model change as we vary the **decision threshold**. We can see that as the threshold increases, the precision score rises and recall score drops.

![](/assets/images/precision-recall-changing-threshold.png)

### Precision-Recall Curve




## Other Classification Metrics

In addition to precision and recall, there are quite a number of other metrics for measuring the performance of a classification model. The table below summarises some of the commonly used ones.

Metric | Formula | Description
---    | ---     | ---
**Specificity** | $\frac{TN}{FP + TN}$ | This is also called the true negative rate, which refers to the ability of the model to identify true negatives. This is actually equivalent to the recall of the negative class.
**Sensitivity** | $\frac{TP}{TP + FN}$ | This is the same as recall of the positive class as we discussed above.
**F-Score** | |
**AUC** | |

## Precision and Recall in Multi-class Classification



## Debugging ML Models with Precision and Recall


## Summary


## Refereces

1. Marina Sokolova & Guy Lapalme. [A systematic analysis of performance measures for classification tasks](http://rali.iro.umontreal.ca/rali/sites/default/files/publis/SokolovaLapalme-JIPM09.pdf). Information Processing and Management 45 (2009) 427–437.
