import numpy as np

# Function to create arrays
def create_array():
    array1 = np.arange(1, 6)  # Creates array [1, 2, 3, 4, 5]
    array2 = np.arange(6, 11)  # Creates array [6, 7, 8, 9, 10]
    return array1, array2

# Getting the arrays
arr1, arr2 = create_array()

# Performing mathematical operations
sum_result = arr1 + arr2      # Element-wise addition
diff_result = arr1 - arr2     # Element-wise subtraction
prod_result = arr1 * arr2     # Element-wise multiplication
div_result = arr1 / arr2      # Element-wise division

# Printing results
# print("Array 1:", arr1)
# print("Array 2:", arr2)
# print("Sum:", sum_result)
# print("Difference:", diff_result)
# print("Product:", prod_result)
# print("Division:", div_result)


# Creating a 4x4 matrix
matrix = np.array([
    [1, 2, 3, 4], 
    [6, 7, 3, 2], 
    [1, 2, 4, 8], 
    [4, 8, 0, 1]
])

# Sum of all elements in the matrix
total_sum = np.sum(matrix)

# Sum of each row (axis=1)
row_sum = np.sum(matrix, axis=1)

# Sum of each column (axis=0)
column_sum = np.sum(matrix, axis=0)

# Printing results
print("Matrix:\n", matrix)
print("\nTotal Sum:", total_sum)
print("Sum of each row:", row_sum)
print("Sum of each column:", column_sum)

