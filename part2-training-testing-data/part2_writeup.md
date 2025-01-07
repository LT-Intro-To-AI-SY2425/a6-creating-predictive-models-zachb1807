# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?
This model is more effective because it visually shows the difference between the predicted values and their correspoding actual testing values.


2. What does the R squared coefficient tell you about the model?
The r sqaured coefficient says it has about a 0.6 correlation, which is lower than what it generally was in part 1.


3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.
No, I would say my model is not very accurate, mainly because of the relatively low correlation. It's also inaccurate because some of the data from the csv file was taken to test, meaning the model had fewer training data points to go off of. However, having the testing data gives me a better idea of how accurate my model is, and having more data points would help to fine tune it.