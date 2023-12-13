from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField,  SubmitField, DateField
from wtforms.validators import DataRequired, Length

class AlbumForm(FlaskForm):
    album_id = StringField('Album ID', validators=[DataRequired(), Length(min=1, max=50)])
    album_name = StringField('Album Name', validators=[DataRequired(), Length(min=1, max=255)])
    album_popularity = IntegerField('Album Popularity')
    total_tracks = IntegerField('Total Tracks')
    album_img = StringField('Album Image', validators=[DataRequired(), Length(min=1, max=255)])
    release_date = DateField('Release Date', validators=[DataRequired(), Length(min=1, max=10)])
    label_name = StringField('Label Name', validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Submit')

class AlbumSearchForm(FlaskForm):
    album_name = StringField('Album Name')
    album_popularity = IntegerField('Album Popularity')
    album_total_tracks = IntegerField('Total Tracks')
    label_name = StringField('Label Name')
    limit = IntegerField("Limit", default=10)
    sort = SelectField("Sort")
    order = SelectField("Order", choices=[("asc","+"), ("desc","-")])
    submit = SubmitField("Filter")
class AlbumSearchSQLForm(FlaskForm):
    album_name = StringField('Album Name')
    submit = SubmitField('Submit')

class AlbumFetchForm(FlaskForm):
    album_id = StringField('Album ID', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Submit')