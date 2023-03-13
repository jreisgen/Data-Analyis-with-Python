#!/usr/bin/env python3

import pandas as pd

def split_date(df):
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

#Write function split_date_continues that does
#read the bicycle data set
#clean the data set of columns/rows that contain only missing values
#drops the Päivämäärä column and replaces it with its splitted components as before
#Use the concat function to do this. The function should return a DataFrame with 25 columns 
# (first five related to the date and then the rest 20 concerning the measument location.)
def split_date_continues():
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
    return df

    
    


    

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
