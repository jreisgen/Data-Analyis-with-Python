#!/usr/bin/env python3

import pandas as pd

def main():
    file = pd.read_csv("src/municipal.tsv", sep="\t")
    shape = file.shape
    shapestring = str(shape[0]) + "," + str(shape[1])
    print("Shape: ", shapestring)
    print("Columns:")
    for i in file.columns:
        print(i)   
        

if __name__ == "__main__":
    main()
