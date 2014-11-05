from flask_wtf import Form
from wtforms import StringField, HiddenField, IntegerField
from wtforms.validators import DataRequired

class CityForm(Form):
  id = HiddenField('id')
  name = StringField('City')
  population = IntegerField('Population', validators=[DataRequired()])
  altitude = IntegerField('Altitude (m)', validators=[DataRequired()])


class CapitalForm(CityForm):
  state = StringField('state', validators=[DataRequired()])

