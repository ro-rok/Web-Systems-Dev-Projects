from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField,  SubmitField
from wtforms.validators import DataRequired, Length

class AlbumForm(FlaskForm):
    album_id = StringField('Album ID', validators=[DataRequired(), Length(min=1, max=50)])
    album_name = StringField('Album Name', validators=[DataRequired(), Length(min=1, max=255)])
    album_popularity = IntegerField('Album Popularity', validators=[DataRequired(), Length(min=1, max=3)])
    album_uri = StringField('Album URI', validators=[DataRequired(), Length(min=1, max=100)])
    album_img = StringField('Album Image', validators=[DataRequired(), Length(min=1, max=255)])
    total_tracks = IntegerField('Total Tracks', validators=[DataRequired(), Length(min=1, max=3)])
    release_date = StringField('Release Date', validators=[DataRequired(), Length(min=1, max=10)])
    label_name = StringField('Label Name', validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Submit')

class AlbumSearchForm(FlaskForm):
    album_name = StringField('Search', validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Submit')