"""
Project name: twitter sentiment analysis
Author: Aayush Kurup
Libraries used: tweepy, nltk, pandas, flask, pickle, sklearn and os
Start Date: 22-12-2018
End Date: 01-02-2019
"""

# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# a class for our search form
class SearchFormClass(FlaskForm):
    search = StringField('Search Keyword', validators=[DataRequired()])
    submit = SubmitField('Search')
