from threading import*
from time import sleep
mylock=Lock()
def task(mylock,msg):
    mylock.acquire()
    for i in range (5):
        print(msg)
    sleep(3)
    mylock.release()
t1=Thread(target=task,args=(mylock,"hello"))
t2=Thread(target=task,args=(mylock,"bye"))
t1.start()
t2.start()