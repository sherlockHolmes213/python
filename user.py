from flask import request,redirect,url_for,Blueprint
from flask_cors import CORS, cross_origin
from mysqlDemo import mysqlConn 
import json
user = Blueprint('user',__name__)
CORS(user, supports_credentials=True, resources=r'/*')
# @cross_origin()
@user.route('/signUp', methods=['POST'])
def signUp():
    newMysqlConn = mysqlConn('world')
    resultFlag = newMysqlConn.insert('insert into user (name, password) values (%s, %s)',[request.json['name'],request.json['password']])
    # cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    return resultFlag
@user.route('/login', methods=['POST'])
def login():
    newMysqlConn = mysqlConn('world')
    resultFlag = json.loads(newMysqlConn.select('select password from user where name = %s',[request.json['name']]))
    if(len(resultFlag['data']) == 0):
        resultFlag['code'] = 1
        resultFlag['message'] = '账号未注册'
    elif(resultFlag['data'][0]['password'] != request.json['password']):
        resultFlag['code'] = 1
        resultFlag['message'] = '账号密码不匹配'
    else:
        resultFlag['code'] = 0
        resultFlag['message'] = '登陆成功'
    return json.dumps(resultFlag) 