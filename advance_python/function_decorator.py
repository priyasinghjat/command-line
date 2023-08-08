# def dec(fun):
#     def inner():
#         print("this is piyush")
#         fun()
#         print("this is kshitiz")
#     return inner
# def num():
#     print("this is priya")
#     print("this is neha")
# result=dec(num)
# result()              # decorator is a function which take a argument of function and its also return a functio
# def dec(num):
#     def inner():
#         print("this is piyush")
#         num()
#         print("this is kshitiz")
#     return inner
# @dec  #this is called decorator function
# def num():
#     print("this is priya")
#     print("this is neha")
# num()

# def dec(fun):
#     def inner():
#         a=fun()
#         add=a+5
#         return add
#     return inner
# @dec
# def a():
#     return 10
# print(a())
# result=dec(a)
# print(result())

def dec(fun):
    def inner():
        b=fun()
        mul=b*5
        return mul
    return inner
def dec1(fun):
    def inner():
        a=fun()
        add=a+5
        return add
    return inner

def a():
    return 10
num=dec1(dec(a))
print(num())