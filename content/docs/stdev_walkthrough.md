---
title: "Calculating the Standard Deviation"
date: 2023-07-04T16:12:51-05:00
draft: false
weight: 1
math: true
---

## Problem Statement

Write a function `stdev(xx)` that returns the standard deviation of the elements in the list `xx`.

The formula for standard deviation is:

$$ s = \sqrt{\Sigma |x - \mu|^2 \over n} $$

where $\mu$ is the average of the list and $n$ is the length.

Example: if `xx == [10,20,30,40,50]`, then `s == 14.1421`.


## Strategy

To solve a programming problem, the first step is almost always to break the problem down into smaller steps.
In this particular example, to compute the standard deviation, we have to do at least three things in the right order.

- First, we have to compute $\mu$.
- Second, we have to find the sum of each $(x-\mu)^2$ for the $x$s in `xx` 
- Finally, we have to devide by $n$ and take the square root.

Each step depends on the previous ones, so we have to do these tasks in this order.

## Part 1: Find $\mu$.

To take the average of a list, we have to sum up all the elements and then divide by the size.  We are using the size later
so it makes sense to store that in the variable `n`.  To sum up the elements, we also need a variable to keep track of the
sum as we go.  Let's call it `a`, short for /accumulator/.

So, we will set `n` to be the lenght of `xx`, set `a` to be zero, and then loop through `xx`, adding each element to `a`.
When we are done, we can divide by `n` and put the result in a new variable `mu`.  Here is the Python code:

```python
def stdev(xx):
    # Part 1 - Get the average
    n = len(xx)
    a = 0
    for x in xx:
        a = a + x
    mu = a / n
```

## Part 2: Sum the squares of the deviations

This second part also requires that we loop over all the elements in the list.  This time, we sum up the "deviations":
we subtract $\mu$ from each $x$ and square it, then add that result to the accumulator.

```python
    # Part 2 - Sum the square of the deviations
    a = 0 # We can just reuse this variable
    for x in xx:
        a = a + (x - mu) ** 2
```

## Part 3: Divide by $n$ and take the square root.

This part is simple since we don't have to loop over anything.  You may use `math.sqrt` or `numpy.sqrt` if you know about those
things already, but for this we will just raise to the power of 0.5.

```python
    # Part 3 - Final result
    return (a / n) ** 0.5
```

Here is the whole program:

```python
def stdev(xx):
    # Part 1 - Get the average
    n = len(xx)
    a = 0
    for x in xx:
        a = a + x
    mu = a / n

    # Part 2 - Sum the square of the deviations
    a = 0 # We can just reuse this variable
    for x in xx:
        a = a + (x - mu) ** 2

    # Part 3 - Final result
    return (a / n) ** 0.5
```
