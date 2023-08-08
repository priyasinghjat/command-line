class student:
    def __init__(self):
        self.name="priya"
        self.age=90
    def com(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=student()
c2=student()
if c1.com(c2):
    print("same age")
print(c1.name,c1.age)
print(c2.name,c2.age)