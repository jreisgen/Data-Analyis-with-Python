#!/usr/bin/env python3

def main():
    for i in range(1,11):
        for j in range(1,11):
            print(f"{i*j} ", end="")
            if j == 10:
                print("")

if __name__ == "__main__":
    main()
