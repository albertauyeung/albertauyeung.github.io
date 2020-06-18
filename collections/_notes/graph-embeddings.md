---
layout: article
title:  "Graph Emebeddings"
tags: [machine learning, graphs, embeddings]
---

Notes on graph embeddings, major references are:
- Hamilton et al. 2018. [Representation Learning on Networks](http://snap.stanford.edu/proj/embeddings-www/) WWW 2018 Tutorial
- Primož Godec. 2018. [Graph Embeddings — The Summary](https://towardsdatascience.com/graph-embeddings-the-summary-cc6075aba007)

## What is Graph Embeddings?

- Graph embeddings are the transformation of property graphs to a vector or a set of vectors.
- Similar to word embeddings, which are vector representation of words.
- Two major types of graph embeddings:
    1. Vertex Embeddings - Each vertex has its own vector representation. Two vertices with similar properties (e.g. similar neighbours, similar connection types, etc.) should have vectors close to each other.
    2. Graph Embeddings - Represent the whole graph as a single vector

## Applications

There are many different machine learning tasks that are related to graphs and networks:
- **node classification**: predict the class of a node
- **link prediction**: predict whether two nodes are connected
- **community detection**: detect densely linked clusters of nodes
- **network similarity**: determine how similar two (sub)networks are



## Challenges

- Make sure that the embeddings describe well the properties of the graphs
- The speed of creating or learning the embeddings should not increase drastically with the size of the graph
- How to determine the number of dimensions of the embedding


## Node Embeddings

- Learn a representation of the nodes in the embedding space (where the number of dimensions is smaller than the number of nodes)
- The goal is to embed nodes such that similarity in the embedding space approximates similarity of the nodes in the network
- Steps to learn node embeddings
    1. Define an encoder (i.e. a mapping from nodes to vectors)
    2. Define a node similarity function (i.e. a measure of node similarity in the original network)
    3. Optimize the parameters such that $z_u^{\top}z_v$ approximates $similarity(u, v)$

### Different Approaches to Similarity

#### Adjacency-based Similarity

- References:
    - [Ahmed et al. 2013](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40839.pdf)
- Similarity function is just the edge weight between two nodes $u$ and $v$ in the original network
- We want to minimize the following loss function: $\mathcal{L} = \sum_{(u,v)\in V \times V} || z_u^{\top}z_v - A_{u,v}||^2$, where $A_{u,v}$ is the corresponding cell in the adjacency matrix
- Limitations:
    - $O(|V|^2)$ runtime (it must consider all node pairs)
    - It only considers direct and location connections

#### Multi-hop Similarity


#### Random Walk Approaches


### Methods

#### DeepWalk

- [DeepWalk: Online Learning of Social Representations](https://arxiv.org/abs/1403.6652)
- Implementation: [https://github.com/phanein/deepwalk](https://github.com/phanein/deepwalk)
- DeepWalk uses local information obtained from truncated random walks tolearnlatent representations by treating walks as the  equivalent of sentences.
- Steps:
    1. Sampling with random walks: about 32 to 64 random walks from each node will be performed
    2. Training skip-gram model: accept a vector representing one random walk of a node, predict the neighbour nodes (e.g. 20)
    3. Computing the embedding of each node

#### node2vec

- [node2vec: Scalable Feature Learning for Networks](https://cs.stanford.edu/~jure/pubs/node2vec-kdd16.pdf)
- A generalization of DeepWalk
- Parameters
    - **$p$ (return parameter)**: controls how likely the random walk would go back to the previous node
    - **$q$ (in-out parameter)**: controls how likely the random walk will visit new (undiscovered) nodes in the graph
- Random walks become 2nd order Markov chains
- Increase efficient sampling rate by reusing samples, for example:
    - Let $k$ be the number of steps we need to sample
    - We can perform a random walk of length $l > k$, such that we can generate samples for $l - k$ nodes at once
    - e.g. a random walk $\{u, s1, s2, s3, s4, s5\}$ results in $N(u) = \{s1, s2, s3\}$, $N(s1) = \{s2, s3, s4\}$, $N(s2) = \{s3, s4, s5\}$.
- DeepWalk can be considered as a special case of node2vec with $p = q = 1$

![](/assets/images/node2vec_01.png)

#### Structural Deep Network Embedding (SDNE)

- [Structural Deep Network Embedding](https://www.kdd.org/kdd2016/papers/files/rfp0191-wangAemb.pdf)
- Implementation: [https://github.com/suanrong/SDNE](https://github.com/suanrong/SDNE)
- Does not perform random walks
- Designed to preserve the first and second order proximity:
    - **First order proximity**: local pairwise similarity between nodes linked by an edge, characterise local network sturcture (e.g. if a paper cites another paper, they address similar topics)
    - **Second order proximity**: indicate the similarity of the nodes' neighbourhood structures; if two nodes share many neighbours, they tend to be similar to each other
- SDNE is semi-supervised:
    - The unsupervised component: to learn a representation to reconstruct the second order proximity of nodes
    - The supervised component: to learn a representation that preserves the first order proximity of nodes

![](/assets/images/sdne_network.png)


## Graph Embeddings

### Graph2vec

- [graph2vec: Learning Distributed Representations of Graphs](https://arxiv.org/abs/1707.05005)
- Implementation: [https://github.com/benedekrozemberczki/graph2vec](https://github.com/benedekrozemberczki/graph2vec)




## Collective Classification

According to Sen et al., Give a network and an object $o$ in the network, three types of correlations can be utilized to determine the label of $o$:

1. Correlations between the label of $o$ and the attributes of $o$
2. Correlations between the label of $o$ and the attributes of the objects in the neighbourhood of $o$
3. Correlations between the label of $o$ and the unobserved labels of the objects in the neighbourhood of $o$

Collective classification refers to the combined classification of a set of interlinked objects using all three types of information described above.

Applications: classification of webpages



- Prithviraj Sen, Galileo Namata, Mustafa Bilgic, Lise Getoor, Brian Gallagher, Tina Eliassi-Rad. [Collective Classification in Network Data](http://eliassi.org/papers/ai-mag-tr08.pdf). 



## References

### Research Papers

- William L. Hamilton, Rex Ying, Jure Leskovec. 2017. [Representation Learning on Graphs: Methods and Applications](https://arxiv.org/abs/1709.05584). IEEE Data Engineering Bulletin, September 2017.
- Amr Ahmed et al. 2013. [Distributed Large-scale Natural Graph Factorization](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40839.pdf). WWW 2013.
- Bryan Perozzi, Rami Al-Rfou, Steven Skiena. [DeepWalk: Online Learning of Social Representations](https://arxiv.org/abs/1403.6652)
- Aditya Grover, Jure Leskovec. 2016. [node2vec: Scalable Feature Learning for Networks](https://cs.stanford.edu/~jure/pubs/node2vec-kdd16.pdf). KDD 2016.
- Daixin Wang, Peng Cui, Wenwu Zhu. 2016. [Structural Deep Network Embedding](https://www.kdd.org/kdd2016/papers/files/rfp0191-wangAemb.pdf). KDD 2016.
- Annamalai Narayanan et al. 2017. [graph2vec: Learning Distributed Representations of Graphs](https://arxiv.org/abs/1707.05005). MLGWorkshop 2017.

### Blogs and Articles

- Alessandro Epasto and Bryan Perozzi. 2019. [Innovations in Graph Representation Learning](https://ai.googleblog.com/2019/06/innovations-in-graph-representation.html)
- Primož Godec. 2018. [Graph Embeddings — The Summary](https://towardsdatascience.com/graph-embeddings-the-summary-cc6075aba007)


### Tutorials

- Hamilton et al. 2018. [Representation Learning on Networks](http://snap.stanford.edu/proj/embeddings-www/) WWW 2018 Tutorial.


### Source Codes

- [Papers with code - graph embedding](https://paperswithcode.com/task/graph-embedding)

