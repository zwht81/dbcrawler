
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
            'password': user.password,
            'usertype': user.usertype
        }
        return jsonify(response)
    response={
        'success': 0,
    }
    return jsonify(response)

@app.route('/api/logout/',methods=['GET'])
def logout():
    response={
        'success': 1
    }
    return jsonify(response)

# 注册
@app.route('/api/register/', methods=['POST'])
def register():
    username = User.query.filter(User.username == request.form['username']).first()
    if(username):
        response={
            'success': 0
        }
        return jsonify(response)
    new_user=User(username=request.form['username'], password=request.form['password'], usertype=request.form['usertype'])
    db.session.add(new_user)
    db.session.commit()
    response={
        'success': 1
    }
    return jsonify(response)

# 展示所有信息
@app.route('/api/list_all_knowledge/', methods=['GET'])
def list_all_knowledge():
    all_knowledge = Knowledge.query.all()
    response={}
    response['success'] = 1
    response['data'] = []
    for k in all_knowledge:
        tmp={}
        # tmp['jyfw'] = k.jyfw[7:25]+'...'
        tmp['jyfw'] = k.jyfw
        tmp['jycs'] = k.jycs[0:12]+'...'
        tmp['kid'] = k.tyshxydm
        response['data'].append(tmp)
    return jsonify(response)

# 根据ID查询某个爬虫信息
@app.route('/api/list_single_knowledge/', methods=['POST'])
def list_single_knowledge():
    k = Knowledge.query.filter(Knowledge.tyshxydm == request.form['kid']).first()
    response={}
    response['success'] = 1
    response['data'] = {}
    response['data']['jyfw'] = k.jyfw
    response['data']['tyshxydm'] = k.tyshxydm
    response['data']['zzjgdm'] = k.zzjgdm
    response['data']['recordid'] = k.recordid
    response['data']['bizhong'] = k.bizhong
    response['data']['hzrq'] = k.hzrq
    response['data']['yyzt'] = k.yyzt
    response['data']['clrq'] = k.clrq
    response['data']['qymc'] = k.qymc
    response['data']['zczb'] = k.zczb
    response['data']['djjgdh'] = k.djjgdh
    response['data']['jycs'] = k.jycs
    response['data']['zch'] = k.zch
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug = True, port = 8123)
    