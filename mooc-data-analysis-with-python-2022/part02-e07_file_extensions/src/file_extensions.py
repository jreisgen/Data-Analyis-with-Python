#!/usr/bin/env python3

def file_extensions(filename):
    """Return a list of file extensions in the given filename."""
    dicty = {}
    noext = []
    with open(filename) as f:
        for line in f:
            stripped = line.strip()
            if "." not in stripped:
                noext.append(stripped)
            else: 
                extensions = stripped.split(".")
                length = len(extensions)
                sub = length-1
                if extensions[sub] in dicty:
                    dicty[extensions[sub]].append(stripped)
                else:
                    dicty[extensions[sub]] = [stripped]


    return (noext, dicty)

def main():
    var1 = file_extensions("filenames.txt")
    print(f"{len(var1[0])} files with no extension")
    for i in var1[1]:
        print(f"{i} {len(var1[1][i])} ")


if __name__ == "__main__":
    main()
