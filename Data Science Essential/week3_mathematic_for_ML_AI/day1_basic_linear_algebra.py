import numpy as np

# 1. Vectors & Matrices
# ---------------------
# Vector (1D array)
v = np.array([2, 12, 1])
print("Vector v:", v)

# Matrix (2D array)
M = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [76, 85, 80]
])
print("\nMatrix M:\n", M)


# 2. Matrix Operations (number of col of 1st matrix should be equal to the no of rows of 2nd matrix     )
# --------------------

# a) Addition & Subtraction
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("\nA + B =\n", A + B)
print("A - B =\n", A - B)

# b) Scalar Multiplication
scalar = 2.5
print(f"\n{scalar} * A =\n", scalar * A)

# c) Matrix Multiplication (dot product)
# A (2×2) times B (2×2)
print("\nA @ B =\n", A @ B)

# d) Transpose
print("\nTranspose of M:\n", M.T)

# e) Inverse (only for square matrices)
invA = np.linalg.inv(A)
print("\nInverse of A:\n", invA)
print("Check A @ A⁻¹ =\n", A @ invA)

# Identity matrix 4 by 4
identity=np.eye(4)

# zero matrix
zero=np.zeros((2,3))

# Diagnol matrix
d=np.diag([1,2,3])
print("Diagnol matrix \n ", d)


