Importing Libraries used in this project

Using pandas from sklearn Library
Using TfidVectorizer from sklearn feature Extraction Library
Using train_test_split from sklearn Library
Using Logistic Regression from sklearn Library as a ML model in this project
Using accuracy_score from sklearn.metrics Library

Data Used in this project is from kraggle.com

Step-1 : Loading Data from spam.csv in pandas DataFrame, Since Data is in not in the form of csv UTF-8 Format so we convert it into ISO-8859-1 format

Step-2 : We have to replace null values with null string as data have some null values

Step-3 : Now, we have to Label Spam Mails as 0 and Ham Mails as 1

Step-4 : Splitting the data into test and train sets

Step-5 : Transform the text data to numbers that can be used as input to Logistic Regression

Step-6 : Convert Y_train and Y_test values as integers as datatype of the Y value is in object form as declared in shape

Step-7 : Training the Logistic Regression Model with the training data

Step-8 : Prediction on Training data and Testing data , Feed Input Message in a array which we want to predict and Convert text to feature vectors and Make Prediction
