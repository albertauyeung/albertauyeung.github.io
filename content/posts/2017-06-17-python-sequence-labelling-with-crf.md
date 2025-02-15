---
title:  "🔍 Performing Sequence Labelling using CRF in Python"
tags: [python, machine learning, sequence labelling, crf]
weight: -20170617
url: /2017/06/17/python-sequence-labelling-with-crf.html
date: 2017-06-17
---

In [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing), it is a common task to **extract words or phrases of particular types** from a given sentence or paragraph. For example, when performing analysis of a corpus of news articles, we may want to know which countries are mentioned in the articles, and how many articles are related to each of these countries.

<!--more-->

## Sequence Labelling in NLP

This is actually a special case of **sequence labelling** in NLP (others include [POS tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging) and [Chunking](https://en.wikipedia.org/wiki/Shallow_parsing)), in which the goal is to assign a label to each member in the sequence. In the case of identifying country names, we would like to assign a '*country*' label to words that form part of a country name, and a '*irrelevant*' label to all other words. For example, the following is a sentence broken down into tokens, and its desired output after the sequence labelling process:

```python
input = ["Paris", "is", "the", "capital", "of", "France"]
output = ["I", "I", "I", "I", "I", "C"]
```

where *I* means that the token of that position is an irrelevant word, and *C* means that the token of that position is a word that form part of a country name.

## Methods of Sequence Labelling

A simple, though sometimes quite useful, approach is to prepare a **dictionary** of country names, and look for these names in each of the sentences in the corpus. However, this method relies heavily on the comprehensiveness of the dictionary. While there is a limited number of countries, in other cases such as city names the number of possible entries in the dictionary can be huge. Even for countries, many countries may be referred to using different sequence of characters in different contexts. For example, the United States of America may be referred to in an article as *the USA*, *the States*, or simply *America*.

In fact, a person reading a news article would usually recognise that a word or a phrase refers to a country, even when he or she has not seen the name of that country before. The reason is that there are many differnt **cues** in the sentence or the whole article that can be used to determine whether a word or a phrase is a country name. Take the following two sentences as examples:

- Kerry travels to **Laos**'s capital, Vientiane, on Monday for meetings of foreign ministers from the 10-member Association of South East Asia Nations (ASEAN).
- The Governments of **Bolivia** and **Uruguay** will strengthen ties with a customs cooperation agreement to be in force on June 15th.

The first sentence implies that something called **Lao** has a capital, suggesting that **Lao** is a country. Similarly, in the second sentence we know that both **Bolivia** and **Uruguay** are countries as the news mentioned about their governments. In other words, the words around 'Lao', 'Bolivia' and 'Uruguay' provide clues as to whether they are country names.

## Conditional Random Field (CRF)

To take advantage of the surrounding context when labelling tokens in a sequence, a commonly used method is [conditional random field](https://en.wikipedia.org/wiki/Conditional_random_field) (CRF), first proposed by [Lafferty et al.](http://repository.upenn.edu/cgi/viewcontent.cgi?article=1162&context=cis_papers) in 2001. It is  a type of probabilistic graphical model that can be used to model sequential data, such as labels of words in a sentence.

This article is not intended to discuss the technical details of CRF. If you are interested, you are recommended to check out one of the following tutorials which provide very good explanation of how CRF works:

- [An Introduction to Conditional
Random Fields](http://homepages.inf.ed.ac.uk/csutton/publications/crftut-fnt.pdf) by Charles Sutton and Andrew McCallum
- [Introduction to Conditional Random Fields](http://blog.echen.me/2012/01/03/introduction-to-conditional-random-fields/) by Edwin Chen

In CRF, we will design a set of **feature functions** to extract features for each word in a sentence. During model training, CRF will try to determine the weights of different feature functions that will maximise the likelihood of the labels in the training data.

## Train CRF Model in Python

One of the commonly used CRF library is [CRFSuite implemented by Naoaki Okazaki](http://www.chokkan.org/software/crfsuite/) in C/C++. The library is already easy to use given its command line interface. A Python binding to CRFSuite, [pycrfsuite](https://github.com/scrapinghub/python-crfsuite) is available for using the API in Python. This Python module is exactly the module used in the POS tagger in the [nltk module](http://www.nltk.org/).

To demonstrate how pysrfsuite can be used to train a linear chained CRF sequence labelling model, we will go through an example using some data for *named entity recognition*.

### Named Entity Recogniton

To train a named entity recognition model, we need some labelled data. The dataset that will be used below is the **Reuters-128 dataset**, which is an English corpus in the NLP Interchange Format (NIF). It contains 128 economic news articles. The dataset contains information for **880** named entities with their position in the document and a URI of a [DBpedia](http://wiki.dbpedia.org/) resource identifying the entity. It was created by the [Agile Knowledge Engineering and Semantic Web research group at Leipzig University, Germany](http://aksw.org/About.html). More details can be found in [their paper](http://svn.aksw.org/papers/2014/LREC_N3NIFNERNED/public.pdf). 

In the following, we will use the XML verison of the dataset, which can be downloaded from [https://github.com/AKSW/n3-collection](https://github.com/AKSW/n3-collection). Below is some lines extracted from the XML data file:

```html
<document id="8">
    <documenturi>http://www.research.att.com/~lewis/Reuters-21578/15009</documenturi>
    <documentsource>Reuters-21578</documentsource>
    <textwithnamedentities>
    <namedentityintext uri="http://aksw.org/notInWiki/Home_Intensive_Care_Inc">Home Intensive Care Inc</namedentityintext>
    <simpletextpart> said it has opened a Dialysis at Home office in </simpletextpart>
    <namedentityintext uri="http://dbpedia.org/resource/Philadelphia">Philadelphia</namedentityintext>
    <simpletextpart>, its 12th nationwide.</simpletextpart>
    </textwithnamedentities>
</document>
```

The XML block shown above refers to one of the documents in the dataset. The semantics is self-explanatory. The document has a sentence 'Home Intensive Care Inc said it has opened a Dialysis at Home office in Philadelphia, its 12th nationwide', in which **Home Intensive Care Inc** and **Philadelphia** are labelled as named entities.

### Prepare the Dataset for Training

In order to prepare the dataset for training, we need to label every word (or token) in the sentences to be either *irrelevant* or part of a *named entity*. Since the data is in XML format, we can make use of [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the file and extract the data as follows:

```python
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
import codecs

# Read data file and parse the XML
with codecs.open("reuters.xml", "r", "utf-8") as infile:
    soup = bs(infile, "html5lib")

docs = []
for elem in soup.find_all("document"):
    texts = []

    # Loop through each child of the element under "textwithnamedentities"
    for c in elem.find("textwithnamedentities").children:
        if type(c) == Tag:
            if c.name == "namedentityintext":
                label = "N"  # part of a named entity
            else:
                label = "I"  # irrelevant word
            for w in c.text.split(" "):
                if len(w) > 0:
                    texts.append((w, label))
    docs.append(texts)
```

The result will be a list of documents, each of which contains a list of (word, label) tuples. For example:

```python
>>> doc[0][:10]
[('Paxar', 'N'),
 ('Corp', 'N'),
 ('said', 'I'),
 ('it', 'I'),
 ('has', 'I'),
 ('acquired', 'I'),
 ('Thermo-Print', 'N'),
  ...
```

### Generating Part-of-Speech Tags

To train a CRF model, we need to create features for each of the tokens in the sentences. One particularly useful feature in NLP is the [part-of-speech (POS) tags](https://en.wikipedia.org/wiki/Part-of-speech_tagging) of the words. They indicates whether a word is a noun, a verb or an adjective. (In fact, a POS tagger is also usually a trained CRF model.)

We can use [NLTK's POS tagger](http://www.nltk.org/book/ch05.html) to generate the POS tags for the tokens in our documents as follows:

```python
import nltk
data = []
for i, doc in enumerate(docs):

    # Obtain the list of tokens in the document
    tokens = [t for t, label in doc]

    # Perform POS tagging
    tagged = nltk.pos_tag(tokens)

    # Take the word, POS tag, and its label
    data.append([(w, pos, label) for (w, label), (word, pos) in zip(doc, tagged)])
```

The output of the above process will be a list of documents, each of which is a list of tuples with the word, its POS tag and its label:

```python
>>> data[0]
[('Paxar', 'NNP', 'N'),
 ('Corp', 'NNP', 'N'),
 ('said', 'VBD', 'I'),
 ('it', 'PRP', 'I'),
 ('has', 'VBZ', 'I'),
 ('acquired', 'VBN', 'I'),
 ('Thermo-Print', 'NNP', 'N'),
 ...
```

### Generating Features

Given the POS tags, we can now continue to generate more features for each of the tokens in the dataset. The features that will be useful in the training process depends on the task at hand. Below are some of the commonly used features for a word $w$ in named entity recognition:

- The word $w$ itself (converted to lowercase for normalisation)
- The prefix/suffix of $w$ (e.g. -ion)
- The words surrounding $w$, such as the previous and the next word
- Whether $w$ is in uppercase or lowercase
- Whether $w$ is a number, or contains digits
- The POS tag of $w$, and those of the surrounding words
- Whether $w$ is or contains a special character (e.g. hypen, dollar sign)

Below is a function for generating features for our documents. It takes a doc (in the form of a listof tuples as shown above), and an index (the $i$th document), and return the documents with features extracted. (A similar example can be found in [the repository of pyscrfsuite](https://github.com/scrapinghub/python-crfsuite/blob/master/examples/CoNLL%202002.ipynb).)

```python
def word2features(doc, i):
    word = doc[i][0]
    postag = doc[i][1]

    # Common features for all words
    features = [
        'bias',
        'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit(),
        'postag=' + postag
    ]

    # Features for words that are not
    # at the beginning of a document
    if i > 0:
        word1 = doc[i-1][0]
        postag1 = doc[i-1][1]
        features.extend([
            '-1:word.lower=' + word1.lower(),
            '-1:word.istitle=%s' % word1.istitle(),
            '-1:word.isupper=%s' % word1.isupper(),
            '-1:word.isdigit=%s' % word1.isdigit(),
            '-1:postag=' + postag1
        ])
    else:
        # Indicate that it is the 'beginning of a document'
        features.append('BOS')

    # Features for words that are not
    # at the end of a document
    if i < len(doc)-1:
        word1 = doc[i+1][0]
        postag1 = doc[i+1][1]
        features.extend([
            '+1:word.lower=' + word1.lower(),
            '+1:word.istitle=%s' % word1.istitle(),
            '+1:word.isupper=%s' % word1.isupper(),
            '+1:word.isdigit=%s' % word1.isdigit(),
            '+1:postag=' + postag1
        ])
    else:
        # Indicate that it is the 'end of a document'
        features.append('EOS')

    return features
```

### Training the Model

To train the model, we need to first prepare the training data and the corresponding labels. Also, to be able to investigate the accuracy of the model, we need to separate the data into training set and test set. Below are some codes for preparing the training data and test data, using the [`train_test_split` function in scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).

```python
from sklearn.model_selection import train_test_split

# A function for extracting features in documents
def extract_features(doc):
    return [word2features(doc, i) for i in range(len(doc))]

# A function fo generating the list of labels for each document
def get_labels(doc):
    return [label for (token, postag, label) in doc]

X = [extract_features(doc) for doc in data]
y = [get_labels(doc) for doc in data]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

In `pycrfsuite`, A CRF model in can be trained by first creating a **trainer**, and then submit the training data and corresponding labels to the trainer. After that, set the parameters and call `train()` to start the training process. For the complete list of parameters, one can refer to the [documentation of CRFSuite](http://www.chokkan.org/software/crfsuite/manual.html#idp8849114176). With the very small dataset in this example, the training with `max_iterations=200` can be finished in a few seconds. Below is the code for creating the trainer and start training the model:

```python
import pycrfsuite
trainer = pycrfsuite.Trainer(verbose=True)

# Submit training data to the trainer
for xseq, yseq in zip(X_train, y_train):
    trainer.append(xseq, yseq)

# Set the parameters of the model
trainer.set_params({
    # coefficient for L1 penalty
    'c1': 0.1,

    # coefficient for L2 penalty
    'c2': 0.01,  

    # maximum number of iterations
    'max_iterations': 200,

    # whether to include transitions that
    # are possible, but not observed
    'feature.possible_transitions': True
})

# Provide a file name as a parameter to the train function, such that
# the model will be saved to the file when training is finished
trainer.train('crf.model')
```

If you have set `verbose=True` when initialising the trainer, the trainer will print out the training progress as it is trained against the provided training data.

### Checking the Results

Once we have the model trained, we can apply it on our test data and see whether it gives reasonable results. Assuming that the model is saved to a file named `crf.model`. The following block of code shows how we can load the model into memory, and apply it on to our test data.

```python
tagger = pycrfsuite.Tagger()
tagger.open('crf.model')
y_pred = [tagger.tag(xseq) for xseq in X_test]

# Let's take a look at a random sample in the testing set
i = 12
for x, y in zip(y_pred[i], [x[1].split("=")[1] for x in X_test[i]]):
    print("%s (%s)" % (y, x))

'''
The following will be printed:

sci-med (N)
life (N)
systems (N)
inc (N)
said (I)
its (I)
directors (I)
approved (I)
a (I)
previously (I)
...
'''
```

The result looks reasonable as the first four words are correctly identified as part of a named entity.

To study the performance of the CRF tagger trained above in a more quantitative way, we can check the **precision** and **recall** on the test data. This can be done very easily using the [`classification_report` function in scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html). However, given that the predictions are sequences of tags, we need to transform the data into a list of labels before feeding them into the function.

```python
import numpy as np
from sklearn.metrics import classification_report

# Create a mapping of labels to indices
labels = {"N": 1, "I": 0}

# Convert the sequences of tags into a 1-dimensional array
predictions = np.array([labels[tag] for row in y_pred for tag in row])
truths = np.array([labels[tag] for row in y_test for tag in row])

# Print out the classification report
print(classification_report(
    truths, predictions,
    target_names=["I", "N"]))
```

which will prints a report as follows:

```python
              precision   recall  f1-score   support
          I       0.98      0.98      0.98      3322
          N       0.85      0.85      0.85       405
avg / total       0.97      0.97      0.97      3727
```

We can see that we have achieved 85% precision and 85% recall in predicting whether a word is part of a named entity. There are several things by which we can improve the performance, including creating better features or tuning the parameters of the CRF model.

### Source Codes

The source code for reproducing the above results can be found in the following github repository: [https://github.com/albertauyeung/python-crf-named-entity-recognition](https://github.com/albertauyeung/python-crf-named-entity-recognition).

## References

- Lafferty, J., McCallum, A., Pereira, F. (2001). ["Conditional random fields: Probabilistic models for segmenting and labeling sequence data"](http://repository.upenn.edu/cgi/viewcontent.cgi?article=1162&context=cis_papers). Proc. 18th International Conf. on Machine Learning. Morgan Kaufmann. pp. 282–289.
- Erdogan, H. (2010). [Sequence Labeling: Generative and Discriminative Approaches - Hidden Markov Models, Conditional Random Fields and Structured SVMs](http://www.icmla-conference.org/icmla10/CFP_Tutorial_files/hakan.pdf). ICMLA 2010 Tutorial.
