#!/usr/bin/env python3
import numpy as np
from functools import reduce


#Repeat the functionality of the NumPy function numpy.linalg.matrix_power, 
# which raises a square matrix of shape (m,m) to the nth power. 
# Here the multiplication is the matrix multiplication.
#  Square matrix a raised to power n is therefore a @ a @ ... @ a where a is repeated n times.
#  When n is zero then �0a 0  is equal to np.eye(m).Write function matrix_power that gets as 
# first argument a square matrix a and as second argument a non-negative integer n. 
# The function should return the matrix a multiplied by itself n-1 times.
#  Use Python's reduce function and a generator expression.Extend the matrix_power function. 
# For negative powers, we define �−1a−1  to be equal to the multiplicative inverse of a. 
# You can use NumPy's function numpy.linalg.inv for this. 
# And you may assume that the input matrix is invertible.

def matrix_power(a, n):
    if n == 0:
        return np.eye(len(a))
    elif n > 0:
        return reduce(np.dot, (a for _ in range(n)))
    else:
        return np.linalg.inv(reduce(np.dot, (a for _ in range(-n))))

    

def main():
    print(matrix_power(np.array([[1, 2], [3, 4]]), 2))

if __name__ == "__main__":
    main()
