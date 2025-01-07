import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
print(data)

# Step 2: Standardize the data using StandardScaler, 
scaler = StandardScaler().fit(x)

# Step 3: Transform the data
x = scaler.transform(x)

# Step 4: Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x,y)

# Step 6: Create a LogsiticRegression object and fit the data
model = linear_model.LogisticRegression().fit(x_train, y_train)

# Step 7: Print the score to see the accuracy of the model
print("Accuracy: " + str(model.score(x_test, y_test)))

# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data
print("Testing results:")

predicted_purchases = model.predict(x_test)

for i in range(len(x_test)):

    x = scaler.inverse_transform(x_test)[i]
    if(x[2] == 1):
        gender = 'Female'
    else:
        gender = 'Male'
    # thisx = thisx.reshape(-1, 3)
    print("===========================")
    print("Age: " + str(x[0]))
    print("Estimated Salary: " + str(x[1]))
    print("Gender: " + gender)
    print("Predicted Purchase: " + ("Yes" if predicted_purchases[i] == 1 else "No"))
    print("Actually Purchased: " + ("Yes" if y_test[i] == 1 else "No"))

print('------------------')
print("Accuracy: " + str(model.score(x_test, y_test)))
print('34 y/o F with 56000 salary:', model.predict(scaler.transform([[34, 56000, 1]])))