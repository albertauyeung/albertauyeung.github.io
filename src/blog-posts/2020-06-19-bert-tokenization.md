---
layout: default
route: /2020/06/19/bert-tokenization.html
date: 2020-06-19
tags:
  - python
  - machine learning
  - nlp
  - deep learning
  - bert
icon: dot
order: 20200619
---

# BERT - Tokenization and Encoding

To use a pre-trained BERT model, we need to convert the input data into an appropriate format so that each sentence can be sent to the pre-trained model to obtain the corresponding embedding. This article introduces how this can be done using modules and functions available in Hugging Face's `transformers` package ([https://huggingface.co/transformers/index.html](https://huggingface.co/transformers/index.html)).

## Input Representation in BERT

Let's first try to understand how an input sentence should be represented in BERT. BERT embeddings are trained with two training tasks:
1. **Classification Task**: to determine which category the input sentence should fall into
2. **Next Sentence Prediction Task**: to determine if the second sentence naturally follows the first sentence.

### The `[CLS]` and `[SEP]` Tokens

For the classification task, a **single** vector representing the whole input sentence is needed to be fed to a classifier. In BERT, the decision is that the hidden state of the **first token** is taken to represent the whole sentence. To achieve this, an additional token has to be added manually to the input sentence. In the original implementation, the token `[CLS]` is chosen for this purpose.

In the "next sentence prediction" task, we need a way to inform the model where does the **first sentence end**, and where does the **second sentence begin**. Hence, another artificial token, `[SEP]`, is introduced. If we are trying to train a classifier, each input sample will contain only one sentence (or a single text input). In that case, the `[SEP]` token will be added to the end of the input text.

In summary, to preprocess the input text data, the first thing we will have to do is to add the `[CLS]` token at the beginning, and the `[SEP]` token at the end of each input text.

### Padding Token `[PAD]`

The BERT model receives a fixed length of sentence as input. Usually the maximum length of a sentence depends on the data we are working on. For sentences that are shorter than this maximum length, we will have to add paddings (empty tokens) to the sentences to make up the length. In the original implementation, the token `[PAD]` is used to represent paddings to the sentence.

### Converting Tokens to IDs

When the BERT model was trained, each token was given a **unique ID**. Hence, when we want to use a pre-trained BERT model, we will first need to convert each token in the input sentence into its corresponding unique IDs.

There is an important point to note when we use a pre-trained model. Since the model is pre-trained on a certain corpus, the **vocabulary** was also fixed. In other words, when we apply a pre-trained model to some other data, it is possible that some tokens in the new data might not appear in the fixed vocabulary of the pre-trained model. This is commonly known as the **out-of-vocabulary (OOV)** problem.

For tokens not appearing in the original vocabulary, it is designed that they should be replaced with a special token `[UNK]`, which stands for **unknown** token.

However, converting all unseen tokens into `[UNK]` will take away a lot of information from the input data. Hence, BERT makes use of a **WordPiece** algorithm that breaks a word into several *subwords*, such that commonly seen subwords can also be represented by the model.

For example, the word `characteristically` does not appear in the original vocabulary. Nevertheless, when we use the BERT tokenizer to tokenize a sentence containing this word, we get something as shown below:

```python
>>> from transformers import BertTokenizer
>>> tz = BertTokenizer.from_pretrained("bert-base-cased")
>>> tz.convert_tokens_to_ids(["characteristically"])
[100]

>>> sent = "He remains characteristically confident and optimistic."
>>> tz.tokenize(sent)
['He',
 'remains',
 'characteristic',
 '##ally',
 'confident',
 'and',
 'optimistic',
 '.']

>>> tz.convert_tokens_to_ids(tz.tokenize(sent))
[1124, 2606, 7987, 2716, 9588, 1105, 24876, 119]
```

We can see that the word `characteristically` will be converted to the ID `100`, which is the ID of the token `[UNK]`, if we do not apply the tokenization function of the BERT model.

The BERT tokenization function, on the other hand, will first breaks the word into two subwoards, namely `characteristic` and `##ally`, where the first token is a more commonly-seen word (prefix) in a corpus, and the second token is prefixed by two hashes `##` to indicate that it is a suffix following some other subwords.

After this tokenization step, all tokens can be converted into their corresponding IDs.


### Summary

In summary, an input sentence for a **classification task** will go through the following steps before being fed into the BERT model.

1. Tokenization: breaking down of the sentence into tokens
2. Adding the `[CLS]` token at the beginning of the sentence
3. Adding the `[SEP]` token at the end of the sentence
4. Padding the sentence with `[PAD]` tokens so that the total length equals to the maximum length
5. Converting each token into their corresponding IDs in the model

An example of preparing a sentence for input to the BERT model is shown below. For simplicity, we assume the maximum length is 10 in the example below (while in the original model it is set to be 512).

```markdown
# Original Sentence
Let's learn deep learning!

# Tokenized Sentence
['Let', "'", 's', 'learn', 'deep', 'learning', '!']

# Adding [CLS] and [SEP] Tokens
['[CLS]', 'Let', "'", 's', 'learn', 'deep', 'learning', '!', '[SEP]']

# Padding
['[CLS]', 'Let', "'", 's', 'learn', 'deep', 'learning', '!', '[SEP]', '[PAD]']

# Converting to IDs
[101, 2421, 112, 188, 3858, 1996, 3776, 106, 102, 0]
```


## Tokenization using the transformers Package

While there are quite a number of steps to transform an input sentence into the appropriate representation, we can use the functions provided by the `transformers` package to help us perform the tokenization and transformation easily. In particular, we can use the function `encode_plus`, which does the following in one go:

1. Tokenize the input sentence
2. Add the `[CLS]` and `[SEP]` tokens.
3. Pad or truncate the sentence to the maximum length allowed
4. Encode the tokens into their corresponding IDs
Pad or truncate all sentences to the same length.
5. Create the attention masks which explicitly differentiate real tokens from `[PAD]` tokens

The following codes shows how this can be done.

```python
# Import tokenizer from transformers package
from transformers import BertTokenizer

# Load the tokenizer of the "bert-base-cased" pretrained model
# See https://huggingface.co/transformers/pretrained_models.html for other models
tz = BertTokenizer.from_pretrained("bert-base-cased")

# The senetence to be encoded
sent = "Let's learn deep learning!"

# Encode the sentence
encoded = tz.encode_plus(
    text=sent,  # the sentence to be encoded
    add_special_tokens=True,  # Add [CLS] and [SEP]
    max_length = 64,  # maximum length of a sentence
    pad_to_max_length=True,  # Add [PAD]s
    return_attention_mask = True,  # Generate the attention mask
    return_tensors = 'pt',  # ask the function to return PyTorch tensors
)

# Get the input IDs and attention mask in tensor format
input_ids = encoded['input_ids']
attn_mask = encoded['attention_mask']
```

After executing the codes above, we will have the following content for the `input_ids` and `attn_mask` variables:

```python
>>> input-ids
tensor([[ 101, 2421,  112,  188, 3858, 1996, 3776,  106,  102,    0,    0,    0,
            0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
            0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
            0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
            0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
            0,    0,    0,    0]])
>>>
>>> attn_mask
tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
```

The **"attention mask"** tells the model which tokens should be attended to and which (the `[PAD]` tokens) should not (see the [documentation](https://huggingface.co/transformers/glossary.html#attention-mask) for more detail). It will be needed when we feed the input into the BERT model.


## Reference

- Devlin et al. 2018. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
- BERT - transformers documentation: [https://huggingface.co/transformers/model_doc/bert.html](https://huggingface.co/transformers/model_doc/bert.html)


