from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField , IntegerField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired(), Length(min=1, max=255)])
    limit = IntegerField('Limit', validators=[DataRequired()])
    submit = SubmitField('Submit')

