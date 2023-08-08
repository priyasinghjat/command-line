from time import time,ctime,localtime
epoc=time()
print(epoc)

et=ctime(epoc)
print(et)

a=localtime()
print(a)
print(a.tm_wday,end="/")
print(a.tm_hour,end="/")
print(a.tm_mon)
print(type(a))



b=ctime()
print(b)
print(type(b))

c=time()
print(c)
print(type(c))