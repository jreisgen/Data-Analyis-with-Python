#!/usr/bin/env python3
import numpy as np

def get_row_vectors(a):
    returnV = []
    for row in a:
        returnV.append(np.reshape(row,(1,len(row))))
    return (returnV)

def get_column_vectors(a):
    returnV2 = []
    for column in a.T:
        returnV = []
        for i in range(len(column)):
            returnV.append([column[i]])
        returnV2.append(np.array(returnV))
    return (returnV2)

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
