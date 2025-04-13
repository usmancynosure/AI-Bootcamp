import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Ali', 'Sara', 'Usman', 'Aisha', 'Bilal', 'Fatima', 'Hamza', 'Zara'],
    'Class': ['10th', '10th', '11th', '11th', '10th', '12th', '12th', '11th'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 92, 78, 88, 90, 95, 80, 87],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

new_df = df.groupby('Class')['Marks'].mean()
new_dff = df.groupby('Class').agg({'Marks': ['mean', 'max', 'min'], 'Name': 'count'})
# print(new_dff)

# print(new_df)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Exercises>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 1: Group Data by a Categorical Column

# Sample dataset
data = {
    'Region': ['North', 'South', 'North', 'East', 'West', 'South', 'East', 'West'],
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'],
    'Sales': [100, 200, 150, 300, 250, 180, 220, 275]
}

df = pd.DataFrame(data)

# Group by Region
grouped_by_region = df.groupby('Region')
print(grouped_by_region.sum())  # Sum of Sales per Region

# Group by Category
grouped_by_category = df.groupby('Category')
print(grouped_by_category.sum())  # Sum of Sales per Category


# Exercise 2: Calculate Summary Statistics for Grouped Data
# Calculate summary statistics
summary_stats = df.groupby('Region')['Sales'].agg(['sum', 'mean', 'count'])
print(summary_stats)
