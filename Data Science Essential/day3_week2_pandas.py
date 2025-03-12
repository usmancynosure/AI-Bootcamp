# pandas -->python powerful library for data manipulation and analysis 
# Pandas Data structure  -->series and dataframe
# series -->one dimentional labeled  array cappable of holding data of any type 
# data frame -->two dimentional labeled data structure like a table 
import pandas as pd
'''🔹 What is Pandas?
Pandas is a Python library for data manipulation and analysis. It provides powerful data structures such as:
✅ Series (1D labeled array)
✅ DataFrame (2D labeled table like an Excel sheet)


import pandas as pd
🔹 Core Pandas Concepts with Real-World Use Cases
📌 Scenario 1: Sales Data Analysis for an E-Commerce Store
You run an eCommerce store and track sales data. You need to analyze total revenue, filter high-value orders, and visualize sales trends.

👉 Implementation
'''
# Sample sales data
data = {
    'Order ID': [101, 102, 103, 104, 105],
    'Customer': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman'],
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Price': [1000, 500, 300, 1100, 600],
    'Quantity': [1, 2, 1, 1, 3]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)
print(df)

# 1️⃣ Calculate Total Revenue
df['Total'] = df['Price'] * df['Quantity']
print("\nTotal Revenue for each order:\n", df)

# 2️⃣ Filter High-Value Orders (above $1000)
high_value_orders = df[df['Total'] > 1000]
print("\nHigh-Value Orders:\n", high_value_orders)

# 3️⃣ Group by Product and Calculate Total Sales
sales_summary = df.groupby('Product')['Total'].sum()
print("\nTotal Sales per Product:\n", sales_summary)
# Concepts Used
# ✅ Creating a DataFrame
# ✅ Column operations (df['Total'] = df['Price'] * df['Quantity'])
# ✅ Filtering (df[df['Total'] > 1000])
# ✅ Grouping and Aggregation (groupby() for sales summary)

# 📌 Scenario 2: Customer Data Cleaning & Analysis
# Your company has a customer database, but there are missing values and duplicate records. You need to clean the data and find the top customers.

# 👉 Implementation
# Creating a DataFrame with missing values & duplicates
customer_data = {
    'Customer ID': [1, 2, 3, 4, 5, 5],
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman', 'Usman'],
    'City': ['Karachi', 'Lahore', 'Islamabad', 'Lahore', None, 'Lahore'],
    'Age': [25, 30, 22, 27, 35, 35],
    'Spending ($)': [500, 700, 200, 450, 900, 900]
}

df = pd.DataFrame(customer_data)

# 1️⃣ Handling Missing Values
df.fillna("Unknown", inplace=True)  # Fill missing city names
print("\nData after handling missing values:\n", df)

# 2️⃣ Removing Duplicates
df.drop_duplicates(inplace=True)
print("\nData after removing duplicates:\n", df)

# 3️⃣ Finding the Top 2 Customers by Spending
top_customers = df.nlargest(2, 'Spending ($)')
print("\nTop 2 Customers by Spending:\n", top_customers)
# Concepts Used
# ✅ Handling missing values (fillna())
# ✅ Removing duplicates (drop_duplicates())
# ✅ Finding top values (nlargest())

# 🔹 Other Pandas Functions
# 📌 Read & Write Files


df = pd.read_csv('data.csv')  # Read CSV file
df.to_excel('data.xlsx')  # Save as Excel
# 📌 Sorting Data

df_sorted = df.sort_values('Price', ascending=False)
# 📌 Merging DataFrames


merged_df = pd.merge(df1, df2, on='Customer ID')



df['Date'] = pd.to_datetime(df['Date'])

