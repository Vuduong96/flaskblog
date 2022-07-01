from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from flaskblog.models import Sentiment
from flaskblog import db

from flaskblog.sentiments.forms import SentimentForm
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer



nltk.download('vader_lexicon')



sentiments = Blueprint('sentiments', __name__)

@sentiments.route("/sentiment/new", methods=['GET', 'POST'])
@login_required
def new_sentiment():
    form = SentimentForm()
    if form.validate_on_submit():
        sentiment = Sentiment(topic=form.topic.data, sentence=form.sentence.data, author=current_user)
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(sentiment.sentence)
        sentiment.neg = score["neg"]
        sentiment.neu = score["neu"]
        sentiment.pos = score["pos"]
        sentiment.score = (sentiment.neg + sentiment.neu + sentiment.pos)/3
        db.session.add(sentiment)
        db.session.commit()
        flash('Your comment is recorded! Thank you!', 'success')        
        return redirect(url_for('main.sentiment_home'))
    return render_template('create_sentiment.html', title='New Sentiment Analysis', 
                            form=form, legend='New Sentiment Analysis')

@sentiments.route("/sentiment/<int:sentiment_id>")
def sentiment(sentiment_id):
    sentiment = Sentiment.query.get_or_404(sentiment_id)
    return render_template('sentiment.html', topic=sentiment.topic, sentiment=sentiment, 
                            message= "Negative😢😢" if sentiment.neg!=0 else "Positive😁😁")

