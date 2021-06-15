from tkinter import*
from tkinter import ttk
import random
import sqlite3
import time
from datetime import datetime
import tkinter.messagebox
u="000"
p="000"
def main():
    root=Tk()
    app=Window1(root)
    root.mainloop()


class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Library Management System")
        self.master.geometry('1350x750+0+0')
        self.master.configure(bg='powder blue')
        self.frame=Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.lblTitle=Label(self.frame, text='Library Management System', font=('arial',50,'bold'),bg='powder blue',fg='black')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)

  #==========================================================================================================

        self.LoginFrame1=LabelFrame(self.frame, width=1350, height=600, font=('arial',20,'bold'),relief='ridge', bg='cadet blue',bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2=LabelFrame(self.frame, width=1000, height=600, font=('arial',20,'bold'),relief='ridge', bg='cadet blue',bd=20)
        self.LoginFrame2.grid(row=2, column=0)

  #================================================= Label & Entry===========================================================================

        self.lblUsername=Label(self.LoginFrame1, text= 'Username', font=('arial',20,'bold'), bd=22,bg='cadet blue' , fg='Cornsilk')
        self.lblUsername.grid( row=0, column=0)
        self.txtUsername=Entry(self.LoginFrame1, font=('arial',20,'bold'),textvariable=self.Username)
        self.txtUsername.grid( row=0, column=1, padx=119)

        self.lblPassword=Label(self.LoginFrame1, text= 'Password', font=('arial',20,'bold'),bd=22,bg='cadet blue' , fg='Cornsilk')
        self.lblPassword.grid( row=1, column=0)
        self.txtPassword=Entry(self.LoginFrame1, font=('arial',20,'bold'),show = "*", textvariable=self.Password)
        self.txtPassword.grid( row=1, column=1, columnspan=2, pady=30)
                                     
  #====================================================  Button==============================================================================
        self.btnLogin=Button(self.LoginFrame2, text='Login',width=17,font=('arial',20,'bold'),command=self.Login_System)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=8)

        self.btnReset=Button(self.LoginFrame2, text='Reset',width=17,font=('arial',20,'bold'),command=self.Reset)
        self.btnReset.grid(row=3,column=1,pady=20,padx=8)

        self.btnExit=Button(self.LoginFrame2, text='Exit',width=17,font=('arial',20,'bold'), command=self.iExit)
        self.btnExit.grid(row=3,column=2,pady=20,padx=8)

  #===========================================================================================================================================

    def Login_System(self):
        global u
        u=(self.Username.get())
        db1 = Db()
        global p
        p = db1.getadmin()
        
        #p=(self.Password.get())

        if(p==(self.Password.get())):
            self.newWindow=Toplevel(self.master)
            self.app=Library(self.newWindow)
        else:
            tkinter.messagebox.askyesno("Login Systems", "Invalid login detail")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Login Systems", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command=self.new_window
            return   
       

    def new_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Library(self.newWindow)
 
    

