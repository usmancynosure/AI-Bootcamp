import pandas as pd

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Print the first five rows
print(f"First five rows: \n{df.head()}")

# Print the last five rows
print(f"Last five rows:\n{df.tail()}")

# Summary of DataFrame
print(df.info())

# Statistical information
print(df.describe())

# Select specific columns and filter rows
# Correcting column name from "sepal_lenght" to "sepal_length"
selected_col = df[["species", "sepal_length"]]
print(selected_col)


filter_row=df[(df["sepal_length"] > 5.0)]
print(filter_row)
