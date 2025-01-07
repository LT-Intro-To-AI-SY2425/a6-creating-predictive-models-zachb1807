# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
The R squared coefficient for my model is 0.86. This means I have strong data with strong correlation, which means my model will be more accurate.

2. Is your model accurate? Why or why not?
Yes, my model is mostly accurate because it was generally able to predict the value of the car.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
The model predicts that the 10 year old car is worth $13,083 and the 20 year old car is worth $8,388.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
This is happening because the model is linear. Since the rate of change of the model is not zero, it must cross the x axis at some point. Therefore, the car values must hit zero at some point, and then fall below zero as the values continue to increase. In reality, a car's value will begin to flatten out as it gets lower and lower. The model fails to account for the fact that car values do not decrease linearally, and a newer car will depreciate much faster than an older one. 