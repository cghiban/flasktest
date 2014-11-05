from app import db

class City(db.Model):

  __tablename__ = "cities"

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String, nullable=False)
  population = db.Column(db.Integer, nullable=False)
  altitude = db.Column(db.Integer, nullable=False)

  def __init__(self, name, pop, alt):
    self.name = name
    self.population = pop
    self.altitude = alt

  def __repr__(self):
    return '<City {}>'.format(self.name)
  
class Capital(db.Model):

  __tablename__ = "capitals"

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String, nullable=False)
  population = db.Column(db.Float, nullable=False)
  altitude = db.Column(db.Integer, nullable=False)
  state = db.Column(db.String(2), nullable=False)

  def __init__(self, name, pop, alt, state):
    self.name = name
    self.population = pop
    self.altitude = alt
    self.state = state

  def __repr__(self):
    return '<Capital {}/{}>'.format(self.name, self.state)
 
