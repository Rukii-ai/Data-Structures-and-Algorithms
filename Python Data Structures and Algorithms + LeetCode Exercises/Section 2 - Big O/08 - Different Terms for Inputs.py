"""Example code to demonstrate different terms for inputs in big O notation."""

def print_items(a, b):
    """A function that takes two arguments and prints numbers from 0 to a-1 and 0 to b-1."""
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

"""In this program, we have two loops where the first loop runs 'a' times and 
the second loop runs 'b' times. Thus, we have a total of a + b operations. 
And a time complexity of O(a + b).

Before we could simplify further when we had n + n operations resulting in 2n 
operations, but in this case since a and b are different variables representing 
different inputs, we cannot simplify this further by dropping the constant 
because there is no constant to drop.

If a and b are different values, we cannot simplify this further because 
both terms are significant.
"""

def print_items_2(a, b):
    """A function that takes two arguments and prints pairs (i, j) of numbers from 0 to a-1 and 0 to b-1."""
    for i in range(a):
        for j in range(b):
            print(i, j)

"""In this program, we have a nested loop where the outer loop runs 'a' times and 
the inner loop runs 'b' times for each iteration of the outer loop. 
Thus, we have a total of a * b operations. 
And a time complexity of O(a * b) instead of O(n^2).
"""