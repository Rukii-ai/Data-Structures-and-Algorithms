"""Instructions:
<> Big O: O(n)
Implement a Python function called print_items.

This function should take a single integer as an argument and print out a sequence of numbers from 0 up to, but not including, the provided integer.

The function should use a for loop and Python's built-in range function to generate the sequence of numbers.

The function signature should be: def print_items(n):


Example:
Here is an example of how your function should behave:
If you call print_items(10), your function should print:
0
1
2
3
4
5
6
7
8
9
"""


"""Psuedo code:
1) Define the function print_items(n)

    a) Start a for loop that will run n times

        a.i) During each iteration, i is the current loop count, starting from 0 and ending at n - 1

        a.ii) Inside the loop, print the current value of i

2) End the function definition

3) Call the function print_items with a specific number (e.g., print_items(10))

"""



## WRITE THE PRINT_ITEMS FUNCTION HERE ##
def print_items(n):
    """A function that takes a single integer n as an argument
    and prints 0 to n-1."""
    for i in range(n):
        print(i)

# DO NOT CHANGE THIS LINE:
print_items(10)