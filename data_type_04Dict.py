# ---------Dictionary {"key" , "value"}---------

#  Dictionary is a collection of key-value pairs.


person = {
    "name" : "Bhaskar" ,
    "age" : 18 ,
    "city" : "Hyderabad" ,
    "is_student" : True
}

print (f"person : {person}")


# acessing value from dictionary
print (f"person name : {person["name"]}")

# add element to dictionary
person["occupation"] = "Student"
print(f"person new info : {person}")

# update element in dictionary
person["age"] = 19
print(f"person updated info : {person}")

# delete element from dictionary
del person ["is_student"]
print(f"person after deleting is_student : {person}")

# to get all keys in dictionary
for key , value in person.items() :
    print (f"key in person : {key} , value of key : {value}")

# check if key exists in dictionary
"""is_student = "is_student" in person
print (f"Is student key exists : {is_student}")"""
if "is_student" in person :
    print (f"Is student key exists : {person['is_student']}")
else :  
    print ("Is student key does not exists")