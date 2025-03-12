import pandas as pd
import numpy as np

# Creating a sample DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],   # 80% non-null (kept)
    'B': [np.nan, np.nan, np.nan, 3, 4],  # 40% non-null (dropped)
    'C': [10, 20, 30, np.nan, np.nan],   # 60% non-null (kept)
    'D': [np.nan, np.nan, np.nan, np.nan, 5]  # 20% non-null (dropped)
}

df = pd.DataFrame(data)
# print("🔹 Original DataFrame:\n", df)

# Drop columns with more than 50% missing values
# thresh--->sets the minimum number of non-null (not missing) values required to keep a column.
df_cleaned = df.dropna(thresh=len(df) * 0.5, axis=1)
# print("\n🔹 DataFrame after Dropping Columns:\n", df_cleaned)





# Ex2----->merge three datasset and analyze relationship beetween them 
import pandas as pd

# Creating Customer Data
customers = pd.DataFrame({
    'Customer_ID': [101, 102, 103, 104, 105],
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman'],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Lahore', 'Karachi']
})

# Creating Order Data
orders = pd.DataFrame({
    'Order_ID': [201, 202, 203, 204, 205],
    'Customer_ID': [101, 103, 102, 105, 104],
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Camera'],
    'Amount': [1000, 500, 300, 200, 700]
})

# Creating Payment Data
payments = pd.DataFrame({
    'Order_ID': [201, 202, 203, 204, 205],
    'Payment_Method': ['Credit Card', 'Cash', 'Debit Card', 'Credit Card', 'UPI'],
    'Status': ['Paid', 'Pending', 'Paid', 'Paid', 'Pending']
})

# Display the three datasets
print("🔹 Customers Data:\n", customers)
print("\n🔹 Orders Data:\n", orders)
print("\n🔹 Payments Data:\n", payments)

# merge order and payment based on order_ID

new_df=pd.merge(orders,payments, on='Order_ID', how='inner')