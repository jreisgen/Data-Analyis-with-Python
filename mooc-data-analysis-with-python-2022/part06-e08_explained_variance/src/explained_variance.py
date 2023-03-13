#!/usr/bin/env python3

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

""" In the main function print these values in the following form:
#Write function explained_variance which reads the tab separated file "data.tsv". 
# The data contains 10 features. Then fit PCA to the data. 
# The function should return two lists (or 1D arrays). 
# The first list should contain the variances of all the features. 
# The second list should consist of the explained variances returned by the PCA.

The variances are: ?.??? ?.??? ...The explained variances after PCA are: ?.??? ?.??? ...﻿
Print the values with three decimal precision and separate the values by a space. """
def explained_variance():

    df = pd.read_csv("src/data.tsv", sep="\t")
    pca = PCA()
    pca.fit(df)
    return df.var(), pca.explained_variance_
#Plot the cumulative explained variances.
#  The y-axis should be the cumulative sum, and the x-axis the number of terms in the cumulative sum.

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    print("The variances are: ", " ".join(["{:.3f}".format(i) for i in v]))
    print("The explained variances after PCA are: ", " ".join(["{:.3f}".format(i) for i in ev]))
    plt.plot(range(1, len(ev)+1), ev.cumsum())
    plt.show()



if __name__ == "__main__":
    main()
