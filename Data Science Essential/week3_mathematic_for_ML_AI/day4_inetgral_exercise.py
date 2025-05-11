import sympy as sp


# Define a function
x=sp.Symbol('x')
f=sp.exp(-x)

# lets compute the indefinete integral
indef_integral=sp.integrate(f,x)
print("Indefinete integral \n", indef_integral)

# definiete integral
def_integral=sp.integrate(f, (x,0,sp.oo))
print("Definite integral \n", def_integral)



# Exercise 2 --> implement scholastic Gradient Decent for linear model 

import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + noise

# Initialize parameters (slope and intercept)
m = 0  # slope
b = 0  # intercept

# Hyperparameters
learning_rate = 0.01
epochs = 100

# Stochastic Gradient Descent
for epoch in range(epochs):
    for i in range(len(X)):
        xi = X[i]
        yi = y[i]
        y_pred = m * xi + b
        error = y_pred - yi
        
        # Gradient calculation
        grad_m = 2 * error * xi
        grad_b = 2 * error
        
        # Parameter update
        m -= learning_rate * grad_m
        b -= learning_rate * grad_b

    if epoch % 10 == 0:
        print(f"Epoch {epoch}: m={m[0]:.4f}, b={b:.4f}")

# Final model
print(f"\nFinal parameters: m = {m[0]:.4f}, b = {b:.4f}")

# Plot the data and the regression line
plt.scatter(X, y, color="blue", label="Data points")
plt.plot(X, m * X + b, color="red", label="Regression Line")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression using SGD")
plt.legend()
plt.show()
