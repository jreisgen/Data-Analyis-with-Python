#!/usr/bin/env python3

def main():
    resList = []
    for i in range(1,7):
        for j in range(1,7):
            if i + j == 5:
                print(tuple((i,j)))

if __name__ == "__main__":
    main()
