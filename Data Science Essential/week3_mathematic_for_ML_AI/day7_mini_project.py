# Hand-on-Project :Linear Regression from Sratch
# Task 1->implement the mathematical formula for linear regression
# Linear Algebra
    #  -Mathematical model : y(predicted values)=X(Feature matric)θ(weights and bais)

import numpy as np


# Generate random data 
np.random.seed(42)  # For reproducibility
X = np.random.rand(100, 1) * 10  # Feature matrix (100 samples, 1 feature)
y = 2.5 * X + np.random.randn(100, 1) * 2  # Target variable with some noise    

# Add bias term (intercept) to the feature matrix
X = np.c_[np.ones((X.shape[0], 1)), X]  # Add a column of ones to X for the intercept
# Initialize parameters (weights)
theta = np.random.randn(2, 1)  # Random initialization of weights (2 parameters: intercept and slope)
# Learning rate and number of iterations
learning_rate = 0.01
iterations = 1000



def predict(X, theta):
    return np.dot(X, theta)

# Task 2 ->Use gradient decient to optimize the model parameter
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)  # number of training examples
    for _ in range(iterations):
        prediction = predict(X, theta)               # ŷ = Xθ
        error = prediction - y                      # error = ŷ - y
        gradient = (1/m) * np.dot(X.T, error)       # compute gradient
        theta -= learning_rate * gradient           # update parameters
    return theta    

# Task 3---> Calculate Evaluation matrix 
def mean_squared_error(y_true, y_pred):
    # Calculate the Mean Squared Error  
    # formula of Mean Squared Error (MSE) is:
    # MSE = (1/n) * Σ(y_true - y_pred)^2
    return np.mean((y_true - y_pred) ** 2)

def r_squared(y_true, y_pred):
    ss_residual = np.sum((y_true - y_pred) ** 2)
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1 - (ss_residual / ss_total)
    return r2



# Perform the gradient descent optimization
optimized_theta = gradient_descent(X, y, theta, learning_rate, iterations)
# Make predictions using the optimized parameters
y_pred = predict(X, optimized_theta)
# Calculate evaluation metrics
mse = mean_squared_error(y, y_pred)
r2 = r_squared(y, y_pred)
# Print the results
print("Optimized parameters (theta):", optimized_theta)
print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)