#!/usr/bin/env python3

import pandas as pd
import numpy as np
#Read again the bicycle data set from src folder, and clean it as in the earlier exercise. 
# Then split the Päivämäärä column into a DataFrame with five columns with column names Weekday,
#  Day, Month, Year, and Hour. Note that you also need to to do some conversions. To get Hours, 
# drop the colon and minutes. Convert field Weekday according the following rule:
#ma -> Mon
#ti -> Tue
#ke -> Wed

def split_date():
    file = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    file = file.dropna(how="all")
    file = file.dropna(axis=1, how="all")
    #only keep first column
    file = file[file.columns[0]]
    #split the column into 5 columns
    file = file.str.split(expand=True)
    #rename columns

    file.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    file["Hour"] = file["Hour"].str.split(":", expand=True)[0]
    #Hour should have 0, not 00 value
    file["Hour"] = file["Hour"].astype(int)
    file["Weekday"] = file["Weekday"].map({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"})
    file["Day"] = file["Day"].astype(int)
    file["Year"] = file["Year"].astype(int)
    file["Month"] = file["Month"].map({"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12})
    
    return file
    

def main():
    print(split_date())
       
if __name__ == "__main__":
    main()
