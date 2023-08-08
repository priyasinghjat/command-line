from datetime import datetime
obj=datetime.today()
print(obj)

new=obj.strftime("%B,%A,%Y")
print(new)
new=obj.strftime("%B/%A/%Y")
print(new)
new=obj.strftime("%B-%A-%Y")
print(new)
new=obj.strftime("%B:%A:%Y")
print(new)
print(type(new))