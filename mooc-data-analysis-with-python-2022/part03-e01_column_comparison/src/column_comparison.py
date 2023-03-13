#!/usr/bin/env python3
import numpy as np
#The function should return a new array containing those rows from
#  the input that have the value in the second column larger than in the second
#  last column. You may assume that the input contains at least two columns. 
# Don't use loops, but instead vectorized operations. Try out your function in the main function.
def column_comparison(a):
    return a[a[:,1] > a[:,-2]]
    
def main():
    print(column_comparison(np.array([[1,2,3],[4,5,6],[7,8,9]])))
    

if __name__ == "__main__":
    main()
