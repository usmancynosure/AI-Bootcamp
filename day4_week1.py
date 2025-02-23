# String manipulation 
# concatenation
'''
first = "Hello"
second = "World"
print(first + second)
print(first + " " + second)
'''
# slicing 
# 1. slicing---extracting a part of the string

'''
text ="Python Programming"
print(text[0:6]) #six is not included
print(text[-16:-10])
'''
# formatting 
# 1. formatting---changing the format of the string
'''
name="usman"
age=20
print("My name is {} and I am {} years old".format(name,age))
'''

# Common string methods
# 1. upper()---converts the string into uppercase
# 2. lower()---converts the string into lowercase
# 3. title()---converts the first letter of each word into uppercase
# 4. capitalize()---converts the first letter of the string into uppercase
# 5. swapcase()---converts the uppercase letter into lowercase and vice versa
# 6. len()---returns the length of the string
# 7. count()---returns the number of times the specified value appears in the string
# 8. find()---returns the index of the first occurrence of the specified value
# 9. replace()---replaces a specified value with another value in the string
# 10. split()---splits the string into substrings if it finds instances of the separator

# split() method
'''
text="Python is famous Programming language"
print(text.split()) #splitting the string into substrings
'''

# Join
# 1. join()---joins the elements of the list with the specified separator
'''
text="Python is famous Programming language"
split_word=text.split()
print(" ,".join(split_word)) #joining the elements of the list with the specified separator
'''

# strip
mesage="    Hello World    "
print(mesage.strip()) #removes the white spaces from the beginning and end of the string

# replace 
'''
text="Java is famous Programming language"
print(text.replace("Java","Python")) #replaces a specified value with another value in the string
'''

# find
'''
text="Python is famous Programming language"
print(text.find("is")) #returns the index of the first occurrence of the specified value
'''


# Regular Expressions
# 1. regular expressions---sequence of characters that forms a search pattern
# 2. regular expressions---used to search, replace, and match text
# 3. regular expressions---used to validate the input
# 4. regular expressions---used to extract the information from the text
# Example are the email validation, phone number validation, etc
# 5. regular expressions---used to search the specific pattern in the text
# using the re module from the regex operations
