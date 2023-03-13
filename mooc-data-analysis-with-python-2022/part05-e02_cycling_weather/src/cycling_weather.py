#!/usr/bin/env python3

import pandas as pd
#Merge the processed cycling data set (from the previous exercise) and 
# weather data set along the columns year, month, and day. Note that the names of these
#  columns might be different in the two tables: use the left_on and right_on parameters.
#  Then drop useless columns 'm', 'd', 'Time', and 'Time zone'.

#Write function cycling_weather that reads the data sets and returns the resulting DataFrame.

def cycling_weather():
    first = split_date_continues()
    first = first.dropna(how="all")
    first = first.dropna(axis=1, how="all")

    #merge the two dataframes
    weather = pd.read_csv('kumpula-weather-2017.csv')
    weather = weather.dropna(how="all")
    weather = weather.dropna(axis=1, how="all")
    weather = weather.rename(columns={"m": "Month", "d": "Day"})
    weather["Month"] = weather["Month"].astype(int)
    weather["Day"] = weather["Day"].astype(int)
    #merge the two dataframes
    merged = pd.merge(first, weather, how="inner", left_on=["Year", "Month", "Day"], right_on=["Year", "Month", "Day"])
    #drop useless columns Time and Time zone
    merged = merged.drop(columns=["Time", "Time zone"])
    return merged

def split_date_continues():
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
    return df
    

def main():
    print(cycling_weather())

if __name__ == "__main__":
    main()
