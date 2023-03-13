#!/usr/bin/env python3

def sum_equation(L):
    rS = ""
    summy = sum(L)
    if not len(L):
        return "0 = 0"
    for i,x in enumerate(L):
        if i == 0 and i == len(L)-1:
            rS = f"{str(x)} = {str(x)}"
        if i == 0 :
            rS += str(x)
        
        elif i == len(L)-1:
            rS += f" + {str(x)} = {summy}"
        else:
            rS += f" + {str(x)}"

    return rS

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
