from itertools import product
import numpy as np

# calculate the probability of even number 

SampleSpace = list(range(1, 7))

even_numbers = [2, 4, 6]

# probability of even number
prob_even = len(even_numbers) / len(SampleSpace)
print(f"Probability of even number: {prob_even:.2f}")



# Random variable :dice roll

outcomes= np.array([1,2,3,4,5,6])
probabilities =np.array([1/6*6])
# Expected value of the random variable
expected_value = np.sum(outcomes * probabilities)
print(f"Expected value of the random variable: {expected_value:.2f}")
# Variance of the random variable
variance = np.sum((outcomes - expected_value) ** 2 * probabilities)
print(f"Variance of the random variable: {variance:.2f}")
# Standard deviation of the random variable
std_deviation = np.sqrt(variance)
print(f"Standard deviation of the random variable: {std_deviation:.2f}")

