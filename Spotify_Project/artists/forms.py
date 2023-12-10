from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class ArtistForm(FlaskForm):
    artist_id = StringField('Artist ID', validators=[DataRequired(), Length(min=1, max=50)])
    artist_name = StringField('Artist Name', validators=[DataRequired(), Length(min=1, max=255)])
    artist_popularity = IntegerField('Artist Popularity', validators=[DataRequired(), Length(min=1, max=3)])
    followers_total = IntegerField('Followers Total', validators=[DataRequired(), Length(min=1, max=10)])
    artist_uri = StringField('Artist URI', validators=[DataRequired(), Length(min=1, max=100)])
    artist_img = StringField('Artist Image', validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Submit')

class ArtistSearchForm(FlaskForm):
    artist_name = StringField('Search', validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Submit')

class ArtistFetchForm(FlaskForm):
    artist_id = StringField('Artist ID', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Submit')