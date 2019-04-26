# 导入MySQL驱动:
import mysql.connector
import json
class mysqlConn(object):
    def __init__(self, database):
        self.database = database
    def insert(self,sql,sqlValue):
        conn = mysql.connector.connect(user='root', password='yang1113', database=self.database)
        cursor = conn.cursor()
        try:
            cursor.execute(sql, sqlValue)
        except BaseException as e :
            return "error"
        else:
            return "success"
        finally: 
            conn.commit()
            cursor.close()
    def select(self,sql,sqlValue):
        conn = mysql.connector.connect(user='root', password='yang1113', database=self.database)
        cursor = conn.cursor(dictionary=True)
        result = returnData()
        try:
            cursor.execute(sql, sqlValue)
            psw = cursor.fetchall()
        except BaseException as e :
            print(e)
            result.setCode(1)
            result.setData([])
            result.setMessage('失败')
            return result.getResult()
        else:
            result.setCode(0)
            result.setData(psw)
            result.setMessage('成功')
            return result.getResult()
        finally: 
            conn.commit()
            cursor.close()
    def dele(self,sql,sqlValue):
        conn = mysql.connector.connect(user='root', password='yang1113', database=self.database)
        cursor = conn.cursor()
        result = returnData()
        try:
            cursor.execute(sql, sqlValue)
        except BaseException as e :
            result.setCode(1)
            result.setMessage('失败')
            return result.getResult()
        else:
            result.setCode(0)
            result.setMessage('成功')
            return result.getResult()
        finally: 
            conn.commit()
            cursor.close()
class returnData(object):
    def __init__(self):
        self.__result = {
            'code':0,
            'data':[],
            'message':''
        }
    def setCode(self,code):
        self.__result['code'] = code
    def setData(self,data):
        self.__result['data'] = data
    def setMessage(self,message):
        self.__result['message'] = message
    def getResult(self):
        print(self.__result)
        return json.dumps(self.__result)