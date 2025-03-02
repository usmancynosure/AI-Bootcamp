# clean code structure: -->Always start with the function 

# List Comprehension
# List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.


# Example 1-->list of squares of numbers from 1 to 10
'''
square=[i**2 for i in range(1,11)]
print(square)

# Filter Even Number 
even_num= [x for x in range(10) if x%2==0]
print(even_num)

'''


# Lamba keyword  
# anonumouus , single line function

# add the two number 
# argument : expression

'''
add = lambda x,y : x+y
print(add(2,3))

'''

# Example 2-->filter even number using lambda function
'''
even_num = lambda x : x%2==0    
print(even_num(2))
'''

# MAP function
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
'''
numbers=[1,2,3,4,5]
square =map( lambda x: x**2, numbers)

print(list(square))
'''

# filter function
# filter() function constructs an iterator from elements of an iterable for which a function returns true.


'''
numbers=[1,2,3,4,5]
even_num = filter(lambda x: x%2==0, numbers)
print(list(even_num))
'''
# Real Life exmaple of MAP() and FILTER() function
# Example 3-->convert the list of string to list of integer


# Using map() function
'''
string_num=['1','2','3','4','5']
int_num = map(lambda x: int(x), string_num)
print(list(int_num))
'''

# using reduce function
# reduce() function is for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list.
'''
from functools import reduce
numbers=[1,2,3,4,5]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)
'''
# Real Life exmaple of reduce() function
# Example 4-->find the maximum number from the list

'''
numbers=[1,2,3,4,5]
max_num = reduce(lambda x,y: x if x>y else y, numbers)
print(max_num)

'''


# Python os and sys module 
# os module provides a way of using operating system dependent functionality.
# sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import os 

print(os.getcwd())  # get the current working directory
os.chdir('test')    # change the directory

# sys module 
import sys
print(sys.argv)  # get the command line argument
print(sys.path)  # get the search path for the module
print(sys.version)  # get the python version