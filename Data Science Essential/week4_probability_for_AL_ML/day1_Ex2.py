import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform

# create the discreate random variable 
outcomes = np.array([1, 2, 3, 4, 5, 6])
probabilities = np.array([1/6] * 6)  # uniform distribution for a fair die

plt.bar(outcomes, probabilities, color='blue', alpha=0.7)
plt.xlabel('Outcomes')
plt.ylabel('Probability')
plt.title('Probability Distribution of a Fair Die')
plt.show()

# continuous random variable
# create a continuous random variable

x= np.linspace(0, 1, 100)
pdf= uniform.pdf(x, 0, 1)

plt.plot(x, pdf, color='red')
plt.xlabel('x')
plt.ylabel('Probability Density Function')
plt.title('Probability Density Function of Uniform Distribution')
plt.show()
