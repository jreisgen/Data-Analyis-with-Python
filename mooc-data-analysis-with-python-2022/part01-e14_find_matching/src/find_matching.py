#!/usr/bin/env python3

def find_matching(L, pattern):
    rList = []
    for indr, word in enumerate(L):
        if pattern in word:

            rList.append(indr)
    return rList

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))


if __name__ == "__main__":
    main()
