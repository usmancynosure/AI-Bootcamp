from statistics import mode
# day 6 statistics

# Measure of Central Tendency and Dispersion
# This program calculates the mean, median, and mode of a list of numbers.
# mean is the average of the numbers
# median is the middle number when the numbers are sorted
# mode is the number that appears most frequently

 

data=[10,20,30,40]
mean= sum(data)/len(data)
print("Mean:", mean)

# median 
data_sorted = sorted(data)
if len(data_sorted) % 2 == 0:
    # If even, average the two middle numbers
    median = (data_sorted[len(data_sorted)//2 - 1] + data_sorted[len(data_sorted)//2]) / 2
else:
    # If odd, take the middle number
    median = data_sorted[len(data_sorted)//2]
print("Median:", median)


# mode
# if there are unique values, mode will return the first one
# if there are no repeating values, mode will raise an exception


try:
    mode_value = mode(data)
    print("Mode:", mode_value)
except StatisticsError:
    print("No unique mode found")
    
    
# Variance and Standard Deviation
# Variance is the average of the squared differences from the mean
# Standard deviation is the square root of the variance

# variance
def variance(data):
    mean = sum(data) / len(data)
    # Calculate the variance
    # using the formula: variance = sum((x - mean) ** 2 for x in data) / len(data)
    # where x is each value in the data set
    # mean is the average of the data set
    # len(data) is the number of values in the data set
    # The variance measures how far each number in the set is from the mean
    return sum((x - mean) ** 2 for x in data) / len(data)

# standard deviation
def standard_deviation(data):
    return variance(data) ** 0.5
# Example data
data = [10, 20, 30, 40, 50]
# Calculate variance and standard deviation
var = variance(data)
std_dev = standard_deviation(data)
print("Variance:", var)
print("Standard Deviation:", std_dev)


