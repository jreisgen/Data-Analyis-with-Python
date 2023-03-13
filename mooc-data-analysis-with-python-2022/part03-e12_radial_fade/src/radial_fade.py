#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

#Write function center that returns coordinate pair (center_y, center_x) of the image center.
# The function should work both for two and three dimensional images, that is grayscale and color images. 
# Note that these coordinates might not be integers. Example of usage:
def center(a):
    # note the order: (center_y, center_x)
    center_x = (a.shape[1]-1)/2
    center_y = (a.shape[0]-1)/2
    return (center_y, center_x)

#Write also function radial_distance that returns for image with width w and
#  height h an array with shape (h,w), where the number at index (i,j) 
# gives the euclidean distance from the point (i,j) to the center of the image.
def radial_distance(a):
    heighta = a.shape[0]
    widtha = a.shape[1]
    center_y, center_x = center(a)
    y, x = np.ogrid[0:heighta, 0:widtha]
    return np.sqrt((x - center_x)**2 + (y - center_y)**2)

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    a = a.astype("float64")
    a -= a.min()
    a /= a.max()
    a *= (tmax - tmin)
    a += tmin
    return a
#Using the functions radial_distance and scale write function radial_mask that takes
#  an image as a parameter and returns an array with same height and width filled with
#  values between 0.0 and 1.0. Do this using the scale function. To make the resulting 
# array values near the center of array to be close to 1 and closer to the edges of the 
# array are values closer to be 0,subtract the previous array from 1.
#In the center of the image there should be no fading!
# Maximum value in the mask cannot be above 1.0
# make sure the radial_mask function works correctly for arrays of size 1
def radial_mask(a):
#make sure no nan values in the array
    height = a.shape[0]
    width = a.shape[1]
    center_y, center_x = center(a)
    if a.shape[0] == 1:
        return np.ones((height, width))
    new =  1 - scale(radial_distance(a))    
    np.nan_to_num(new, copy=False)
    #center should be value 1
    new[int(center_y), int(center_x)] = 1
    return new


def radial_fade(a):
    return a * radial_mask(a)[:,:,np.newaxis]
    #Test your functions in the main function, which should create, using matplotlib, a figure that has three subfigures stacked vertically.
    #  On top the original painting.png, in the middle the mask, and on the bottom the faded image.
def main():
    img = plt.imread("src/painting.png")
    plt.figure()
    plt.subplot(3,1,1)
    plt.imshow(img)
    plt.subplot(3,1,2)
    plt.imshow(radial_mask(img))
    plt.subplot(3,1,3)
    plt.imshow(radial_fade(img))
    plt.show()




if __name__ == "__main__":
    main()
