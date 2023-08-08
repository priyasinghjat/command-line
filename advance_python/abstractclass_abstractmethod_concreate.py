from abc import ABC,abstractmethod
# # abstract class
# class father(ABC):
#     # abstract method
#     @abstractmethod
#     def disp(self):
#         pass
#     #concreate method
#     def show(self):   #this called is called signature in abstract class we cannot make a object 
#         print("concreate method") #with help of child class we can access parent class
# class child(father):          #we not define abstract menthod in abstract class we can define abstract method in child class
#     def disp(self):
#         print("abstract method")

# ob1=child()
# ob1.disp()
# ob1.show()



class defence(ABC):
    def __init__(self):
        self.id=101
    @abstractmethod
    def show(self):
        pass
    def dis(self):
        self.gun="AK27"
        print(self.gun , self.id)
class army(defence):
    def show(self):
        print("army")
class airforce(defence):
    def show(self):
        print("airforce")
class navy(defence):
    def show(self):
        print("navy")
a=army()
a.show()
a.dis()
a=airforce()
a.show()
a.dis()
a=navy()
a.show()
a.dis()

