"""Code example of a program with O(n^2) time complexity."""

def print_items(n):
    """Define a function that prints numbers from 0 to n-1."""
    for i in range(n):
        for j in range(n):
            """Identical for loop to the first but using j instead of i."""
            print(i, j)

print_items(10)


"""For every value of i, we loop through j n times, thus we have n j operations
for every single i operation. And since we have n i operations in total
we end up with n * n operations which is n^2 operations, 
thus we say this function has O(n^2) time complexity.

The graph of O(n^2) is a parabola, and it grows much faster than O(n) as n increases.
It's also much steeper than O(n) because of the n^2 term, which means that as n
increases, the number of operations grows much more rapidly than O(n).

Thus we can see that O(n^2) is significantly less efficient than O(n) from a 
time complexity perspective for large values of n, thuse we should always strive
 to write code with lower time complexity when possible."""