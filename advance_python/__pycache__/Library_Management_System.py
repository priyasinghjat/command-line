from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        # =====================================================================================================

        # self.member_var=StringVar()
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finallprice_var = StringVar()



        # Create the title label
        lb1title = Label(self.root, text="Library Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lb1title.pack(side=TOP, fill=X)
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        # =====================================================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue", fg="green", bd=12, relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lb1Member=Label(DataFrameLeft,font=("arial",12,"bold"),text="Member Type",padx=2,pady=6,bg="powder blue")
        lb1Member.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readonly",font=("arial",12,"bold"),width=27)
        comMember['value']=("Admin Staff","Lecturer","Student") 
        comMember.current(0)
        comMember.grid(row=0,column=1) 

        

        
        lb1PRN_NO=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN NO",padx=2,bg="powder blue")
        lb1PRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)


        lb1Title=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No.",padx=2,pady=4,bg="powder blue")
        lb1Title.grid(row=2,column=0,sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        

        lb1FirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="First Name",padx=2,pady=6,bg="powder blue")
        lb1FirstName.grid(row=3,column=0,sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.firstname_var ,width=29)
        txtFirstName.grid(row=3,column=1)

        

        lb1LastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Last Name",padx=2,pady=6,bg="powder blue")
        lb1LastName.grid(row=4,column=0,sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.lastname_var ,width=29)
        txtLastName.grid(row=4,column=1)
 
        

        lb1Address1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lb1Address1.grid(row=5,column=0,sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.address1_var ,width=29)
        txtAddress1.grid(row=5,column=1)


        lb1Address2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lb1Address2.grid(row=6,column=0,sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)


        lb1PostalCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Postal Code",padx=2,pady=4,bg="powder blue")
        lb1PostalCode.grid(row=7,column=0,sticky=W)
        txtPostalCode = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.postcode_var ,width=29)
        txtPostalCode.grid(row=7,column=1)
        

        lb1Mobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Phone Number",padx=2,pady=4,bg="powder blue")
        lb1Mobile.grid(row=8,column=0,sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8,column=1)

        lb1BookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id",padx=2,bg="powder blue")
        lb1BookId.grid(row=0,column=2,sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.bookid_var ,width=29)
        txtBookId.grid(row=0,column=3)

        lb1BookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title",padx=2,pady=6,bg="powder blue")
        lb1BookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.booktitle_var ,width=29)
        txtBookTitle.grid(row=1,column=3)

        lb1Auther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther",padx=2,pady=4,bg="powder blue")
        lb1Auther.grid(row=2,column=2,sticky=W)
        txtAuther= Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.auther_var ,width=29)
        txtAuther.grid(row=2,column=3)
        

        lb1DateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed",padx=2,pady=4,bg="powder blue")
        lb1DateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dateborrowed_var ,width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lb1DateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due",padx=2,pady=4,bg="powder blue")
        lb1DateDue.grid(row=4,column=2,sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.datedue_var ,width=29)
        txtDateDue.grid(row=4,column=3)

        lb1DayOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Day On Book",padx=2,pady=4,bg="powder blue")
        lb1DayOnBook.grid(row=5,column=2,sticky=W)
        txtDayOnBook = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.daysonbook_var ,width=29)
        txtDayOnBook.grid(row=5,column=3)

        lb1LateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine",padx=2,pady=4,bg="powder blue")
        lb1LateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.lateratefine_var ,width=29)
        txtLateReturnFine.grid(row=6,column=3)


        lb1DateOverDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Date",padx=2,pady=4,bg="powder blue")
        lb1DateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dateoverdue_var, width=29)
        txtDateOverDate.grid(row=7,column=3)
        

        lb1ActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price",padx=2,pady=4,bg="powder blue")
        lb1ActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.finallprice_var, width=29)
        txtActualPrice.grid(row=8,column=3)
