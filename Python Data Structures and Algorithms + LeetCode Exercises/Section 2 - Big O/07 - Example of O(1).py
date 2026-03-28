"""Example code to demonstrate O(1) time complexity."""

def add_items(n):
    """A function that takes a single number as an argument and adds that number to itself"""
    return n + n

"""The program above performs one operation which is adding n to itself, 
and thus it has O(1) time complexity. Even if the function were to return 
n + n + n + n + n + n + n + n + n + n (10 times) it would still have O(1) instead
of O(10) time complexity because it is still performing a constant number of operations,

O(1) is also known as constant time complexity because the number of operations 
is constant and does not change with the size of the input n. It is the most 
efficient form of time complexity because it does not grow as the input size 
increases, and thus it is the ideal time complexity to strive for when writing code.
"""