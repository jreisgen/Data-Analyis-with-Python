#!/usr/bin/env python3
class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.value = numerator / denominator


    def __add__(self, other):
        return Rational(self.value+other.value, 1)
    
    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Rational(n, d)
    
    def __mul__(self, other):
        return Rational(self.value * other.value, 1)

    def __truediv__(self, other):
        return Rational(self.value / other.value, 1)

    def __eq__(self, other):
        return self.value == other.value
    
    def __gt__(self, other):
        return self.value > other.value 

    def __lt__(self, other):    
        return self.value < other.value
    
    def __str__(self):
        return (str(self.numerator) + "/" + str(self.denominator))

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
