#!/usr/bin/env python3
import numpy as np
from numpy import linalg as LA

def vector_lengths(a):
    returnV = np.sqrt(np.sum(a**2, axis=1))


    return returnV

def main():
    print(vector_lengths(np.array([[1,2,3],[4,5,6]])))
if __name__ == "__main__":
    main()
