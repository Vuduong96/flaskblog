from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class SentimentForm(FlaskForm):
    topic = StringField('Topic', validators=[DataRequired()])
    sentence = TextAreaField('Sentence', validators=[DataRequired()])
    submit = SubmitField('Post')
