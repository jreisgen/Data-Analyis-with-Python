#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt
#Write function toint that converts a nucleotide to an integer. Use the following mapping:

#A -> 0C -> 1G -> 2T -> 3
import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def toint(x):
    if x == "A":
        return 0
    elif x == "C":
        return 1
    elif x == "G":
        return 2
    elif x == "T":
        return 3
    else:
        return None
    
#Write also function get_features_and_labels that gets a filename as a parameter.
#  The function should load the contents of the file into a DataFrame. The column X contains a string. 
# Convert this column into a feature matrix using the above toint function. 
# For example the column ["GGATAATA","CGATAACC"] should result to the feature matrix

""" [[2,2,0,3,0,0,3,0],[1,2,0,3,0,0,1,1]]
The function should return a pair, whose first element is the feature matrix and the second element is the label vector. """
def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")
    x = df["X"]
    y = df["y"]
    x = x.apply(lambda x: [toint(i) for i in x])
    x = np.array(x.tolist())
    y = np.array(y.tolist())
    return x, y
    

def plot(distances, method='average', affinity = 'euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

#Create function cluster_euclidean that gets a filename as parameter. Get the features and labels using the function from part 1. Perform hierarchical clustering using the function sklearn.cluster.AgglomerativeClustering. 
# Get two clusters using average linkage and euclidean affinity. Fit the model and predict the labels. 
#it should return the accuracy score of the model.
def cluster_euclidean(filename):
    x, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(n_clusters=2, affinity="euclidean", linkage="average")
    model.fit(x)
    y_pred = model.labels_
    distances = pairwise_distances(x, metric="euclidean")
#    plot(distances, method='average', affinity='euclidean')
    return accuracy_score(y, y_pred)

#let us now compute the Hamming distance matrix explicitly. We can achieve this using the function sklearn.metrics.pairwise_distances. 
# Use the affinity parameter precomputed to AgglomerativeClustering. 
# And give the distance matrix you got from pairwise_distances, instead of the feature matrix, to the fit_predict method of the model. 
# If you want, you can visualize the clustering using the provided plot function.

def cluster_hamming(filename):
    x, y = get_features_and_labels(filename)
#let us now compute the Hamming distance matrix explicitly
    distances = pairwise_distances(x, metric="hamming")
#    plot(distances, method='average', affinity='hamming')
    model = AgglomerativeClustering(n_clusters=2, affinity="precomputed", linkage="average")
    model.fit(distances)
    y_pred = model.labels_
    return 1 - accuracy_score(y, y_pred)

def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
