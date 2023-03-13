#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def bicycle_timeseries():
    df = pd.read_csv("Helsingin_pyorailijamaarat.csv", sep=";")
    #create copy of df
    dfcopy = df.copy()
    df = df.dropna(how="all")
    dfcopy = dfcopy.dropna(how="all")
    df = df.dropna(axis=1, how="all")
    dfcopy = dfcopy.dropna(axis=1, how="all")
    #dfcopy drop first column
    dfcopy = dfcopy[dfcopy.columns[1:]]
    #only keep first column
    df = df[df.columns[0]]
    #split the column into 5 columns
    df = df.str.split(expand=True)
    #rename columns
    df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df["Hour"] = df["Hour"].str.split(":", expand=True)[0]
    #Hour should have 0, not 00 value
    df["Hour"] = df["Hour"].astype(int)
    df["Weekday"] = df["Weekday"].map({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"})
    df["Day"] = df["Day"].astype(int)
    df["Year"] = df["Year"].astype(int)
    df["Month"] = df["Month"].map({"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12})
    df["Month"] = df["Month"].astype(int)

    df = pd.concat([df, dfcopy],  axis=1)
#turns its Päivämäärä column into (row) DatetimeIndex (that is, to row names) of that DataFrame
#returns the new DataFrame
    df = df.set_index(pd.to_datetime(df[["Year", "Month", "Day", "Hour"]]))
    df = df.drop(["Year", "Month", "Day", "Hour"], axis=1)
    return df
#In function commute do the following:

#Use the function bicycle_timeseries to get the bicycle data. Restrict to August 2017, group by the weekday, aggregate by summing. Set the Weekday column to numbers from one to seven. Then set the column Weekday as the (row) index. Return the resulting DataFrame from the function.

#In the main function plot the DataFrame. Xticklabels should be the weekdays. Don't forget to call show function!
def commute():
    df = bicycle_timeseries()
    df = df["2017-08"]
    df = df.groupby("Weekday").sum()
    df["Weekday"] = [1, 2, 3, 4, 5, 6, 7]
    df = df.set_index("Weekday")
    return df
     
    
def main():
    df = commute()
    print(df)
    df.plot()
    plt.xticks(df.index, ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    plt.show()
    


if __name__ == "__main__":
    main()
