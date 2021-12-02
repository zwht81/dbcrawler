from functools import wraps
from flask import Flask, flash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_,not_
import config
app = Flask(__name__)
app.config.from_object(config)
app.secret_key = '\xc9ixnRb\xe40\xd4\xa5\x7f\x03\xd0y6\x01\x1f\x96\xeao+\x8a\x9f\xe4'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    username = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255))
  