import time, threading
import requests
from mysqlDemo import mysqlConn 
import json
userData = {}
# 创建线程数组
def getInfo(uid):
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
def getStat(uid):
    url="http://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp" % uid
    r=requests.get(url)
    userData['follower'] = r.json()['data']['follower']
    userData['following'] = r.json()['data']['following']
def getUpstat(uid):
    url="http://api.bilibili.com/x/space/upstat?mid=%s&jsonp=jsonp" % uid
    r=requests.get(url)
    print(r.text)
    userData['age'] = uid
print(time.ctime(time.time()) )
n=2000
while n<2002:
    try:
        getInfo(n)
        getStat(n)
        getUpstat(n)
        # newMysqlConn = mysqlConn('bilibili')
        # resultFlag = newMysqlConn.insert('insert into user (id,name,sex,face,sign,level,birthday,coins,following,follower) values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',[userData['id'],userData['name'],userData['sex'],userData['face'],userData['sign'],userData['level'],userData['birthday'],userData['coins'],userData['following'],userData['follower']])
    except:
        pass
    finally:
        n = n+1
print(time.ctime(time.time()) )
# threads = []
# getStat(9)
# 创建线程t1，并添加到线程数组
# t1 = threading.Thread(target=getInfo(1))
# threads.append(t1)
# t2 = threading.Thread(target=getStat(1))
# threads.append(t2)
# # t3 = threading.Thread(target=getUpstat())
# # threads.append(t3)
# for t in threads:
#     # print(t)
#     t.start()
# t.join()

# newMysqlConn = mysqlConn('world')
# resultFlag = newMysqlConn.insert('insert into user (name, password) values (%s, %s)',[request.json['name'],request.json['password']])