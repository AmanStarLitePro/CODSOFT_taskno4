# Importing Libraries used in this project

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Loading Data from spam.csv in pandas DataFrame
# Since Data is in not in the form of csv UTF-8 Format so we convert it into ISO-8859-1 format
cm = pd.read_csv("spam.csv", encoding = "ISO-8859-1")

# Analyzing the data
# print(cm.head())

#replacing null values with null string as data have some null values
df = cm.where((pd.notnull(cm)),'')

# Analyzing the data
# print(cm.head())

# Labelling Spam Mails as 0 and Ham Mails as 1
df['v1'] = df['v1'].replace({'spam': 0, 'ham': 1})
# Analyzing the data
# print(df.head())

# Seperating the data as text and label
X = df['v2']
# print(X)
Y = df['v1']
# print(Y)

# Splitting the data into test and train sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

# Transform the text data to numbers that can be used as input to Logistic Regression
feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase=True)
X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# Convert Y_train and Y_test values as integers as datatype of the Y value is in object form as declared in shape
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

# Training the model
model = LogisticRegression()

# Training the Logistic Regression Model with the training data
model.fit(X_train_features, Y_train)

# Prediction on training data
Prediction_on_Training_data = model.predict(X_train_features)
accuracy_on_Training_data = accuracy_score(Y_train, Prediction_on_Training_data)

print("The accuracy score on Test Data is : " + str(accuracy_on_Training_data * 100) + "%") 

# Prediction on test data
Prediction_on_Test_data = model.predict(X_test_features)
accuracy_on_Test_data = accuracy_score(Y_test, Prediction_on_Test_data)

print("The accuracy score on Test Data is : " + str(accuracy_on_Test_data * 100) + "%") 

# Input Message which we want to predict
input_Message = ["I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise. You have been wonderful and a blessing at all times.,,,"]

# Convert text to feature vectors
input_data_features = feature_extraction.transform(input_Message)

# Making Prediction
Prediction = model.predict(input_data_features)
if (Prediction[0] == 1) : 
    print("It is a Ham Mail")
else:
    print("It is a Spam Mail")