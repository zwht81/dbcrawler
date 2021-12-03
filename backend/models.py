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
    usertype = db.Column(db.Integer())

class Knowledge(db.Model):
    __tablename__='knowledge'
    jyfw = db.Column(db.String(255))
    tyshxydm = db.Column(db.String(255), primary_key=True)
    zzjgdm = db.Column(db.String(255))
    recordid = db.Column(db.String(255))
    bizhong = db.Column(db.String(255))
    hzrq = db.Column(db.String(255))
    yyzt = db.Column(db.String(255))
    clrq = db.Column(db.String(255))
    qymc = db.Column(db.String(255))
    zczb = db.Column(db.Double())
    djjgdh = db.Column(db.String(255))
    jycs = db.Column(db.String(255))
    zch = db.Column(db.String(255))

