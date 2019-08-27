import re
import nltk
import pickle
import numpy as np
import pandas as pd
#nltk.download("stopwords") # Uncomment this line if you do not have stopwords
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

# Importing the data
cols = ['sentiment', 'id', 'date', 'query_string', 'user', 'text']
dataset = pd.read_csv('F:\\twitter-sentiment-analysis\\ML Script\\sentiment140.csv', header=None, names=cols, encoding='latin-1')

# Function to clean the tweets
def clean_tweet(t,corpus): 
    twe=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", t)
    twe=twe.lower()
    twe=twe.split()
    ps = PorterStemmer()
    twe = [ps.stem(word) for word in twe if not word in set(stopwords.words("english"))]
    twe = ' '.join(twe)
    corpus.append(twe)


# Removing all the unwanted columns
dataset.drop(['id', 'date', 'query_string', 'user'],axis=1,inplace=True)
corpus = []

# cleaning all the tweets
for i in range(775000,825000):
    clean_tweet(dataset["text"][i], corpus)


# Pickling the corpus of clean tweets
corpus_file = open('../models/corpus.pkl','wb')
pickle.dump(corpus, corpus_file)
corpus_file.close()

# Converting the tweets to vector (Bag of words model a.k.a Count Vectorizer)
cv = CountVectorizer(max_features = 17000)
X = cv.fit_transform(corpus).toarray()  
y = dataset.loc[:, "sentiment"].values

# Pickling the Count Vectorizer object
CV_object = open('../models/cv_obj.pkl', 'wb')
pickle.dump(cv, CV_object)
CV_object.close()

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=121)

# Creating the MultinomialNB classifier
log_clf = LogisticRegression(C=0.9)
log_clf.fit(X_train,y_train)

# Evaluating the model
y_pred = log_clf.predict(X_test)
confusionMatrix = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)

print(accuracy)
print(confusionMatrix)

# Pickling the model
log_model = open('../models/logistic_reg_model.pkl', 'wb')
pickle.dump(log_clf, log_model)
log_model.close()
