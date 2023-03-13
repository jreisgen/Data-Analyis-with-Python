#!/usr/bin/env python3
def square(value):
    return value **2

def triple(value):
    return value *3


def main():
    for i in range(1,11):
        sq = square(i)
        tr = triple(i)
        if sq > tr:
            break
        print(f"triple({i})=={tr} square({i})=={sq}")
     
        

        

if __name__ == "__main__":
    main()
