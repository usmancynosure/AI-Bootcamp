import pandas as pd

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Print the first five rows
# print(f"First five rows: \n{df.head()}")

# Print the last five rows
# print(f"Last five rows:\n{df.tail()}")

# Summary of DataFrame
# print(df.info())

# Statistical information
# print(df.describe())

# Select specific columns and filter rows
selected_col = df[["species", "sepal_length"]]

# Filtering rows correctly
filtered_row = df[(df["sepal_length"] > 5.0)]
# print("\n Filtered data:\n", filtered_row)

# save filtered data to new csv file 
# filtered_row.to_csv("newdata.csv")


# craete the dataframe from dictionaryand add a new calculated col
data = {
    'Order ID': [101, 102, 103, 104, 105],
    'Customer': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman'],
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Price': [1000, 500, 300, 1100, 600],
    'Quantity': [1, 2, 1, 1, 3]
}

# Convert dictionary to DataFrame


df = pd.DataFrame(data)



# Add a new calculated column: Total Cost
df["Total Cost"] = df["Price"] * df["Quantity"]
print(df)
