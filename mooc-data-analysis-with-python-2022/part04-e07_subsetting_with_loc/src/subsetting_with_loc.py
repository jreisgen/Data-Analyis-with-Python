#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    file = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    file = file.loc["Akaa":"Äänekoski", ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    return file
    

def main():
    print(subsetting_with_loc())

if __name__ == "__main__":
    main()
