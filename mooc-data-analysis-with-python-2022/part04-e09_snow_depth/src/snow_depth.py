#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    file = pd.read_csv("src/kumpula-weather-2017.csv")
    file = file["Snow depth (cm)"]
    file = file[file != -9999.9]
    return file.max()
    

def main():
    #Max snow depth: xx.x
    print("Max snow depth: {:.1f}".format(snow_depth()))
    

if __name__ == "__main__":
    main()
