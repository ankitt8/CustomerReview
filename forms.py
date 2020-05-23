from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()])
    product_name = StringField('ProductName', validators=[DataRequired()])
    product_review = TextAreaField('ProductReview', validators=[DataRequired()])
    submit = SubmitField('Post Review')