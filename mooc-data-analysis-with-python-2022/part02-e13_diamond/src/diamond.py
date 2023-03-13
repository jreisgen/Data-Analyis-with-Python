#!/usr/bin/env python3
import numpy as np
def diamond(n):
    if n == 1:
        return np.array([[1]])
    else:
        ey = np.eye(n)
        under =  np.concatenate((ey, ey[::-1]), axis=1)
        upper = np.concatenate((ey[::-1],ey), axis=1)
        combined = np.concatenate((upper, under), axis=0)
        slimmed = np.delete(combined, [n], axis=1)
        slimmed2 = np.delete(slimmed.T, [n], axis=1)
        final = slimmed2.astype(int)
        return final
        
def main():
    print(diamond(6))

if __name__ == "__main__":
    main()
