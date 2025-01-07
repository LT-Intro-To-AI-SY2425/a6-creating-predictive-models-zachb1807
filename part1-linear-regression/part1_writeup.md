# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model?
The r sqaured value is the variance between the points and the line of best fit. It tells how well the data matches the model.

2. According to your model, what is the predicted systolic blood pressure for a person who is 42 years old?
The predicted value is 136

3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?
I think this model would be somewhat accurate at predicting their blood pressure. I'm sure the blood pressure of an actual 42 year old would be within the ballpark of 136. However, it's definitely not reliable enough to predict a blood pressure based on someone's age - the correlation is not very strong, as seen based on the data points and line of best fit. I think this is mainly due to the other factors that contribute to blood pressure, such as exercise, eating habits, stress, preexitsing conditions, family history, etc. This model could be improved by taking into account these other factors that also have a major impact on blood pressure.