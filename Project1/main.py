import numpy as np
from numpy.linalg import matrix_power
v = np.array([2,4,5])
# Finding the normal of a vector
vector_mag = np.linalg.norm(v)
# Finding the inverse of a matrix
arr = np.array([[1,2],
                [3,4]])
# Calculating the power of a matrix:
i = np.array([[0, 1], [-1, 0]]) # matrix equiv. of the imaginary unit
print("Normal of the vector is:",vector_mag)
print("Inverse of the vector is")
print(np.linalg.inv(arr))
print("Power of the given matrix is")
print(matrix_power(i, 3))