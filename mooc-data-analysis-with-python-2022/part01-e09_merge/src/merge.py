#!/usr/bin/env python3

def merge(L1, L2):
    resList = []
    leng1 = len(L1)
    leng2 = len(L2)
    i = 0
    j = 0
    while (i < leng1 or j < leng2):
        if i == leng1:
            resList.append(L2[j])
            j +=1
        elif j == leng2:
            resList.append(L1[i])
            i +=1
        elif L1[i] < L2[j]:
            resList.append(L1[i])
            i +=1
        else:
            resList.append(L2[j])
            j += 1
    return resList


def main():
    pass

if __name__ == "__main__":
    main()
