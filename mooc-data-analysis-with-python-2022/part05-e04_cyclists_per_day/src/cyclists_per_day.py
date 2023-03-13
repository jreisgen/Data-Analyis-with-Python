#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
#Part 1.Read, clean and parse the bicycle data set. Group the rows by year, month, and day. 
# Get the sum for each group. Make function cyclists_per_day that does the above.
#  The function should return a DataFrame. Make sure that the columns Hour and Weekday are not included in 
# the returned DataFrame.

def cyclists_per_day():
    #Group the    
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

    #Group the rows by year, month, and day. Get the sum for each group
    #Make sure that the columns Hour and Weekday are not included in the returned DataFrame.
    df = df.groupby(["Year", "Month", "Day"]).sum()
    #drop hour
    df = df.drop("Hour", axis=1)

    return df

    
#Part 2.In the main function, using the function cyclists_per_day, get the daily counts. 
# The index of the DataFrame now consists of tuples (Year, Month, Day).
#  Then restrict this data to August of year 2017, and plot this data. 
# Don't forget to call the plt.show function of matplotlib. 
# The x-axis should have ticks from 1 to 31, and there should be a curve to each measuring station.
#  Can you spot the weekends?
def main():
    df = cyclists_per_day()
    print(df)
    df = df.loc[(2017,8), :]
    #print(df)
    df.plot()
    plt.show()

if __name__ == "__main__":
    main()
