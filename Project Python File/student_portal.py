##                           STUDENT PORTAL CODE............


import tkinter as tk                   #tkinter module for GUI
from firebase import firebase            ### For online data storing
from tkinter import messagebox          ## For POP-UP message
from datetime import datetime                ## For working on dates
from datetime import timedelta                       ## For Arthematic Operations on days
class student_port:                            # Name of class
    def __init__(self):                         # Class Constructor
        self.admin_no=""                        # Admission Number
        self.total_book=""
        self.book_issued=""
        self.book_returned=""
        self.ph=""
        self.fine=0
        self.f_name=""
        self.name=""
        self.like=[]
        self.email=""
    def main(self):
        global ent_1                           ## Define Global so that it can easily be used in other class members
        global ent_2
        global win                               ## It is the window object decleared global to easliy destroy in other function 
        win=tk.Tk()
        win.title("STUDENT LOGIN")
        win.geometry("500x200")
        tk.Label(win,text="XYZ ENGINEERING COLLEGE").grid(row=0,column=0)
        tk.Label(win,text="GHAZIABAD\n").grid(row=1,column=0)
        tk.Label(win,text="ADMISSION NUMER::").grid(row=2,column=0)
        ent_1=tk.Entry(win)
        ent_1.grid(row=2,column=1)
        tk.Label(win,text="PASSWORD::").grid(row=3,column=0)
        ent_2=tk.Entry(win,show="*")
        ent_2.grid(row=3,column=1)
        tk.Button(win,text="Log IN",command=self.enter).grid(row=4,column=2)
        tk.Label(win,text="\n Default Password has been sent on your mail!!",fg="green").grid(row=5,column=0)
        win.mainloop()
    def enter(self):
        try:
            self.admin_no=ent_1.get()
            conn=firebase.FirebaseApplication("https://library-9cf92.firebaseio.com/",None)                ## Setup Connection with online database i.e., firebase
            a=conn.get(ent_1.get()+"/",None)                                  ## Fetching data from firebase for particular user
            b=list(a.keys())                                ## It returns a json file so to extract key
            self.key=b[0]
        except:
            self.key=""                                   ## if there is no user with such admission number
        if(self.key==""):
            messagebox.showinfo("ERROR!!","YOU are not registered OUR Check your Internet Connection")
            
        else:
            self.admin_no=ent_1.get()
            password=conn.get("/"+self.admin_no+"/"+self.key+"/PASSWORD",None)              ## Fettching the password of that particular admission number
            if(password==ent_2.get()):
                fbconn=firebase.FirebaseApplication("https://library-9cf92.firebaseio.com/",None)          ## Connecting with database of students
                mydata=fbconn.get("/"+self.admin_no,None)                #get whole json file of that particular admission number
                info=mydata[self.key]                    ##Passing the unique key set by firebase
                self.total_book=info["TOTAL BOOK ISSUED"]               ###Fetching all the data in different variables
                self.book_issued=info["BOOK PRESENT"]
                self.book_returned=info["BOOK RETURNED"]
                self.ph=info['PHONE NUMBER']
                self.fine=info['FINE']
                self.f_name=info['FATHER NAME']
                self.name=info['NAME']
                self.like=info["LIKE"]
                self.email=info['EMAIL']
                win.destroy()                 ##Removing the main login window
                global win1                   ## Again declaring the variable for the tkinter window
                win1=tk.Tk()
                win1.title("WELCOME")                                #Tile of the window
                tk.Label(win1,text="PERSONAL DETAILS::\n").grid(row=0,column=0)             ## Displaying the static info of the student
                tk.Label(win1,text="NAME::"+self.name).grid(row=1,column=0)
                tk.Label(win1,text="FATHER'S NAME::"+self.f_name).grid(row=1,column=1)
                tk.Label(win1,text="PHONE No. ::"+self.ph).grid(row=1,column=2)
                tk.Label(win1,text="EMAIL ::"+self.email+"\n").grid(row=2,column=1)
                tk.Button(win1,text="TOTAL BOOK ISSUED",command=self.total).grid(row=3,column=0)             ## Button to show the total book issued by the student till date
                tk.Button(win1,text="BOOK PRESENT",command=self.present).grid(row=3,column=1)               ## Button to show how many books are with the student
                tk.Button(win1,text="BOOK RETURNED",command=self.returned).grid(row=3,column=2)            ##Butthon to show how many books have bben returned by the student 
                tk.Label(win1,text="\n").grid(row=4,column=0)
                tk.Button(win1,text="NOTIFICATION",command=self.notification).grid(row=5,column=0)                   ##Notting in this button for future use
                tk.Button(win1,text="FIELD OF INTEREST",command=self.like).grid(row=5,column=1)             ##Notting in this button for future use
                tk.Button(win1,text="CHANGE PASSWORD",command=self.password).grid(row=5,column=2)                 ## Change the default password provided by library
                tk.Label(win1,text="\n").grid(row=6,column=0)
                tk.Button(win1,text="SWAP BOOK TO FRIEND",command=self.friend).grid(row=7,column=0)                  ##Notting in this button for future use
                tk.Label(win1,text="\n").grid(row=8,column=0)
            else:
                messagebox.showinfo("PASSWORD ERROR!!","Please Enter Correct Password")                           # Pop-up mas if user enter wrong password
    def total(self):
        fbcon1=firebase.FirebaseApplication("https://book-a0103.firebaseio.com/",None)                       ##Setting a connection with the college book database
        def quitt():                                                       ## Function to quit the total book window
            win2.destroy()
        win2=tk.Tk()                            ##Object of the window for adding widgets
        win2.title("Total Book Issued")                                    ## Title of the window
        count=0                             # # For grid of the tkinter window
        if(len(self.total_book)>1):                             ##Traversing in the list
            l=len(self.total_book)
            tk.Label(win2,text="BOOK  NAME ").grid(row=0,column=0)                  #title
            tk.Label(win2,text=" AUTHOR  NAME ").grid(row=0,column=1)
            tk.Label(win2,text=" PUBLICATION  NAME").grid(row=0,column=2)
            tk.Label(win2,text=" ISSUE DATE").grid(row=0,column=3)
            for i in range(1,l,2):                              #for taking one book at a time
                count+=1
                get=fbcon1.get("/"+self.total_book[i],None)
                b=list(get.keys())[0]
                bname=get[b]["NAME"]                 #Book name
                aname=get[b]["AUTHOR NAME"]                    #Author Name
                pname=get[b]["PUBLICATION NAME"]                                        #Publication name
                tk.Label(win2,text=bname).grid(row=count,column=0)
                tk.Label(win2,text=aname).grid(row=count,column=1)
                tk.Label(win2,text=pname).grid(row=count,column=2)
                tk.Label(win2,text="  "+self.total_book[i+1]+"\t").grid(row=count,column=3)                          ##Issue date of the book
        else:
            tk.Label(win2,text="SORRY NO BOOK").grid(row=0,column=1)                     #if the total book list is empty
        
        tk.Button(win2,text="CLOSE",command=quitt).grid(row=count+1,column=1)                  ##TO close the issue window
    def present(self):                                   ##Function to show the book present with the student
        fbcon1=firebase.FirebaseApplication("https://book-a0103.firebaseio.com/",None)                    ##Setting up conncetion with the library book data
        win3=tk.Tk()
        win3.title("Present Book")
        count=0
        if(len(self.book_issued)>1):
            l=len(self.book_issued)
            tk.Label(win3,text="BOOK  NAME ").grid(row=0,column=0)
            tk.Label(win3,text=" AUTHOR  NAME ").grid(row=0,column=1)
            tk.Label(win3,text=" PUBLICATION  NAME ").grid(row=0,column=2)
            tk.Label(win3,text=" ISSUE DATE ").grid(row=0,column=3)
            tk.Label(win3,text="RETURN DATE").grid(row=0,column=4)
            for i in range(1,l,2):
                count+=1
                get=fbcon1.get("/"+self.book_issued[i],None)
                b=list(get.keys())[0]
                bname=get[b]["NAME"]
                aname=get[b]["AUTHOR NAME"]
                pname=get[b]["PUBLICATION NAME"]
                tk.Label(win3,text=bname).grid(row=count,column=0)
                tk.Label(win3,text=aname).grid(row=count,column=1)
                tk.Label(win3,text=pname).grid(row=count,column=2)
                tk.Label(win3,text="  "+self.book_issued[i+1]+"\t").grid(row=count,column=3)
                date=datetime.strptime(self.book_issued[i+1],'%Y-%m-%d %H:%M:%S')+timedelta(days=7)                     #it is used to calculate the return date of the book
                tk.Label(win3,text=date).grid(row=count,column=4)
        else:
            tk.Label(win3,text="SORRY NO BOOK").grid(row=0,column=1)
        def quitt():
            win3.destroy()
        tk.Button(win3,text="CLOSE",command=quitt).grid(row=count+1,column=3)
        
    def returned(self):
        fbcon1=firebase.FirebaseApplication("https://book-a0103.firebaseio.com/",None)
        win4=tk.Tk()
        win4.title("Returned Books")
        count=0
        if(len(self.book_returned)>1):
            l=len(self.book_returned)
            tk.Label(win4,text="BOOK  NAME ").grid(row=0,column=0)
            tk.Label(win4,text=" AUTHOR  NAME ").grid(row=0,column=1)
            tk.Label(win4,text=" PUBLICATION  NAME ").grid(row=0,column=2)
            tk.Label(win4,text=" ISSUE DATE ").grid(row=0,column=3)
            tk.Label(win4,text=" RETURN DATE ").grid(row=0,column=4)
            
            for i in range(1,l,3):
                count+=1
                get=fbcon1.get("/"+self.book_returned[i],None)
                b=list(get.keys())[0]
                bname=get[b]["NAME"]
                aname=get[b]["AUTHOR NAME"]
                pname=get[b]["PUBLICATION NAME"]
                tk.Label(win4,text=bname).grid(row=count,column=0)
                tk.Label(win4,text=aname).grid(row=count,column=1)
                tk.Label(win4,text=pname).grid(row=count,column=2)
                tk.Label(win4,text="  "+self.book_returned[i+1]+"\t").grid(row=count,column=3)
                tk.Label(win4,text=self.book_returned[i+2]).grid(row=count,column=4)
        else:
            tk.Label(win4,text="SORRY NO BOOK").grid(row=0,column=0)
        def quitt():
            win4.destroy()
        tk.Button(win4,text="CLOSE",command=quitt).grid(row=count+1,column=1)
        
    def notification(self):
        pass
    def like(self):
        pass
    def friend(self):
        pass
    def password(self):                        ##Function to change the password
        def change():                           #Function to call when submit button is clicked
            fbconn=firebase.FirebaseApplication("https://library-9cf92.firebaseio.com/",None)                    ## Connecting with the student database
            password=fbconn.get("/"+self.admin_no+"/"+self.key+"/PASSWORD",None)                       ## geting present password of the user
            if(password==ent_pp.get()):                                        ##checking the password
                fbconn.put("/"+self.admin_no+"/"+self.key,"PASSWORD",ent_np.get())                                                         ##changing the the user password
                messagebox.showinfo("PASSWORD!!","PASSWORD CHANGED")                                                                         #+ve pop-up msg
                win_pass.destroy()
            else:
                messagebox.showinfo("PASSWORD ERROR!!","Please Enter Correct Password")                    ## -ve pop-up msg
        win_pass=tk.Tk()
        win_pass.title("CHANGE PASSWORD")
        tk.Label(win_pass,text="Enter Previous Password::",fg="red").grid(row=1,column=0)
        ent_pp=tk.Entry(win_pass,show="*")
        ent_pp.grid(row=1,column=1)
        tk.Label(win_pass,text="Enter New Password::",fg="green").grid(row=2,column=0)
        ent_np=tk.Entry(win_pass,show="*")
        ent_np.grid(row=2,column=1)
        tk.Label(win_pass,text="\n4 SHOULD BE MINIMUM LENGTH OF PASSWORD",fg="red").grid(row=3,column=0)
        tk.Button(win_pass,text="SUBMIT",command=change).grid(row=4,column=1)
a=student_port(                )## declaring the object for the class
a.main()                               ## Calling class member named"main"
