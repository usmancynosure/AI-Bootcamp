# Plot and explore the distribution of the data
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm

# gausain distribution
'''
x=np.linspace(-4, 4, 100)
mu, sigma = 0, 1
y=norm.pdf(x, mu, sigma)
plt.plot(x, y)
plt.title("Gausain Distribution")
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.grid()
plt.show()
'''

# Binomial distribution(fixed number of independent Bernoulli trials)
# Model the number of successes in n independent Bernoulli trials
'''
n, p = 10, 0.5
x = np.arange(0, n+1)
y = binom.pmf(x, n, p)
plt.bar(x, y, color="Silver")
plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.xticks(x)
plt.grid()
plt.show()
'''
# Poisson distribution(fixed interval of time and space)
# Model the number of events in a fixed interval of time and space

'''
lam = 3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)
plt.bar(x, y, color="yellow")
plt.title("Poisson Distribution")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.xticks(x)
plt.grid()
plt.show()
'''

# create and visualize the multinomial distribution
# Multinomial distribution
# Model the number of successes in n independent trials with k possible outcomes
n = 10  # number of trials
k = 3   # number of outcomes
p = [0.2, 0.5, 0.3]  # probabilities of each outcome
x = np.arange(0, n+1)
y = np.zeros((len(p), n+1))
for i in range(len(p)):
    y[i] = binom.pmf(x, n, p[i])
plt.bar(x, y.T, color=["red", "green", "blue"], alpha=0.5)
plt.title("Multinomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.xticks(x)
plt.legend(["Outcome 1", "Outcome 2", "Outcome 3"])
plt.grid()
plt.show()

