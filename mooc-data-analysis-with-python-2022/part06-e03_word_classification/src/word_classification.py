#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

#Write function get_features that gets a one dimensional np.array, containing words, as parameter. 
# It should return a feature matrix of shape (n, 29), where n is the number of elements of the input array. 
# There should be one feature for each of the letters in the following alphabet: "abcdefghijklmnopqrstuvwxyzäö-". 
# The values should be the number of times the corresponding character appears in the word.
def get_features(a):
    alphabet2 = "abcdefghijklmnopqrstuvwxyzäö-"
    features = np.zeros((len(a), len(alphabet2)))
    for i, word in enumerate(a):
        for j, letter in enumerate(alphabet2):
            features[i][j] = word.count(letter)
    return features

#Write function contains_valid_chars that takes a string as a parameter and returns the truth value of whether all the characters in the string belong to the alphabet or not.
def contains_valid_chars(s):
    for letter in s:
        if letter not in alphabet_set:
            return False
    return True
    
#Write function get_features_and_labels that returns the tuple (X, y) of the feature matrix and the target vector. 
# Use the labels 0 and 1 for Finnish and English, respectively. 
# Use the supplied functions load_finnish() and load_english() to get the lists of words. Filter the lists in the following ways:
""" Convert the Finnish words to lowercase, and then filter out those words that contain characters that don't belong to the alphabet.
For the English words first filter out those words that begin with an uppercase letter to get rid of proper nouns. Then proceed as with the Finnish words.
Use get_features function you made earlier to form the feature matrix. """
def get_features_and_labels():
    finnish = load_finnish()
    english = load_english()
    #length of map
    finnish_words = [word.lower() for word in finnish if contains_valid_chars(word)]
    finnish_labels = np.zeros(len(finnish_words))
    #english filter out uppercase
    english_words = [word.lower() for word in english if word[0].islower() and contains_valid_chars(word)]
    english_labels = np.ones(len(english_words))


    words = finnish_words + english_words + "two words"
    labels = np.concatenate((finnish_labels, english_labels))
    x = get_features(np.array(words))
    return (x, labels)

#Use the function get_features_and_labels you made earlier to get the feature matrix and the labels. 
# Use multinomial naive Bayes to do the classification. 
# Get the accuracy scores using the sklearn.model_selection.cross_val_score function; use 5-fold cross validation. 
# The function should return a list of five accuracy scores.
def word_classification():
    x, y = get_features_and_labels()
    clf = MultinomialNB()
#call KFold with 5 splits
    kf = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(clf, x, y, cv=kf)
    return scores



def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
