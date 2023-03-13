#!/usr/bin/env python3

import pandas as pd
#Write function growing_municipalities that gets subset of municipalities (a DataFrame) as a parameter and returns
#  the proportion of municipalities with increasing population in that subset.
def growing_municipalities(df):
    file = df
    file = file[file["Population change from the previous year, %"] > 0]
    return len(file) / len(df) 
    

def main():
    print("Proportion of growing municipalities: {:.1f}%".format(growing_municipalities(pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")["Akaa":"Äänekoski"])))

if __name__ == "__main__":
    main()
