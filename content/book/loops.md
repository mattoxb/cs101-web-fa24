+++
title = "Looping"
date = 2024-02-19
draft = false
weight = 1
+++

## Introduction {#introduction}

Computer programs tend to focus on just a few kinds of things.  One of them is _making decisions_,
which in Python usually involves an `if` statement.

Another is _repeating things_, which usually involve loops.

In this chapter we will talk about `for` loops and `while` loops.


## Objectives {#objectives}

-   Explain the purpose of a `for` loop and a `while` loop.
-   Write syntactically correct code using loops.
-   Use a `for` loop to process elements of a list.
-   Use `range` to count the number of times a loop runs.
-   Use `while` to repeat a task until something becomes true.
-   Use `continue` to skip one run of a loop.
-   Use `break` to stop the loop altogether.


## Motivation {#motivation}

Suppose you wanted to print out a table of squares for your child's math practice.  We will do the first 5
to preserve our own sanity. The Python program below accomplishes this.  Badly.

```python
i = 1
print(f"{i} * {i} = {i * i}")
i = 2
print(f"{i} * {i} = {i * i}")
i = 3
print(f"{i} * {i} = {i * i}")
i = 4
print(f"{i} * {i} = {i * i}")
i = 5
print(f"{i} * {i} = {i * i}")
```

This results in the following output.

```nil
1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25
```

This code isn't bad because it doesn't function; it is bad because you, the programmer, repeated yourself
over and over for the computer.  This breaks [Mattox's Law of Computing]({{< relref "mattoxs-law-of-computing" >}}).

Looking at this code, you see the only thing that changes is the value of the variable `i`.  The code that
makes use of `i` doesn't change at all.


## Looping with a for loop. {#looping-with-a-for-loop-dot}

We can tell Python that we want to run the two lines repeatedly, but for _different values of `i`_.  We do this
with a `for` loop.  Here is what it would look like:

```python
for i in [1,2,3,4,5]:
    print(f"{i} * {i} = {i * i}")
```

Here is the syntax you should notice:

-   A for-loop starts with the keyword `for`.
-   Next comes a variable name, in this case `i`.
-   The `in` keyword separates the variable from the data, which comes next.  In this case the data is
    the list `[1,2,3,4,5]`.
-   The line ends with a colon.  In python, this always indicates that a _block of code_ follows.
-   The next line is indented: this is the line that gets repeated.  This code is called the _body_ of the
    `for` loop.  It can be multiple lines long.  Python knows when you are done when the code is no longer
    indented.

What Python actually does with this code is this:

-   It sets variable `i` to be 1, the first element in the data.
-   It then runs the `print` statement.
-   Once that is done, the `for` sets `i` to be the next element in the data, in this case 2.
-   It then runs the `print` statement (with `i` being 2).
-   ... and so on until `i` has had all the values in the data list.

You should try this yourself to make sure it works.  Here are some variations:

-   We can change the variable name to something else.
    ```python
        for x in [1,2,3,4,5]:
            print(f"{x} * {x} = {x * x}")
    ```

-   We can iterate over different data.  Maybe we only want odd numbers to 9 for our table:
    ```python
        for i in [1,3,5,7,9]:
            print(f"{i} * {i} = {i * i}")
    ```

-   We can print lines in between each row.  Notice now we have _two_ lines in the body of the `for` loop.  The last line is unindented,
    signalling to Python that the loop body code is over.
    ```python
        for i in [1,2,3,4,5]:
            print(f"{i} * {i} = {i * i}")
            print(f"-------------------")
        print("Done.")
    ```
    Here is what it will output:
    ```text
        1 * 1 = 1
        -------------------
        2 * 2 = 4
        -------------------
        3 * 3 = 9
        -------------------
        4 * 4 = 16
        -------------------
        5 * 5 = 25
        -------------------
        Done.
    ```


## Using range. {#using-range-dot}

Typing out a list of sequential numbers is something we would need to do often.  To automate this, Python provides a function called
`range()`.  It has three forms.

-   `range(n)` gives you a range from 0 to \\(n-1\\).
-   `range(a,b)` gives you a range from a to \\(b-1\\).
-   `range(a,b,s)` gives you a range from a to \\(b-1\\), but skips every \\(s\\) elements.

The output is a _range object_.  For example,

```python
print(range(10))
```

will result in

```text
range(0, 10)
```

This can be used as the data part of a `for` loop, like this:

```python
for i in range(5):
    print(f"{i} * {i} = {i * i}")
    print(f"-------------------")
print("Done.")
```

Here the result.  The `range` function starts from zero by default, so we will have to adjust this in a minute.

```text
0 * 0 = 0
-------------------
1 * 1 = 1
-------------------
2 * 2 = 4
-------------------
3 * 3 = 9
-------------------
4 * 4 = 16
-------------------
Done.
```

Why does it start from 0 and leave out the last element?
