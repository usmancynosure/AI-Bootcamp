# List
# what is List-->list are oredered, changeable(mutable), allow duplicate values

'''fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits)
'''
# List with the combition of data types
'''Stu_list=["John", 25, "New York", 1000.0]
print(Stu_list)'''

# Accessing the elements of the list
'''print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# Negative indexing
print(fruits[-1])
print(fruits[-2])'''

# Modification of the list
# change the value of the list
'''fruits[1]="blackcurrant"
print(fruits)

fruits.append("Litchi") # add the element at the end of the list
print(fruits)

fruits.insert(0, "cherry") # add the element at the specific position
print(fruits)'''

# Remove the element from the list
'''fruits.remove("cherry")
print(fruits)'''


# del fruits[0] # remove the element from the specific position
'''del fruits[0]
print(fruits)'''


# pop method
'''fruits.pop() # remove the last element from the list
print(fruits)'''

# slicing of the list (end index is not included)
''''
print(fruits[2:5]) # start from 2 and end at 4
print(fruits[:4]) # start from 0 and end at 3
print(fruits[2:]) # start from 2 and go till the end
print(fruits[-4:-1]) # start from -4 and go till -2

'''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>tuple>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Tuple
# Tuple is a collection of ordered and unchangeable(immutable) elements
# Tuple is represented by ()
# Tuple allows duplicate values
# Tuple is immutable
# Tuple is ordered

'''colors=("red", "blue", "green", "yellow")
print(colors)'''

# Accessing the elements of the tuple
'''print(colors[0])
print(colors[1])
'''
# Negative indexing
'''print(colors[-1])
print(colors[-2])
'''
# Modification of the tuple
# colors[1]="black" # tuple does not support the item assignment
# print(colors)


# Tuple with one element
'''tup=(1,)
print(tup)
'''
# Tuple without parenthesis
'''tup=1,2,3,4
print(tup)
'''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Dictionary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Dictionary
# Dictionary is a collection of unordered, changeable and indexed elements
# Dictionary is represented by {}
# Dictionary has key-value pair
'''
student={"name":"John", "age":25, "courses":["Math", "CompSci"]}
print(student)
'''
# Accessing the elements of the dictionary
'''
print(student["name"])
print(student["age"])
print(student["courses"])
print(student["courses"][0]) # accessing the element of the list

'''
# Accessing the elements of the dictionary using get() method
'''print(student.get("name"))
print(student.get("age"))
print(student.get("courses"))
print(student.get("courses")[0]) # accessing the element of the list

'''
# add the element in the dictionary
'''student["phone"]="555-5555"
print(student)'''

# update the element in the dictionary
'''student["name"]="Jane"
print(student)'''


# remove the element from the dictionary
'''del student["age"]
print(student)'''

# pop method
'''
student.pop("phone")
'''
# update the element in the dictionary
'''student["name"]="Jane"
print(student)
'''
# loop through the dictionary
'''for key in student:
    print(key)
    
for key, value in student.items():
    print(key, value)
'''


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SETS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Sets
# Set is a collection of unordered and unindexed elements
# Set is represented by {}
# Set does not allow duplicate values
'''
fruits={"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print(fruits)
'''
# Accessing the elements of the set
'''
for x in fruits:
    print(x)
'''
# Add the element in the set
'''
fruits.add("Litchi")
print(fruits)
'''

# update the set
'''
fruits.update(["grapes", "papaya"])
print(fruits)
'''

# remove the element from the set
'''
fruits.remove("banana")
print(fruits)
'''
# Union of the set
'''
set1={1,2,3,4,5}
set2={6,7,8,9,10}
set3=set1.union(set2)
print(set1 | set2)
print(set3)
'''
# Intersection of the set
'''
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3=set1.intersection(set2)
print(set1 & set2)
print(set3)
'''

# Difference of the set
'''
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3=set1.difference(set2)
print(set1 - set2)
print(set3)
'''




