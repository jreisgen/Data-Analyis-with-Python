#!/usr/bin/env python3
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    #return slope and intercept
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    return model.coef_[0], model.intercept_
    
def main():
    #Modify your main function to plot the fitted line using matplotlib, in addition to the textual output. Plot also the original data points.
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    slope, intercept = fit_line(x, y)
    print("Slope: ", slope)
    print("Intercept: ", intercept)
    plt.scatter(x, y)
    plt.plot(x, slope*x+intercept)
    plt.show()
if __name__ == "__main__":
    main()
