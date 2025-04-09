# ---------Tuple ( ) ---------

# A tuple is an immutable data type in Python, meaning its elements cannot be changed after creation.

fruit_tuple = ("apple" , "banana", "cherry")
print(fruit_tuple)

# add element in tuple (not possible)

"""fruit_tuple[1] = "orange"
print(fruit_tuple)"""

print (fruit_tuple[0:2])

print (len(fruit_tuple))

print(fruit_tuple.count("banana"))

print(fruit_tuple.index("banana"))