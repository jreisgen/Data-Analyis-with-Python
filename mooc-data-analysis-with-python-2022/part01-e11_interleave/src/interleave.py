#!/usr/bin/env python3

def interleave(*lists):
    zipped = list(zip(*lists))
    rList = []
    for item in zipped:
        for el in item:
            rList.append(el)
    return rList

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
