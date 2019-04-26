from multiprocessing import Process, Queue
from multiprocessing import Pool
import os, time, random
import requests
from mysqlDemo import mysqlConn 
import json

my_headers = [
    {'user-agent':"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
    {'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"},
    {'user-agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"},
    {'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14"},
    {'user-agent':"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"},
    {'user-agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'},
    {'user-agent':'Opera/9.25 (Windows NT 5.1; U; en)'},
    {'user-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'},
    {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
]
my_proxies = [
    {'http':'http://1.202.245.84:8080'},
    {'http':'http://111.26.9.26:80'},
    {'http':'http://36.112.135.44:3128'}
]
# 写数据进程执行的代码:
def write(q):
    userData = {}
    try:
        url="http://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp" % q
        r1=requests.get(url,headers=my_headers[random.randint(0,8)],proxies=random.choice(my_proxies),timeout=5)
        userData['id'] = r1.json()['data']['mid']
        userData['name'] = r1.json()['data']['name']
        userData['sex'] = r1.json()['data']['sex']
        userData['face'] = r1.json()['data']['face']
        userData['sign'] = r1.json()['data']['sign']
        userData['level'] = r1.json()['data']['level']
        userData['birthday'] = r1.json()['data']['birthday']
        userData['coins'] = r1.json()['data']['coins']
        url="http://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp" % q
        r=requests.get(url,headers=my_headers[random.randint(0,8)],proxies=random.choice(my_proxies),timeout=5)
        userData['follower'] = r.json()['data']['follower']
        userData['following'] = r.json()['data']['following']
        read(userData)
    except BaseException as e:
        print(e)
        pass
    finally:
        pass
        # print(q)
        # n=n+1

# 读数据进程执行的代码:
def read(userData):
    try:
        newMysqlConn = mysqlConn('bilibili')
        resultFlag = newMysqlConn.insert('insert into user_copy1 (id,name,sex,face,sign,level,birthday,coins,following,follower) values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',[userData['id'],userData['name'],userData['sex'],userData['face'],userData['sign'],userData['level'],userData['birthday'],userData['coins'],userData['following'],userData['follower']])
    except:
        pass

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # # pr = Process(target=read, args=(q,))
    # # 启动子进程pw，写入:
    # print(time.ctime(time.time()) )
    # pw.start()
    # # 启动子进程pr，读取:
    # # pr.start()
    # # 等待pw结束:
    # pw.join()
    # print(time.ctime(time.time()) )
    # # pr进程里是死循环，无法等待其结束，只能强行终止:
    # pr.terminate()


    p = Pool(12)
    print(time.ctime(time.time()) )
    i=1
    while True:
        p.apply_async(write, args=(i,))
        i = i+1
    p.close()
    p.join()
    print(time.ctime(time.time()) )