#!/usr/bin/env python3
import numpy as np
import pandas as pd
    #Write function suicide_fractions that loads the data set and returns a Series that has the country 
    # as the (row) index and as the column the mean fraction of suicides per population in that country. 
    # In other words, the value is the average of suicide fractions. 
    # The information about year, sex and age is not used
def suicide_fractions():
    file = pd.read_csv("src/who_suicide_statistics.csv")
    #filter file 

    
    for row in file:
        try:
        
            value = (file["suicides_no"])
            pop = (file["population"])
            file["average"] = value / pop
        except:
            file["average"] = (0)

    return file.groupby("country") ["average"].mean()
    #amount of people per country



    

    



def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
