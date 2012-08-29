from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgres://tutorial:password@192.168.100.20/vagrant_ansible_tutorial'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route('/')
def index():
    return render_template('index.html', users=User.query.all())


@app.before_first_request
def invalidate_data():
    db.drop_all()
    db.create_all()
    for u, e in [('matt', 'matt@nobien.net'),
                 ('marc', 'marc@nobien.net')]:
        db.session.add(User(u, e))
