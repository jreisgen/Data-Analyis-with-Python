#!/usr/bin/env python3

import scipy
#apply k-means clustering with 3 clusters. Create a function plant_clustering that loads the iris data set, clusters the data and returns the accuracy_score
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():

    iris = load_iris()
    kmeans = KMeans(n_clusters=3, random_state=0).fit(iris.data)
    permutation = find_permutation(3, iris.target, kmeans.labels_)
    return accuracy_score(iris.target, [permutation[label] for label in kmeans.labels_])
    

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
