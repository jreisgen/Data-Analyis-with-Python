#!/usr/bin/env python3

def reverse_dictionary(d):
    revD = {}
    english = d.keys()
    finnish = d.values()

    for word in english:
       finword = d[word]
       for newford in finword:
        if newford in revD:
            revD[newford].append(word)
        else:
            revD[newford] = [word]
    return revD

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
