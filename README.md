# Twitter Tweets Sentiment Prediction

## About
This app can be used to get a dataset of tweets with the sentiment label in .tsv format which can be used for data analysis, sentiment analysis, or any other such activity. Users can search for a keyword on the webpage. On submitting the search form, all the recent tweets from twitter will be shown on the webpage along with its sentiment. Users can download the displayed data in .tsv by clicking on the download button.

## Project Structure

```bash
├── ML Script
│   ├── ml_script.py
├── models
│   ├── corpus.pkl
│   ├── cv_obj.pkl
│   ├── logistic_reg_model.pkl
├── static
│   ├── v.png
│   ├── v.svg
├── templates
│   ├── home.html
├── .gitignore
├── forms.py
├── README.md
├── script.py
├── server.py
```
## Dataset
 I used the sentiment140 dataset to train my model.The tweets have been annotated (0 = negative, 2 = neutral, 4 = positive) and they can be used to detect sentiment . The dataset contains 6 columns:-

- 0 - the polarity of the tweet (0 = negative, 4 = positive)
- 1 - the id of the tweet (2087)
- 2 - the date of the tweet (Sat May 16 23:58:44 UTC 2009)
- 3 - the query (lyx). If there is no query, then this value is NO_QUERY.
- 4 - the user that tweeted (robotickilldozr)
- 5 - the text of the tweet (Lyx is cool)

It also has 1.6 million rows with 8 hundred thousand negative and 8 hundred thousand positive. Hence it is a very big dataset.

Follow this link to download the dataset:- http://help.sentiment140.com/for-students

## Models

To train a model to predict weather the data is I used the **Logistic Regression**. Since the dataset is very large, it will require a lot of resources to load the data in the memory. That is why I used 50k tweets for training. The model gives an accuracy of **77%**.

Cleaning 50k tweets might also take time and so I also stored the result in a pickle file named _"corpus.pkl"_

I also stored the CountVectorizer object in a file named _"cv_obj.pkl"_.

## App Dependancies

You will need to download the following modules to run this app:-

- pandas            ( For creating dataframes )
- tweepy            ( To get data from twitter )
- sklearn           ( For predicting the tweet sentiment )
- flask             ( For the creating the backend server )
- pickle            ( For Loading the pickled files )
- python-dotenv     ( For loading environment variables )
- flask_wtf         ( For creating forms )
- nltk              ( For NLP )

## How to run
If you want to use the source code, you'll have to make the following change :-

- Install all the app dependancies I mentioned above. I would suggest to install them in a virtual environment like pipenv or venv but installing on the local machine would work fine as well.

- You'll also need the twitter api keys to get data from twitter. You can get it by signing in to the twitter developer program. once you get all the keys store them in a .env file. The .env file you be in the same directory as server.py.

After installing all the dependancies and setting up the running api keys, simply open a terminal/cmd at the project directory and run "python3 server.py"  

If you want to train a model, I would suggest to run the scripts on a cloud machine (I used an AWS EC2 Instance).

Thank you
