# Basic syntax
import pandas as pd

# Sample Data
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Values': [10, 20, 30, 40, 50, 60]}

df = pd.DataFrame(data)

# Group by Category
grouped = df.groupby('Category')
# print(grouped.mean())  # Aggregating with mean


# sum of each group 
df.groupby('Category')['Values'].sum()
# Multiple aggregation
df.groupby('Category')['Values'].agg(['sum', 'mean', 'max'])

# Grouping multiple couloums 
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'SubCategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Values': [10, 20, 30, 40, 50, 60]
})

df.groupby(['Category', 'SubCategory'])['Values'].sum()







# Exercise 1--->grouped data by categorical colunm



