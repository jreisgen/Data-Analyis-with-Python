#!/usr/bin/env python3

def word_frequencies(filename):
    word_count = {}
    with open(filename) as f:
        for line in f:
            words = line.split()

            for word in words:
                stripped = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if stripped not in word_count:
                    word_count[stripped] = 1
                else:
                    word_count[stripped] += 1
    return word_count

def main():
    pass

if __name__ == "__main__":
    print(word_frequencies("src/alice.txt"))
