#!/usr/bin/env python3

import pandas as pd
#We use again the UK top 40 data set from the first week of 1964 in the src folder. 
# Here we define "goodness" of a record company (Publisher) based on the sum of the weeks on chart (WoC)
#  of its singles. Return a DataFrame of the singles by the best record company 
# (a subset of rows of the original DataFrame). 
# Do this with function best_record_company.
def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")
    df["WoC"] = df["WoC"].astype(int)
    #create copy of df
    dfcopy = df.copy()
    
    df = df.groupby("Publisher").sum()
    df = df.sort_values("WoC", ascending=False)
    #take first publisher
    publisher = df.index[0]
    #filter dfcopy by publisher
    dfcopy = dfcopy[dfcopy["Publisher"] == publisher]
    return dfcopy
    

    

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()
