# ---------Set ---------

# A set is a collection data type in Python that is unordered and unindexed.

fruits =  {"apple" ," banana" , "mango", "cherry"  }
print(fruits)
print(type(fruits))

# add element in set 
fruits.add ("orange")
print(fruits)

# delete item in set
fruits.pop()
print(fruits)

# remove item from set (not possible)
fruits.discard("banana")
print (fruits)

# updated set
fruits.update({"kiwi", "grape"})
print(fruits)

# check if item exists in set
is_fruits = "kiwi" in fruits
print(f"Is kiwi in fruits set : {is_fruits}")

# union set
#union sign = set1 | set2
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set3 = set1.union(set2)
print(set3)

# intersection set
# intersection sign = set1 & set2
set4 = set1.intersection(set2)  
print(set4)

# difference set
set5 = set1.difference(set2)
print(set5)