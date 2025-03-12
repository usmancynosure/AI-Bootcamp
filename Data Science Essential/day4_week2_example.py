# concatination
import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ali', 'Sara', 'Ahmed']})
df2 = pd.DataFrame({'ID': [4, 5, 6], 'Name': ['Fatima', 'Usman', 'Hassan']})

# Concatenate along rows (axis=0)
df_combined = pd.concat([df1, df2], ignore_index=True)
print(df_combined)

# colunm axis=1 merge means add two more col

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ali', 'Sara', 'Ahmed']})
df2 = pd.DataFrame({'Age': [25, 30, 22], 'City': ['Lahore', 'Karachi', 'Islamabad']})

df_combined = pd.concat([df1, df2], axis=1)
print(df_combined)


# Merging 
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ali', 'Sara', 'Ahmed']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [30, 22, 40]})

df_merged = pd.merge(df1, df2, on="ID", how="inner")  # Inner join
print(df_merged)

