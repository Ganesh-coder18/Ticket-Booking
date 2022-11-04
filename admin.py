#def admin_window():
 #   top = Toplevel()
  #  top.title("LOGIN FORM")
   # top.geometry("1499x800+0+0")
    #top.resizable(False, False)
   # top.bg = ImageTk.PhotoImage(file="1.jpg")
   # top.bg_image = Label(top, image=top.bg).place(x=0, y=0, relwidth=1, relheight=1)

    #admin_login = Frame(top, bg="white")
    #admin_login.place(x=300, y=150, height=340, width=500)

   # title = Label(admin_login, text="SIGN UP", font=("Calibri", 35), fg="black", bg="white")
   # title.place(x=175, y=10)

    #username = StringVar()
    #password = StringVar()

    #user = Label(admin_login, text="Username", font=("Times new roman", 15), fg="black", bg="white")
    #user.place(x=50, y=90)
    #username = Entry(admin_login, font=("Times new roman", 15), bg="white", borderwidth=1, relief=SUNKEN)
    #sername.place(x=50, y=125, width=350, height=35)

   # user1 = Label(admin_login, text="Password", font=("Times new roman", 15), fg="black", bg="white")
    #user1.place(x=50, y=175)
    #password = Entry(admin_login, font=("Times new roman", 15), bg="white", borderwidth=1, relief=SUNKEN)
   # password.place(x=50, y=210, width=350, height=35)

    #def popup():

     #   if username.get() == "" or password.get() == "":
      #      messagebox.showerror("Error", "All fields are required",parent=top)
       # elif password.get() == "Admin" or username.get() == "Ganesh":
        #    messagebox.showinfo("Welcome", "LOGIN SUSCESSFULLY",parent=top)
         #   top4 = Toplevel()
          #  top4.title("TICKET BOOKING")
           # top4.geometry("1499x800+0+0")
           # top4.resizable(False, False)
            #top4.configure(bg="white")
           # top4.bg = ImageTk.PhotoImage(file="19.jpg")
           #top4.bg_image = Label(top4, image=top4.bg).place(x=0, y=0, relwidth=1)

          #  top4.train_btn_img = ImageTk.PhotoImage(file="20.jpg")
           # train_btn = Button(top4,command=traindata ,image=top4.train_btn_img, bd=0)
            #train_btn.place(x=90, y=550)

           # top4.bus_btn_img = ImageTk.PhotoImage(file="21.jpg")
           # bus_btn = Button(top4, image=top4.bus_btn_img, bd=0)
           # bus_btn.place(x=1100, y=550)

            #top4.airplane_btn_img = PhotoImage(file="23.png")
            #airplane_btn = Button(top4,  image=top4.airplane_btn_img, bd=0)
            #airplane_btn.place(x=600, y=550)


        #else:
         #   messagebox.showerror("Error", "Invalid Username/password",parent=top)



    #login = Button(admin_login,command=popup ,text="Login", bd=1, bg="white", fg="green", font=("times new roman", 15, "bold"))
    #login.place(x=170, y=290, width=150, height=40)

#admin_btn_img = ImageTk.PhotoImage(file="41.jpg")
#admin_btn = Button(root, image=admin_btn_img,command= admin_window,bd=0,bg="gray")
#admin_btn.place(x=5, y=10)
