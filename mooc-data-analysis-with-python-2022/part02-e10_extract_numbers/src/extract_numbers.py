#!/usr/bin/env python3

def extract_numbers(s):
    words = s.split()
    returnV = []
    for word in words:
        try:
            value = int(word)
            returnV.append(value)
        except ValueError:
            try:
                value = float(word)
                returnV.append(value)
            except ValueError:
                continue
        
    return returnV
def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))
if __name__ == "__main__":
    main()
