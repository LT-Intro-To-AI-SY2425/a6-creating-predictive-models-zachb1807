# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
After commenting out the StandardScaler, the model seems to have the same accuracy. This might be because StandardScaler is not necessary for this dataset, as the data is already normalized.


2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
With StandardScaler, the model has an accuracy of 0.85. This model is accurate enough for the given use case, as it has an accuracy of 85%.


3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model seemed to be the most incorrect when the input age and income didn't seem to match up with each other, or what is considered the norm from the data set. For example, it seemed to be less accurate when the age was high AND the income was low, or vice versa.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
No, the model predicts that a 34 year female who makes 56000 a year would not buy an SUV.

