# ControlFlow in Python 
# Example 1 "checking the particular number "


'''num=10
if num>0:
    print("Positive")   
elif num<0:
    print("Negative")
    
else:
    print("Zero")'''
    
# Example 2 "checking the nested condition"
'''age=32
if age>18:
    if age<60:
        print("Adult")
    else:
        print("Old")
else:
    print("Child")
    '''
    
    
# Loops
# Example 1 "for loop"
'''name=["usman", "Ali", "Waleed"]
for item in name:
    print(item)'''


# loop with range
'''for i in range(5):
    print(i)
    '''
# loop with while 


fruits=["apple", "banana", "cherry"]
i=0
while i<=2:
    print(fruits[i])   
    i+=1 
    
# break and continue
'''for i in range(5):
    if i==3:
        break
    print(i)'''

# continue
'''for i in range(5):
    if i==3:
        continue
    print(i)'''
    
    
# exercise if the number is prime 
'''n=int(input("Enter the number: "))
is_prime=True
for i in range(2,n):
    if n%i==0:
        is_prime=False 
        break
if is_prime:
    print("Prime")  
else:
    print("Not Prime")'''
    
    
# exercise 2 "menu driven calculater"


# define the function
def menu():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter the choice: "))
    return choice

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):   
    return
def div(a,b):
    return a/b

while True:
    choice=menu()
    if choice==5:
        
        break
    if choice>5:
        print("Invalid choice")
        print("Please enter the valid choice")
        continue
    a=int(input("Enter the first number: "))    
    b=int(input("Enter the second number: "))
    if choice==1:
        print("Addition:",add(a,b))
    elif choice==2:
        print("Subtraction:",sub(a,b))
    elif choice==3:
        print("Multiplication:",mul(a,b))
    elif choice==4:
        print("Division:",div(a,b))
    else:
        print("Invalid choice") 
print("Thank you for using the calculator")
                