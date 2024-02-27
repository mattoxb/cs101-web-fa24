+++
title = "Looping Patterns With For Loops"
date = 2024-02-19
draft = false
weight = 2
+++

When using `for` loops, a few patterns show up frequently.  If you learn these patterns --- how to recognize them and how to code them ---
it can speed up your programming.


## The Action Pattern {#the-action-pattern}

In the _action_ pattern, we want to _do something_ to (or with) each element of a list.

Here is the pseudocode template:

```nil
possible setup code
for each x in xx:
    do somethign using x
```


### Example: Printing the Elements of a List {#example-printing-the-elements-of-a-list}

```python
for x in xx:
    print(x)
```


### Example: Printing the Elements of a List and Their Squares {#example-printing-the-elements-of-a-list-and-their-squares}

```python
for x in xx:
    print(f"{x}, {x*x}")
```


### Reading Elements from a File a Printing Them {#reading-elements-from-a-file-a-printing-them}

```python
with open('foo.txt') as file:
    for x in file.readlines()
        print(x)
```


### Writing Elements of a List to a File {#writing-elements-of-a-list-to-a-file}

```python
with open('foo.txt','w') as file:
    for x in xx:
        file.write(f"{x}\n")
```


## The Accumulator Pattern {#the-accumulator-pattern}

In the accumulator pattern, we want to _build up_ a pattern using a collection of data.

Here is the pseudocode template:

```nil
initialize the accumulator
for each x in xx:
    modify accumulator using x
final result is in accumulator
```


### Example: Counting the Elements of a List {#example-counting-the-elements-of-a-list}

For this, `count` is the accumulator, and at each step we add one to it.

```python
count = 0
for x in xx:
    count = count + 1
```


### Example: Summing the Elements of a List {#example-summing-the-elements-of-a-list}

For this, `sum` is the accumulator, and at each step we add `x` to it.

```python
sum = 0
for x in xx:
    sum = sum + x
```


### Example: Taking the Maximum of the Elements of a List {#example-taking-the-maximum-of-the-elements-of-a-list}

For this, `themax` is the accumulator, and at each step we update it with `x` using the built-in funciton `max`.

```python
themax = xx[0]
for x in xx[1:]:
    themax = max(themax,x)
```

Note here we initialize `themax` to the first element of the list, and iterate over the rest of the elements.


### Example: Create a Dictionary with the Elements of a List and Their Squares {#example-create-a-dictionary-with-the-elements-of-a-list-and-their-squares}

For this, `d` is the accumulator, and at each step we update it by inserting key `x` with value `x*x`.

```python
d = {}
for x in xx:
    d[x] = x * x
```


### Your turn! {#your-turn}

Try to write Python code to

-   Take the product of the elements of a list
-   Take the minimum of the elements of a list
