"""Example code to demonstrate simplifying big O notation by dropping non-dominant terms."""

def print_items(n):
    """Define a function that prints numbers from 0 to n-1."""
    for i in range(n):
        for j in range(n):
            """Identical for loop to the first but using j instead of i."""
            print(i, j)

    for k in range(n):
       """Identical for loop to the first but using k instead of i."""
       print(k)


print_items(10)

"""In this program we have the nested loops which give us n^2 operations, 
and then we have the last loop which gives us n operations. Thus we have a 
total of n^2 + n operations. And a time complexity of O(n^2 + n).

But due to the fact that n^2 grows much faster than n as n increases, as n 
becomes large, the n^2 term will become extremely large and the n term will
contribute only a small percentage of the overall operations thus making it
insignificant in comparison to the n^2 term, and thus a non-dominant term.

Thus we can drop the n term and simplify our time complexity 
to O(n^2) instead of O(n^2 + n)"""
