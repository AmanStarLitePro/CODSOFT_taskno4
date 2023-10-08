# Spam-Mail-Detection
This Project is all about to detect Spam Mail using a dataset, Spam Mail Detection is a cutting-edge machine learning project designed to combat the ever-growing problem of unsolicited and potentially harmful email messages. 

![image](https://github.com/AmanStarLitePro/Spam-Mail-Detection/assets/143260479/7a450d3f-f109-4aed-bd42-49a35745a466)

# Dependencies

# Importing Libraries used in this project

Using pandas from sklearn Library

Using TfidVectorizer from sklearn feature Extraction Library

Using train_test_split from sklearn Library

Using Logistic Regression from sklearn Library as a ML model in this project

Using accuracy_score from sklearn.metrics Library

# Data Used in this project is from kraggle.com

# Step-1 : 

Loading Data from spam.csv in pandas DataFrame, Since Data is in not in the form of csv UTF-8 Format so we convert it into ISO-8859-1 format

![image](data:image/png;base64,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)

# Step-2 : 

We have to replace null values with null string as data have some null values

# Step-3 : 

Now, we have to Label Spam Mails as 0 and Ham Mails as 1

# Step-4 : 

Splitting the data into test and train sets

# Step-5 : 

Transform the text data to numbers that can be used as input to Logistic Regression

# Step-6 : 

Convert Y_train and Y_test values as integers as datatype of the Y value is in object form as declared in shape

# Step-7 : 

Training the Logistic Regression Model with the training data

# Step-8 : 

Prediction on Training data and Testing data , Feed Input Message in a array which we want to predict and Convert text to feature vectors and Make Prediction
