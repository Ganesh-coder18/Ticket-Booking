import sqlite3
from tkinter import*
import random
import smtplib
from PIL import ImageTk
from tkinter import messagebox


root = Tk()
otp = random.randint(1000, 9999)

ticket_cost = StringVar()
gst_cost = StringVar()
total_cost = StringVar()
Receipt_Ref = StringVar()
Firstname1 = StringVar()
Lastname1 = StringVar()
Age = StringVar()
Address = StringVar()
Mobile_no1 = StringVar()
Pin_code = StringVar()
email_id1 = StringVar()
non_ac = IntVar()
nonac = StringVar()
ac_1 = IntVar()
ac = StringVar()
totalcost = StringVar()
ticketcost = StringVar()
gstcost = StringVar()
x = IntVar()
otp_veri = StringVar()

# ----------------------------------- FIRST PAGE---------------------------------------------------------------------------------

root.title("Registeration window")
root.geometry("1499x800+0+0")
root.resizable(False, False)
bg = ImageTk.PhotoImage(file="24.jpg")
bg_image = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)


#----------------------------------- SECOND PAGE ------------------------------------------------------------------------------


def traindata(args):
    top15=Toplevel()
    top15.title("Train Detail")
    top15.geometry("1499x800+0+0")
    top15.resizable((False, False))

#------------------------------------------------- USER PAGE ----------------------------------------------------------------------------



def user_window():
    top1 = Toplevel()
    top1.title("LOGIN FORM")
    top1.geometry("1499x800+0+0")
    top1.resizable(False, False)
    top1.bg = ImageTk.PhotoImage(file="1.jpg")
    top1.bg_image = Label(top1, image=top1.bg).place(x=0, y=0, relwidth=1, relheight=1)

    user_login = Frame(top1, bg="white")
    user_login.place(x=300, y=150, height=340, width=500)

    title = Label(user_login, text="SIGN UP", font=("Calibri", 35), fg="black", bg="white")
    title.place(x=175, y=10)

    username = StringVar()
    password = StringVar()

    user = Label(user_login, text="Username", font=("Times new roman", 15), fg="black", bg="white")
    user.place(x=50, y=90)
    username = Entry(user_login, font=("Times new roman", 15), bg="white", borderwidth=1, relief=SUNKEN)
    username.place(x=50, y=125, width=350, height=35)

    user1 = Label(user_login, text="Password", font=("Times new roman", 15), fg="black", bg="white")
    user1.place(x=50, y=175)
    password = Entry(user_login, font=("Times new roman", 15), bg="white", borderwidth=1, relief=SUNKEN,show="*")
    password.place(x=50, y=210, width=350, height=35)


    def popup():

        if username.get() == "" or password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=top1)
        else :
            try:
                con = sqlite3.connect("user_registration")
                cur=con.cursor()
                cur.execute('Select * from user_detail where email_id= ? and password= ?',(username.get(),password.get()))
                row=cur.fetchone()
                con.commit()
                con.close()

                print(row)

                if row==None:
                    messagebox.showerror("Error","Invalid Username & password",parent=top1)
                else:
                    messagebox.showinfo("Succesfully", "Welcome", parent=top1)
                    top4=Toplevel()
                    top4.title("TICKET BOOKING")
                    top4.geometry("1499x800+0+0")
                    top4.resizable(False, False)
                    top4.configure(bg="white")
                    top4.bg = ImageTk.PhotoImage(file="19.jpg")
                    top4.bg_image = Label(top4, image=top4.bg).place(x=0, y=0, relwidth=1)

                    top4.train_btn_img = ImageTk.PhotoImage(file="20.jpg")
                    train_btn = Button(top4, command=train_popup, image=top4.train_btn_img, bd=0)
                    train_btn.place(x=90, y=550)

                    top4.bus_btn_img = ImageTk.PhotoImage(file="21.jpg")
                    bus_btn = Button(top4, command=bus_popup, image=top4.bus_btn_img, bd=0)
                    bus_btn.place(x=1100, y=550)

                    top4.airplane_btn_img = PhotoImage(file="23.png")
                    airplane_btn = Button(top4, command=airplane_popup, image=top4.airplane_btn_img, bd=0)
                    airplane_btn.place(x=600, y=550)

            except EXCEPTION as e:
                print(e)


    forget = Button(user_login,command=forgetpass_window, text="Forget Password?", bd=0, bg="white", fg="blue", font=("times new roman", 12))
    forget.place(x=50, y=255)


    login = Button(user_login, command=popup,text="Login", bd=1, bg="white", fg="green",font=("times new roman", 15, "bold"))
    login.place(x=170, y=290, width=150, height=40)

