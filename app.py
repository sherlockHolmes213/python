from flask import Flask
from flask import request,redirect,url_for
from flask_cors import CORS, cross_origin
from mysqlDemo import mysqlConn 
import json
import os
app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')

@app.route('/', methods=['GET', 'POST','OPTIONS'])
def home():
    return '<h1>测试文档</h1>'

@cross_origin()
@app.route('/flaskDemo/signUp', methods=['POST'])
def signUp():
    newMysqlConn = mysqlConn('world')
    resultFlag = newMysqlConn.insert('insert into user (name, password) values (%s, %s)',[request.json['name'],request.json['password']])
    # cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    return resultFlag
@app.route('/flaskDemo/login', methods=['POST'])
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
@app.route('/flaskDemo/getCity', methods=['GET'])
def getCity():
    newMysqlConn = mysqlConn('world')
    resultFlag = json.loads(newMysqlConn.select('select * from city limit %s, %s',[int(request.args['pageNum'])*int(request.args['pageSize']),int(request.args['pageSize'])]))
    return json.dumps(resultFlag)
@app.route('/flaskDemo/deleteCityById', methods=['DELETE'])
def deleteCityById():
    newMysqlConn = mysqlConn('world')
    resultFlag = json.loads(newMysqlConn.dele('delete from city where id = %s',[request.args['id']]))
    return json.dumps(resultFlag)
@app.route('/flaskDemo/upload', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath,'static/uploads/',f.filename)
        f.save(upload_path)
        return redirect(url_for('upload'))
    return "ok"
if __name__ == '__main__':
    app.run()