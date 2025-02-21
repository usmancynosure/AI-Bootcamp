# function and modules in python 
# 1. function---block of code which is executed when it is called 
# 2. modules---collection of functions
# 3. built-in functions---functions which are already defined in python
# 4. user-defined functions---functions defined by the user
# 5. syntax of function:
# def function_name(parameters):
#     block of code
#     return value
# 6. calling a function\
    

'''def add_num(a,b):
    c=a+b
    return c

result_add=add_num(10,20)
print(result_add) 
'''

# Scope and LIfetime of variable 
# 1. scope of variable---part of the program where the variable is accessible
# 2. lifetime of variable---period throughout which the variable exits in the memory
# 3. local variable---variable defined inside the function
# 4. global variable---variable defined outside the function
# 5. global keyword---used to create a global variable inside a function
# 6. syntax of global keyword:
# def function_name():
#     global variable_name
#     variable_name=value

# Exampe of local keyword

'''def add_num(a,b):
    c=a+b
    return c'''

# Example of Global keyword
'''greeting="Hello"
def greet():
    return greeting+"Good Morning"

print(greet())
print(greeting)'''



# >>>>>>>>>>>>>>>>>>>>>>>>>Moduules>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 1. module---collection of functions
from math import sqrt # importing a specific function
print(sqrt(16))

import math  # importing the entire module
print(math.sqrt(16))

# 2. creating a module
# 3. creating a module---a file containing a set of functions
# 4. creating a module---functions are defined in a file and saved as .py file
# 5. creating a module---functions can be imported and used in other programs
# 6. syntax of creating a module:
# def function_name(parameters):
#     block of code
#     return value
# 7. saving the file as .py file 
# 8. importing the module
# 9. using the functions of the module

# Example of creating a module
# 1. creating a module
# 2. importing the module
# 3. using the functions of the module

# 1. creating a module
# creating a module named mymodule.py
# def greeting(name):
#     return
# 2. importing the module
# import mymodule
# 3. using the functions of the module
# print(mymodule.greeting("Jonathan"))



# use of alais
# 1. alias---alternative name given to the module
# 2. alias---used to shorten the module name
# 3. syntax of alias:
# import module_name as alias_name
'''import math as m
print(m.sqrt(16))'''




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Exercise>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# find the factorial of the number 
'''def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("Enter the number: "))
print(factorial(num))'''



# >>>>>>>>>>>>>>>>>>>>>>>>>import the custom module>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# importing the custom module
import custom_module
print(custom_module.add(10,20))
print(custom_module.sub(20,10))
print(custom_module.mul(10,20))
print(custom_module.div(20,10))








