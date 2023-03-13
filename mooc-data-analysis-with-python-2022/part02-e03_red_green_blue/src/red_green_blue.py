#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    returnV = []
    with open(filename) as f:
        lines = f.readlines()

    
    for number,line in enumerate(lines):
        if number != 0:
            pattern = r"\d+\s+\d+\s+\d+\s+(\w+(\s+\w+)?(\s+\w+)?)"
            match = re.search(pattern, line)
            if match:
                rgb = match.group(0).split()
                if len(rgb) == 4:
                    returnV.append(f"{rgb[0]}\t{rgb[1]}\t{rgb[2]}\t{rgb[3]}")
                if len(rgb) == 5:
                    returnV.append(f"{rgb[0]}\t{rgb[1]}\t{rgb[2]}\t{rgb[3]} {rgb[4]}")
                elif len(rgb) == 6:
                    returnV.append(f"{rgb[0]}\t{rgb[1]}\t{rgb[2]}\t{rgb[3]} {rgb[4]} {rgb[5]}")
    return returnV

            
        




def main():
    pass

if __name__ == "__main__":
    print(red_green_blue())
