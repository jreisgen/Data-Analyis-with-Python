#!/usr/bin/env python3
import numpy as np
import pandas as pd

def create_series(L1, L2):
    first =  pd.Series(L1, index=["a", "b", "c"])
    second = pd.Series(L2, index=["a", "b", "c"])
    return first, second


    
def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del s2["b"]
    return s1, s2
    
def main():
    s1 = create_series([1, 2, 3], [4, 5, 6])
    s2 = create_series([1, 2, 3], [4, 5, 6])
    print("s1:\n", s1)
    print("s2:\n", s2)
    s3, s4 = modify_series(s1[0], s1[1])
    print("s3:\n", s3)
    print("s4:\n", s4)
    print(s3.__add__(s4))
    
if __name__ == "__main__":
    main()
