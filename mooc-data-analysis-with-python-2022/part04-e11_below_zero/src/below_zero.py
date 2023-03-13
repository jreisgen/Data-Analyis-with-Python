#!/usr/bin/env python3

import pandas as pd

def below_zero():
    file = pd.read_csv("src/kumpula-weather-2017.csv")
    file = file[file["Air temperature (degC)"] < 0]
    return file.shape[0]

def main():
    #Number of days below zero: xx
    print("Number of days below zero: {:.1f}".format(below_zero()))
    
if __name__ == "__main__":
    main()
