from threading import*
from time import sleep
mylock=RLock()
def task(mylock,msg):
    mylock.acquire()
    mylock.acquire()
    print(mylock)
    for i in range (5):
        print(msg)
    sleep(3)
    mylock.release()
    mylock.release()
t1=Thread(target=task,args=(mylock,"hello"))
t2=Thread(target=task,args=(mylock,"bye"))
t1.start()
t2.start()