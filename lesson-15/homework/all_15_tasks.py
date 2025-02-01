import numpy as np

# 1. Create a vector with values ranging from 10 to 49.

# vector = np.arange(10, 50)
# print(vector)


# 2. Create a 3x3 matrix with values ranging from 0 to 8.

# matrix = np.arange(9).reshape(3, 3)
# print(matrix)

# 3. Create a 3x3 identity matrix.

# matrix = np.eye(3, dtype=int)
# print(matrix)

# 4. Create a 3x3x3 array with random values.

# arr = np.random.randint(0, 100, (3, 3, 3))
# print(arr)

# 5. Create a 10x10 array with random values and find the minimum and maximum values.

# arr = np.random.randint(0, 100, (10, 10))
# print(arr, arr.min(), arr.max())

# 6. Create a random vector of size 30 and find the mean value.

# vector = np.random.randint(0, 100, 30)
# print(vector, vector.mean())

# 7. Normalize a 5x5 random matrix.

#Column wise normalisation is used
# matr = np.random.randint(0, 10, (5, 5))
# print(matr)
# sum_squares = ((matr**2).sum(axis=0))

# root_sum_squares = (sum_squares ** 0.5).round(2)
# print(root_sum_squares)

# print(matr / root_sum_squares)



# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).

# A = np.random.randint(0, 10, (5, 3))
# B = np.random.randint(0, 10, (3, 2))
# print(A @ B)

# 9. Create two 3x3 matrices and compute their dot product.

# A = np.random.randint(0, 10, (3, 3))
# B = np.random.randint(0, 10, (3, 3))
# print(np.dot(A, B))

# 10. Given a 4x4 matrix, find its transpose.

# A = np.random.randint(0, 10, (4, 4))
# print(A)
# print(A.transpose())

# 11. Create a 3x3 matrix and calculate its determinant.

# A = np.random.randint(0, 10, (3, 3))
# print(A)
# print(np.linalg.det(A))

# 12. Create two matrices ( A ) (3x4) and ( B ) (4x3), and compute the matrix product ( A \cdot B ).

# A = np.random.randint(0, 10, (3, 4))
# B = np.random.randint(0, 10, (4, 3))
# print(A, "\n", B)
# print(np.dot(A, B))

# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.

# A = np.random.randint(0, 10, (3, 3))
# B = np.random.randint(0, 10, (3))
# print(A, '\n', B)
# print(A * B)

# 14. Solve the linear system ( Ax = b ) where ( A ) is a 3x3 matrix, and ( b ) is a 3x1 column vector.

# A = np.random.randint(0, 10, (3, 3))
# b = np.random.randint(0, 10, (3))
# print(A)
# print(b)

# if np.linalg.det(A) != 0:
#     print(np.linalg.inv(A) @ b)
# else:
#     print("Matrix is not invertible, so there is NO uniques solution for x")

# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.

# A = np.random.randint(0, 10, (5, 5))
# print(A)
# print(f"row-wise sum: {A.sum(axis=1)}")
# print(f"column-wise sum: {A.sum(axis=0)}")