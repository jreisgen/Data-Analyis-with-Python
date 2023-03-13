#!/usr/bin/env python3

import numpy as np
#Write function first_half_second_half that gets a two dimensional array of shape (n,2*m) as a parameter. 
# The input array has 2*m columns
#The output from the function should be a matrix with those rows from the 
# input that have the sum of the first m elements larger than the sum of the 
# last m elements on the row.
def first_half_second_half(a):
    length = len(a[0])
    half = int(length/2)
    

    return a[np.sum(a[:,0:half], axis=1) > np.sum(a[:,half:length], axis=1)]
    
def main():
    print(first_half_second_half(np.array([[1, 3, 4, 2],[2, 2, 1, 2]])))
if __name__ == "__main__":
    main()
