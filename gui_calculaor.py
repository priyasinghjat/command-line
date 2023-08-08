from tkinter import *
from PIL import Image,ImageTk
# Create the main window
a=Tk()
a.geometry("500x600")
a.title("this my calc")
# b=Label(text='''Computer networking refers to 
#         interconnected computing devices that can 
#         exchange data and share resources with each 
#         other. These networked devices use a system of rules,
#         called communications protocols, to transmit information 
#         over physical or wireless technologies.''',bg="red",fg="white",padx=50,pady=70,font=("comicsansms",19,"bold"),border=3,relief=SUNKEN)
# b.pack(side="bottom", anchor="ne",fill="x")
# b.pack()
# a.maxsize(200,100)
# a.minsize(800,700)
# label does not interact
# Add a label to the window
# b=Label(text="This my GUI calculator")
# it allow only png photo
# photo=PhotoImage(file="")
# its allow jpg
image=Image.open("piyush.jpg")
photo=ImageTk.PhotoImage(image)
# b=Label(image=photo)
b=Label(image=photo)
b.pack()
# mainloop provide basic gui window
a.mainloop()


