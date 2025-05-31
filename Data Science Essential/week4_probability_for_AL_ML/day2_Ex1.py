# Ex-> Plot and Exploer Varoius Dsitribution

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, binom , poisson, Uniform

# Gaussian (normal ) Distribution

# Generate data for Gaussian distribution
data = norm.rvs(loc=5, scale=2, size=1000)

# Plot histogram
plt.hist(data, bins=20, density=True, alpha=0.6, color='b')

# Plot Gaussian distribution
x = np.linspace(0, 10, 100)
plt.plot(x, norm.pdf(x, loc=5, scale=2), 'r-', label='Gaussian PDF')

# Add labels and title 
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Gaussian Distribution')
plt.legend()
plt.show()

# Binomial Distribution

# Generate data for Binomial distribution
n = 10
p = 0.5
data = binom.rvs(n, p, size=1000)  

# Plot histogram
plt.hist(data, bins=11, density=True, alpha=0.6, color='g')

# Plot Binomial distribution
x = np.arange(0, 11)
plt.plot(x, binom.pmf(x, n, p), 'b-', label='Binomial PMF')

# Add labels and title
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution')
plt.legend()
plt.show()

# Poisson Distribution

# Generate data for Poisson distribution
mu = 3
data = poisson.rvs(mu, size=1000)

# Plot histogram
plt.hist(data, bins=11, density=True, alpha=0.6, color='y')

# Plot Poisson distribution
x = np.arange(0, 11)
plt.plot(x, poisson.pmf(x, mu), 'c-', label='Poisson PMF')  

# Add labels and title
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.title('Poisson Distribution')
plt.legend()
plt.show()







