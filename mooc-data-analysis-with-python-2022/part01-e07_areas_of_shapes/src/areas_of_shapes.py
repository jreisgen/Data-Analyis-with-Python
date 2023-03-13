#!/usr/bin/env python3

import math


def main():
    while True:
        test = input("Choose a shape (triangle, rectangle, circle): ")
        if test == "":
            break
        if test == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            print(f"The area is {base*height*0.5}")
        elif test == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            print(f"The area is {width*height}")
        elif test == "circle":
            radius = float(input("Give radius of the circle: "))
            print(f"The area is {math.pi * radius*radius}")
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
