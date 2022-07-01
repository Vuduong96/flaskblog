from flask import Blueprint, render_template, request
from flaskblog.models import Sentiment


sentiment_home = Blueprint('sentiment_home', __name__)

@sentiment_home.route("/")
@sentiment_home.route("/sentiment_home")
def home():
    page = request.args.get('page', 1, type=int)
    sentiments = Sentiment.query.order_by(Sentiment.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('sentiment_home.html', sentiments=sentiments)



# @main.route("/about")
# def about():
#     return render_template('about.html', title='About')