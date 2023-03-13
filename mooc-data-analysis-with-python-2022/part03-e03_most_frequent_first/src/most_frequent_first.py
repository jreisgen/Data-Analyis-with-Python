#!/usr/bin/env python3

import numpy as np
#Write function most_frequent_first that gets a two dimensional array and an index c of a column as parameters. 
# The function should then return the array whose rows are sorted based on column c, in the following way.
#  Rows are ordered so that those rows with the most frequent element in column c come first, 
# then come the rows with the second most frequent element in column c, and so on. 
# Therefore, the values outside column c don't affect the ordering in any way.

def most_frequent_first(a, c):
    uniquevalues, counts = np.unique(a[:,c], return_counts=True)
    sortedcounts = np.sort(counts)[::-1]
    sorteduniquevalues = uniquevalues[np.argsort(counts)[::-1]]
    sortedarray = np.empty_like(a)
    start = 0
    counter = 0
    for i in (sortedcounts):
        sortedarray[start:start+i] = a[a[:,c] == sorteduniquevalues[counter]]
        start += i
        counter += 1

       #sortedarray[i*sortedcounts[i]:(i+1)*sortedcounts[i]] = a[a[:,c] == sorteduniquevalues[i]]
    return  sortedarray





def main():
    a = np.array([[1, 2, 3], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]])
    print(most_frequent_first(a, -1))

if __name__ == "__main__":
    main()
