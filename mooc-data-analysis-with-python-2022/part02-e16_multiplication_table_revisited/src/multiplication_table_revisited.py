#!/usr/bin/env python3
import numpy as np

def multiplication_table(n):
    rV = np.broadcast_arrays(np.arange(0,n).reshape(-1,1), np.arange(0,n).reshape(1,-1))
    return rV[0]*rV[1]
def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
