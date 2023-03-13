#!/usr/bin/env python3

import pandas as pd
#The first column of the dataFrame should be the input Series, 
# the second column should contain the Series raised to power of two.
#  The third column should contain the Series raised to the power of three, 
# and so on until (and including) power of k
def powers_of_series(s, k):
    mydict = {}
    for i in range(1, k+1):
        mydict[i] = s**i
    return pd.DataFrame(mydict)
    
    
def main():
    s = pd.Series([1, 2, 3, 4, 5])
    print(powers_of_series(s, 4))
    
    
    
if __name__ == "__main__":
    main()