# =================================================================================================
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue", fg="green", bd=12, relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=["The Great Gatsby",
             "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "Harry Potter and the Sorcerer's Stone",
    "The Lord of the Rings",
    "The Catcher in the Rye",
    "Animal Farm",
    "Brave New World",
    "The Hobbit",
    "The Da Vinci Code",
    "The Hunger Games",
    "The Alchemist",
    "Gone with the Wind",
    "The Chronicles of Narnia",
    "Fahrenheit 451",
    "The Book Thief",
    "Wuthering Heights",
    "Jane Eyre",
    "The Little Prince","Python Crash Course: A Hands-On, Project-Based Introduction to Programming",
    "Learn Python the Hard Way",
    "Automate the Boring Stuff with Python",
    "Effective Python: 59 Specific Ways to Write Better Python",
    "Clean Code: A Handbook of Agile Software Craftsmanship",
    "The Pragmatic Programmer: Your Journey to Mastery",
    "JavaScript: The Good Parts",
    "Eloquent JavaScript: A Modern Introduction to Programming",
    "Learning Web Design: A Beginner's Guide to HTML, CSS, JavaScript, and Web Graphics",
    "Head First Java",
    "Java: The Complete Reference",
    "C++ Primer",
    "Programming: Principles and Practice Using C++",
    "C#: Programming Basics for Absolute Beginners",
    "HTML and CSS: Design and Build Websites",
    "PHP and MySQL Web Development",
    "Ruby on Rails Tutorial: Learn Web Development with Rails",
    "Learning Perl",
    "The Go Programming Language",
    "Learning Swift: Building Apps for macOS, iOS, and Beyond"]
        
        # def SelectBook(event=""):
        #     value=str(listBox.get(listBox.curselection))
        #     x=value
        #     if(x=="Head First Book"):
        #         self.bookid_var.set("BKID5454")
        #         self.booktitle_var.set("Python Manual")
        #         self.auther_var.set("Paul Berry")

        #         d1=datetime.datetime.today()
        #         d2=datetime.timedelta(days=15)
        #         d3=d1+d2
        #         self.dateborrowed_var.set(d1)
        #         self.datedue_var.set(d3)
        #         self.daysonbook_var.set(15)
        #         self.lateratefine_var.set("Rs.50")
        #         self.dateoverdue_var.set("No")
        #         self.finalprice_var.set("Rs.788")
        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            
            if (x == "The Great Gatsby"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif( x == "To Kill a Mockingbird"):
                self.bookid_var.set("BKID54678")
                self.booktitle_var.set("Basic Of Python")
                self.auther_var.set("ZED A.SHAW")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.725")

            elif (x == "1984"):
                self.bookid_var.set("BKID54632")
                self.booktitle_var.set("Programming language Python")
                self.auther_var.set("Rakesh Singh")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.lateratefine_var.set("Rs.30")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.715")

            elif (x == "Pride and Prejudice"):
                self.bookid_var.set("BKID7040")
                self.booktitle_var.set("Advance Python")
                self.auther_var.set("Nil Kamal")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("18")
                self.lateratefine_var.set("Rs.27")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.925")

            elif( x == "Harry Potter and the Sorcerer's Stone"):
                self.bookid_var.set("BKID54670")
                self.booktitle_var.set("Core Python")
                self.auther_var.set("kusal chdr.")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.lateratefine_var.set("Rs.35")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.735")

            elif (x == "The Lord of the Rings"):
                self.bookid_var.set("BKID548943")
                self.booktitle_var.set("Python is high level language")
                self.auther_var.set("ashish sharma")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.lateratefine_var.set("Rs.95")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.825")

            elif x == ("The Catcher in the Rye"):
                self.bookid_var.set("BKID54600")
                self.booktitle_var.set("Python")
                self.auther_var.set("khushi singh")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.765")

        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<listboxselect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
        


        # =============================================================================button=======
        frameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameButton.place(x=0,y=530,width=1530,height=70)


        
        btnAddData=Button(frameButton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="white",fg="black")
        btnAddData.grid(row=0,column=0) 

        btnAddData=Button(frameButton,text="Show Data",font=("arial",12,"bold"),width=23,bg="white",fg="black")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(frameButton,text="Update",font=("arial",12,"bold"),width=23,bg="white",fg="black")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(frameButton,text="Delete",font=("arial",12,"bold"),width=23,bg="white",fg="black")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(frameButton,text="Reset",font=("arial",12,"bold"),width=23,bg="white",fg="black")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(frameButton,text="Exit",font=("arial",12,"bold"),width=23,bg="white",fg="black")
        btnAddData.grid(row=0,column=5)

        btnAddData=Button(frameButton,text="Add Data",font=("arial",12,"bold"),width=23,bg="white",fg="black")
        btnAddData.grid(row=0,column=0)

        # ==========================================================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)
        
        
        # self.library_table=ttk.Treeview(Table_frame,columns=("membertpye","prnno","title","firstname","lastname","address1","address2","postid","phoneno","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"))
        
        
        # self.library_table.heading("membertpye",text="Member Type")
        # self.library_table.heading("prnno",text="Reference Id")
        # self.library_table.heading("title",text="Title")
        # self.library_table.heading("firstname",text="First Name")
        # self.library_table.heading("lastname",text="Last Name")
        # self.library_table.heading("address1",text="Address 1")
        # self.library_table.heading("address2",text="Address 2")
        # self.library_table.heading("postid",text="Post Id")
        # self.library_table.heading("phoneno",text="Phone No")
        # self.library_table.heading("bookid",text="Book Id")
        # self.library_table.heading("booktitle",text="Book Title")
        # self.library_table.heading("author",text="Auther")
        # self.library_table.heading("datebarrowed",text="Date Borrowed")
        # self.library_table.heading("datedue",text="Date Due")
        # self.library_table.heading("days",text="Days")
        # self.library_table.heading("latereturnfine",text="Late Return Fine")
        # self.library_table.heading("dateoverdue",text="Date Over Due")
        # self.library_table.heading("finalprice",text="Final Price")
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        
        self.library_table = ttk.Treeview(Table_frame, columns=("membertpye", "prnno", "title", "firstname", "lastname", "address1", "address2", "postid", "mobile", "bookid", "booktitle", "auther", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertpye", text="Member Type")  # Corrected column name here
        self.library_table.heading("prnno", text="Reference Id")  # Corrected column name here
        self.library_table.heading("title", text="Title")  # Corrected column name here
        self.library_table.heading("firstname", text="First Name")  # Corrected column name here
        self.library_table.heading("lastname", text="Last Name")  # Corrected column name here
        self.library_table.heading("address1", text="Address 1")  # Corrected column name here
        self.library_table.heading("address2", text="Address 2")  # Corrected column name here
        self.library_table.heading("postid", text="Post Id")  # Corrected column name here
        self.library_table.heading("mobile", text="Phone No")  # Corrected column name here
        self.library_table.heading("bookid", text="Book Id")  # Corrected column name here
        self.library_table.heading("booktitle", text="Book Title")  # Corrected column name here
        self.library_table.heading("auther", text="Author")  # Corrected spelling here
        self.library_table.heading("dateborrowed", text="Date Borrowed")  # Corrected column name here
        self.library_table.heading("datedue", text="Date Due")  # Corrected column name here
        self.library_table.heading("days", text="Days")  # Corrected column name here
        self.library_table.heading("latereturnfine", text="Late Return Fine")  # Corrected column name here
        self.library_table.heading("dateoverdue", text="Date Over Due")  # Corrected column name here
        self.library_table.heading("finalprice", text="Final Price")  # Corrected column name here



        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("membertpye", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

    # def add_data(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("insert into library value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member_var.get(),
    #                                                                                                           self.prn_var.get(),
    #                                                                                                           self.id_var.get(),
    #                                                                                                           self.firstname_var.get(),
    #                                                                                                           self.lastname_var.get(),
    #                                                                                                           self.address1_var.get(), 
    #                                                                                                           self.address2_var.get(),
    #                                                                                                           self.postcode_var.get(),
    #                                                                                                           self.phoneno_var.get(),
    #                                                                                                           self.bookid_var.get(),
    #                                                                                                           self.auther_var.get(),
    #                                                                                                           self.dateborrowed_var.get(),
    #                                                                                                           self.datedue_var.get(),
    #                                                                                                           self.daysonbook_var.get(),
    #                                                                                                           self.lateratefine_var.get(),
    #                                                                                                           self.dateoverdue_var.get(),
    #                                                                                                           self.finalprice_var.get(),
    #                                                                                                           self.booktitle_var.get(),
    #                                                                                                         #   self.dateborrowed_var.get(),
    #                                                                                                         #   self.datedue_var.get(),
    #                                                                                                         #   self.lateratefine_var.get(),
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
    #                                                                          ))
        

    #     conn.commit()
    #     conn.close() 
    #     messagebox.showinfo("success","member has been inserted successfully") 

    def add_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="_Priya2002", database="org")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                      (self.member_var.get(),
                       self.prn_var.get(),
                       self.id_var.get(),
                       self.firstname_var.get(),
                       self.lastname_var.get(),
                       self.address1_var.get(),
                       self.address2_var.get(),
                       self.postcode_var.get(),
                       self.mobile_var.get(),
                       self.bookid_var.get(),
                       self.booktitle_var.get(),
                       self.auther_var.get(),
                       self.dateborrowed_var.get(),
                       self.datedue_var.get(),
                       self.daysonbook_var.get(),
                       self.lateratefine_var.get(),
                       self.dateoverdue_var.get(),
                       self.finallprice_var.get()
                       ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Member has been inserted successfully")

    



if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()