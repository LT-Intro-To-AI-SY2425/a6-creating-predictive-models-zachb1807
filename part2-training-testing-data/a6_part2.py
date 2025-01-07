import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

x = x.reshape(-1,1)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)

# Create your training and testing datasets:
model = LinearRegression().fit(xtrain,ytrain)

# Use reshape to turn the x values into 2D arrays:
# xtrain = xtrain.reshape(-1,1)

# Create the model

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_[0]),2)
intercept = round(float(model.intercept_), 2)
r_sqaured = model.score(x,y)


# Print out the linear equation and r squared value:
print("Linear equation: y={}x + {}".format(coef, intercept))
print("r squared:", r_sqaured)

'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array
# get the predicted y values for the xtest values - returns an array of the results
predict = model.predict(xtest)

# round the value in the np array to 2 decimal places
predict = np.around(predict, 2)


# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")

for i in range(len(xtest)):
    print('x value:{}. predicted y value:{}. actual y value: {}'.format(xtest[i], predict[i], ytest[i]))


'''
**********CREATE A VISUAL OF THE RESULTS**********
'''

plt.figure(figsize=(5,4))

#creates a scatter plot and labels the axes
plt.scatter(xtrain,ytrain, c="purple", label="Training Data")
plt.scatter(xtest, ytest, c="blue", label="Testing Data")

plt.scatter(xtest, predict, c="red", label="Predictions")

plt.xlabel("Age")
plt.ylabel("Blood pressure")
plt.title("Blood pressure by age")
plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

plt.legend()
plt.show()