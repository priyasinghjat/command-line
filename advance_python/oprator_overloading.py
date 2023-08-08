class student:
    no_of_leave=8
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def show(self):
        return f"my name is {self.name} and my rollno {self.roll}"
    
    @classmethod
    def display(cls,newleave):
        cls.no_of_leave=newleave
    def __add__(self,other):
        return self.roll+other.roll
    def __pow__(self,other):
        return self.roll**other.roll

ob1=student("harry",3)
ob2=student("neha",2)
print(ob1.show())
print(ob1+ob2)
print(ob1**ob2)
