#!/usr/bin/env python3
#Merge the DataFrames UK top40 and the bands DataFrame that are stored in the src folder. 
# Do all this in the parameterless function top_bands, which should return the merged DataFrame.
#  Use the left_on and right_on parameters to merge. 
# Test your function from the main function.
import pandas as pd

def top_bands():
    top40 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    bands = pd.read_csv("src/bands.tsv", sep="\t")
    for artist in top40["Artist"]:
        #lower case
        top40["Artist"] = top40["Artist"].str.lower()
    
    for band in bands["Band"]:
        #lower case
        bands["Band"] = bands["Band"].str.lower()
        
    
    merged = pd.merge(top40, bands, how="inner", left_on="Artist", right_on="Band")
    return merged

def main():
    print(top_bands())

if __name__ == "__main__":
    main()
