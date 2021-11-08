from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TopCitiesForm(FlaskForm):
    city_name = StringField('City Name', validators=[DataRequired()])
    city_rank = IntegerField('City Rank', validators=[DataRequired()])
    visited = BooleanField('Visited')
    submit = SubmitField('submit')

