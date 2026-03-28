"""Code example to demonstrate simplifying big O notation by dropping constants."""

def print_items(n):
    """Define a function that prints numbers from 0 to n-1."""
    for i in range(n):
        print(i)

    for j in range(n):
        """Identical for loop to the first but using j instead of i."""
        print(j)

print_items(10)

"""This second loop makes our function print 0 through n-1 twice, and in the case
of n = 10, it outputs 20 numbers thus carrying out 20 operations.

This might appear to thus have a time complexity of O(n + n) = O(2n).
But we can simplify this by dropping the constant, and thus we say 
that this function has a time complexity of O(n) instead of O(2n).

Thus even if it's O of 2n, 10n or 100n, we drop the constant and simplify to O(n)"""