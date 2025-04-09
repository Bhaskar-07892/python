
# ---------String " "---------

name = " Bhaskar Pathak "  # " " is a string 
print ("name" , name)
print (f"Name : {name} ")


# some common function -

# to write upper case
print (f"Name in upper case : {name.upper()}")

# to write cpitalized case
print (f"Name in capitalized case : {name.capitalize()}")

# to write lower case
print (f"Name in lower case : {name.lower()}")

# to write split case with default: whitespace
print (f"the split func changed string into list : {name.split( " , ")}")

# to count char in string
print (f"Count --> count the char in string : {name.count('a')}")

# find char or word in string 
print (f"Count --> find the as position in string : {name.find('as')}")

# replace a char in string
print (name.replace("a","A"))