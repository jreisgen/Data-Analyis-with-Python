#!/usr/bin/env python3

import pandas as pd
# The dataset contains some empty rows at the end. Get rid of these.
#  Also, get rid of columns that contain only missing values. Return the cleaned dataset
def cyclists():
    file = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    file = file.dropna(how="all")
    file = file.dropna(axis=1, how="all")
    return file

def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()
