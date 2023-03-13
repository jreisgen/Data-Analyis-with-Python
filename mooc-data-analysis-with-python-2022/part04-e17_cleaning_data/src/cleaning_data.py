#!/usr/bin/env python3
#The entries in the following table of US presidents are not uniformly formatted.
#  Make function cleaning_data that reads the table from the tsv file src/presidents.tsv and returns the 
# cleaned version of it. Note, you must do the edits programmatically using the string edit methods, 
# not by creating a new DataFrame by hand. The columns should have dtypes object, integer, float, integer,
#  object. The where method of DataFrames can be helpful, likewise the string methods of Series objects. 
# You get an additional point, if you manage to get the columns President and Vice-president right!
import pandas as pd
import numpy as np


def cleaning_data():
    file = pd.read_csv("src/presidents.tsv", sep="\t")
    for name in file["President"]:
        if "," in name:
            last, first = name.split(",")
            first = first.strip().capitalize()
            
            last = last.strip().capitalize()
            file["President"] = file["President"].replace(name, first + " " + last)

        else:
            file["President"] = file["President"].str.title()
    
    for date in file["Start"]:
        try:
            int(date)
            file["Start"] = file["Start"].replace(date, int(date))
        except ValueError:
            #if includes string 
            file["Start"] = file["Start"].replace(date, int(date.split(" ")[0].strip()))
    for date in file["Last"]:
        try:
            int(date)
            file["Last"] = file["Last"].replace(date, float(date))
        except ValueError:
            file["Last"] = file["Last"].replace(date, np.nan)
    for num in file["Seasons"]:
        try:
            int(num)
            file["Seasons"] = file["Seasons"].replace(num, int(num))
        except ValueError:
            if num =="one":
                file["Seasons"] = file["Seasons"].replace(num, 1)
            elif num =="two":
                file["Seasons"] = file["Seasons"].replace(num, 2)
    for name in file["Vice-president"]:
        if "," in name:
            last, first = name.split(",")
            first = first.strip().capitalize()
            
            last = last.strip().capitalize()
            file["Vice-president"] = file["Vice-president"].replace(name, first + " " + last)

        else:
            file["Vice-president"] = file["Vice-president"].str.title()
    return file


def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
