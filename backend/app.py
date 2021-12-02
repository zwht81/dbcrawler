
from functools import wraps
from flask import Flask, request, render_template, redirect, url_for, flash, session,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_,not_,func
from models import *
from manage import *
from flask_cors import CORS
import config
import datetime,time
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config.from_object(config)
app.secret_key = '\xc9ixnRb\xe40\xd4\xa5\x7f\x03\xd0y6\x01\x1f\x96\xeao+\x8a\x9f\xe4'
db = SQLAlchemy(app)

####################################
########## User 操作 ###############
####################################

#登录
@app.route('/api/login/', methods=['POST'])
def login():
    if valid_login(request.form['username'], request.form['password']):
        user = User.query.filter(User.username == request.form['username']).first()
        print(type(user))
        response={
            'success': 1,
            'username': user.username,
            'password': user.password
        }
        return jsonify(response)
    response={
        'success': 0
    }
    return jsonify(response)

@app.route('/api/logout/',methods=['GET'])
def logout():
    content='success'
    return jsonify(content)

# 注册
@app.route('/api/register/', methods=['POST'])
def register():
    if request.method == 'POST':
        username = User.query.filter(User.username == request.form['username']).first()
        if(username):
            return jsonify('fail')
        else:
            new_user=User(id=id, username=request.form['username'], password=request.form['password'])
    return jsonify('success')

if __name__ == '__main__':
    app.run(debug = True, port = 8123)
    