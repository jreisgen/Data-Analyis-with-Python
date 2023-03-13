#!/usr/bin/python3

import numpy as np

def meeting_lines(a1, b1, a2, b2):
    # a1*x + b1 = y =  a2*x + b2
    # a1*x - y +b1 = 0
    # a2*x - y +b2 = 0
    x,y = np.linalg.solve([[a1, -1], [a2, -1]], np.array([-b1,-b2]))
    return x,y
    
def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
