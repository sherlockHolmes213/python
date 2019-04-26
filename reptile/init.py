import time, threading
import requests
from mysqlDemo import mysqlConn 
import json
userData = {}
# 创建线程数组
def getInfo(uid):
    print("开始任务1")
    url="http://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp" % uid
    r=requests.get(url)
    userData['id'] = r.json()['data']['mid']
    userData['name'] = r.json()['data']['name']
    userData['sex'] = r.json()['data']['sex']
    userData['face'] = r.json()['data']['face']
    userData['sign'] = r.json()['data']['sign']
    userData['level'] = r.json()['data']['level']
    userData['birthday'] = r.json()['data']['birthday']
    userData['coins'] = r.json()['data']['coins']
    print("任务1结束")
def getStat(uid):
    print("开始任务2")
    url="http://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp" % uid
    r=requests.get(url)
    userData['follower'] = r.json()['data']['follower']
    userData['following'] = r.json()['data']['following']
    print("任务2结束")
def getUpstat(uid):
    url="http://api.bilibili.com/x/space/upstat?mid=%s&jsonp=jsonp" % uid
    r=requests.get(url)
    print(r.text)
    userData['age'] = uid
def insertMysql():
    print("开始注入",userData)
    newMysqlConn = mysqlConn('bilibili')
    resultFlag = newMysqlConn.insert('insert into user (id,name,sex,face,sign,level,birthday,coins,following,follower) values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',[userData['id'],userData['name'],userData['sex'],userData['face'],userData['sign'],userData['level'],userData['birthday'],userData['coins'],userData['following'],userData['follower']])
n=1
# 创建线程t1，并添加到线程数组
threads = []
t1 = threading.Thread(target=getInfo,args=(n,))
threads.append(t1)
t2 = threading.Thread(target=getStat,args=(n,))
threads.append(t2)
# t3 = threading.Thread(target=insertMysql)
# threads.append(t3)
for t in threads:
    t.start()
    n=n+1
# t.join()
