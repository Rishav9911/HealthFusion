import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Basic structure of the model 

# Load data
file_path = r'Sleep_Analysis.csv'
df = pd.read_csv(file_path)


df.head() # checking if it is successful

df.info() #getting some info on the data before proceeding


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=104, test_size=0.10, shuffle=True)


model.fit(X_train, y_train)

y_pred = model.predict(X_test)


accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)