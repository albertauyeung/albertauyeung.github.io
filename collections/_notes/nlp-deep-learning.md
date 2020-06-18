---
layout: article
title:  "Deep Learning for NLP"
tags: [nlp, deep learning, machine learning]
---

## Word Vectors



## Sequence-to-Sequence Models


## The Transformer

- [Attention is all you need](https://arxiv.org/abs/1706.03762)
- [Transformer: A Novel Neural Network Architecture for Language Understanding ](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)
- [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html) by Alexander Rush (PyTorch implementation, paper available at [https://www.aclweb.org/anthology/W18-2509/](https://www.aclweb.org/anthology/W18-2509/))

### Architecture

- **Input --> Transformer --> Output**
- The Transformer contains:
    - **Encoders** (six stacked on top of one another)
    - **Decoders** (six stacked on top of one another)
    - **Connections** between the encoders and decoders
- Each encoder has **two** sub-layers:
    1. Self-attention
        - helps the encoder to **look at other words** in the input sentence as it encodes a specific word
    2. Feed forward neural network
- Each decoder has **three** sub-layers:
    1. Self-Attention
    2. Encoder-Decoder Attention
        - helps the decoder to focus on relevant parts of the input sentence
    3. Feed forward neural network

#### Self-Attention

- When the model is processing a word in the sentence, self-attention allows it to look at other positions in the input sequence for clues that can help encode this word
- **Three vectors** (of length 64) are created for each of the encoder's inputs
    - **Query**
    - **Key**
    - **Value**

![](/assets/images/bert_001.png)

- Referring to the figure above:
    - Multiplying $X_1$ by the $W_Q$ matrix results in $q_1$
    - Similarly we can obtain the other query/key/value vectors
    - They can be considered as differernt **projections** of the original word vectors
- To compute self-attention of a word in the sentence, we need to **score** each word of the input sentence **against** this word. It refers to the extent to which focus should be placed on other words when trying to encode the given word.
- Steps:
    - Multiple query vector with the key vector
    - Divide it by $\sqrt{d_k}$, the square root of the chosen number of dimensions of the key vector
    - Apply softmax on the results
    - Mupltiple by the value vector

$Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$

#### Multi-head Attention

- Maintain **multiple** attention modules by having multiple sets of $W_Q$/$W_K$/$W_V$ matrices
- Expands the model's ability to focus on different positions at the same time
- Achieve multiple "representation subspaces"


## Universal Language Model Fine-tuning for Text Classification (ULMFiT)

- Paper: [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146)


## BERT

- Paper: [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
- Code: [https://github.com/google-research/bert](https://github.com/google-research/bert)


## References

### Research Papers

- Ashish Vaswani et al. 2017. [Attention is all you need](https://arxiv.org/abs/1706.03762). NIPS 2017.
- Jeremy Howard, Sebastian Ruder. 2018. [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146). ACL 2018.

### Blogs and Articles

- Jay Alammar. 2018. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- Jay Alammar. 2018. [The Illustrated BERT, ELMo, and co. (How NLP Cracked Transfer Learning)](http://jalammar.github.io/illustrated-bert/)
- Jakob Uszkoreit, 2017. [Transformer: A Novel Neural Network Architecture for Language Understanding ](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html) on Google AI Blog
