#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename) as f:   
        lines = f.readlines()
        l1 = len(lines)
        charactercount = 0
        for line in lines:
            charactercount += len(line)
        l2 = charactercount
        wordcount = 0
        for line in lines:
            wordcount += len(line.split())
        l3 = wordcount
        
    return (l1,l3,l2)

def main():
    for filename in sys.argv[1:]:
        outp = (file_count(filename))
        print(f"{outp[0]}\t{outp[1]}\t{outp[2]}\t{filename}")

if __name__ == "__main__":
    main()