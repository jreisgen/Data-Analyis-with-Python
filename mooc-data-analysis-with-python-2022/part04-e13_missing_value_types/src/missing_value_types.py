#!/usr/bin/env python3

import pandas as pd
import numpy as np

#Make function missing_value_types that returns the following DataFrame. 
# Use the State column as the (row) index.
#  The value types for the two other columns should be float and object, respectively. 
# Replace the dashes with the appropriate missing value symbols.
#State	Year of independence	President
#United Kingdom	-	-
#Finland	1917	Niinistö
#USA	1776	Trump
#Sweden	1523	-
#Germany	-	Steinmeier
#Russia	1992	Putin
def missing_value_types():
    df = pd.DataFrame({"State": ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"], "Year of independence": [np.nan, 1917, 1776, 1523, np.nan, 1992], "President": [np.nan, "Niinistö", "Trump", np.nan, "Steinmeier", "Putin"]})
    df = df.set_index("State")
    return df

               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
