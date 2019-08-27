'''
Project name: twitter sentiment analysis
Author: Aayush Kurup
Libraries used: tweepy, nltk, pandas, flask, pickle, sklearn and os
Start Date: 22-12-2018
End Date: 01-02-2019
'''

# imports
from flask import Flask, render_template, url_for, request, Response, redirect
from forms import SearchFormClass
import script
import dotenv
import os

print(os.getcwd())
dotenv.load_dotenv(os.getcwd() + '\.env')

apiKey = os.environ.get('apiKey')
apiSecret = os.environ.get('apiSecret')
accessKey = os.environ.get('accessKey')
accessSecret = os.environ.get('accessSecret')

app = Flask(__name__)
api = script.tweets_sentiment_analyzer(apiKey, apiSecret, accessKey, accessSecret)

app.config['SECRET_KEY'] = '7eaa32bfa81cf2b06a62f030764f238d'


@app.route("/", methods = ['GET','POST'])
def index():
    search = SearchFormClass(request.form)
    if request.method == 'POST':
        return searched(search)

    return render_template('home.html', tweets=None, sentiments=None, len=None, form=search)


def searched(search):
    search = SearchFormClass(request.form)
    tweets = api.search(search.data['search'])
    sentiments = api.get_sentiments()
    num_tweets = None if sentiments == None else len(sentiments)
    return render_template('home.html', tweets=tweets, sentiments=sentiments, len=num_tweets, form=search)


@app.route('/download')
def download():
    if(api.convert_to_tsv() == None):
        return redirect('/')
    else:
        file = open('tweets.tsv')
        return Response(file, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=tweets.tsv"})


if(__name__ == "__main__"):
    app.run(debug=True)