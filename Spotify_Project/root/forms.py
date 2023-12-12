from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField , IntegerField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired(), Length(min=1, max=255)])
    type = StringField('Type', validators=[Length(min=1, max=255)])
    limit = IntegerField('Limit', validators=[Length(min=1, max=255)])
    offset = IntegerField('Offset', validators=[Length(min=1, max=255)])
    submit = SubmitField('Submit')

