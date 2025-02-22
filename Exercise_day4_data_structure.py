person={"name":"usman", "age":25, "courses":["Math", "CompSci"]}
# print(person)

# add new key 
person["Phone_no"]="320078777"

# update the age
person["age"]=30

if "name" in person:
    print("Name is present in the dictionary")

if "name" in person.keys():
    del person["name"]
    print("Name is deleted from the dictionary")

# loop through the dictionary
for key in person:
    print(key)

# Exercise 2 word frequency counter
# 1. create a dictionary
# 2. take the input from the user
# 3. count the frequency of the word
# 4. display the frequency of the word
inp=input("Enter the word: ")
inp=inp.split()
words={}
for key in inp:
    count=0
    for i in key:
        count+=1
    words[key]=count
print(words)
        
# 5. display the frequency of the word
for key, value in words.items():
    print(key, value)
    


# write a program to revere a list and remove the duplicates using sets
# 1. create a list
# 2. reverse the list
# 3. remove the duplicates
# 4. display the list
list1=[1,2,3,4,5,1,2,3,4,5]
list1.reverse()
print(list1)
list2=set(list1)
print(list2)

# create a program that store student grades and calculate the average grade
# 1. create a dictionary
# 2. take the input from the user
# 3. calculate the average grade
# 4. display the average grade
grades={"Math":90, "Science":80, "English":70, "Computer":85}
sum=0
for key, value in grades.items():
    sum+=value
print(sum)
average=sum/len(grades)
print(average)

