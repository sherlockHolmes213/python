from multiprocessing import Process, Queue
import os, time, random
import requests
from mysqlDemo import mysqlConn 
import json

# 读数据进程执行的代码:
def read(q):
    n=1
    while n<1000:
        try:
            newMysqlConn = mysqlConn('bilibili')
            resultFlag = newMysqlConn.insert('insert into user_copy1 (id,name,sex,face,sign,level,birthday,coins,following,follower) values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',[n,"测试","性别","地址","简介",5,"5",200,100,100])
        except Exception as e:
            print(e)
            pass
        finally:
            n=n+1

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=read, args=(q,))
    # pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    print(time.ctime(time.time()) )
    pw.start()
    # 启动子进程pr，读取:
    # pr.start()
    # 等待pw结束:
    pw.join()
    print(time.ctime(time.time()) )
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pw.terminate()