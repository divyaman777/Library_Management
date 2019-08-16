### LIBRARY PORTAL CODE.................


import tkinter as tk                                                              #importing tkinter library used for GUI as tk
from tkinter import messagebox                                      ###For Pop-up message for errors
import pickle                                                                      ## for handling Binary files
import sqlite3 as sql                                                          #Creating database 
from firebase import firebase                                           #Creating online databse
import smtplib, ssl                                                             ##Online E-mail Service
from datetime import datetime                                         # For Date and time
class lib_login:                                                                   #create a class for the first log_in of the Librarian
    
    def __init__(self):                                                            #lib_login class constructor
        self.win=""                                                                    # class variable to create main window 
        self.user_name=""                                                      # for librarian user_name
        self.password=""                                                         # for librarian password 
        self.name=" "                                                               #student name
        self.f_name=" "                                                            # student father name
        self.ph_no=0                                                                # student phone number
        self.ad_no=" "                                                              #student admission number
        self.std_mail=" "                                                           #student email
        self.ad_no_list=[]                                                         # student list containing all student admission number
        try:                                                                                # for exception handling in opening the binary file
            fr=open("pass_dict.dat","rb")                                   # open a binary file having dictonary of user_name and password
            self.password_dict=pickle.load(fr)                          ## this dictonary contains the password for librarians
            fr.close()                                                                    # closing the above open file to avoid accidental damage to file
            fr1=open("usr_set.dat","rb")                                     # open a binary file having list of user_name
            self.user_set=pickle.load(fr1)                                  ## This list contains list of librarians
            fr1.close()                                                                  # closing the above opened file
        except:                                                                           # for exception handling in opening the binary files
            self.password_dict={}                                              ## this dictonary contains the password for librarians
            self.user_set=set()                                                   ## This set contains list of librarians

         
    def view(self):                                                                   # main function i.e., the first function which will be called
        global ent1                                                                    # ent1 is global so that it can be used in other function for comparison
        global ent2                                                                    # ent1 is global so that it can be used in other function for comparison
        self.win=tk.Tk()                                                              # Created the window
        self.win.title("WELCOME")                                           # title for the main window
        self.win.geometry("400x190")                                      #setting the geometry of the login window
        tk.Label(self.win,text="WELCOME").grid(row=0,column=1)                        ###  simple text
        tk.Label(self.win,text="XYZ ENGINEERING COLLEGE").grid(row=1,column=1)               ###  simple text
        tk.Label(self.win,text="LOGIN PORTAL FOR LIBRARIAN\n\n").grid(row=2,column=1)      ### simple text
        tk.Label(self.win,text="USER NAME:::").grid(row=5,column=0)         ###  simple text
        tk.Label(self.win,text="PASSWORD:::").grid(row=6,column=0)       ###   simple text
        ent1=tk.Entry(self.win)                                           ### Entry for enter username
        ent1.grid(row=5,column=3)                                   # setting position of the entry widget
        ent2=tk.Entry(self.win,show="*")                          ### Entry for enter password 
        ent2.grid(row=6,column=3)                                  # This is in Next line bcz grid returns none 
        tk.Button(self.win,text="LOG IN",command=self.check).grid(row=7,column=1)              ##  Button for login
        tk.Button(self.win,text="NEW LIBRARIAN..REGISTER NOW!!",command=self.new_reg).grid(row=8,column=1)   ## To add a librarian
        self.win.mainloop()                                                          ## TO hold the tkinter window on screen
    def check(self):                                                                   # This function is called when login button is clicked
        self.user_name=ent1.get()                                            # get function is used to import user name form the gui entry box
        self.password=ent2.get()                                              # get function is used to import password form the gui entry box
        if(self.user_name=="" or self.password==""):             # this condition to check all field should are filled
            messagebox.showinfo("ERROR!!","All Fields Are Mandatory")           #   Error message box
        elif(self.user_name not in self.user_set):                                                   ### This condition to check both username is correct
            messagebox.showinfo("ERROR!!","This User Does Not Exists!!!")                     #   Error message box
        elif(self.password != self.password_dict[self.user_name]):                            ### this condition to check if username is correct and password is wrong
            messagebox.showinfo("PASSWORD ERROR!!","Please Enter Correct Password")            #   Error message box
        else:                                                                               ## if all the entries are correct
            self.win.destroy()                                          ## Remove the previous window
            self.main()                               ##  Calling main fxn  
    def new_reg(self):
        global ent3                                                                 ##   declaring these gloal so that all these can be used in other class members
        global ent4
        global ent5
        global ent6
        global ent7
        global ent8
        global ent9
        global ent_re
        self.win.destroy()                                                               ## Closing very first window
        global win1                                                                        # so that second window can be closed in other fxn
        win1=tk.Tk()                                                                      # WINDOW FOR librarian registration
        win1.title("NEW LIBRARIAN")                                        # title of the librarian registration window
        win1.geometry("700x200")                                             ## Setting geometry
        tk.Label(win1,text="\nXYZ ENGINEERING COLLEGE").grid(row=0,column=1)
        tk.Label(win1,text="Fill The Below Registeration Form\n").grid(row=1,column=1)
        tk.Label(win1,text="NAME  ").grid(row=2,column=0)
        tk.Label(win1,text="Reg.Number  ").grid(row=3,column=0)
        tk.Label(win1,text="Date Of Joining  (dd/mm/yyyy) ").grid(row=4,column=0)
        tk.Label(win1,text="Phone Number  ").grid(row=5,column=0)
        tk.Label(win1,text="E-Mail  ").grid(row=2,column=2)
        tk.Label(win1,text="User_Name  ").grid(row=3,column=2)
        tk.Label(win1,text="Password  ",).grid(row=4,column=2)
        tk.Label(win1,text="Renter Password  ").grid(row=5,column=2)
        ent3=tk.Entry(win1)
        ent3.grid(row=2,column=1)
        ent4=tk.Entry(win1)
        ent4.grid(row=3,column=1)
        ent5=tk.Entry(win1)
        ent5.grid(row=4,column=1)
        ent6=tk.Entry(win1)
        ent6.grid(row=5,column=1)
        ent7=tk.Entry(win1)
        ent7.grid(row=2,column=3)
        ent8=tk.Entry(win1)
        ent8.grid(row=3,column=3)
        ent9=tk.Entry(win1,show="*")
        ent9.grid(row=4,column=3)
        ent_re=tk.Entry(win1,show="*")
        ent_re.grid(row=5,column=3)
        
        tk.Button(win1,text="SUBMIT AND CREATE ACCOUNT",command=self.add_usr,fg="green").grid(row=6,column=2)
        
    
        win1.mainloop()
    def add_usr(self):
        name=ent3.get()
        reg=ent4.get()
        doj=ent5.get()
        ph_no=ent6.get()
        e_mail=ent7.get()
        usr=ent8.get()
        pas=ent9.get()
        re_pas=ent_re.get()
        if(name=="" or reg=="" or doj=="" or ph_no=="" or e_mail=="" or usr=="" or pas==""):                 #this condition to check all field should are filled
            messagebox.showinfo("ERROR!!","All Fields Are Mandatory")
        elif(usr in self.user_set):                                        ##Every Username sholud be unique
            messagebox.showinfo("ERROR!!","This User_Name ALL ready exist please try some other User_Name")
        elif(pas!=re_pas):                                                      ## To confirm the password
            messagebox.showinfo("ERROR!!","BOTH PASSWORD DOES NOT MATCH")

        else:
            win1.destroy()
            import smtp_try as smtp                           ## Self made py file for OTP/Email
            otp=smtp.otp_fire(e_mail)                               ##Get otp
            def check():
                pin=ent10.get()
                if(otp==pin):
                    win2.destroy()
                    self.user_set.add(usr)
                    self.password_dict[usr]=pas
                    fw=open("pass_dict.dat","wb")
                    pickle.dump(self.password_dict,fw)
                    fw.close()
                    fw1=open("usr_set.dat","wb")
                    pickle.dump(self.user_set,fw1)
                    fw1.close()
                    
                    global db
                    db=sql.connect('college.db')
                    cnn=db.cursor()
                    cmd='CREATE TABLE IF NOT EXISTS librarians(name TEXT,registration_no TEXT,date_of_join TEXT,phone INTEGER,email TEXT,user_name TEXT,password TEXT)'
                    cnn.execute(cmd)
                    cnn.execute('INSERT INTO librarians(name,registration_no,date_of_join,phone,email,user_name,password)VALUES (?,?,?,?,?,?,?)',(name,reg,doj,ph_no,e_mail,usr,pas))
                    var=cnn.execute("SELECT * FROM librarians")
                    db.commit()
                else:
                    messagebox.showinfo("ERROR!!","WRONG PIN ..PLEASE TRY AGAIN")
                    win2.destroy()
                    self.new_reg()

            win2=tk.Tk()
            tk.Label(win2,text="ENTER OTP SENT ON YOUR REGISTERED MAIL::::").grid(row=0,column=0)
            ent10=tk.Entry(win2)
            ent10.grid(row=1,column=0)
            tk.Label(win2,text="NOTE:::PLEASE ENTER OTP SENT ON YOUR EMAIL ADDRESS").grid(row=2,column=0)
            tk.Label(win2,text="NOTE::::SOMETIMES OTP IS PRESENT IN SPAM FOLDER",fg="red").grid(row=3,column=0)
            tk.Button(win2,text="SUBMIT",fg="green",command=check).grid(row=4,column=0)
            win2.mainloop()
    def inva(self):
        self.name=b1.get()
        self.f_name=b2.get()
        self.ph_no=b3.get()
        self.ad_no=b4.get()
        self.std_mail=b5.get()
        std_conn=firebase.FirebaseApplication("https://library-9cf92.firebaseio.com/",None)
        a=std_conn.get("/",None)
        self.ad_no_list=list(a.keys())
        if(self.name=="" or self.f_name=="" or self.ph_no==0 or self.ad_no=="" or self.std_mail==""):
            messagebox.showinfo("ERROR!!","All Fields Are Mandatory")
        if(self.ad_no in self.ad_no_list):
            messagebox.showinfo("ERROR!!","This Admission Number Already Exists!!!")
        else:
            try:
                fbconn=firebase.FirebaseApplication("https://library-9cf92.firebaseio.com/",None)
                data_to_upload={
                "NAME":self.name,
                "FATHER NAME":self.f_name,
                "PHONE NUMBER":self.ph_no,
                "EMAIL":self.std_mail,
                "TOTAL BOOK ISSUED":[" "],
                "BOOK RETURNED":[" "],
                "BOOK PRESENT":[" "],
                "FINE":0,
                "LIKE":[" "],
                "PASSWORD":self.ad_no
                }
                key=fbconn.post("/"+self.ad_no,data_to_upload)
                ## port for ssl port=587
                msg1="""hello {},
                            your Default Password is Your Admission Number
                            For Security Purpose Please Change it....
                                Link For Direct Download Of Student Appliation:::<https://drive.google.com/uc?id=1XzwNsSDZ2hFOFdIIsSiPOp5PcZr_a8hv&export=download> 
                                
                                Google Drive Link

                                Link To Download Student Application
                                https://drive.google.com/open?id=1XzwNsSDZ2hFOFdIIsSiPOp5PcZr_a8hv"""
                cont=ssl.create_default_context()
                with smtplib.SMTP("smtp.gmail.com",587) as server:
                    server.ehlo()
                    server.starttls(context=cont)
                    server.ehlo()
                    server.login("EMAIL","PASSWORD")
                    server.sendmail("EMAIL",self.std_mail,msg1.format(self.name))
                messagebox.showinfo("DONE!!","STUDENT ADDED")
                window1.destroy()
            except:
                window1.destroy()
                messagebox.showinfo("ERROR!!","ERROR OCCURED TRY AGAIN")
                
    
    def inp(self):
        
        global b1
        global b2
        global b3
        global b4
        global b5
        global window1
        window1=tk.Tk()

        tk.Label(window1,text='REGISTER NOW!!').grid(row=0,column=1)
        tk.Label(window1,text='NAME').grid(row=1)
        tk.Label(window1,text="FATHER'S NAME").grid(row=2)
        tk.Label(window1,text='PHONE NUMBER').grid(row=3)
        tk.Label(window1,text='ADMISSION NUMBER').grid(row=4)
        tk.Label(window1,text='E_MAIL').grid(row=5)
        b1=tk.Entry(window1)
        b2=tk.Entry(window1)
        b3=tk.Entry(window1)
        b4=tk.Entry(window1)
        b5=tk.Entry(window1)
        b1.grid(row=1,column=2)
        b2.grid(row=2,column=2)
        b3.grid(row=3,column=2)
        b4.grid(row=4,column=2)
        b5.grid(row=5,column=2)
        btn=tk.Button(window1,text='SUBMIT',command=self.inva)
        btn.grid(row=6,column=1)
        window1.mainloop()
    def ret(self):
        def returnn():
            def proceed():
                try:
                    fbconn1.delete(student_key+"/BOOK PRESENT/",str(index))
                    fbconn1.delete(student_key+"/BOOK PRESENT/",str(index+1))
                    book_returned1=fbconn1.get(student_key+"/BOOK RETURNED/",None)
                    book_returned=[bid,date,present_date]
                    fbconn1.put(student_key,"BOOK RETURNED",book_returned1+book_returned)
                    win_fine.destroy()
                    win_ret.destroy()
                    messagebox.showinfo("DONE!!","BOOK RETURNED !!")
                except:
                     messagebox.showinfo("ERROR!!","TRY AGAIN !!")
            adno=ent_sid.get()
            bid=ent_bid.get()
            try:
                conn=firebase.FirebaseApplication("https://library-9cf92.firebaseio.com/",None)         ## Setup Connection with online database i.e., firebase
                a=conn.get(adno+"/",None)                 ## Fetching data from firebase for particular user
                b=list(a.keys())                                        ## It returns a json file so to extract key
                student_key=b[0]
                fbconn1=firebase.FirebaseApplication("https://library-9cf92.firebaseio.com/"+adno+"/",None)
                book_present=fbconn1.get(student_key+"/BOOK PRESENT/",None)
                if(len(book_present)==None):
                    messagebox.showinfo("ERROR!!","YOU HAVE NO BOOK ISSUED !!")
                else:
                    if(bid not in book_present):
                        messagebox.showinfo("ERROR!!","YOU DON'T HAVE THIS BOOK !!")
                    else:
                        index=book_present.index(bid)
                        i_date=book_present[index+1]
                        date=datetime.strptime(i_date,'%Y-%m-%d %H:%M:%S')
                        present_date=datetime.now()
                        days=(present_date-date).days
                        if(days>7):
                            fine=(days-7)*5
                        else:
                            fine=0
                        win_fine=tk.Tk()
                        win_fine.title('FINE')
                        fbconn=firebase.FirebaseApplication("https://book-a0103.firebaseio.com/",None)
                        a=fbconn.get(bid+"/",None)                        ## Fetching data from firebase for particular book
                        b=list(a.keys())                                        ## It returns a json file so to extract key
                        book_key=b[0]
                        book_info=fbconn.get(bid+"/"+book_key+"/",None)
                        tk.Label(win_fine,text="NOTE::BOOK WAS ISSUED FOR 7 DAYS ONLY \n A FINE OF Rs. 5/day IS CHARED").grid(row=0,column=0)
                        tk.Label(win_fine,text="BOOK NAME:: "+book_info["NAME"]).grid(row=1,column=0)
                        tk.Label(win_fine,text="AUTHOR NAME:: "+book_info["AUTHOR NAME"]).grid(row=2,column=0)
                        tk.Label(win_fine,text="PUBLICATION  NAME:: "+book_info["PUBLICATION NAME"]).grid(row=3,column=0)
                        tk.Label(win_fine,text="ISSUE DATE:: "+str(date)).grid(row=4,column=0)
                        tk.Label(win_fine,text="NOTE:\nRECEIVE A FINE OF  Rs."+str(fine)+"\t",fg="red").grid(row=5,column=1)
                        tk.Label(win_fine,text="PAYTM NUMBER FOR FINE PAYMENT::8755066033",fg="green").grid(row=6,column=0)
                        tk.Button(win_fine,text="FINE RECEIVED",command=proceed,fg="green").grid(row=7,column=1)
                        win_fine.mainloop()
            except:
                messagebox.showinfo("ERROR!!","YOU ARE NOT A REGISTERED STUDENT\n OR Check Your Internet Connection!!")
                        
        win_ret=tk.Tk()
        win_ret.title("RETURN PORTAL")
        win_ret.geometry("350x120")
        tk.Label(win_ret,text="BOOK RETURN PORTAL").grid(row=0,column=1)
        tk.Label(win_ret,text="STUDENT ADMISSION No. ::").grid(row=1,column=0)
        ent_sid=tk.Entry(win_ret)
        ent_sid.grid(row=1,column=1)
        tk.Label(win_ret,text="UNIQUE BOOK Id.  ::").grid(row=2,column=0)
        ent_bid=tk.Entry(win_ret)
        ent_bid.grid(row=2,column=1)
        tk.Button(win_ret,text="RETURN",command=returnn,fg="green").grid(row=3,column=2)
        win_ret.mainloop()
    def iss(self):
        def add():
            adno=ent_sid.get()
            bid=ent_bid.get()
            try:
                conn=firebase.FirebaseApplication("https://library-9cf92.firebaseio.com/",None)                    ## Setup Connection with online database i.e., firebase
                a=conn.get(adno+"/",None)                          ## Fetching data from firebase for particular user
                b=list(a.keys())                                                    ## It returns a json file so to extract key
                student_key=b[0]
                conn1=firebase.FirebaseApplication("https://book-a0103.firebaseio.com/",None)                     ## Setup Connection with online database i.e., firebase
                a=conn1.get("/",None)                                     ## Fetching data from firebase for particular user
                total_book=list(a.keys())                                        ## It returns a json file so to extract key
                if(bid in total_book):
                    issue_dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    total_book_issued1=[bid,issue_dt]
                    book_present1=[bid,issue_dt]
                    total_book_issued=conn.get("/"+adno+"/"+student_key+"/TOTAL BOOK ISSUED/",None)
                    book_present=conn.get("/"+adno+"/"+student_key+"/BOOK PRESENT/",None)
                    if(type(total_book_issued)!=list or type(book_present)!=list):
                        try:
                            conn.put(adno+"/"+student_key,"TOTAL BOOK ISSUED",total_book_issued1)
                            conn.put(adno+"/"+student_key,"BOOK PRESENT",book_present1)
                            messagebox.showinfo("DONE!!","BOOK ISSUED \n BOOK IS ISSUED FOR 7 DAYS\n AFTER 7 DAYS A FINE OF Rs. 5 WILL BE CHARGED!!")
                            win_iss.destroy()
                        except:
                            messagebox.showinfo("ERROR!!","ERROR OCCURED TRY AGAIN !!")
                    else:
                        if(bid in book_present):
                            messagebox.showinfo("ERROR!!","YOU ALREADY HAVE THIS BOOK !!")
                        else:
                            try:
                                conn.put("/"+adno+"/"+student_key,"TOTAL BOOK ISSUED",total_book_issued+total_book_issued1)
                                conn.put("/"+adno+"/"+student_key,"BOOK PRESENT",book_present+book_present1)
                                win_iss.destroy()
                                messagebox.showinfo("DONE!!","BOOK ISSUED !!")
                            except:
                                messagebox.showinfo("ERROR!!","ERROR OCCURED TRY AGAIN !!")
                else:
                    messagebox.showinfo("ERROR!!","THERE IS NO SUCH BOOK IN LIBRARY")

            except:
                messagebox.showinfo("ERROR!!","YOU are not registered OUR Check your Internet Connection")
                
                    
                
        win_iss=tk.Tk()
        win_iss.title("ISSUE BOOK")
        win_iss.geometry("350x120")
        tk.Label(win_iss,text="BOOK ISSUE PORTAL\n").grid(row=0,column=1)
        tk.Label(win_iss,text="STUDENT ADMISSION No. ::").grid(row=1,column=0)
        ent_sid=tk.Entry(win_iss)
        ent_sid.grid(row=1,column=1)
        tk.Label(win_iss,text="UNIQUE BOOK Id.  ::").grid(row=2,column=0)
        ent_bid=tk.Entry(win_iss)
        ent_bid.grid(row=2,column=1)
        tk.Button(win_iss,text="ISSUE",command=add,fg="green").grid(row=3,column=2)
        win_iss.mainloop()
    def main(self):
        import sqlite3 as sql;
        db=sql.connect(r"college.db")
        c=db.cursor()
        temp_name=c.execute("SELECT name FROM librarians WHERE user_name IS ? ",(self.user_name,))
        name=temp_name.fetchall()[0][0]
        temp_phone=c.execute("SELECT phone FROM librarians WHERE user_name IS ? ",(self.user_name,))
        phone=temp_phone.fetchall()[0][0]
        temp_email=c.execute("SELECT email FROM librarians WHERE user_name IS ? ",(self.user_name,))
        email=temp_email.fetchall()[0][0]
        temp_usr_name=c.execute("SELECT user_name FROM librarians WHERE user_name IS ? ",(self.user_name,))
        usr_name=temp_usr_name.fetchall()[0][0]
        temp_reg=c.execute("SELECT registration_no FROM librarians WHERE user_name IS ? ",(self.user_name,))
        reg=temp_reg.fetchall()[0][0]
        win=tk.Tk()
        win.geometry("580x270")
        tk.Label(win,text='XYZ COLLEGE,GZB').grid(row=0,column=1)
        tk.Label(win,text='WELCOME!!').grid(row=1,column=1)
        tk.Label(win,text='CURRENT LIBRARIAN NAME    ::::     '+name).grid(row=2,column=0)
        tk.Label(win,text='REGISTRATION No.      ::::    '+reg).grid(row=3,column=0)
        tk.Label(win,text='PHONE No.     ::::     '+str(phone)).grid(row=4,column=0)
        tk.Label(win,text='E_MAIL     :::     '+email).grid(row=5,column=0)
        tk.Label(win,text='CURRENT LIBRARIAN USER_NAME     :::::       '+usr_name+"\n\n").grid(row=6,column=0)
        btn=tk.Button(win,text="ADD NEW STUDENT",command=self.inp).grid(row=7,column=1)
        tk.Label(win,text='\n').grid(row=8,column=0)
        btn=tk.Button(win,text="ADD BOOK",command=self.lib_book).grid(row=9,column=0)
        btn=tk.Button(win,text="RETURN BOOK",command=self.ret).grid(row=9,column=1)
        btn=tk.Button(win,text="ISSUE BOOK",command=self.iss).grid(row=9,column=2)
        
        win.mainloop()
    def msg(self):
        showinfo("Window","All Fields Are Mandatory")
    def lib_book(self):
        def add_fxn():
                bname=ent_bname.get()
                aname=ent_aname.get()
                pname=ent_pname.get()
                dname=ent_dname.get()
                tname=ent_tname.get()
                price=ent_price.get()
                if(bname=="" or aname=="" or pname=="" or dname=="" or tname=="" or price==""):
                    messagebox.showinfo("ERROR!!","All Fields Are Mandatory")
                else:
                    try:
                        fbconn=firebase.FirebaseApplication("https://book-a0103.firebaseio.com/",None)
                        data_to_upload={
                        "NAME":bname,
                        "AUTHOR NAME":aname,
                        "PUBLICATION NAME":pname,
                        "DEPARTMENT":dname,
                        "TOPIC":tname,
                        "PRICE":price,
                        }
                        key=fbconn.post("/"+dt_str,data_to_upload)
                        messagebox.showinfo("DONE!!","BOOK ADDED \n Special Book ID is {} \n paste it on the book".format(dt_str))
                        win_b.destroy()
                    except:
                        messagebox.showinfo("ERROR!!","All Fields Are Mandatory")
                        
        dt=datetime.now()
        dt_str=dt.strftime("%Y%m%d%H%M%S")
        win_b=tk.Tk(className="lib")                           #GUI WINDOW FOR BOOK MANAGEMENT
        tk.Label(win_b,text="ENTER BOOK NAME  ::  ").grid(row=1,column=0)
        ent_bname=tk.Entry(win_b)
        ent_bname.grid(row=1,column=1)
        tk.Label(win_b,text="ENTER AUTHOR NAME  :: ").grid(row=2,column=0)
        ent_aname=tk.Entry(win_b)
        ent_aname.grid(row=2,column=1)
        tk.Label(win_b,text="ENTER PUBLICATION NAME  ::  ").grid(row=3,column=0)
        ent_pname=tk.Entry(win_b)
        ent_pname.grid(row=3,column=1)
        tk.Label(win_b,text=" ENTER DEPARTMENT  :::  ").grid(row=4,column=0)
        ent_dname=tk.Entry(win_b)
        ent_dname.grid(row=4,column=1)
        tk.Label(win_b,text=" ENTER SPECIFIC TOPIC :::  ").grid(row=5,column=0)
        ent_tname=tk.Entry(win_b)
        ent_tname.grid(row=5,column=1)
        tk.Label(win_b,text=" PRICE      :::  ").grid(row=6,column=0)
        ent_price=tk.Entry(win_b)
        ent_price.grid(row=6,column=1)
        btn=tk.Button(win_b,text="ADD",command=add_fxn).grid()
        win_b.mainloop
              
a=lib_login()
a.view()

###CREATED BY DIVYAMAN TYAGI AND KUSH JINDAL
