---
title: "🧩 Determining if a 15 Puzzle is solvable"
url: /2025/02/23/15-puzzble-solvability.html
date: 2025-02-23
tags:
    - python
    - game
    - puzzle
weight: -20250223
---

I recently became interested in how we can programmatically solve the 15 puzzle. The 15 puzzle is a sliding puzzle that consists of a 4 x 4 board of tiles numbered from 1 to 15, with one empty space. The tiles are shuffled and the goal is to slide the tiles around until they are in order, i.e. the numbered tiles will run from 1 to 15 starting from the top left corner from left to right and top to bottom, with the empty space at the bottom right corner.

<!--more-->

```
# A shuffled 15 puzzle
┌───┬───┬───┬───┐
│ 2 │ 8 │ 3 │ 4 │
├───┼───┼───┼───┤
│ 1 │ 6 │   │ 7 │
├───┼───┼───┼───┤
│ 5 │ 9 │ 11│ 12│   
├───┼───┼───┼───┤
│ 13│ 10│ 15│ 14│
└───┴───┴───┴───┘


# The target state of the 15 puzzle
┌───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │
├───┼───┼───┼───┤
│ 9 │ 10│ 11│ 12│   
├───┼───┼───┼───┤
│ 13│ 14│ 15│   │
└───┴───┴───┴───┘
```

## Solvability of the 15 puzzle

It is interesting to note that not all configurations of the 15 puzzle are solvable. In other words, give a certain arrangement of the numbered tiles on the board, it may not be possible to arrange the tiles in order by only sliding them around. It turns out that out of the `16! = 20,922,789,888,000` (about 21 trillion) possible configurations, only **half of them** are solvable.

Writing a program to determine whether a certain configuration is solvable is easy. Ask ChatGPT about it and it will give you a snippet that works out of the box. But here let's take a look at the details and try to understand how it works.

### Permutations

Mathematically, the 15 puzzle can be represented as a permutation of the numbers from 1 to 15 (or 16 if we include the blank space). A [permutation](https://en.wikipedia.org/wiki/Permutation) is an arrangement of objects in a specific order. For example, the permutation `(2, 1, 3)` represents a specific arrangement of the numbers 1, 2, and 3.

Given a set of elements (e.g. 1, 2, 3), a permutation can be changed into another permutation by a sequence of swapping pairs of elements (called **transpositions**). For example: we can change the permutation `(1, 2, 3)` into `(2, 1, 3)` by swapping the first two elements, i.e. performing a transposition of 1 and 2. Hence, to solve the 15 puzzle, we need to find a sequence of transpositions that will transform the initial permutation into the target permutation (with some restrictions of course, because we cannot simply exchange any two tiles).

### Parity of Permutations

When moving from one permutation to another, it either involves an **even** or **odd** number of transpositions. This is called the [parity of a permutation](https://en.wikipedia.org/wiki/Parity_of_a_permutation). For example:

- From `(1, 2, 3)` to `(2, 1, 3)` requires one transposition (swapping 1 and 2) --> **odd** parity
- From `(1, 2, 3)` to `(3, 2, 1)` requires two transpositions (swapping 1 and 3, then 2 and 3). --> **even** parity

Although there can be multiple sequence of transpositions that can transform one permutation to another, the parity of the number of transpositions will be the same. For example, from `(1, 2, 3)` to `(3, 2, 1)` we can swap 1 and 3 first, then 2 and 3, or we can swap 2 and 3 first, then 1 and 3.

### Inversions

It turns out that this concept of parity of permutations is crucial in determining whether a given configuration of the 15 puzzle is solvable or not. But before going back to the 15 puzzle, let's talk about the concept of **inversions**.

Let's say we have an ordering of the set of elements involved in a permutation. In the case of the 15 puzzle, we can order the numbers from 1 to 16 (including the blank space) in ascending order (which is also the target state of the puzzle). We would like to know if a certain permutation (arrangement of the numbers) is of even or odd parity. This is equivalent to asking the question of whether we need an even or odd number of transpositions to move from the initial permutation to the target permutation.

If the number of elements is small, or the permutation is not too different from the target permutation, it would be relatively easy to tell. For example:
```
Given  : ( 1, 2, 3, 4, 5)
Target : ( 2, 1, 5, 4, 3)
```
In this case, we can see that we need to swap 1 and 2, and 3 and 5. This requires two transpositions, which is an even number. Hence, the permutation is of even parity.

However, if the number of elements is large, or the permutation is very different from the target permutation, it would be difficult to tell just by looking at it. It turns out that we can rely on the concept of [inversions](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)) to determine the parity of a permutation. An inversion is a pair of elements `(i, j)` such that `i < j` but `i` appears after `j` in the permutation. For example, in the permutation `(2, 4, 1, 3)` the pair `(2, 1)`, `(4, 1)` and `(4, 3)` are inversions.

The number of inversions in a permutation is directly related to the parity of the permutation. If the number of inversions is even, the permutation is of even parity. If the number of inversions is odd, the permutation is of odd parity.

Programmatically, the number of inversions in a permutation can be calculated by iterating over all pairs of elements and counting the number of inversions:

```python
def count_inversions(arr):
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

arr = [2, 4, 1, 3]
print(count_inversions(arr))
# Output: 3  (because there are two inversions: (2, 1), (4, 1), (4, 3))
```

### Parity and Solvability of the 15 Puzzle

So, how does the concept of parity and inversion help us determine if a given configuration of the 15 puzzle is solvable? As mentioned above, solving the 15 puzzle is equivalent to transforming the initial permutation into the target permutation. It turns out that the number of inversions in the initial permutation is crucial.

To understand how parity or the number of inversions helps us determine solvability, let's consider the following board.

```
Current state:
┌───┬───┬───┬───┐
│ 2 │ 8 │ 3 │ 4 │
├───┼───┼───┼───┤
│ 1 │ 6 │ 14│ 5 │
├───┼───┼───┼───┤
│ 7 │ 9 │ 11│ 12│
├───┼───┼───┼───┤
│ 13│ 10│ 15│   │
└───┴───┴───┴───┘
```

In order to convert this board into the target state, we need to swap tiles around. However, we can only do so by sliding tiles into the empty space or, in other words, by "moving" the empty space around.

Note that in the end the empty space should still be at the bottom right corner of the board. We can easily see that in order for the empty space to move around and finally get back to the bottom right corner, the number of swapping happened must be **even**. Hence, assuming that after a number of moves we finally get to the target state, we will always have an even number of moves. This is true for any configuration of the board with the empty space at the bottom right corner.

What this analysis follows is that: for all configuration of the board with the empty space at the bottom right corner, the permutation of the numbers must be of **even parity**. This is because these configurations are all created by starting from the target state in which the empty space is also at the bottom right corner.

Consider the following configuration of the board:

```
┌───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │
├───┼───┼───┼───┤
│ 9 │ 10│ 11│ 12│   
├───┼───┼───┼───┤
│ 13│ 15│ 14│   │
└───┴───┴───┴───┘
```

in which only the tiles `14` and `15` are swapped. In this case, the parity of this permutation is 1, which is odd. Thus, this is an unsolvable configuration, as it is not possible to reach this configuration from the target state by simply sliding the tiles around.

This would become obvious if we consider a 2 x 2 board instead of a 4 x 4 board. For example, the following is a configuration with odd parity (since the number of inversions is 1):

```
┌───┬───┐
│ 2 │ 1 │
├───┼───┤
│ 3 │   │
└───┴───┘
```

We can easily see that there's no way to solve this puzzle by sliding the tiles around.


### Distance of the Empty Space from the Bottom Right Corner

But wait, what happen when the empty space is NOT at the bottom right corner? This is actually a trivial extension to the problem above. This is because given any configuration, we can always "move" the empty space to the bottom right corner by sliding the tiles around.

To determine if any configuration is solvable, we can do one of the following:
1. Move the empty space to the bottom right corner, and then check whether the parity of the permutation of the numbers is even.
2. Check whether the sum of the following two numbers is even:
    - The number of inversions in the permutation of the numbers
    - The number of moves required to move the empty space to the bottom right corner

The second method is more efficient because it avoids the need to actually move the empty space around. The number of moves required to move the empty space to the bottom right corner can be known by checking the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) (or taxicab distance) of the empty space from the bottom right corner.


