---
title:  "⚡ Making pandas Operations Faster"
tags: [python, pandas]
weight: -20170708
url: /2017/07/08/fast-pandas-operation.html
date: 2017-07-08
---

[pandas](http://pandas.pydata.org/) is one of the most commonly used Python library in data analysis and machine learning. It is versatile and can be used to handle many different types of data. Before feeding a model with training data, one would most probably pre-process the data and perform feature extraction on data stored as pandas `DataFrame`. I have been using pandas extensively in my work, and have recently discovered that the time required to manipulate data stored in a `DataFrame` can vary hugely depending on the method you used.

<!--more-->

## Numerical Operations

To demonstrate the differences, let's generate some random data first. The following block of code will generate a `DataFrame` with 5,000 rows and 3 columns (`A`, `B` and `C`) with values ranging from -10 to 10.

```python
In [1]: import pandas as pd
In [2]: import numpy as np
In [3]: data = np.random.randint(-10, 10, (5000, 3))
In [4]: df = pd.DataFrame(data=data, columns=["A", "B", "C"], index=None)
```

To track the time required to finish an operation, we can make use of the IPython magic function [`%timeit`](https://ipython.org/ipython-doc/3/interactive/magics.html#magic-timeit) to measure the time required to execute a line in Python.

To start with, let's consider a simple task of creating a new column in the DataFrame, whose values depend on whether the sum of the values in other columns are greater than zero. First, let's try using the `apply` function of the DataFrame:

```python
In [5]: %timeit df["D"] = df.apply(lambda x: 1 if x["A"] + x["B"] + x["C"] > 0 else 0, axis=1)
134 ms ± 1.59 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

It takes about 134ms to finish the operation, which seems quite fast. However, if we take another approach by using numpy's `where()` function, we can actually be much faster:

```python
In [6]: %timeit df["E"] = np.where(df["A"] + df["B"] + df["C"] > 0, 1, 0)
757 µs ± 38.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

This is ~170 times faster! We can verified that the two methods actually give the same results as follows. (`np.any` checks if any of the values in a list is `True`).

```python
In [7]: np.any(df["D"] != df["E"])
False
```

## String Operations

As another example, let's try searching substrings in a column. Firstly, let's generate some random text data in a new column:

```python
In [8]: df["F"] = np.random.choice(["apple", "banana", "orange", "pear"], 5000)
```

Let's say we want to create a new column, whose values depend on whether Column `F` contains the substring **an**. Firstly, let's try the `apply` function:

```python
In [9]: %timeit df["G"] = df.apply(lambda x: 1 if "an" in x["F"] else 0, axis=1)
61.1 ms ± 685 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

Now, if we use the second approach:

```python
In [10]: %timeit df["H"] = np.where(df["F"].str.contains("an"), 1, 0)
2.65 ms ± 40.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

which is ~30 times faster.

The conclusion is that whenever we can operate on the whole column, we should avoid using `apply`, which is looping over every row of the DataFrame, and is not able to take advantage of numpy vectorization when performing the calculation.
