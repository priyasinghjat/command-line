from threading import*
import time
obj=Semaphore(3)
def display(name):
    obj.acquire()
    for i in range(5):
        print("hello")
        print(name)
        time.sleep(0.5)
    obj.release()

t1=Thread(target=display,args=("thread-1",))
t2=Thread(target=display,args=("thread-2",))
t3=Thread(target=display,args=("thread-3",))
t4=Thread(target=display,args=("thread-4",))
t5=Thread(target=display,args=("thread-5",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()