### Summing Up

Given the above discussions, we can now write a function to determine whether a given configuration of the 15 puzzle is solvable or not. The function will take a list of numbers representing the configuration of the board, and return `True` if the configuration is solvable, and `False` otherwise.

```python
def is_solvable(board, empty_space_num=16):
    """
    Assuming `board` is a list of 16 numbers
    representing the configuration of the 15 puzzle board.
    """

    # Count the number of inversions
    def count_inversions(arr):
        inversions = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    inversions += 1
        return inversions

    # Get the Manhattan distance of the empty space from the bottom right corner
    def manhattan_distance(board):
        empty_space_index = board.index(empty_space_num)
        empty_space_row = empty_space_index // 4
        empty_space_col = empty_space_index % 4
        return 3 - empty_space_row + 3 - empty_space_col

    num_inversions = count_inversions(board)
    distance = manhattan_distance(board)

    # Check if the sum of the number of inversions and the distance is even
    return (num_inversions + distance) % 2 == 0
```

Examples:
```python
# Solvable
board = [
     1,  2,  3,  4,
     5,  6,  7,  8,
     9, 10, 16, 11,
    13, 14, 15, 12,
]
print(is_solvable(board))  # Output: True

# Unsolvable
board = [
     1,  2,  3,  4,
     5,  6,  7,  8,
     9, 10, 11, 12,
    13, 15, 14, 16,
]
print(is_solvable(board))  # Output: False
```

We can also generalize this to any size of the board, not just the 4 x 4 board, or even to different requirements (e.g. the empty space needs to be at the top left corner in the target state). But this should give you a good idea of how to determine the solvability of the 15 puzzle.


## What's Next?

Determining whether a given configuration of the 15 puzzle is solvable is the first step in solving the puzzle programmatically. The next step would be to implement an algorithm to find the sequence of moves that will transform the initial configuration into the target configuration. Two algorithms are commonly used: the [A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) and the [IDA* algorithm](https://en.wikipedia.org/wiki/Iterative_deepening_A*). I will try to cover these in another post.


## References
- [Notes on the "15" Puzzle](https://www.jstor.org/stable/2369492) by Johnson and Story, 1879 in *American Journal of Mathematics*
- [The Fifteen Puzzle](https://mohamedrezk122.github.io/fifteen-puzzle) by Mohamed El Shorbagy
- [15 Puzzle -- from Wolfram MathWorld](https://mathworld.wolfram.com/15Puzzle.html)
