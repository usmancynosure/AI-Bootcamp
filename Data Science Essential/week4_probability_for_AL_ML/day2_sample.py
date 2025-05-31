import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, Uniform

# Gaussian Distribution
# 1. Generate data points for x-axis
x = np.linspace(-4, 4, 1000)  # Create 1000 points between -4 and 4

# 2. Calculate the probability density function (PDF) for different means and standard deviations
# Standard normal distribution (mean=0, std=1)
y1 = norm.pdf(x, loc=0, scale=1)

# Distribution with mean=1 and std=1
y2 = norm.pdf(x, loc=1, scale=1)

# Distribution with mean=0 and std=2
y3 = norm.pdf(x, loc=0, scale=2)

# 3. Create the plot
plt.figure(figsize=(10, 6))

# Plot the three different normal distributions
plt.plot(x, y1, 'b-', label='μ=0, σ=1 (Standard Normal)')
plt.plot(x, y2, 'r--', label='μ=1, σ=1')
plt.plot(x, y3, 'g:', label='μ=0, σ=2')

# 4. Add labels and title
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Gaussian (Normal) Distribution Examples')
plt.grid(True, alpha=0.3)
plt.legend()

# 5. Show the plot
plt.show()

# 6. Additional example: Generate random samples from normal distribution
samples = np.random.normal(loc=0, scale=1, size=1000)

# 7. Create a histogram of the samples
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=30, density=True, alpha=0.7, color='blue', label='Histogram of samples')

# 8. Plot the theoretical PDF on top of the histogram
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x, loc=0, scale=1), 'r-', label='Theoretical PDF')

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram of Normal Distribution Samples vs Theoretical PDF')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

