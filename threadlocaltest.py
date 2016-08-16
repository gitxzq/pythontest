#coding=utf-8
'''
@author:xzq
'''
import threading

local_school=threading.local()

def process_student():
    print 'hello,%s (in %s)'%(local_school.student,threading.current_thread().name)

def process_thread(name):

    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=('alice',),name='Thread_a')
t2=threading.Thread(target=process_thread,args=('bob',),name='Thread_b')
t1.start()
t2.start()
t1.join()
t2.join()