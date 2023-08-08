# from tkinter import *
# from PIL import Image,ImageTk
# root = Tk()

# root.minsize(768,455)
# Heading = Label(text = "My New Album..")
# Heading.pack()
# image = Image.open("ak1.jpg")                    
# image1 = Image.open("ak2.jpg")
# image2 = Image.open("ak3.jpg")
# image3 = Image.open("ak4.jpg")
# image4 = Image.open("ak5.jpg")

# photo = ImageTk.PhotoImage(image)
# photo1 = ImageTk.PhotoImage(image1)
# photo2 = ImageTk.PhotoImage(image2)
# photo3 = ImageTk.PhotoImage(image3)
# photo4 = ImageTk.PhotoImage(image4)

# image_label = Label(image = photo)
# image_label1 = Label(image = photo1)
# image_label2 = Label(image = photo2)
# image_label3 = Label(image = photo3)
# image_label4 = Label(image = photo4)

# image_label.pack()
# image_label1.pack()
# image_label2.pack()
# image_label3.pack()
# image_label4.pack()
# root.mainloop()
# from tkinter import *
# from PIL import Image, ImageTk

# root = Tk()

# root.minsize(768, 455)

# Heading = Label(text="My New Album..")
# Heading.grid(row=0, column=0, columnspan=3)

# image = Image.open("ak1.jpg")
# image1 = Image.open("ak2.jpg")
# image2 = Image.open("ak3.jpg")
# image3 = Image.open("ak4.jpg")
# image4 = Image.open("ak5.jpg")

# photo = ImageTk.PhotoImage(image)
# photo1 = ImageTk.PhotoImage(image1)
# photo2 = ImageTk.PhotoImage(image2)
# photo3 = ImageTk.PhotoImage(image3)
# photo4 = ImageTk.PhotoImage(image4)

# image_label = Label(image=photo)
# image_label1 = Label(image=photo1)
# image_label2 = Label(image=photo2)
# image_label3 = Label(image=photo3)
# image_label4 = Label(image=photo4)

# image_label.grid(row=1, column=0)
# image_label1.grid(row=1, column=1)
# image_label2.grid(row=1, column=2)
# image_label3.grid(row=2, column=0)
# image_label4.grid(row=2, column=1)

# root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()

root.minsize(768, 455)

Heading = Label(text="My New Album..")
Heading.grid(row=0, column=0, columnspan=3)

image_path = os.path.join(os.getcwd(), "ak1.jpg")
image1_path = os.path.join(os.getcwd(), "ak2.jpg")
image2_path = os.path.join(os.getcwd(), "ak3.jpg")
image3_path = os.path.join(os.getcwd(), "ak4.jpg")
image4_path = os.path.join(os.getcwd(), "ak5.jpg")

# Load images and resize them if necessary
image = Image.open(image_path)
if image.size[0] > 300 or image.size[1] > 200:
    image = image.resize((300, 200))
photo = ImageTk.PhotoImage(image)

image1 = Image.open(image1_path)
if image1.size[0] > 300 or image1.size[1] > 200:
    image1 = image1.resize((300, 200))
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open(image2_path)
if image2.size[0] > 300 or image2.size[1] > 200:
    image2 = image2.resize((300, 200))
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open(image3_path)
if image3.size[0] > 300 or image3.size[1] > 200:
    image3 = image3.resize((300, 200))
photo3 = ImageTk.PhotoImage(image3)

image4 = Image.open(image4_path)
if image4.size[0] > 300 or image4.size[1] > 200:
    image4 = image4.resize((300, 200))
photo4 = ImageTk.PhotoImage(image4)

# Create image labels
image_label = Label(image=photo)
image_label1 = Label(image=photo1)
image_label2 = Label(image=photo2)
image_label3 = Label(image=photo3)
image_label4 = Label(image=photo4)

# Position image labels
image_label.grid(row=1, column=0)
image_label1.grid(row=1, column=1)
image_label2.grid(row=1, column=2)
image_label3.grid(row=2, column=0)
image_label4.grid(row=2, column=1)

root.mainloop()




