# Simulate dice rolls and calculatet the probability 

import numpy as np

# Simulate 1000 dice rolls
num_rolls = 1000
roll = np.random.randint(1, 7, num_rolls)
# Calculate the probability of rolling an even number
even_count = np.sum(roll % 2 == 0)
greater_than_4_count = np.sum(roll > 4)
# Calculate the probability of rolling a number greater than 4
prob_greater_than_4 = greater_than_4_count / num_rolls
print(f"Simulated probability of rolling a number greater than 4: {prob_greater_than_4:.2f}")   
prob_even = even_count / num_rolls
print(f"Simulated probability of even number: {prob_even:.2f}")