#---------------------------------------------- FOURTH PAGE ------------------------------------------------------------------------------
    def reg_window():
        top2 = Toplevel()
        top2.title("Registeration window")
        top2.geometry("1499x750+0+0")
        top2.resizable(False, False)
        top2.bg = ImageTk.PhotoImage(file="2.jpg")
        top2.bg_image = Label(top2, image=top2.bg).place(x=0, y=0, relwidth=1, relheight=1)
        Frame_register = Frame(top2, bg="white", borderwidth=1, relief=SUNKEN)
        Frame_register.place(x=580, y=200, width=750, height=500)
        title = Label(Frame_register, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white",fg="green")
        title.place(x=50, y=25)

        first_name = StringVar()
        last_name = StringVar()
        contact_no = StringVar()
        email_id = StringVar()
        password = StringVar()
        cpassword = StringVar()

        title = Label(Frame_register, text="First Name", font=("times new roman", 18), bg="white", fg="black")
        title.place(x=50, y=80)
        first_name = Entry(Frame_register, font=("times new roman", 18), bg="white",textvariable=first_name)
        first_name.place(x=50, y=110, width=250)
        title = Label(Frame_register, text="Last Name", font=("times new roman", 18), bg="white", fg="black")
        title.place(x=400, y=80)
        last_name = Entry(Frame_register, font=("times new roman", 18), bg="white",textvariable=last_name)
        last_name.place(x=400, y=110, width=250)
        title = Label(Frame_register, text="Contact No.", font=("times new roman", 18), bg="white", fg="black")
        title.place(x=50, y=160)
        contact_no = Entry(Frame_register, font=("times new roman", 18), bg="white",textvariable=contact_no)
        contact_no.place(x=50, y=190, width=250)
        title = Label(Frame_register, text="Email ID", font=("times new roman", 18), bg="white", fg="black")
        title.place(x=400, y=160)
        email_id = Entry(Frame_register, font=("times new roman", 18), bg="white",textvariable=email_id)
        email_id.place(x=400, y=190, width=250)
        title = Label(Frame_register, text="Password", font=("times new roman", 18), bg="white", fg="black")
        title.place(x=50, y=240)
        password = Entry(Frame_register, font=("times new roman", 18), bg="white",textvariable=password,show="*")
        password.place(x=50, y=270, width=250)
        title = Label(Frame_register, text="Confirm Password", font=("times new roman", 18), bg="white", fg="black")
        title.place(x=400, y=240)
        cpassword = Entry(Frame_register, font=("times new roman", 18), bg="white",textvariable=cpassword,show="*")
        cpassword.place(x=400, y=270, width=250)
        chk = Checkbutton(Frame_register, text="All the informations are right", onvalue=1, offvalue=0,font=("times new roman", 15), bg="white")
        chk.place(x=50, y=325)

        def popup2():


            if first_name.get() == "" or last_name.get() == "" or email_id.get() == "" or contact_no.get()=="" or password.get()=="" or cpassword.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=top2)

            elif password.get() != cpassword.get():
                messagebox.showerror("Error", "password not match", parent=top2)

            else:
                try:

                    firstname = first_name.get()
                    lastname = last_name.get()
                    contact = contact_no.get()
                    email = email_id.get()
                    pass1 = password.get()
                    cpass= cpassword.get()
#-------------------------------------------------------------Code for database-----------------------------------------------------------------------------------------------
                    con = sqlite3.connect("user_registration")
                    cur = con.cursor()
                    cur.execute('Select * from user_detail where email_id=?', (email_id.get(),))
                    row = cur.fetchone()
                    if row != None:
                        messagebox.showerror("Error", "User already exist, please try with another Email", parent=top2)
                    else:
                        cur.execute('insert into user_detail(first_name,last_name,contact_no,email_id,password,cpassword)values(?,?,?,?,?,?)',(firstname, lastname, contact, email, pass1, cpass))
                        con.commit()
                        con.close()
                        messagebox.showinfo("success", "Register successfully", parent=top2)
#------------------------------------------------------------------Code for mail---------------------------------------------------------------------------------------------
                        user_email = "agtravels2021@gmail.com"
                        receiver_email = email_id.get()
                        server = smtplib.SMTP("smtp.gmail.com", 587)

                        server.starttls()

                        server.login(user_email, "ganushinde3")

                        subject = "Regarding your ticket"
                        body = ("SUCCESSFULLY REGISTER")

                        message = "Subject:{}\n\n{}".format(subject, body)

                        server.sendmail(user_email, receiver_email, message)

                        server.quit()
                        top2.destroy()

                except EXCEPTION as e:
                      print(e)

        top2.register_btn_img = ImageTk.PhotoImage(file="3.jpg")
        register_btn = Button(Frame_register,command=popup2,image=top2.register_btn_img,bd=0)
        register_btn.place(x=50, y=390)


    new_reg = Button(user_login, text="New Registration?", command=reg_window, bd=0, bg="white", fg="blue",font=("times new roman", 12))
    new_reg.place(x=330, y=255)


