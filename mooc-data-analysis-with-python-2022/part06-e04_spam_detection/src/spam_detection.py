#!/usr/bin/env python3
#Write function spam_detection that does the following:

""" Read the lines from these files into arrays. Use function open from gzip module, since the files are compressed. From each file take only fraction of lines from the start of the file, where fraction is a parameter to spam_detection, and should be in the range [0.0, 1.0].
forms the combined feature matrix using CountVectorizer class' fit_transform method. The feature matrix should first have the rows for the ham dataset and then the rows for the spam dataset. One row in the feature matrix corresponds to one email.
use labels 0 for ham and 1 for spam
divide that feature matrix and the target label into training and test sets, using train_test_split. Use 75% of the data for training. Pass the random_state parameter from spam_detection to train_test_split.
train a MultinomialNB model, and use it to predict the labels for the test set
The function should return a triple consisting of

accuracy score of the prediction
size of test sample
number of misclassified sample points """
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def spam_detection(random_state=0, fraction=1.0):
    #read files
    with gzip.open("src/ham.txt.gz", "rt", encoding="utf-8") as ham:
        ham = ham.readlines()
    with gzip.open("src/spam.txt.gz", "rt", encoding="utf-8") as spam:
        spam = spam.readlines()
    #take fraction of lines
    ham = ham[:int(len(ham)*fraction)]
    spam = spam[:int(len(spam)*fraction)]
    #forms the combined feature matrix using CountVectorizer class' fit_transform method
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(ham + spam)
    #use labels 0 for ham and 1 for spam
    y = np.concatenate((np.zeros(len(ham)), np.ones(len(spam))))
    #divide that feature matrix and the target label into training and test sets, using train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=random_state)
    #train a MultinomialNB model, and use it to predict the labels for the test set
    clf = MultinomialNB()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    #return a triple consisting of accuracy score of the prediction, size of test sample, number of misclassified sample points
    return (accuracy_score(y_test, y_pred), len(y_test), (y_test != y_pred).sum())

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
