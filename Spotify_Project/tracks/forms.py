from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField , IntegerField
from wtforms.validators import DataRequired, Length

class TrackForm(FlaskForm):
    track_id = StringField('Track ID', validators=[DataRequired(), Length(min=1, max=50)])
    album_id = StringField('Album ID', validators=[DataRequired(), Length(min=1, max=50)])
    track_name = StringField('Track Name', validators=[DataRequired(), Length(min=1, max=255)])
    track_popularity = IntegerField('Track Popularity', validators=[DataRequired(), Length(min=1, max=3)])
    preview_url = StringField('Preview URL', validators=[DataRequired(), Length(min=1, max=255)])
    track_number = IntegerField('Track Number', validators=[DataRequired(), Length(min=1, max=3)])
    track_uri = StringField('Track URI', validators=[DataRequired(), Length(min=1, max=100)])
    track_img = StringField('Track Image', validators=[DataRequired(), Length(min=1, max=255)])
    duration_ms = IntegerField('Duration (ms)', validators=[DataRequired(), Length(min=1, max=10)])
    is_explicit = BooleanField('Is Explicit')
    release_date = StringField('Release Date', validators=[DataRequired(), Length(min=1, max=10)])
    submit = SubmitField('Submit')

class TrackSearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Submit')