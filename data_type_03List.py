# ---------List [ ]---------

fruits = [ "Banana" , "Apple" , "Mango" , "Kivi" , "Papaya" ] 

print (fruits[0:4])


# to add an element at the end of list 

fruits.append ( "Orange")
print (fruits)

# to add an element at a specific index

fruits.insert(2,"Grapes")
print (fruits)

# to remove an element from list

fruits.remove("Apple")
print (fruits)

# to remove an element from list by its index 

fruits.pop(3)
print (fruits)

# to remove all elements from list

fruits.clear()
print (fruits)