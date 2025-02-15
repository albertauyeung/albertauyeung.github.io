---
title:  "🐍 Effortlessly Create N-Grams from Text in Python"
tags: [python, nlp, nltk]
weight: -20180603
url: /2018/06/03/generating-ngrams.html
date: 2018-06-03
---

[N-grams](https://en.wikipedia.org/wiki/N-gram) are contiguous sequences of n-items in a sentence. N can be 1, 2 or any other positive integers, although usually we do not consider very large N because those n-grams rarely appears in many different places.

When performing machine learning tasks related to natural language processing, we usually need to generate n-grams from input sentences. For example, in text classification tasks, in addition to using each individual token found in the corpus, we may want to add bi-grams or tri-grams as features to represent our documents. This post describes several different ways to generate n-grams quickly from input sentences in Python.

<!--more-->

## The Pure Python Way

In general, an input sentence is just a string of characters in Python. We can use build in functions in Python to generate n-grams quickly. Let's take the following sentence as a sample input:

```python
s = """
    Natural-language processing (NLP) is an area of
    computer science and artificial intelligence
    concerned with the interactions between computers
    and human (natural) languages.
"""
```

If we want to generate a list of bi-grams from the above sentence, the expected output would be something like below (depending on how do we want to treat the punctuations, the desired output can be different):

```python
[
    "natural language",
    "language processing",
    "processing nlp",
    "nlp is",
    "is an",
    "an area",
    ...
]
```

The following function can be used to achieve this:
    
```python
import re

def generate_ngrams(s, n):
    # Convert to lowercases
    s = s.lower()
    
    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    
    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]
    
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[token[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]
```

Applying the above function to the sentence, with `n=5`, gives the following output:

```python
>>> generate_ngrams(s, n=5)
['natural language processing nlp is',
 'language processing nlp is an',
 'processing nlp is an area',
 'nlp is an area of',
 'is an area of computer',
 'an area of computer science',
 'area of computer science and',
 'of computer science and artificial',
 'computer science and artificial intelligence',
 'science and artificial intelligence concerned',
 'and artificial intelligence concerned with',
 'artificial intelligence concerned with the',
 'intelligence concerned with the interactions',
 'concerned with the interactions between',
 'with the interactions between computers',
 'the interactions between computers and',
 'interactions between computers and human',
 'between computers and human natural',
 'computers and human natural languages']
```

The above function makes use of the `zip` function, which creates a generator that aggregates elements from multiple lists (or iterables in genera). The blocks of codes and comments below offer some more explanation of the usage:

```python
# Sample sentence
s = "one two three four five"

tokens = s.split(" ")
# tokens = ["one", "two", "three", "four", "five"]

sequences = [tokens[i:] for i in range(3)]
# The above will generate sequences of tokens starting
# from different elements of the list of tokens.
# The parameter in the range() function controls
# how many sequences to generate.
#
# sequences = [
#   ['one', 'two', 'three', 'four', 'five'],
#   ['two', 'three', 'four', 'five'],
#   ['three', 'four', 'five']]

bigrams = zip(*sequences)
# The zip function takes the sequences as a list of inputs
# (using the * operator, this is equivalent to
# zip(sequences[0], sequences[1], sequences[2]).
# Each tuple it returns will contain one element from
# each of the sequences.
# 
# To inspect the content of bigrams, try:
# print(list(bigrams))
# which will give the following:
#
# [
#   ('one', 'two', 'three'),
#   ('two', 'three', 'four'),
#   ('three', 'four', 'five')
# ]
#
# Note: even though the first sequence has 5 elements,
# zip will stop after returning 3 tuples, because the
# last sequence only has 3 elements. In other words,
# the zip function automatically handles the ending of
# the n-gram generation.
```


## Using NLTK

Instead of using pure Python functions, we can also get help from some natural language processing libraries such as the [Natural Language Toolkit (NLTK)](https://www.nltk.org/). In particular, nltk has the `ngrams` function that returns a generator of n-grams given a tokenized sentence. (See the documentaion of the function [here](http://www.nltk.org/api/nltk.html#nltk.util.ngrams))

```python
import re
from nltk.util import ngrams

s = s.lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 5))
```

The above block of code will generate the same output as the function `generate_ngrams()` as shown above.

