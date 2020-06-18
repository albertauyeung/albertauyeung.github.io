---
layout: article
title:  "Implementing a Trie in Python"
tags: [python, data structure]
---

## What is a Trie?

**Trie** is a very useful data structure. It is commonly used to represent a dictionary for looking up words in a vocabulary.

For example, consider the task of implementing a search bar with **auto-completion** or **query suggestion**. When the user enters a query, the search bar will automatically suggests common queries **starting with** the characters input by the user.

![](/assets/images/query_suggestion.png)

To implement such a function, we need several things at the backend. The first, obviously, is a list of common queries. Or it can be a list of proper English words for the purpose of auto-completion). Secondly, we will need to have an algorithm to **quickly** look up words starting with the characters input by the user, and this is where we need to use the trie data structure.

The follow example illustrates why a special data structure is necessary to look up words **quickly** given a **prefix**:
- The user inputs the characters `en`
- In our dictionary, we have the following words starting with `en`: `english`, `entertainment`
- Commonly used data structures such as `list` and `dictionary` in Python do not allow quick look up of elements stored inside. For example, to see if there is any word having the prefix `en` in a Python dictionary, we cannot avoid going through each of the keys, resulting in `O(n)` time, where `n` is the number of entries in the dictionary

**Trie** is a tree-like data structure made up of nodes. Nodes can be used to store data. Each node may have none, one or more children. When used to store a vocabulary, **each node is used to store a character**, and consequently each "branch" of the trie represents a unique word. The following figure shows a trie with five words (`was`, `wax`, `what`, `word`, `work`) stored in it.

![](/assets/images/trie_example.png)

## Implementing a Trie in Python

To implement a trie, we can first create a `TrieNode` class, which can be used to represent a node in the trie. Below is how this class can be implemented.

```python
class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}
```

In this implementation, we want to store also the number of times a word has been inserted into the trie. This allows us to support additional features, such as ranking the words by their popularity.

Given the `TrieNode` class, we can go on to implement the `Trie` class as follows.

```python
class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
    
    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
        
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1
        
    def dfs(self, node, prefix):
        """Depth-first traversal of the trie
        
        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of 
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root
        
        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []
        
        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)
```

Below is an example of how this `Trie` class can be used:

```python
>>> t = Trie()
>>> t.insert("was")
>>> t.insert("word")
>>> t.insert("war")
>>> t.insert("what")
>>> t.insert("where")
>>> t.query("wh")
[('what', 1), ('where', 1)]
```

## References

- [Trie](https://en.wikipedia.org/wiki/Trie), Wikipedia
- [Tries](https://brilliant.org/wiki/tries/), Brilliant.org
- [Trie (Prefix Tree)](https://www.cs.usfca.edu/~galles/visualization/Trie.html) - Visualizing the operations on a trie

