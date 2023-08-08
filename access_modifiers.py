# public class we can access anywhere
# bydefault access modifer
# class a:
#     def xyz(self):
#         print("hello")
# class b:
#     def abc(self):
#         print("bye")
#         c2=a()
#         c2.xyz()
# c1=a()
# c1.xyz()
# c3=b()
# c3.abc()


print("/////////////////////////")
# # protected class only access where we inherit the class and we represent protected class with the help of underscore
# # protected member call in inherit class we can not call any where which is not inherit
# class a:
#     def _xyz(self):     # we cannnot access the class anywher bcoz now it protected so only this class is access where we inherit this class meanwhile we access this class only in b class

#         print("hello")
# class b(a):
#     def abc(self):
#         print("bye")
#         c2=a()
#         c2._xyz()
# # c1=a()        we can call this class anywhere with help of _(underscore means it is protected class)
# # c1._xyz()
# c3=b()
# c3.abc()

print("/////////////////")
# private class we cannot access anywhere only we can access inside the class
# with help of other function we can acces private function otherwise we can only call in a same class
# class a:
#     def __xyz(self):
#         print("hello")
#     def abc(self):
#         print("bye")
#         c1=a()
#         c1.__xyz()
# c2=a()
# c2.abc()

# class a:
#     def __xyz(self):
#         print("hello")
#     def abc(self):
#         print("bye")
#         self=a()
#         self.__xyz()

# c1 = a()
# c1.abc()

# class A:
#     def __abc(self):
#         print("hello")
#     def pqr(self):
#         print("bye")
#         a=A()
#         a.__abc()
# c1=A()
# c1.pqr()

