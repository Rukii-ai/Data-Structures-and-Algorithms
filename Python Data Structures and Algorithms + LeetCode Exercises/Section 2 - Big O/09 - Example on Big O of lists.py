"""Example code to demonstrate Big O of lists in Python."""

my_list = [1, 2, 3, 4, 5]

my_list.append(6)  
"""The above action has a time complexity of O(1) because it adds an element to 
the end of the list,and it does not require shifting any existing elements.
No reindexing takes place, and thus it is a constant time operation."""

my_list.pop()
"""The above action also has a time complexity of O(1) because it removes the
last element of the list, and it does not require shifting any existing elements.
No reindexing takes place, and thus it is a constant time operation."""

my_list.pop(0)
"""The above action removes the first element of a list, and when this happens
there is a shifting of all the remaining elements to fill the gap left by the 
removed element. This shifting changes the index of all the remaining elements
by iterating through the list and reassigning the index of each element, 
thus the number of operations is proportional to the number of elements in the 
list, and thus it has a time complexity of O(n)."""

my_list.insert(0, 1)
"""The above action inserts an element at the beginning of the list, and when
this happens there is a shifting of all the existing elements to make room for
the new element. This shifting changes the index of all the existing elements
by iterating through the list and reassigning the index of each element, 
thus the number of operations is proportional to the number of elements in the 
list, and thus it has a time complexity of O(n)."""


"""Thus in a list. Adding or removing an element from the right end of a list
results in a time complexity of O(1).

And from the left end of a list results in a time complexity of O(n)

Even if an item is added or removed from the middle of a list, it's 
time complexity is still O(n) because O(n) measures the worst case time complexity,
And adding or removing an element from the middle of the list only reuires a 
fraction of the total number of operations needed to add or remove an element 
from the left end of the list.

So even if we wanted to say that the time complexity is thun O(kn) where k 
is a constant representing the fraction of the total number of operations needed
to add or remove an element from the left end of the list, we would still drop 
the constant k and simplify it to O(n) because we drop constants in big O notation."""


"""Looking for an element of a list by its value would require iterating through
the list and comparing each element to the target value until a match is found 
or the end of the list is reached, thus it has a time complexity of O(n) because
in the worst case we would have to check every element in the list.


Whereas looking for an element of a list by its index would require directly 
accessing the element at the specified index, thus it has a time complexity of 
O(1) because it does not require iterating through the list and 
is a constant time operation."""