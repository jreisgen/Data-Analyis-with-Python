#!/usr/bin/env python3

def distinct_characters(L):
    myd = {}
    for word in L:
        leng = len("".join(set(word)))
        myd[word]= leng
    return myd

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
