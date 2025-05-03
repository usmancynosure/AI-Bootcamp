import sympy as sp
# Measure the rate at which the function chnage with respect to the input
# f'(x) indicate the slope of the tangent with repect to x
# Role of optimzation
    # to minimize and maximze the funtion which is critical in ML to optimize the loss function
# represent the symbol
x=sp.Symbol('x')
# define the function
f= x**3
# calculate the derivative 
derivative = sp.diff(f,x)
print("The derivative is \n ", derivative)

# Partial derivative 
# Measure hoe the function chnage with respect to one variblee with respect to the one varibale whiile other are constant 

# Gradient
# The Gradient is simply a vector of all partial derivatives.

# apply partial derivative 
x,y =sp.symbols('x y')
f= x**2 + y**2
grad_x= sp.diff(f,x)
grad_y =sp.diff(f,y)

print("Partial derivative", grad_x, grad_y)


# Gradient decent optimzation Algorithm
'''

What is Gradient Descent?
Gradient Descent is an optimization algorithm used to minimize a function by iteratively
moving in the direction of the steepest descent (i.e., opposite to the gradient).

In Machine Learning, we use Gradient Descent to minimize loss functions and train models and optimal model parameters.
''' 
