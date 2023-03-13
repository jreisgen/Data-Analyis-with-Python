#!/usr/bin/env python3

import pandas as pd
import numpy as np
#Read the data set of the top forty singles from the beginning of the year 1964 from the src folder. 
# Return the rows whose singles' position dropped compared to last week's position (column LW=Last Week).

#To do this you first have to convert the special values "New" and "Re" (Re-entry) to missing values (None).
def special_missing_values():
    file = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    file = file.replace("New", np.nan)
    file = file.replace("Re", np.nan)
    file = file.dropna(subset=["LW"])
    file["LW"] = file["LW"].astype(int)	
    file = file[file["Pos"] > file["LW"]]
    return file

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
