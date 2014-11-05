from flask import Flask, render_template, redirect, url_for, request, session, flash
import datetime
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'alababala'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cornel:xxx@localhost/cornel'

# create sqlalchemy db object
db = SQLAlchemy(app)

from models import *
from forms import *

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter


def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      flash('You need to login first')
      return redirect(url_for('login'))

  return wrap


@app.route('/')
@login_required
def home():
  cities = db.session.query(City).all()
  return render_template('index.html', cities=cities)

@app.route('/add', methods=('GET', 'POST'))
def add():
  form = CityForm()
  if form.validate_on_submit():
    city = City(form.name.data, form.population.data, form.altitude.data)
    db.session.add(city)
    db.session.commit()
    flash('New city added')
    return redirect(url_for('home'))

  return render_template('add.html', form = form)

@app.route('/edit/<int:city_id>', methods=('GET', 'POST'))
def edit(city_id):
  city = db.session.query(City).filter(City.id == city_id).first()
  if city:
    form = CityForm(obj = city)
  else:
    flash("Can't find city with id={}".format(city_id))

  if form.validate_on_submit():
    city.name = form.name.data
    city.population = form.population.data
    city.altitude = form.altitude.data
    db.session.add(city)
    db.session.commit()
    flash('City updated')
    return redirect(url_for('home'))

  return render_template('add.html', form = form)



if __name__ == '__main__':
  app.run(debug = True)
