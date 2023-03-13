#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
#Using the same data as in the previous exercise, instead of printing the regression coefficients, 
# print the coefficient of determination. The coefficient of determination, denoted by R2,
#  tells how well the linear regression fits the data. 
# The maximum value of the coefficient of determination is 1
#Using all the features (X1 to X5), fit the data using a linear regression (include the intercept). Get the coefficient of determination using the score method of the LinearRegressionclass. Write a function coefficient_of_determination to do all this. It should return a list containing the R2-score as the only value.
def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep='\t')
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(df.iloc[:, :-1], df.iloc[:, -1])
    coefficients = model.coef_
    intercept = model.intercept_
    r2 = model.score(df.iloc[:, :-1], df.iloc[:, -1])
    
    return [r2]
   
def main():
    #R2-score with feature(s) X: ...
    #R2-score with feature(s) X1: ...
    #should therefore return a list with six R2-scores (the first score is for five features, like in Part 1).
    #  To achieve this, your function should call both the fit method and the score method six times
    #  (once for each number of features). The main method should print the R2-scores in the following form:
    r2 = coefficient_of_determination()
    print("R2-score with feature(s) X: ", r2[0])
   
if __name__ == "__main__":
    main()
