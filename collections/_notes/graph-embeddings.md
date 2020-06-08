---
layout: article
title:  "Graph Emebeddings"
tags: [machine learning, graphs, embeddings]
---

Graph embeddings are the transformation of property graphs to a vector or a set of vectors.

Similar to word embeddings, which are vector representation of words.

Two major types of graph embeddings:

1. Vertex Embeddings
Each vertex has its own vector representation. Two vertices with similar properties (e.g. similar neighbours, similar connection types, etc.) should have vectors close to each other.

2. Graph Embeddings
Represent the whole graph as a single vector


## Vertex Embeddings

Common methods

DeepWalk

implementation: https://github.com/phanein/deepwalk

"DeepWalkuses local information obtained from truncated random walks tolearnlatent representations by treating walks as the  equivalent of sentences."

learns social representations of a graph's vertices
social representations are latent features of the vertices that capture neighbourhood similarity and community membership.





node2vec

SDNE


## Graph Embeddings



## Collective Classification

According to Sen et al., Give a network and an object $o$ in the network, three types of correlations can be utilized to determine the label of $o$:

1. Correlations between the label of $o$ and the attributes of $o$
2. Correlations between the label of $o$ and the attributes of the objects in the neighbourhood of $o$
3. Correlations between the label of $o$ and the unobserved labels of the objects in the neighbourhood of $o$

Collective classification refers to the combined classification of a set of interlinked objects using all three types of information described above.

Applications: classification of webpages



- Prithviraj Sen, Galileo Namata, Mustafa Bilgic, Lise Getoor, Brian Gallagher, Tina Eliassi-Rad. [Collective Classification in Network Data](http://eliassi.org/papers/ai-mag-tr08.pdf). 



## References

tutorial
https://towardsdatascience.com/graph-embeddings-the-summary-cc6075aba007

- Bryan Perozzi, Rami Al-Rfou, Steven Skiena. [DeepWalk: Online Learning of Social Representations](https://arxiv.org/abs/1403.6652)


papers with code - graph embedding:
https://paperswithcode.com/task/graph-embedding
