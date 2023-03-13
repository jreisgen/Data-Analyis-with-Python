#!/usr/bin/env python3
#Load the iris dataset using the provided function load() in the stub solution.
#What is the Pearson correlation between the variables sepal length and petal length. 
# Compute this using the scipy.stats.pearsonr function. 
# It returns a tuple whose first element is the correlation. 
# Write a function lengths that loads the data and returns the correlation
#import scipy.stats
import numpy as np

def load():
    return np.loadtxt("src/iris.csv", delimiter=",")

def lengths():
    data = load()
    return np.corrcoef(data[:,0], data[:,2])[0,1]

#What are the correlations between all the variables. 
# Write a function correlations that returns an array of shape (4,4) containing the correlations. 
# Use the function np.corrcoef. Which pair of variables is the most highly correlated?
def correlations():
    data = load()
    return np.corrcoef(data, rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
