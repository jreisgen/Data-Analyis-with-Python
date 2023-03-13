#!/usr/bin/env python3
import numpy as np
import pandas as pd

#Write function read_series that reads input lines from the user and return a Series. 
# Each line should contain first the index and then the corresponding value, separated by whitespace.
#  The index and values are strings (in this case dtype is object). An empty line signals the end of Series.
#  Malformed input should cause an exception. An input line is malformed, if it is non-empty and, when split
#  at whitespace, does not result in two parts.
def read_series():
    mydict = {}

    while True:
        try:
            line = input()
            if line == "":
                break
            else:
                index, value = line.split(" ")
                mydict[index] = value
        except ValueError:
            print("Malformed input")
            break
    
    return pd.Series(mydict)
            

    
    


def main():
    print(read_series())

if __name__ == "__main__":
    main()
