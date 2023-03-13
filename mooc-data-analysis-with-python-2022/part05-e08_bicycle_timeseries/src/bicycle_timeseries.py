#!/usr/bin/env python3

import pandas as pd
#Write function bicycle_timeseries that

#reads the data set
#cleans it
#turns its Päivämäärä column into (row) DatetimeIndex (that is, to row names) of that DataFrame
#returns the new DataFrame

def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
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
    df = df.drop(["Year", "Month", "Day", "Hour", "Weekday"], axis=1)
    return df
    


def main():
    print(bicycle_timeseries())
    

if __name__ == "__main__":
    main()
