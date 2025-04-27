import numpy as np


# create the 2 by 2 array
matrix=np.array([[1,2],[3,4]])

# find the determinant by using linalg(linear algebra methods)
det=np.linalg.det(matrix)
# print(det) 

# find the inverse 

inverse=np.linalg.inv(matrix)


# Eigenvalue and eigen vector (properties of square matrix that describe transformations)
# if A. v= lambda . v  (v is the eigen vector doesnot change the direction during the tranformation )
# (lamba is the eigen value)

eigenValues, eigenVectors= np.linalg.eigh(matrix)


# Matrix Decomposition
# Prcess of breaking a matrix into simple component to analyze or solve problem
# Singular value decomposition(SVD)
    # -matrix A into three matrix: A=U(left singular matrix). sigma(Diagnol matrix of singular values) . V^T(Right singular matrix)
    
# Application of SVD 
    # - use that noice reduction in Dataset and sometime for image compression
    
U, S, Vt= np.linalg.svd(matrix)
print("U: \n ", U)
print("S: \n ", S)
print("Vt: \n ", Vt)
