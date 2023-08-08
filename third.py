class Reminder:
    def __init__(self,file):
        self.file=open(file,"w+")
        self.data=list(self.file.readline())
        pass
    def add(self,time,message):
        self.data.append ([time,message])
        self.file.write(str(self.data))
        pass
    def update(self,id,time,message):
        pass
    def delete(self,id):
        pass
    def getReminder(self):
        pass
    def printall(self):
        print(self.data)
def run():
    reminder=Reminder("reminder.txt")
    userTime=str(input("Enter time to be reminder:"))
    userMessage=str(input("Enter message to be reminder:"))
    print(userTime,userMessage)
    reminder.add(userTime,userMessage)
    reminder.printall()
    print("hello")
if __name__=="__main__":
    run()