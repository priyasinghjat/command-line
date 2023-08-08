# # single level inheritance
# class a:
#     def xyz(self):
#         self.name = "priya"
#         self.age = 34
#         self.rollno = 101
#         print(self.name,self.age,self.rollno)

# class b(a):
#     def abc(self):
#         self.city="katni"
#         self.bloodgroup='A'
#         print(self.city,self.bloodgroup)
#         # c2=a()
#         # c2._xyz()
# ob1=b()
# ob1.abc()
# ob1.xyz()


# mulilevel inheritance

# class c:
#     def h(self):
#         print("hellon priya")
# class d(c):
#     def g(self):
#         print("hello neha")
# class  e(d):
#     def k(self):
#         print("hello jai")

# ob2=e()
# ob2.h()
# ob2.g()
# ob2.k()


# multiple inheritance

# class c:
#     def h(self):
#         print("hellon priya")
# class d:
#     def g(self):
#         print("hello neha")
# class  e(c,d):
#     def k(self):
#         print("hello jai")
# ob2=e()
# ob2.h()
# ob2.g()
# ob2.k()

class c:
    def h(self):
        print("hellon priya")
class d(c):
    def g(self):
        print("hello neha")
class  e(c):
    def k(self):
        print("hello jai")
object1 = d()  
object2 = e()  
object1.h()  
object1.g()  
object2.h()  
object2.k()