class Library:
    
    
    def __init__(self,master):
        self.master=master
        self.master.title(" Library Library")
        self.master.geometry('1425x700+0+0')
        self.master.configure(bg='cadet blue')

        MType=StringVar()
        Ref=StringVar()
        Title=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Address1=StringVar()
        Address2=StringVar()
        PostCode=StringVar()
        MobileNo=StringVar()
        BookID=StringVar()
        BookTitle=StringVar()
        BookType=StringVar()
        Author=StringVar()
        DateBorrowed=StringVar()
        DateDue=StringVar()
        SellingPrice=StringVar()
        LateReturnFine=StringVar()
        DateOverDue=StringVar()
        DaysOnLoan=StringVar()
        Prescription=StringVar()

        def iReset2():
            MType.set("")
            Ref.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            PostCode.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            BookType.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            self.txtFrameDetail.delete("1.0",END)
            self.txtDisplayR.delete("1.0",END)
                

        def iDelete():
            iReset2()
            self.txtDisplayR.delete("1.0",END)

        def iEliminate():
            msg=tkinter.messagebox.askyesno(" Library Library", "Confirm if you want to exit")
            if msg=="True":
               master.quit()
                                

        def iDisplayData():
            self.txtFrameDetail.set(END,"  "+MType.get()+"\t\t"+Ref.get()+"\t\t"+Title.get()+" "+Firstname.get()+
                                       " "+ Surname.get() +"\t \t"+Address1.get()+"\t"+MobileNo.get()+"\t"+PostCode.get()+"\t"+BookTitle.get()+"\t\t"+
                                       DateBorrowed.get()+"\t "+DaysOnLoan.get()+ "\n")
            # self.txtFrameDetail.insert(END,)
            # self.txtFrameDetail.insert(END,)
            # self.txtFrameDetail.insert(END,)
            # self.txtFrameDetail.insert(END,)
            # self.txtFrameDetail.insert(END,)
            # self.txtFrameDetail.insert(END,)
            # self.txtFrameDetail.insert(END,)
            # self.txtFrameDetail.insert(END,)
            # self.txtFrameDetail.insert(END,)
            # self.txtFrameDetail.insert(END,)

        def iReceipt():
            self.txtDisplayR.delete("1.0",END)
            self.txtDisplayR.insert(END, "Member Type: \t\t" + MType.get() + "\n")
            #self.txtDisplayR.insert(END, "Ref No : \t\t" + Ref.get() + "\n")
            self.txtDisplayR.insert(END, "Name:  \t\t" + Title.get() + Firstname.get()+ Surname.get() + "\n")
            #self.txtDisplayR.insert(END, "First Name: \t\t" + Firstname.get() + "\n")
            #self.txtDisplayR.insert(END, "Surname: \t\t" + Surname.get() + "\n")
            self.txtDisplayR.insert(END, "Address: \t\t" + Address1.get() + PostCode.get() + "\n")
            #self.txtDisplayR.insert(END, "Address 2 : \t\t" + Address2.get() + "\n")
            #self.txtDisplayR.insert(END, "Post Code: \t\t" + PostCode.get() + "\n")
            self.txtDisplayR.insert(END, "Mobile No: \t\t" + MobileNo.get() + "\n")
            self.txtDisplayR.insert(END, "Book ID: \t\t" + BookID.get() + "\n")
            self.txtDisplayR.insert(END, "Book Title: \t\t" + BookTitle.get() + "\n")
            self.txtDisplayR.insert(END, "Author: \t\t" + Author.get() + "\n")
            self.txtDisplayR.insert(END, "Date Borrowed: \t\t" + DateBorrowed.get() + "\n")

    
        MainFrame=Frame(self.master)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle=Label(TitleFrame, width=39 , font=("arial", 40 , "bold"),text="\t Library Management Systems \t", padx=12)
        self.lblTitle.grid()

        ButtonFrame=Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail=Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame , bd=10, width=800, height=300, padx=20, relief=RIDGE, font=("arial",12,"bold"), text="Library Membership Info:",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame , bd=10, width=450, height=300, padx=20, relief=RIDGE, font=("arial",12,"bold"), text="Book Details:",)
        DataFrameRIGHT.pack(side=RIGHT)

        #========================= Widgets=====================================#
        self.lblMemberType = Label(DataFrameLEFT, font=("arial", 12, "bold"), text ="Member Type:", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, state="readonly",textvariable=MType, font=("arial", 12, "bold"), width=23)
        self.cboMemberType['value']=('', 'Student', 'Teacher', 'Admin')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)
        
        self.lblBookID = Label(DataFrameLEFT, font=("arial", 12, "bold"), text ="Book ID:", padx=2, pady=2)
        self.lblBookID.grid(row=0, column=2, sticky=W)
        self.txtBookID=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=BookID)
        self.txtBookID.grid(row=0,column=3)

        self.lblRef = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Reference no:", padx=2,pady=2)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.txtRef=Entry(DataFrameLEFT, font=("arial", 12, "bold"),textvariable=Ref, width=25)
        self.txtRef.grid(row=1,column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Book Title:", padx=2,pady=2)
        self.lblBookTitle.grid(row=1,column=2,sticky=W)
        self.txtBookTitle=Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=BookTitle,width=25)
        self.txtBookTitle.grid(row=1,column=3)

        self.lblTitle=Label(DataFrameLEFT, font= ("arial",12,"bold"), text="Title:",padx=2,pady=2)
        self.lblTitle.grid(row=2,column=0,sticky=W)
        self.cboTitle=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable=Title,font=("arial",12,"bold"),width=23)
        self.cboTitle['value']=('', 'Mr.', 'Miss.', 'Mrs.', 'Dr.', 'Capt.', 'Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2,column=1)

        self.lblAuthor = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Author:", padx=2,pady=2)
        self.lblAuthor.grid(row=2,column=2,sticky=W)
        self.txtAuthor=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Author)
        self.txtAuthor.grid(row=2,column=3)


        self.lblFirstName = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="First Name:", padx=2,pady=2)
        self.lblFirstName.grid(row=3,column=0,sticky=W)
        self.txtFirstName=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Firstname)
        self.txtFirstName.grid(row=3,column=1)
        
        self.lblDateBorrowed = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Date Borrowed:", padx=2,pady=2)
        self.lblDateBorrowed.grid(row=3,column=2,sticky=W)
        self.txtDateBorrowed=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=DateBorrowed)
        self.txtDateBorrowed.grid(row=3,column=3)

        self.lblSurname = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Surname:", padx=2,pady=2)
        self.lblSurname.grid(row=4,column=0,sticky=W)
        self.txtSurname=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Surname)
        self.txtSurname.grid(row=4,column=1)

        self.lblDateDue=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Date Due:", padx=2,pady=2)
        self.lblDateDue.grid(row=4,column=2,sticky=W)
        self.txtDateDue=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=DateDue)
        self.txtDateDue.grid(row=4,column=3)

        self.lblAddress1=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Address 1:", padx=2,pady=2)
        self.lblAddress1.grid(row=5,column=0,sticky=W)
        self.txtAddress1=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Address1)
        self.txtAddress1.grid(row=5,column=1)

        self.lblDaysOnLoan=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Days on Loan:", padx=2,pady=2)
        self.lblDaysOnLoan.grid(row=5,column=2,sticky=W)
        self.txtDaysOnLoan=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=DaysOnLoan)
        self.txtDaysOnLoan.grid(row=5,column=3)
        
        self.lblAddress2 = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Address 2:", padx=2,pady=2)
        self.lblAddress2.grid(row=6,column=0,sticky=W)
        self.txtAddress2=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=Address2)
        self.txtAddress2.grid(row=6,column=1)

        self.lblLateReturnFine=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Late Return Fine:", padx=2,pady=2)
        self.lblLateReturnFine.grid(row=6,column=2,sticky=W)
        self.txtLateReturnFine=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=LateReturnFine)
        self.txtLateReturnFine.grid(row=6,column=3)

        self.lblPostCode=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Post Code:", padx=2,pady=2)
        self.lblPostCode.grid(row=7,column=0,sticky=W)
        self.txtPostCode=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=PostCode)
        self.txtPostCode.grid(row=7,column=1)

        self.lblDateOverDue=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Date Over Due:", padx=2,pady=2)
        self.lblDateOverDue.grid(row=7,column=2,sticky=W)
        self.txtDateOverDue=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=DateOverDue)
        self.txtDateOverDue.grid(row=7,column=3)
        
        self.lblMobileNo=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Mobile No:", padx=2,pady=2)
        self.lblMobileNo.grid(row=8,column=0,sticky=W)
        self.txtMobileNo=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=MobileNo)
        self.txtMobileNo.grid(row=8,column=1)

        self.lblSellingPrice=Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Selling Price:", padx=2,pady=2)
        self.lblSellingPrice.grid(row=8,column=2,sticky=W)
        self.txtSellingPrice=Entry(DataFrameLEFT, font=("arial", 12, "bold"),width=25,textvariable=SellingPrice)
        self.txtSellingPrice.grid(row=8,column=3)

        
        #=========================Widgets=============================================================================#
        self.txtDisplayR=Text(DataFrameRIGHT, font=("arial", 12, "bold"),width=32, height=13, padx=8,pady=20)
        self.txtDisplayR.grid(row=0, column=2)


        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        

        ListOfBooks = ['Software Engineering','Software Quality','Computer Graphics','Computer Fundamental', 'Database System','Operating System','Data Communication',
                       'Artifical Intelligence','Soft Computing','Art of UNIX','Programming With Java','Python Book','Bioinformatics','Anlysis And Design',
                       'Computer Security','Object Technology','Matlab','Internet of Thing','Web design','PC Software','Pattern Of Software','Logical Organisation','Programming In C#']



        def SelectedBook(evt):
            value=str(booklist.get(booklist.curselection()))
            w=value

            if (w == "Software Engineering"):
                BookID.set("ISBN 9870001203708")
                BookTitle.set("Knowledge base")
                Author.set("Nasib Singh Gill")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(800)
                DaysOnLoan.set(14)                 
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Software Quality"):
                BookID.set("ISBN 1200234203409")
                BookTitle.set("Software Quality")
                Author.set("Rajender Singh Chhillar")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(700)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Computer Graphics"):
                BookID.set("ISBN 290505203708")
                BookTitle.set("Programming Book")
                Author.set("James D")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(750)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")                
            elif (w == "Computer Fundamental"):
                BookID.set("ISBN 9870001203708")
                BookTitle.set("Basic Concepts")
                Author.set("Pardeep")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(500)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Database System"):
                BookID.set("ISBN 3260721203708")
                BookTitle.set("Knowledge base")
                Author.set("Korth")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(900)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Operating System"):
                BookID.set("ISBN 9870001319066")
                BookTitle.set("Knowledge Base")
                Author.set("Haldar")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(800)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Data Communication"):
                BookID.set("ISBN 3563991203708")
                BookTitle.set("Greate")
                Author.set("Forouzan")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(700)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Artifical Intelligence"):
                BookID.set("ISBN 9870002888548")
                BookTitle.set("Learning Book")
                Author.set("Ela Kumar")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(500)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Soft Computing"):
                BookID.set("ISBN 3252241203708")
                BookTitle.set("Greate Book")
                Author.set("S N Deepa")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(900)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Art of UNIX"):
                BookID.set("ISBN 1247613234309")
                BookTitle.set("Command base")
                Author.set("Eric Ramand")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(500)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Programming With Java"):
                BookID.set("ISBN 9780071416908")
                BookTitle.set("Programming Book")
                Author.set("E Balagurusamy")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(750)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Python Book"):
                BookID.set("ISBN 9788177002300")
                BookTitle.set("Programming Book")
                Author.set("Sumit Arora")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(600)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Bioinformatics"):
                BookID.set("ISBN 3374051203708")
                BookTitle.set("Bio Book")
                Author.set("Zhumur Ghosh")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(1000)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Computer Security"):
                BookID.set("ISBN 130043603708")
                BookTitle.set("Knowledge base")
                Author.set("Sonka Milan")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(850)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Object Technology"):
                BookID.set("ISBN 9871276453708")
                BookTitle.set("Programming Book")
                Author.set("Ivor Horton")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(800)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Matlab"):
                BookID.set("ISBN 9781118629864")
                BookTitle.set("Knowledge base")
                Author.set("Amos Gilat")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(550)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Anlysis And Design"):
                BookID.set("ISBN 9870001566781")
                BookTitle.set("Algorithms Base")
                Author.set("Udit Agarwal")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(900)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Internet of Thing"):
                BookID.set("ISBN 2137569403708")
                BookTitle.set("Sensor Knowledge")
                Author.set("Koegel")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(600)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Web design"):
                BookID.set("ISBN 9870001203708")
                BookTitle.set("Knowledge base")
                Author.set("Sinclair")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(850)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "PC Software"):
                BookID.set("ISBN 3259013203708")
                BookTitle.set("Knowledge base")
                Author.set("Tosijasu")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(550)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Programming In C#"):
                BookID.set("ISBN 9780070702073")
                BookTitle.set("Programming Book")
                Author.set("E Balagurusamy")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(800)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Pattern Of Software"):
                BookID.set("ISBN 1497510003708")
                BookTitle.set("Pattern Design")
                Author.set("Richard")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(750)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Logical Organisation"):
                BookID.set("ISBN 9872346710708")
                BookTitle.set("Logic Design")
                Author.set("Nasib Singh Gill")

                LateReturnFine.set("1 Rupees Per Day")
                SellingPrice.set(800)
                DaysOnLoan.set(14)               
                
                import datetime
                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            

        booklist= Listbox(DataFrameRIGHT, width=20,height=12,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0, column=0,padx=8)
        scrollbar.config(command=booklist.yview)

        
        for items in ListOfBooks:
            booklist.insert(END,items)

        #=========================Labels==============================================================================#
        self.MType=Label(FrameDetail, font=("arial",10,'bold'), pady=8,padx=12,text="Member Type",)
        self.MType.grid(row=0, column=0)
        self.Rno=Label(FrameDetail, font=("arial",10,'bold'), pady=8,padx=12,text="Reference No.",)
        self.Rno.grid(row=0, column=1)
        self.Name=Label(FrameDetail, font=("arial",10,'bold'), pady=8,padx=12,text="NAME",)
        self.Name.grid(row=0, column=2)
        self.Add=Label(FrameDetail, font=("arial",10,'bold'), pady=8,padx=12,text="Address",)
        self.Add.grid(row=0, column=3)
        self.Mno=Label(FrameDetail, font=("arial",10,'bold'), pady=8,padx=12,text="Mobile Number",)
        self.Mno.grid(row=0, column=4)
        self.Pcode=Label(FrameDetail, font=("arial",10,'bold'), pady=8,padx=12,text="Post Code",)
        self.Pcode.grid(row=0, column=5)
        self.Btitle=Label(FrameDetail, font=("arial",10,'bold'), pady=8,padx=1,text="Book Title",)
        self.Btitle.grid(row=0, column=6)
        self.Dborrowed=Label(FrameDetail, font=("arial",10,'bold'), pady=8,padx=12,text="Date Borrowed",)
        self.Dborrowed.grid(row=0, column=7)
        self.Dol=Label(FrameDetail, font=("arial",10,'bold'), pady=8,padx=12,text="Days on Loan",)
        self.Dol.grid(row=0, column=8)

        self.txtFrameDetail=Text(FrameDetail,font=('arial',12,'bold'),width=50,height=4,padx=2, pady=4)
        self.txtFrameDetail.grid()
        
        #=========================Buttons=============================================================================#        
        self.btnDisplayData=Button(ButtonFrame, text='Display Data', font=('arial',12,'bold'),width=20, bd=4,command=iDisplayData)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnDelete=Button(ButtonFrame, text='Delete', font=('arial',12,'bold'),width=20, bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=2)

        self.btnReset1=Button(ButtonFrame, text='Reset', font=('arial',12,'bold'),width=20, bd=4, command=iReset2)
        self.btnReset1.grid(row=0,column=3)

        self.btnExit1=Button(ButtonFrame, text='Exit', font=('arial',12,'bold'),width=20, bd=4, command=iEliminate)
        self.btnExit1.grid(row=0,column=4)

        self.btnSubmit=Button(ButtonFrame, text='Submit', font=('arial',12,'bold'),width=20, bd=4, command=iReceipt)
        self.btnSubmit.grid(row=0,column=0)



           
        #======================Frames==========================================#
