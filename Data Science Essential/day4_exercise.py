import pandas as pd
import numpy as np

# Creating the sample dataset
data = {
    'Name': ['Ali', 'Sara', 'Ahmed', np.nan, 'Usman'],
    'Age': [25, 30, 22, np.nan, 28],
    'Salary': [50000, 60000, 55000, 52000, np.nan]
}

df = pd.DataFrame(data)

# Printing original dataset
print("\nOriginal Data Set \n", df)

# Handling missing values: Fill missing 'Age' with mean age
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Handling missing values: Fill missing 'Salary' with median salary
df['Salary'].fillna(df['Salary'].interpolate(), inplace=True)

# Handling missing values: Fill missing 'Name' with "Unknown"
df['Name'].fillna("Unknown", inplace=True)

# Renaming columns
df.rename(columns={'Name': 'Full Name', 'Age': 'Person Age', 'Salary': 'Monthly Salary'}, inplace=True)

# Printing cleaned dataset
print("\nCleaned Data Set \n", df)



# Exercise two -->meerge two dataset and apply tranformation
data1 = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman'],
    'Math_Score': [90, np.nan, 78, np.nan, 85],
    'English_Score': [88, 75, np.nan, 82, 90]
}


data2 = {
    'Student_ID': [101, 102, 103, 104, 106],
    'Attendance_Percentage': [95, 80, np.nan, 85, 92],
    'School': ['ABC School', 'XYZ School', 'ABC School', 'XYZ School', 'LMN School']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# merge two data frame
new_data=pd.merge(df1,df2, on='Student_ID', how='right')
print("\n new dataset is\n : ",new_data)
