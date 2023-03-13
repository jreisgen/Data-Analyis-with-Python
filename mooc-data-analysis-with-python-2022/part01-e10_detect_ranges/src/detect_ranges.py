#!/usr/bin/env python3

def detect_ranges(L):
    rList = []
    L = sorted(L)
    rising = False
    first = 0
    second = 0
    for i in range(1, len(L)):
            if L[i] - L[i-1] == 1:
                if rising and len(L)-1 == i:
                    second = L[i]
                    rList.append((first,second+1))
                elif rising: 
                    second = L[i]

                elif len(L)-1 == i:
                    first = L[i-1]
                    second = L[i]
                    rList.append((first,second+1))

                else:
                    rising = True
                    first = L[i-1]
                    second = L[i]
            elif len(L)-1 == i:
                if rising:
                    rList.append((first,second+1))
                    rList.append(L[i])
                else:
                    rList.append(L[i-1])
                    rList.append(L[i])
            else:
                if rising:
                    rList.append((first,second+1))
                    rising = False
                else:
                    rList.append(L[i-1])

    return rList
        



def main():
    L = [-4, -2, 0, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
