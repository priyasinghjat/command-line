# function overloading
class area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("nothing print")    # it has same function name but diffrent parameter name is called over loading

ob1=area()
ob1.find_area(12)
ob1.find_area(10,23)    # same object having different behaviour is called polymorphism
ob1.find_area()

# function overriding

class student:
    def show(self):
        print("hello priya")
class student1(student):
    def show(self):
        print("hello neha")
ob1=student()
ob1.show()
ob1=student1()
ob1.show()   # it mainly used for memory reducing process
# overriding concept will come in inheritance it has same function and parameter name

#  super function

class student:
    def show(self):
        print("hello priya")
class student1(student):
    def show(self):
        super().show()      # super fucntio work to display override function 
        print("hello neha")
ob1=student()
ob1.show()
ob1=student1()
ob1.show()