class Db:
    
    def insrtuser(self,title,name,surname,phone,add1,add2,add3,poscode,Bookid,dobo,memtype):
            conn = sqlite3.connect('libr.db')
            conn.execute("INSERT INTO USER(TITLE,NAME,SURNAME,PHONE,ADDRESS1,ADDRESS2,ADDRESS3,POSTCODE,BOOKID,DATEBORROWED,MEMBERTYPE)\
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",self.title,self.name,self.surname,self.phone,self.add1,self.add2,self.add3,self.poscode,self.Bookid,self.dobo,self.memtype)
            conn.commit()
            conn.close()
    def insrbook(self,BookID,BOOKTITLE,Author):
        conn = sqlite3.connect('libr.db')
        conn.execute("INSERT INTO BOOKS(BOOKTITLE,BOOKID,AUTHERNAME,PRICE)\
            VALUES(?,?,?,?)",self.BookID,self.BOOKTITLE,self.Author)
        conn.commit()
        conn.close()
    def insradmin(self,id,admname,admpass):
        conn = sqlite3.connect('libr.db')
        conn.execute("INSERT INTO ADMIN(ID,NAME,PASSWORD)\
            VALUES(?,?,?)",self.id,self.admname,self.admpass)
        conn.commit()
        conn.close()
    def getbook(self):
        conn = sqlite3.connect('libr.db')
        bok=conn.execute("SELECT * FROM BOOKS WHERE BOOKID=?",)
        conn.commit()
        conn.close() 
    def getuser(self,user):
        conn = sqlite3.connect('libr.db')
        usr=conn.execute("SELECT * FROM USER WHERE USERNAME=?",self.user)
        conn.commit()
        conn.close()
    def getadmin(self):
        conn = sqlite3.connect('libr.db')
        global u 
        adm= conn.execute("SELECT PASSWORD FROM ADMIN WHERE NAME=?",(u,)).fetchone()
        conn.commit()
        conn.close()
        #print(adm[0])
        return adm[0]
             
if __name__=="__main__":
    main()