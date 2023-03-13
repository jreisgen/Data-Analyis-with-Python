#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
# Its first five columns define the features, and the last column is the response. Use scikit-learn's LinearRegression to fit this data. Implement function mystery_data that reads this file and learns and returns the regression coefficients for the five features. You don't have to fit the intercept. The main method should print output in the following form:

#Coefficient of X1 is ...
#Coefficient of X2 is ...
def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep='\t')
    model = LinearRegression(fit_intercept=False)
    model.fit(df.iloc[:, :-1], df.iloc[:, -1])
    return model.coef_
    
def main():
    coefficients = mystery_data()
    # print the coefficients here
    for i in range(len(coefficients)):
        print("Coefficient of X{} is {}".format(i+1, coefficients[i]))
    
if __name__ == "__main__":
    main()
