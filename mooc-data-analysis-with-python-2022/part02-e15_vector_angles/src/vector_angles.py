#!/usr/bin/env python3
import numpy as np
from numpy import linalg as LA
def vector_angles(X, Y):
    np.clip(X,-1,1)
    np.clip(Y,-1,1)
    returnV = np.arccos(np.sum(X*Y, axis=1)/(np.sqrt(np.sum(X**2, axis=1))*np.sqrt(np.sum(Y**2, axis=1))))
    

    return (returnV)
def main():
    print(vector_angles(np.array([[1,0,0],[0,1,0]]), np.array([[0,1,0],[1,0,0]])))
if __name__ == "__main__":
    main()
