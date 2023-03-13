#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
#Write a function to_grayscale that takes an RGB image (three dimensional array) 
# and returns a two dimensional gray-scale image.
#  The conversion to gray-scale should take a weighted sum of the red, green, 
# and blue values, and use that as the value of gray. The first axis is the x, 
# the second is y, and the third is the color components (red, green, blue). 
# Use the weights 0.2126, 0.7152, and 0.0722 for red, green, and blue, respectively. 
# These weights are so because the human eye is most sensitive to green color and least 
# sensitive to blue color.
def to_grayscale(img):
    greyscalvalue = np.dot(img[...,:3], [0.2126, 0.7152, 0.0722])
    return greyscalvalue

#Write functions to_red, to_green, and to_blue that get a three dimensional
#  array as a parameter and return a three dimensional arrays. For instance, 
# the function to_red should zero out the green and blue color components and
#  return the result. In the main function create a figure with three subfigures:
#  the top one should be the red image,
#  the middle one the green image, and the bottom one the blue image
def to_red(img):
    red = np.copy(img)
    red[:,:,1] = 0
    red[:,:,2] = 0
    return red
def to_green(img):
    green = np.copy(img)
    green[:,:,0] = 0
    green[:,:,2] = 0
    return green
    
def to_blue(img):
    blue = np.copy(img)
    blue[:,:,0] = 0
    blue[:,:,1] = 0
    return blue
def main():
    plt.gray()
    img = plt.imread("src/painting.png")
    newimage = to_grayscale(img)
    plt.imshow(newimage)
    red = to_red(img)


    blue = to_blue(img)
    
    green = to_green(img)
    
    plt.figure()
    plt.subplot(3,1,1)
    plt.imshow(red)
    plt.subplot(3,1,2)
    plt.imshow(green)
    plt.subplot(3,1,3)
    plt.imshow(blue)
    plt.show()
if __name__ == "__main__":
    main()
