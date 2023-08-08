# class demo:
#     number=20
# c1=demo()
# print(c1.number)  # calling a class variable with object
# c1.number=90 # it change the instance value
# print(c1.number)
# print(demo.number) # calling class variable with class name

# demo.number=87 # it change class variable
# print(demo.number)

# print(c1.number)

# class demo:
#     number=90  # this is called static and class variable bcoz it share only one copy to all object(instance)
#     def __init__(self): # constructor of instance variable
#         self.number1=89  #instace variable
# c1=demo() #c1 is a instance of demo call is also know as object of demo call
# print(c1.number)   # here we are call a class variable with the help of object or instance
# print(demo.number) # here we are call a class variable with the help of class

# print(c1.number1) # here we are call a instance variable with the help of object or instance


class demo:
    def __init__(self):
        self.number1=90
c1=demo()
c1.number1=78
print(c1.number1)  # if we are change instanve variable one object value it does not affect any other intance value
c2=demo()           #but we are cahnge class variable value it affect all the class oject(instance) it change all the object value to previous value
print(c2.number1)


''' A real-life example of this could be a classroom full of students,
where the class represents the "demo" class and each student represents an instance of the class.
The teacher could assign a project to the class (class variable) and each student could work on their own project (instance variable).
If the teacher changes the project requirements (changing the class variable), 
all the students will be affected, but if a student changes their project, 
it will only affect their own work (instance variable).'''