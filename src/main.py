import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import  MultinomialNB
from sklearn.metrics import accuracy_score
data = pd.read_csv("spam.csv", encoding="latin-1")
#print(data.head())
#print(data.columns)
drop_columns = ["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"]
data = data.drop(columns=drop_columns,)
data = data.rename(columns = {"v1": "label", "v2": "message"})
user_input = input("Enter a message:")
# Label Encoding
vectorizer = CountVectorizer()
data["label"] = data["label"].map({'ham': 0, 'spam': 1})
X = data["message"]
Y = data["label"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)
user_input_vector = vectorizer.transform([user_input])
model = MultinomialNB()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
model_prediction = model.predict(user_input_vector)
if model_prediction == 0:
    print("The message is ham (not spam).")
else:    
     print("The message is spam.")
print("Accuracy:", accuracy) 
print(X_train.shape)