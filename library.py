from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

 
class librarymanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("library management ststem")
        self.root.geometry("1550x800+0+0")

        #====================VARIABLE=============================

        self.member_var=StringVar()
        self.Prn_var=StringVar()
        self.ID_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdate_var=StringVar()
        self.finalprice_var=StringVar()
        

        #Header design  heading me jo likha h
        lbltitle=Label(self.root,text="LIBRARY DATA MANAGEMENT",bg="yellow",fg="blue",bd=20,relief=RIDGE,font=("blue",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
    

        #===========================second row===================================

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="yellow")
        frame.place(x=0,y=130,width=1530,height=400)

        #Data frame left 
        DataFrameLeft=LabelFrame(frame,text="Library membership information",bg="yellow",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="yellow",text="Member type",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",13,"bold"),width=29,state="readonly")


        comMember["value"]=("Admin staff","Student","Lecturer")
        comMember.current=(0)
        comMember.grid(row=0,column=1)

        lblPRN=Label(DataFrameLeft,bg="yellow",text="PRN No:",font=("arial",12,"bold"),padx=2,pady=4)   #PRN NUMBER
        lblPRN.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.Prn_var,width=29)       
        txtPRN_NO.grid(row=1,column=1)

        
        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="yellow")   #TITLE
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ID_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblfirstname=Label(DataFrameLeft,font=("arial",12,"bold"),text="FistName:",padx=2,pady=6,bg="yellow")
        lblfirstname.grid(row=3,column=0,sticky=W)
        txtfirstname=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtfirstname.grid(row=3,column=1)

        lbllastname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Surname:",padx=2,pady=6,bg="yellow")
        lbllastname.grid(row=4,column=0,sticky=W)
        txtlastname=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtlastname.grid(row=4,column=1)

        lbladdress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1:",padx=2,pady=6,bg="yellow")
        lbladdress1.grid(row=5,column=0,sticky=W)
        txtaddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtaddress1.grid(row=5,column=1)

        lbladdress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2:",padx=2,pady=6,bg="yellow")
        lbladdress2.grid(row=6,column=0,sticky=W)
        txtaddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtaddress2.grid(row=6,column=1)

        lblpostalcode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Postal Code:",padx=2,pady=6,bg="yellow")
        lblpostalcode.grid(row=7,column=0,sticky=W)
        txtpostalcode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtpostalcode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile No:",padx=2,pady=6,bg="yellow")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblbookid=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2,pady=6,bg="yellow")
        lblbookid.grid(row=0,column=2,sticky=W)
        txtbookid=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtbookid.grid(row=0,column=3)

        lblBooktitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6,bg="yellow")
        lblBooktitle.grid(row=1,column=2,sticky=W)
        txtBooktitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBooktitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name:",padx=2,pady=6,bg="yellow")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="yellow")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDatedue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="yellow")
        lblDatedue.grid(row=4,column=2,sticky=W)
        txtDatedue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDatedue.grid(row=4,column=3)

        lblDaysonbook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book",padx=2,pady=6,bg="yellow")
        lblDaysonbook.grid(row=5,column=2,sticky=W)
        txtDayonbook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDayonbook.grid(row=5,column=3)

        lblLatereturnfine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="yellow")
        lblLatereturnfine.grid(row=6,column=2,sticky=W)
        txtlatereturnfine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtlatereturnfine.grid(row=6,column=3)

        lblDateoverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Date:",padx=2,pady=6,bg="yellow")
        lblDateoverdate.grid(row=7,column=2,sticky=W)
        txtDateoverdate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateoverdate_var,width=29)
        txtDateoverdate.grid(row=7,column=3)

        lblActualprice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="yellow")
        lblActualprice.grid(row=8,column=2,sticky=W)
        txtActualprice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualprice.grid(row=8,column=3)
 
        #Data frame right
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="yellow",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        
        self.txtbox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky="ns")  #ns=north south

        listbook=["English litrature","Discrete mathematics","DBMS","Python","HTML","CSS","Java script","Software engineer","English","Hindi","Soft skills","Physics","Biology","Chemistry","History","Geography","Arts","Machine learning","Ayush Biography","Deepanshu sir Biography","Kamlesh khatri sir Biography"]


        def selectbook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if(x=="English litrature"):
                self.bookid_var.set("ENG5454")
                self.booktitle_var.set("Litrature manual")
                self.author_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.788")


            elif(x=="Discrete mathematics"):
                self.bookid_var.set("MATH10110")
                self.booktitle_var.set("Cs field")
                self.author_var.set("Swapnail sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.600")

            elif(x=="DBMS"):
                self.bookid_var.set("DataBase0110")
                self.booktitle_var.set("Cs field")
                self.author_var.set("Deepanshu sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.1000")

            elif(x=="HTML"):
                self.bookid_var.set("HTML10110")
                self.booktitle_var.set("Web development field")
                self.author_var.set("BY ME")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.630")

            elif(x=="CSS"):
                self.bookid_var.set("CSS10110")
                self.booktitle_var.set("style field")
                self.author_var.set("BY ME")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.650")


            elif(x=="Java script"):
                self.bookid_var.set("js10110")
                self.booktitle_var.set("Cs field")
                self.author_var.set("By me")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.300")

            elif(x=="Python"):
                self.bookid_var.set("PY10110")
                self.booktitle_var.set("Cs field")
                self.author_var.set("kamlesh khatri sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.730")

            elif(x=="Software engineer"):
                self.bookid_var.set("SE10110")
                self.booktitle_var.set("Cs field")
                self.author_var.set("Anshu mam")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("350")
                self.finalprice_var.set("Rs.950")

            elif(x=="English"):
                self.bookid_var.set("ENG10110")
                self.booktitle_var.set("All field")
                self.author_var.set("Amas naide")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.60")

            elif(x=="Hindi"):
                self.bookid_var.set("HIN10110")
                self.booktitle_var.set("All field")
                self.author_var.set("Madhusudan bhatt")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.602")


            elif(x=="Soft skills"):
                self.bookid_var.set("SS10110")
                self.booktitle_var.set("all field")
                self.author_var.set("Btech wle sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.302")


            elif(x=="Physics"):
                self.bookid_var.set("PHY10110")
                self.booktitle_var.set("All field")
                self.author_var.set("Karma sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.350")

            

            elif(x=="Chemistry"):
                self.bookid_var.set("CHE10110")
                self.booktitle_var.set("All field")
                self.author_var.set("Manohar sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.90")


            elif(x=="Biology"):
                self.bookid_var.set("BIO10110")
                self.booktitle_var.set("all field")
                self.author_var.set("Swapnail sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.100")


            elif(x=="History"):
                self.bookid_var.set("MA10110")
                self.booktitle_var.set("Arts field")
                self.author_var.set("khan sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.200")


            elif(x=="Geography"):
                self.bookid_var.set("GEO10110")
                self.booktitle_var.set("Arts field")
                self.author_var.set("Sany sim")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.10")
            

            elif(x=="Machine learning"):
                self.bookid_var.set("ML10110")
                self.booktitle_var.set("Cs field")
                self.author_var.set("Anupam sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.1200")


            elif(x=="Ayush Biography"):
                self.bookid_var.set("AB10110")
                self.booktitle_var.set("Cs field")
                self.author_var.set("own ")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.10000")


            elif(x=="Deepanshu sir Biography"):
                self.bookid_var.set("DSB10110")
                self.booktitle_var.set("Cs field")
                self.author_var.set("Deepanshu sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.100000000")


            elif(x=="Kamlesh khatri sir Biography"):
                self.bookid_var.set("KKS10110")
                self.booktitle_var.set("Cs field")
                self.author_var.set("Kamlesh sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.600")


            elif(x=="Arts"):
                self.bookid_var.set("ART10110")
                self.booktitle_var.set("Arts field")
                self.author_var.set("Swapnail sir")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("NO")
                self.finalprice_var.set("Rs.600")
            



        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)

        listbox.bind("<<ListboxSelect>>",selectbook)

        listbox.grid(row=0,column=0,padx=4)   #Griddig

        listscrollbar.config(command=listbox.yview)

        for item in listbook:
            listbox.insert(END,item)

        #FOR BUTTONS FRAME 

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="yellow")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnaddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnaddData.grid(row=0,column=0)

        btnaddData=Button(Framebutton,command=self.showdata,text="Show Data",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnaddData.grid(row=0,column=1)

        btnaddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnaddData.grid(row=0,column=2)

        btnaddData=Button(Framebutton,command=self.Delete,text="Delete",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnaddData.grid(row=0,column=3)

        btnaddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnaddData.grid(row=0,column=4)

        btnaddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnaddData.grid(row=0,column=5)

        #INFORMATION FRAME

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="yellow")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        #===========================================Database==================================================
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="yellow")
        Table_frame.place(x=0,y=2,width=1460,height=190)
 
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First name")
        self.library_table.heading("lastname",text="Last name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post Id")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")
       

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)


        self.fatch_data()

        self.library_table.bind("<ButtonRelease-1>",self.get_curser)


    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ayush11325@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.Prn_var.get(),
            self.ID_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdate_var.get(),
            self.finalprice_var.get()

                                ))

        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ayush11325@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s ,ID=%s ,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostCode=%s,MobileNo=%s,BookId=%s,BookTitle=%s,AuthorName=%s,DateBorrowed=%s,DateDue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDate=%s,FinalPrice=%s where PRN_NO=%s",(

            self.member_var.get(),
            self.ID_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdate_var.get(),
            self.finalprice_var.get(),
            self.Prn_var.get(),

            ))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("success","Member has been updated")


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ayush11325@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)

            conn.commit()

        conn.close()


    def get_curser(self,event=""):
        curser_row=self.library_table.focus()
        content=self.library_table.item(curser_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.Prn_var.set(row[1]),
        self.ID_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdate_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showdata(self):
        self.txtbox.insert(END,"Member Type: \t\t\t"+self.member_var.get()+"\n")
        self.txtbox.insert(END,"PRN No: \t\t\t"+self.Prn_var.get()+"\n")
        self.txtbox.insert(END,"ID: \t\t\t"+self.ID_var.get()+"\n")
        self.txtbox.insert(END,"First Name: \t\t\t"+self.firstname_var.get()+"\n")
        self.txtbox.insert(END,"Last Name: \t\t\t"+self.lastname_var.get()+"\n")
        self.txtbox.insert(END,"Address1: \t\t\t"+self.address1_var.get()+"\n")
        self.txtbox.insert(END,"Address 2 :\t\t\t"+self.address2_var.get()+"\n")
        self.txtbox.insert(END,"Post Code: \t\t\t"+self.postcode_var.get()+"\n")
        self.txtbox.insert(END,"Mobile No: \t\t\t"+self.mobile_var.get()+"\n")
        self.txtbox.insert(END,"Book Id: \t\t\t"+self.bookid_var.get()+"\n")
        self.txtbox.insert(END,"Book Title: \t\t\t"+self.booktitle_var.get()+"\n")
        self.txtbox.insert(END,"Author Name :\t\t\t"+self.author_var.get()+"\n")
        self.txtbox.insert(END," Date Borrowed:\t\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtbox.insert(END,"Date Due: \t\t\t"+self.datedue_var.get()+"\n")
        self.txtbox.insert(END,"Days On Book :\t\t\t"+self.daysonbook_var.get()+"\n")
        self.txtbox.insert(END,"Later Return Fine: \t\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtbox.insert(END,"Date Over Date: \t\t\t"+self.dateoverdate_var.get()+"\n")
        self.txtbox.insert(END,"Final Price: \t\t\t"+self.finalprice_var.get()+"\n")
        

    def reset(self):
        self.member_var.set(""),
        self.Prn_var.set(""),
        self.ID_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdate_var.set(""),
        self.finalprice_var.set("")

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit")
        if iExit>0:
            self.root.destroy()
            return  

    def Delete(self):
        if self.Prn_var.get()==""or self.ID_var.get()=="":
            messagebox.showerror("Error","First select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ayush11325@",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.Prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member Has been deleted")



if __name__=="__main__":
    root=Tk()
    obj=librarymanagementsystem(root)
    root.mainloop() #screen rok kr rakhe ga

