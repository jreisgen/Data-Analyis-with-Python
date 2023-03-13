#!/usr/bin/env python3

def transform(s1, s2):
    split1 = map(int, s1.split())
    split2 = map(int, s2.split())
    r = []
    two = zip(split1,split2)
    for i in two:

        r.append(i[0]*i[1])
    return r

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
