---
layout: article
title:  "Information Retrieval"
tags: [information retrieval]
---

## Similarity Measures

Let documents be represented by term vectors in the following form: $D_i = (t_1, t_2, ..., t_n)$.

- **Dice coefficient**: 
$
Sim(D_i,D_j) = \frac{2 \times (D_i \cdot D_j)}{||D_i|| + ||D_j||} \quad \quad
\textrm{For sets:} \quad Sim(X,Y) = \frac{2 \times |X \cap Y|}{|X| + |Y|}
$
- **Jaccard coefficient**:
$
Sim(D_i,D_j) = \frac{D_i \cdot D_j}{||D_i|| + ||D_j|| - D_i \cdot D_j} \quad \quad
\textrm{For sets:} \quad Sim(X,Y) = \frac{|X \cap Y|}{|X| + |Y| - |X \cap Y|} = \frac{|X \cap Y|}{|X \cup Y|}
$
- **Cosine coefficient**:
$
Sim(D_i,D_j) = \frac{D_i \cdot D_j}{|D_i| \times |D_j|}
$


## Evaluation

The purpose of evaluation (Keen 1971):

- The need for measures with which to make merit comparisons within a single test situation
- The need for measures with which to make comparisons between results obtained in different test situations
- The need for assessing the merit of a real-life system.

To measure IR effectivenes in a standard way, we need a test collection consists of:

1. A document collection
2. A test suite of information needs, expressible as querys
3. A set of relevance judgement (e.g. a binary assessment of either relevant or non-relevant for each query-document pair.

- **Gold standard / Ground Truth**: a binary classification of a document as either relevant or non-relevant in the collection
- **Relevance**: for assessing relative to information need, NOT a query.
- **Standard test collections** (see Manning et al. (2008) pp.153-154):
    - [Cranfield](http://ir.dcs.gla.ac.uk/resources/test_collections/cran/): 1398 abstracts of aerodynamics journal articles, a set of 225 queries, and relevance judgments of all pair; too small nowadays for evaluation.
    - TREC (Test Retrieval Conference)
- Lancaster (1979) suggested that statistics of documents in an IR system can be summarised in a 2 x 2 matrix:
    - **Precision**: The proportion of retrieved documents that are relevant: $P = \frac{TP}{TP + FP}$
    - **Recall**: The proportion of relevant documents retrieved: $R = \frac{TP}{TP + FN}$
    - **Fallout**: The proportion of non-relevant documents retrieved: $F = \frac{FP}{FP + TN}$
    - **Accuracy**: The fraction of correctly classified documents: $Accuracy = \frac{TP + TN}{TP + FP + TN + FN}$

|               | Relevant               | Not Relevant           |
|---------------|------------------------|------------------------|
| Retrieved     | True Positive<br>(TP)  | False Positive<br>(FP) |
| Not Retrieved | False Negative<br>(FN) | True Negative<br>(TN)  |

- **Weakness of accuracy**: It is not appropriate because in almost all circumstances, the data is extremely skewed: over 99.9% of the documents are in the non-relevant category. A system aims at maximising accuracy can appear to perform well by simply deeming all documents as irrelevant. However, it is totally unsatisfying for the system to label everything as non-relevant because users always want to see some documents, and can be assumed to have a certain tolerance for seeing some false positive. (Manning et al., p.155)
- **Generality**: The proportion of relevant documents per query: $G = \frac{TP + FN}{TP + FP + TN + FN}$
- **F-measure**: A combined measure which assesses the tradeoff between precision and recall. It is a weighted harmonic mean. In its general form, it is defined as: $F = \frac{1}{\alpha \frac{1}{P} + (1 - \alpha) \frac{1}{R}} = \frac{(\beta^2 + 1)PR}{\beta^2 P + R}$, where $\beta = \frac{1 - \alpha}{\alpha}$, $\alpha \in [0,1]$. A balanced measure with equal weights on precision and recall is called an $F_1$ measure: $F_1 = \frac{2 \times P \times R}{P + R}$

### Why harmonic mean is used?

As we can always achieve 100% recall if we return all the documents, an arithmetic mean of $P$ and $R$ can at least achieve 50% in this case. This suggests that it is an unsuitable measure. The harmonic mean, on the other hand, returns a value closer to the minimum of two numbers than arithmetic or geometric means. (Manning et al., pp.156-157)

- Limitations of precision and recall (Chowdhury 2004, pp.251-252)
    - Different users may want different levels of recall , but users are often unable to specify exactly how many items they want to be retrieved
    - Recall assumes that all relevant documents have the same value (importance), which is not always true. Different documents have different degrees of relevance.

## References

- Manning, D. C., Raghavan, P., and SchutzeIntroduction H. (2008) [Introduction to Information Retrieval](http://nlp.stanford.edu/IR-book/html/htmledition/irbook.html). Cambridge, UK: Cambridge University Press.
- Chowdhury, G. G. (2004) Introduction to Modern Information Retrieval, 2nd Edition. London: Facet Publishing.
- Keen, E. M. (1971) 'Evaluation parameters'. In: Salton, G. (ed.), The SMART retrieval system: experiments in automatic document processing. Englewood Cliffs, NJ: Prentice-Hall, pp.74-111.
- Lancaster, F. W. (1979) Information retrieval systems: characteristics, testing and evaluation. New York: John Wiley.
- van Rijsbergen, C. J. (1979) Information retrieval, 2nd Edition. London: Butterworth.
