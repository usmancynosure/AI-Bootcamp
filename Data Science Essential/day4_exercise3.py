# one hot encoding  , 
'''
Why One-Hot Encoding?
Many ML models require numerical input.
Prevents incorrect ordinal relationships.
Ensures better performance in training.

'''
import pandas as pd

# Sample DataFrame
data = {
    'Customer_ID': [101, 102, 103, 104, 105],
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman'],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Lahore', 'Karachi'],
    'Payment_Method': ['Credit Card', 'Cash', 'Debit Card', 'Credit Card', 'UPI']
}

df = pd.DataFrame(data)
print("🔹 Original DataFrame:\n", df)

# Apply One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['City', 'Payment_Method'])

print("\n🔹 One-Hot Encoded DataFrame:\n", df_encoded)
