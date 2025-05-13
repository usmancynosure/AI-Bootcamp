# Exercise 1--->Calculate the mean, median, and mode of a list of numbers.

import numpy as np
data = [10, 20, 30, 40, 50]
mean=np.mean(data)
median=np.median(data)
mode = np.argmax(np.bincount(data))
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

# Exercise 2--->Calculate the variance and standard deviation of a list of numbers.
data = [10, 20, 30, 40, 50]
variance = np.var(data)
std_dev = np.std(data)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

# Perform the T set to compare the two data sets
# T set is a statistical test used to determine if there is a significant difference between the means of two groups
# It is commonly used in hypothesis testing to compare the means of two groups
from scipy.stats import ttest_ind
data1 = [10, 20, 30, 40, 50]
data2 = [15, 25, 35, 45, 55]
t_statistic, p_value = ttest_ind(data1, data2) # independent t-test
# t_statistic is the calculated t-value
# p_value is the probability of observing the data given that the null hypothesis is true
print("T-statistic:", t_statistic)
print("P-value:", p_value)
