# compute the derivation of Basic Function 
import sympy as sp
import numpy as np

x=sp.Symbol('x')
f= x**3 + 5*x -3
derivative= sp.diff(f, x)


# compute the gradient of multi-varibale 

x,y = sp.symbols('x y')
f= x**2 + 3*y**2 + 4*x*y
grad_x=sp.diff(f,x)
grad_y=sp.diff(f,y)

print("gradient_x \n ", grad_x)
print("Gradient_y \n ", grad_y)


# Implement Gradient decent for linear regression 
# Gradient decent --->optimization algorithm used to find the minimum of the the function 
'''
— especially a loss/cost function in machine learning models.

When we train a model (like linear regression, logistic regression, or neural networks),
we try to minimize the error (loss). Gradient Descent helps us do exactly that!
''' 

'''
In ML: What Are We Minimizing?
We minimize a Loss Function, e.g., Mean Squared Error (MSE), which tells us:

“How far is our model's prediction from the actual result?”
'''

'''

θ=θ−α⋅∇J(θ)


'''

import numpy as np

# Define the Gradient Descent function
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)  # number of training examples
    
    for _ in range(iterations):
        prediction = np.dot(X, theta)               # ŷ = Xθ
        error = prediction - y                      # error = ŷ - y
        gradient = (1/m) * np.dot(X.T, error)       # compute gradient
        theta -= learning_rate * gradient           # update parameters
        
    return theta

# Sample Data
# X has a column of 1s for intercept and a feature column
X = np.array([[1, 1],
              [1, 2],
              [1, 2]])

y = np.array([2, 2.5, 3])         # Target values
theta = np.array([0.1, 0.1])      # Initial parameters
learning_rate = 0.1
iterations = 1000

# Perform Gradient Descent
optimized_theta = gradient_descent(X, y, theta, learning_rate, iterations)

# Output the result
print("Optimized parameters:", optimized_theta)





# use sympy to compute the second order derivative (Hessian matrix)
import sympy as sp

# Define the symbol
x = sp.Symbol('x')

# Define the function
f = x**3 + 2*x**2 + x

# First derivative
f_prime = sp.diff(f, x)

# Second derivative
f_double_prime = sp.diff(f_prime, x)

# Print results
print("Original function f(x):", f)
print("First derivative f'(x):", f_prime)
print("Second derivative f''(x):", f_double_prime)





