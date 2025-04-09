# ---------Array [ ]---------

# Array is a data structure that can hold multiple values of the same type.

import array as  arr  # we can also write array without importing array module

my_array =arr.array ("i",[1, 2, 3, 4, 5])
print(my_array)
print (type(my_array) )

# to get the elment at a specific index
print (my_array)

# add element in array 
my_array.append(6)
print(my_array)

# remove element from array
my_array.pop()
print(my_array)

# remove element from array by index
my_array.pop(1)
print(my_array)