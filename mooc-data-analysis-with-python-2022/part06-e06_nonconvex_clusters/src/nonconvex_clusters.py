#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
#Read the tab separated file data.tsv from the src folder into a DataFrame. 
# The dataset has two features X1 and X2, and the label y. 
# Cluster the feature matrix using DBSCAN with different values for the eps parameter. 
# Use values in np.arange(0.05, 0.2, 0.05) for clustering. For each clustering, collect the accuracy score, 
# the number of clusters, and the number of outliers. Return these values in a DataFrame, where columns and
#  column names are as in the below example.
#eps   Score  Clusters  Outliers 
#0    0.05      ?         ?         ?1    0.10      ? 

#Note that DBSCAN uses label -1 to denote outliers , that is, those data points that didn't fit well in any
#  cluster. You have to modify the find_permutation function to handle this: ignore the outlier data points 
# from the accuracy score computation. In addition, if the number of clusters is not the same as the number 
# of labels in the original data, set the accuracy score to NaN.

def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep="\t")
    x = df[["X1", "X2"]]
    y = df["y"]
    eps = np.arange(0.05, 0.2, 0.05)
    scores = []
    clusters = []
    outliers = []
    for e in eps:
        dbscan = DBSCAN(eps=e).fit(x)
        labels = dbscan.labels_
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_outliers = list(labels).count(-1)
        scores.append(accuracy_score(y, labels))
        clusters.append(n_clusters)
        outliers.append(n_outliers)
        #clusters and outliers as float
        clusters = [float(i) for i in clusters]
        outliers = [float(i) for i in outliers]
    return pd.DataFrame({"eps": eps, "Score": scores, "Clusters": clusters, "Outliers": outliers})

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
