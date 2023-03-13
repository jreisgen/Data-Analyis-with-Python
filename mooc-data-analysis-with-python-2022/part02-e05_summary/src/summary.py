#!/usr/bin/env python3
import sys
import statistics

def summary(filename):
    temp = []
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers += line.split()
        for word in numbers:
            try:
                value = float(word)
            except ValueError:
                continue
            else:
                temp.append(value)

    sumy = '%.6f' % sum(temp)
    avg = '%.6f' % statistics.mean(temp)
    sd =  '%.6f' % statistics.stdev(temp)
    return (sumy,avg,sd)

def main():
    for filename in sys.argv[1:]:
        var = (summary(filename))
        print(f"File: {filename} Sum: {var[0]} Average: {var[1]} Stddev: {var[2]}")
    

if __name__ == "__main__":
    main()
