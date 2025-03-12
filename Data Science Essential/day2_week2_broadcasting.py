# Broadcasting -->To perform arithemtic operation on arrays on different shape
import numpy as np

# make the array from the list
array=np.array([1,2,3])
# add the 10 -->by applying broadcasting technique automaticlly
# print(array+10) #This will add the 10 to each element in the array 


# create the 2 by 3 matrix
matrix=np.array([[2,3,4], [6,7,8]])
vector=np.array([1,0,1])  #this means 3  rows and i coloum
# print(matrix.shape)
# print(vector.shape)
# print(matrix+vector)


# Aggregation function-->compute summary statistic for array
# useful in AI-->calculate mean, median ,sum , standard deviation

# create the 2 by 3 matrix
matrix=np.array([[2,3,4], [6,7,8]])
# perform the aggregation methods
print(f"sum of elements are : {np.sum(matrix)}")
print(f"Mean of matrix is :{np.mean(matrix)}")
print(f"Standart Deviation is {np.std(matrix)}")
print(f"Sum across rows {np.sum(matrix ,axis=1)}")
print(f"Sum across col {np.sum(matrix ,axis=0)}")


# Booloean Indexing and Filtering  -->specially usefull when traning models and value chahneg in data sets
arr=np.array([1,2,3,4])

even=arr[arr%2==0]
print("evens, ",even)

arr[arr>2]=0
print("Modified array: ", arr)


# Random number 
np.random.seed(42)  # tgis is very useful in modeel trainnig they ensure the result are from only dataset , result are not changing/out of context
random_array = np.random.rand(5)  # Generates 5 random floats
print(random_array)

random_int = np.random.randint(1, 100)  # Generates a random integer between 1 and 99
print(random_int)

random_int_array = np.random.randint(1, 100, size=(3, 3))  # 3x3 matrix of random integers
print(random_int_array)

