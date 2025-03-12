import pandas as pd

# Sample dataset
data = {'Name': ['Ali', 'Sara', 'Ahmed', None, 'Usman'],
        'Age': [25, 30, 22, None, 28],
        'Salary': [50000, 60000, 55000, 52000, None]}

df = pd.DataFrame(data)

# Drop rows with missing values
df_cleaned = df.dropna()

print(df_cleaned)

# Fill missing values with the mean of the column
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Fill missing values with the mode (most frequent value)
df['Name'].fillna(df['Name'].mode()[0], inplace=True)

# Fill missing values with a fixed value
df['Salary'].fillna(50000, inplace=True)

print(df)


# ...................interpolation...........................
'''
Weather Forecasting: If temperature data is missing for a day, 
    we can estimate it using the temperatures of nearby days.
Stock Market: If stock prices are missing on a holiday, 
    interpolation can estimate the price based on previous and next days.

'''
import numpy as np

# Creating a sample dataset with missing values
data = {'Date': pd.date_range(start='2024-03-01', periods=5, freq='D'),
        'Temperature': [28, np.nan, 30, np.nan, 32]}

df = pd.DataFrame(data)

# Using interpolation to fill missing values
df['Temperature'] = df['Temperature'].interpolate()

print(df)