user_btn_img = ImageTk.PhotoImage(file="25.jpg")
user_btn = Button(root, image=user_btn_img,command= user_window,bd=0,bg="white")
user_btn.place(x=595, y=495)

#-------------------------------------------------------INFO PAGE-----------------------------------------------------------------

def info_window():
    import info

info_btn = Button(root,text="Suggested\n Places",bg="black",command=info_window,fg="white",font = ("Bahnschrift SemiBold SemiConden",20,"bold"))
info_btn.place(x=1350,y=10,width=150,height=95)
#---------------------------------------FORGET PASS WINDOW------------------------------------------------------------------



def forgetpass_window():
    top3 = Toplevel()
    top3.title("FORGET PASS WINDOW")
    top3.geometry("1499x800+0+0")
    top3.resizable(False, False)
    top3.bg = ImageTk.PhotoImage(file="10.jpg")
    top3.bg_image = Label(top3, image=top3.bg).place(x=0, y=0, relwidth=1, relheight=1)

    Frame_forget = Frame(top3, bg="white")
    Frame_forget.place(x=300, y=150, height=440, width=500)

    title = Label(Frame_forget, text="FORGET PASSWORD", font=("Calibri", 28), fg="black", bg="white")
    title.place(x=90, y=10)

    username1 = StringVar()
    password1 = StringVar()
    password2 = StringVar()

    fuser = Label(Frame_forget, text="Username", font=("Times new roman", 15), fg="black", bg="white")
    fuser.place(x=50, y=90)
    username1 = Entry(Frame_forget, font=("Times new roman", 15), bg="white", borderwidth=1, relief=SUNKEN)
    username1.place(x=50, y=125, width=350, height=35)

    fuser1 = Label(Frame_forget, text="New Password", font=("Times new roman", 15), fg="black", bg="white")
    fuser1.place(x=50, y=175)
    password1 = Entry(Frame_forget, font=("Times new roman", 15), bg="white", borderwidth=1, relief=SUNKEN,show="*")
    password1.place(x=50, y=210, width=350, height=35)

    fuser2 = Label(Frame_forget, text="Confirm Password", font=("Times new roman", 15), fg="black", bg="white")
    fuser2.place(x=50, y=260)
    password2 = Entry(Frame_forget, font=("Times new roman", 15), bg="white", borderwidth=1, relief=SUNKEN,show="*")
    password2.place(x=50, y=295, width=350, height=35)

    def popup2():

        if username1.get() == "" or password1.get() == "" or password2.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=top3)
        elif password1.get()!= password2.get():
            messagebox.showerror("Error", "Password doensn't match", parent=top3)
        else:
            try:
                con = sqlite3.connect("user_registration")
                cur = con.cursor()
                cur.execute('Update user_detail set password=?,cpassword=? where email_id=?', (password1.get(),password2.get(),username1.get()))
                con.commit()
                con.close()
                messagebox.showinfo("success", "Register successfully", parent=top3)
                top3.destroy()

            except EXCEPTION as e:
                print(e)

    top3.submit_btn_img = ImageTk.PhotoImage(file="12.jpg")
    submit_btn = Button(Frame_forget, image=top3.submit_btn_img,command=popup2, bd=0)
    submit_btn.place(x=140, y=355)

#-------------------------------------------------BUS POPUP WINDOW-------------------------------------------------------------------
def bus_popup():
    import bus


#-------------------------------------------------AIRPLANE POPUP WINDOW--------------------------------------------------------------

def domestic():
    import plane


def international():
    import plane1


def airplane_popup():
    top10=Toplevel()
    top10.geometry("1499x800+0+0")
    top10.bg = ImageTk.PhotoImage(file="45.jpg")
    top10.bg_image = Label(top10, image=top10.bg).place(x=0, y=0, relwidth=1, relheight=1)
    airplane_btn = Button(top10,text="Domestic Flight",command=domestic,bd=5,bg="white",fg="black",font=("times new roman",15,"bold"),relief=RIDGE)
    airplane_btn.place(x=600, y=500,width="180",height="100")
    airplane_btn = Button(top10, text="International Flight",command=international ,bd=5, bg="white", fg="black",font=("times new roman", 15, "bold"), relief=RIDGE)
    airplane_btn.place(x=900, y=500, width="180", height="100")


#------------------------------------------------TRAIN POPUP WINDOW------------------------------------------------------------------

def train_popup():
    import train

#-----------------------------------------------------------------------------------------------------------------------------------
root.mainloop()
