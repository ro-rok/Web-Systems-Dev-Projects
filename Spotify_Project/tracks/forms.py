from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, SubmitField , IntegerField, DateField
from wtforms.validators import DataRequired, Length

class TrackForm(FlaskForm):
    track_id = StringField('Track ID', validators=[DataRequired(), Length(min=1, max=50)])
    album_id = SelectField('Album', validators=[DataRequired()])
    track_name = StringField('Track Name', validators=[DataRequired(), Length(min=1, max=255)])
    track_popularity = IntegerField('Track Popularity')
    preview_url = StringField('Preview URL', validators=[DataRequired(), Length(min=1, max=255)])
    track_number = IntegerField('Track Number')
    track_img = StringField('Track Image', validators=[DataRequired(), Length(min=1, max=255)])
    duration_ms = IntegerField('Duration (ms)')
    is_explicit = BooleanField('Is Explicit')
    release_date = DateField('Release Date', validators=[DataRequired()])
    artist_id = SelectField('Featuring Artist')
    submit = SubmitField('Submit')

class TrackSearchForm(FlaskForm):
    track_name = StringField('Track Name')
    track_popularity = IntegerField('Track Popularity')
    is_explicit = BooleanField('Is Explicit')
    album_name = StringField('Album Name')
    limit = IntegerField("Limit", default=10)
    sort = SelectField("Sort")
    order = SelectField("Order", choices=[("asc","+"), ("desc","-")])
    submit = SubmitField("Filter")
class TrackSQLSearchForm(FlaskForm):
    track_name = StringField('Track Name')
    submit = SubmitField('Submit')

class TrackFetchForm(FlaskForm):
    track_id = StringField('Track ID/s', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Submit')
