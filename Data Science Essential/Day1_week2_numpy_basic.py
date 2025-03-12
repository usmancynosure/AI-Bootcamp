import numpy as np

numpy_array= np.array([1,2,3,4,5])
# print(numpy_array)

# 2 by 2 matrix of zeros
zeros = np.zeros((2,2))
# print(zeros)

# 2 by 2 matrix of ones
ones = np.ones((2,2))
# print(ones)

# arrange function
array_arrange=np.arange(1, 10,3)
# print(array_arrange)

# linspace
array_linspace=np.linspace(1, 10, 4)
# print(array_linspace)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>Manipulating Arrays>>>>>>>>>>>>>>>>>>>>>>>>>>
# changing the shape of an array
# list=np.arange(1,10)
# new_arr = list.reshape(3,3)
# print(new_arr)

# Add dimention
arr= np.array([1,2,3])
expanded=arr[:, np.newaxis]
# print(expanded)


# Mathmatical operation
# Create the array using numpy
arr=np.array([4,16,32])
arr1=np.array([4,5,6])

# numpy is useful -->reason is that we add , multiply directly without using loop
add_array=arr+arr1
print(add_array)
print(np.sqrt(arr))
print(np.max(arr))


# indexing and slicing 




