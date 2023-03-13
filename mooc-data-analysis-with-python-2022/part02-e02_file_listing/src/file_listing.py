#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    returnV = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            words = line.split()
            newtuple = (int(words[4]), words[5], int(words[6]), int(words[7][0:2]), int(words[7][3:]), words[8])
            returnV.append(newtuple)
            text = re.findall(r'\[\s*([+-]?\d+)\s*\]', line)

    return returnV

def main():
    pass

if __name__ == "__main__":
    print(file_listing())
    print(float("hi"))
