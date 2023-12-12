from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class ArtistForm(FlaskForm):
    artist_id = StringField('Artist ID', validators=[DataRequired(), Length(min=1, max=50)])
    artist_name = StringField('Artist Name', validators=[DataRequired(), Length(min=1, max=255)])
    artist_popularity = IntegerField('Artist Popularity', validators=[DataRequired()])
    followers_total = IntegerField('Followers Total', validators=[DataRequired()])
    artist_img = StringField('Artist Image', validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Submit')

class ArtistSearchForm(FlaskForm):
    artist_name = StringField('Artist Name')
    artist_popularity = IntegerField('Artist Popularity')
    followers_total = IntegerField('Followers Total')
    limit = IntegerField("Limit", default=10)
    sort = SelectField("Sort")
    order = SelectField("Order", choices=[("asc","+"), ("desc","-")])
    submit = SubmitField("Filter")

class ArtistSQLSearchForm(FlaskForm):
    artist_name = StringField('Artist Name')
    submit = SubmitField('Submit')

class ArtistFetchForm(FlaskForm):
    artist_id = StringField('Artist ID', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Submit')
