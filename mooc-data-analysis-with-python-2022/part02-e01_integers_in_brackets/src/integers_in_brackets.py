#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    
    temp =  re.findall(r'\[\s*([+-]?\d+)\s*\]', s)
    temp2 = [int(i) for i in temp]
    
    return temp2

def main():
    print(integers_in_brackets((" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")))

if __name__ == "__main__":
    main()
