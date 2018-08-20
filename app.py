from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotsprings.db'
db = SQLAlchemy(app)

class Hotspring(db.Model):
  __tablename__ = 'hotsprings'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  ZIP = db.Column(db.String, primary_key=True)

@app.route("/")
def hello():
  hotsprings = Hotspring.query.all()
  return render_template("list.html", hotsprings=hotsprings)

@app.route("/hotsprings/")
def hotsprings():
  hotsprings = Hotspring.query.all()
  return render_template("list.html", hotsprings=hotsprings)

@app.route("/hotspring/<ZIP>/")
def hotspring(ZIP):
  hotspring = Hotspring.query.filter_by(ZIP=ZIP).first()
  return render_template("show.html", hotspring=hotspring)

# @app.route('/search')
# def search():
#   name = request.args.get('query')
#   hotsprings = Hotspring.query.filter(Hotspring.Name.contains(name)).all()
#   return render_template('list.html', hotsprings=hotsprings)

# If this is running from the command line
# do something
if __name__ == '__main__':
  app.run(debug=True)