#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
#Write function subfigures that creates a figure that has two subfigures (two axes in matplotlib parlance). The function gets a two dimensional array a as a parameter. In the left subfigure draw using the plot method a graph, whose x coordinates are in the first column of a and the y coordinates are in the second column of a. In the right subfigure draw using the scatter method a set of points whose x coords are again in the first column of a and whose y coordinates are in the second column of a. Additionally, the points should get their color from the third column of a, and size of the point from the fourth column of a. For this, use the c and s named parameters of scatter, respectively
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(a[:,0], a[:,1])
    ax2.scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    plt.show()

def main():
    a = np.array([[1,2,3,4], [2,3,4,5], [3,4,5,6], [4,5,6,7], [5,6,7,8], [6,7,8,9]])
    subfigures(a)
  

if __name__ == "__main__":
    main()
