from threading import Thread
# def show():
#     print("hello priya")
# t=Thread(target=show)
# t.start()


# def display(a,b):
#     a=90
#     b=87
#     print(a,b)
# a=Thread(target=display,args=(2,3))
# a.start()


def disp(a,b):
    print("Threads running",a , b)
# for i in range(5):
#     t=Thread(target=disp, args=(2,3))
#     t.start()
for i in range(5):
 t=Thread(target=disp,args=(10,20))
 t.start()