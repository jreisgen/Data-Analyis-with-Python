#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    pos = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)
    neg = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
    return (pos,neg)


def main():
    pass

if __name__ == "__main__":
    print(solve_quadratic(1,-3,2))
