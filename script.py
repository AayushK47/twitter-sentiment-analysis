"""
Project name: twitter sentiment analysis
Author: Aayush Kurup
Libraries used: tweepy, nltk, pandas, flask, pickle, sklearn and os
Start Date: 22-12-2018
End Date: 01-02-2019
"""

# Imports
import re
import tweepy
import pickle
import pandas as pd
# nltk.download("stopwords") # Uncomment this line if you do not have stopwords
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# A class with all the required functionalities
class tweets_sentiment_analyzer:
    # Class constructor, configure twitter auth
    def __init__(self, consumerKey, consumerSecret, accessKey, accessSecret):
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessKey, accessSecret)

        # Class attributes
        self.__count_vectorizer = pickle.load(open('models/cv_obj.pkl', 'rb'))
        self.__classifier = pickle.load(open('models/logistic_reg_model.pkl', 'rb'))
        self.__api = tweepy.API(auth)
        self.__tweets = None
        self.__sentiments = None

    # method that searches tweets from twitter based on the provided keyword
    def search(self, searchKeyword):
        print(searchKeyword)
        # if we get nothing, we return None
        if (searchKeyword == None or searchKeyword == ''):
            return None
        # otherwise we search the keyword in twitter abd return the results.
        else:
            self.__tweets = self.__api.search(searchKeyword)
            return self.__api.search(searchKeyword)

    def clean_tweet(self, t):
        twe = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", t)
        twe = twe.lower()
        twe = twe.split()
        ps = PorterStemmer()
        twe = [ps.stem(word) for word in twe if not word in set(stopwords.words("english"))]
        twe = ' '.join(twe)
        return twe

    # A method that analyzes the tweets and returns the sentiment of the tweet (positive or negative)
    def get_sentiments(self):
        if self.__tweets == None:
            return None
        else:
            tweets = []
            corpus = []
            for tweet in self.__tweets:
                tweets.append(tweet.text)
                corpus.append((self.clean_tweet(tweet.text)))
            X = self.__count_vectorizer.transform(corpus)
            sentiments = self.__classifier.predict(X)
            self.__sentiments = sentiments
            return list(sentiments)

    # A method that generates .tsv file for the tweets searched most recently
    def convert_to_tsv(self):
        if self.__tweets == None:
            return None
        data_dict = {'Tweet': [], 'sentiment': []}
        for i in range(len(self.__tweets)):
            data_dict['Tweet'].append(self.__tweets[i].text)
            data_dict['sentiment'].append(self.__sentiments[i])

        df = pd.DataFrame(data_dict)

        df.to_csv('tweets.tsv', sep='\t', encoding='utf-8', index=False)
        return None
