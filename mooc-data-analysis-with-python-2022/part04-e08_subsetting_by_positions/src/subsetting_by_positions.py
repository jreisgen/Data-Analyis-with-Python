#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    #Return the top 10 entries and only the columns Title and Artist. Get these elements by their positions, 
    # that is, by using a single call to the iloc attribute
    file = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    file = file.iloc[:10, [2, 3]]
    return file

def main():
    print(subsetting_by_positions())

if __name__ == "__main__":
    main()
