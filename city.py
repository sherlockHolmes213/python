from flask import request,redirect,url_for,Blueprint
from flask_cors import CORS, cross_origin
from mysqlDemo import mysqlConn 
import json
import os
city = Blueprint('city',__name__)
CORS(city, supports_credentials=True, resources=r'/*')

@city.route('/getCity', methods=['GET'])
def getCity():
    newMysqlConn = mysqlConn('world')
    resultFlag = json.loads(newMysqlConn.select('select * from city limit %s, %s',[int(request.args['pageNum'])*int(request.args['pageSize']),int(request.args['pageSize'])]))
    return json.dumps(resultFlag)
@city.route('/deleteCityById', methods=['DELETE'])
def deleteCityById():
    newMysqlConn = mysqlConn('world')
    resultFlag = json.loads(newMysqlConn.dele('delete from city where id = %s',[request.args['id']]))
    return json.dumps(resultFlag)
if __name__ == '__main__':
    city.run()