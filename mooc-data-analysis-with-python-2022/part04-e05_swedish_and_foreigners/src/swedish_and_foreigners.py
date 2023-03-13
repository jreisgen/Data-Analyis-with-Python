#!/usr/bin/env python3

import pandas as pd

#Write function swedish_and_foreigners that

#Reads the municipalities data set
#Takes the subset about municipalities (like in previous exercise)
#Further take a subset of rows that have proportion of Swedish speaking people and proportion of foreigners both above 5 % level
#From this data set take only columns about population, the proportions of Swedish speaking people and foreigners, that is three columns.
def swedish_and_foreigners():
    file = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    file = file["Akaa":"Äänekoski"]
    file = file[(file["Share of Swedish-speakers of the population, %"] > 5) & (file["Share of foreign citizens of the population, %"] > 5)]
    file = file[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    return file
    

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
