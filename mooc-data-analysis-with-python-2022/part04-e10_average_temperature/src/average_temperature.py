#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    file = pd.read_csv("src/kumpula-weather-2017.csv")
    file = file[file["m"] == 7]
    file = file["Air temperature (degC)"]
    return file.mean()

def main():
    #Average temperature in July: xx.x
    print("Average temperature in July: {:.1f}".format(average_temperature()))

if __name__ == "__main__":
    main()
