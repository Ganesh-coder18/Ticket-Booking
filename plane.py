from calendar import calendar
from tkinter import*
from tkcalendar import *
from tkinter import ttk
import random
import time;
import datetime
import smtplib
otp = random.randint(1000, 9999)
from PIL import ImageTk
from tkinter import messagebox
top6 = Toplevel()
top6.geometry("350x400")
top6.title("BUS BOOKING WINDOW")
top6.geometry("1499x800+0+0")
top6.resizable(False, False)
top6.configure(bg="black")
customer_details_frame=Frame(top6,bd=5,relief=SUNKEN)
customer_details_frame.configure(bg="white")
customer_details_frame.place(x=0,y=100,height=700,width=1499)
maintitle=Label(top6,text="FLIGHT BOOKING",font=("times new roman",35,"bold"),fg="white",bg="black")
maintitle.place(x=600,y=15)


#-------------------------------------------Define------------------------------------------
ticket_cost=StringVar()
gst_cost=StringVar()
total_cost=StringVar()
Receipt_Ref=StringVar()
Firstname1=StringVar()
Lastname1=StringVar()
Age=StringVar()
Address=StringVar()
Mobile_no1=StringVar()
Pin_code=StringVar()
email_id1=StringVar()
non_ac=IntVar()
nonac=StringVar()
ac_1=IntVar()
ac=StringVar()
totalcost=StringVar()
ticketcost=StringVar()
gstcost=StringVar()
x=IntVar()
otp_veri=StringVar()





customer_name = LabelFrame(customer_details_frame,bd=2, font=("Times new roman", 15,"bold"),text='Customer Detail',relief=RIDGE)
customer_name.configure(bg="white")
customer_name.place(x=0,y=0,height=550,width=500)

travel_detail = LabelFrame(customer_details_frame,bd=2, font=("Times new roman", 15,"bold"),text='Travel Details',relief=RIDGE)
travel_detail.configure(bg="white")
travel_detail.place(x=500,y=0,height=550,width=500)

receipt_detail = LabelFrame(customer_details_frame,bd=2, font=("Times new roman", 15,"bold"),text='Reciept Details',relief=RIDGE)
receipt_detail.configure(bg="white")
receipt_detail.place(x=1000,y=0,height=550,width=480)

button_detail = LabelFrame(customer_details_frame,bd=2, font=("Times new roman", 15,"bold"),relief=RIDGE)
button_detail.configure(bg="white")
button_detail.place(x=1000,y=550,height=140,width=480)

cost_detail = LabelFrame(customer_details_frame,bd=2, font=("Times new roman", 15,"bold"),relief=RIDGE)
cost_detail.configure(bg="white")
cost_detail.place(x=500,y=550,height=140,width=500)

acnonac_detail= LabelFrame(customer_details_frame,bd=2,text="Class Cost",font=("Times new roman", 15,"bold"),relief=RIDGE)
acnonac_detail.configure(bg="white")
acnonac_detail.place(x=0,y=550,height=140,width=500)


#----------------------------------------------- Customer_detail frame-----------------------------------------------------------
title1 = Label(customer_name, text="First Name", font=("times new roman", 18) ,fg="black",bg="white")
title1.place(x=0, y=10)
first_name = Entry(customer_name, font=("times new roman", 18),bd=5,relief=RIDGE,textvariable=Firstname1)
first_name.place(x=130, y=10, width=350)

title2 = Label(customer_name, text="Last Name", font=("times new roman", 18) ,fg="black",bg="white")
title2.place(x=0, y=65)
last_name = Entry(customer_name, font=("times new roman", 18),bd=5,relief=RIDGE,textvariable=Lastname1)
last_name.place(x=130, y=65, width=350)

title3 = Label(customer_name, text="Gender", font=("times new roman", 18) ,fg="black",bg="white")
title3.place(x=0, y=120)
list_gender=["Male","Female","other"]
menu_head = StringVar()
menu_head.set("--select your gender--")
gender_menu=OptionMenu(customer_name,menu_head,*list_gender)
gender_menu.configure(bg="white",bd=5,relief=RIDGE)
gender_menu.place(x=130, y=120, width=170)

title4 = Label(customer_name, text="Age", font=("times new roman", 18) ,fg="black",bg="white")
title4.place(x=0, y=175)
age = Entry(customer_name, font=("times new roman", 18),bd=5,relief=RIDGE,textvariable=Age)
age.place(x=130, y=175, width=350)

title5 = Label(customer_name, text="Address", font=("times new roman", 18) ,fg="black",bg="white")
title5.place(x=0, y=230)
address = Entry(customer_name, font=("times new roman", 18),bd=5,relief=RIDGE,textvariable=Address)
address.place(x=130, y=230, width=350)

title6 = Label(customer_name, text="Pin Code", font=("times new roman", 18) ,fg="black",bg="white")
title6.place(x=0, y=285)
pin_code = Entry(customer_name, font=("times new roman", 18),bd=5,relief=RIDGE,textvariable=Pin_code)
pin_code.place(x=130, y=285, width=350)

title7 = Label(customer_name, text="Mobile No", font=("times new roman", 18) ,fg="black",bg="white")
title7.place(x=0, y=340)
mobile_no = Entry(customer_name, font=("times new roman", 18),bd=5,relief=RIDGE,textvariable=Mobile_no1)
mobile_no.place(x=130, y=340, width=350)

title8 = Label(customer_name, text="Email", font=("times new roman", 18) ,fg="black",bg="white")
title8.place(x=0, y=395)
email_id = Entry(customer_name, font=("times new roman", 18),bd=5,relief=RIDGE,textvariable=email_id1)
email_id.place(x=130, y=395, width=350)

#---------------------------------------------- Travel_detail frame----------------------------------------------------------------------------

title9 = Label(travel_detail, text="Source", font=("times new roman", 18) ,fg="black",bg="white")
title9.place(x=5, y=10)
list_source=["MUMBAI"]
menu_head1 = StringVar()
menu_head1.set("--select--")
source_menu=OptionMenu(travel_detail,menu_head1,*list_source)
source_menu.configure(bg="white",bd=2,relief=RIDGE)
source_menu.place(x=130, y=10, width=200)

title10 = Label(travel_detail, text="Destination", font=("times new roman", 18) ,fg="black",bg="white")
title10.place(x=5, y=65)
list_destination=["Goa"]
menu_head2 = StringVar()
menu_head2.set("--select--")
destination_menu=OptionMenu(travel_detail,menu_head2,*list_destination)
destination_menu.configure(bg="white",bd=2,relief=RIDGE)
destination_menu.place(x=130, y=65, width=200)

title11 = Label(travel_detail, text="Flight Type", font=("times new roman", 18) ,fg="black",bg="white")
title11.place(x=5, y=120)
list_bus=["Economy Class","Buisness Class"]
menu_head3 = StringVar()
menu_head3.set("--select--")
bus_menu=OptionMenu(travel_detail,menu_head3,*list_bus)
bus_menu.configure(bg="white",bd=2,relief=RIDGE)
bus_menu.place(x=130, y=120, width=200)

title_plane = Label(travel_detail, text="Flight Time", font=("times new roman", 18) ,fg="black",bg="white")
title_plane.place(x=5, y=478)
list_source=["2:00AM"]
menu_head5 = StringVar()
menu_head5.set("--select--")
source_menu=OptionMenu(travel_detail,menu_head5,*list_source)
source_menu.configure(bg="white",bd=2,relief=RIDGE)
source_menu.place(x=130, y=478, width=200)


date=StringVar()
title12 = Label(travel_detail, text="Date", font=("times new roman", 18) ,fg="black",bg="white")
title12.place(x=5, y=180)
cal = Calendar(travel_detail,selectmode="day", day=15,moth=5,year=2020)
cal.place(x=130, y=250)
def select_date():
    date.configure(text=cal.get_date())

cal_but = Button(travel_detail, text="OK",command=select_date)
cal_but.place(x=230,y=435,width=50)
date = Label(travel_detail, font=("times new roman", 18),bd=5,bg="white",relief=RIDGE,text="")
date.place(x=130, y=180, width=200)

#------------------------------------------------------Ac/nonAc--------------------------------------------------------------------------------------

def NONAC():
    global paid1
    if(non_ac.get()==1):
        nonac_entry.configure(state=NORMAL)
        price1=float(20)

        nonac.set("₹" + str(price1))
        paid1=nonac.get()
        nonac.set("₹" + str(price1))
    elif non_ac.get() == 0:
        nonac_entry.configure(state=DISABLED)
        nonac.set("0")

nonac_chk=Checkbutton(acnonac_detail,text="Economy",variable=non_ac,onvalue=1,offvalue=0,command=NONAC,bg="white",font=("times new roman",18))
nonac_chk.place(x=5,y=10)
nonac_entry=Entry(acnonac_detail,font=("times new roman",15,"bold"),textvariable=nonac,bg="white",bd=5,relief=RIDGE,state=DISABLED,width=20)
nonac_entry.place(x=150,y=10)


def AC():
    global paid2
    if (ac_1.get() == 1):
        ac_entry.configure(state=NORMAL)
        price2 = float(50)

        ac.set("₹" + str(price2))
        paid2 = ac.get()
        ac.set("₹" + str(price2))
    elif ac_1.get() == 0:
        ac_entry.configure(state=DISABLED)
        ac.set("0")


ac_chk=Checkbutton(acnonac_detail,text="Business",variable=ac_1,onvalue=1,command=AC,offvalue=0,bg="white",font=("times new roman",18))
ac_chk.place(x=5,y=50)
ac_entry=Entry(acnonac_detail,font=("times new roman",15,"bold"),textvariable=ac,bg="white",bd=5,relief=RIDGE,state=DISABLED,width=20)
ac_entry.place(x=150,y=50)

#---------------------------------------------------Reciept Frame-------------------------------------------------------------------------
txt_receipt=Text(receipt_detail,width=47,height=21,font=("times new roman",15,"bold"))
txt_receipt.place(x=0,y=5)
#---------------------------------------------------Button Franme-------------------------------------------------------------------------


def Total():
    if(menu_head1.get()==""):

        if(menu_head2.get()=="THANE"):
            if(non_ac.get()==1):
                x=float(20)
                q1=float(200)
                q2=float(6.5)

                total=x+q1+q2

                total1="Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif(ac_1.get()==1):
                x = float(50)
                q1 = float(200)
                q2 = float(6.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")


        elif (menu_head2.get()=="CST"):
            if (non_ac.get() == 1):
                x = float(20)
                q1 = float(340)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(340)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="PANVEL"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(160)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(160)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="PUNE"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(580)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)

             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(580)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

    elif (menu_head1.get()=="THANE"):

        if (menu_head2.get()=="KALYAN"):

            if(non_ac.get()==1):
                x=float(20)
                q1=float(200)
                q2=float(6.5)

                total=x+q1+q2

                total1="Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif(ac_1.get()==1):
                x = float(50)
                q1 = float(200)
                q2 = float(6.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="CST"):
            if (non_ac.get() == 1):
                x = float(20)
                q1 = float(240)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(240)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="PANVEL"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(200)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(200)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="PUNE"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(650)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)

             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(650)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

    elif (menu_head1.get()=="CST"):

        if(menu_head2.get()=="THANE"):
            if(non_ac.get()==1):
                x=float(20)
                q1=float(240)
                q2=float(6.5)

                total=x+q1+q2

                total1="Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif(ac_1.get()==1):
                x = float(50)
                q1 = float(240)
                q2 = float(6.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="KALYAN"):
            if (non_ac.get() == 1):
                x = float(20)
                q1 = float(340)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(340)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="PANVEL"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(300)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(300)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="PUNE"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(700)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)

             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(700)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

    elif (menu_head1.get()=="PANVEL"):

        if(menu_head2.get()=="THANE"):
            if(non_ac.get()==1):
                x=float(20)
                q1=float(200)
                q2=float(6.5)

                total=x+q1+q2

                total1="Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif(ac_1.get()==1):
                x = float(50)
                q1 = float(200)
                q2 = float(6.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="CST"):
            if (non_ac.get() == 1):
                x = float(20)
                q1 = float(300)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(300)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="KALYAN"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(160)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(160)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="PUNE"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(480)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)

             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(480)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

    elif (menu_head1.get()=="PUNE"):

        if(menu_head2.get()=="THANE"):
            if(non_ac.get()==1):
                x=float(20)
                q1=float(650)
                q2=float(6.5)

                total=x+q1+q2

                total1="Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif(ac_1.get()==1):
                x = float(50)
                q1 = float(650)
                q2 = float(6.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="CST"):
            if (non_ac.get() == 1):
                x = float(20)
                q1 = float(700)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(700)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
            else:
                messagebox.showerror("ERROR","Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="PANVEL"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(480)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(480)
                q2 = float(5.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

        elif (menu_head2.get()=="KALYAN"):
             if (non_ac.get() == 1):
                x = float(20)
                q1 = float(580)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)

             elif (ac_1.get() == 1):
                x = float(50)
                q1 = float(580)
                q2 = float(9.5)

                total = x + q1 + q2

                total1 = "Rs." + str(round(total))

                ticketcost.set(q1)
                gstcost.set(q2)
                totalcost.set(total1)
             else:
                 messagebox.showerror("ERROR", "Please fill AC/NON AC cost details")

total_btn=Button(button_detail,font=("times new roman",18,"bold"),width=7,bd=5,text="TOTAL",command=Total)
total_btn.place(x=0,y=0)


def reset():
    Firstname1.set("")
    Lastname1 .set("")
    Age.set("")
    Address.set("")
    Mobile_no1.set("")
    Pin_code.set("")
    email_id1.set("")
    menu_head.set("--select your gender--")
    menu_head1.set("--select--")
    menu_head2.set("--select--")
    menu_head3.set("--select--")
    ticketcost.set(0)
    gstcost.set(0)
    totalcost.set(0)



reset_btn=Button(button_detail,font=("times new roman",18,"bold"),command=reset,width=8,bd=5,text="RESET")
reset_btn.place(x=115,y=0)


def Receipt():
    txt_receipt.delete("1.0",END)
    x=random.randint(10853,500831)
    randomRef=str(x)
    y=random.randint(1,60)
    randomRef1=str(y)
    z=random.randint(1100,1200)
    randomRef2=str(z)
    Receipt_Ref.set("Travel Bill: " + randomRef)
    txt_receipt.insert(END,'Receipt Ref:\t\t\t' + Receipt_Ref.get() + "\n")
    txt_receipt.insert(END, 'Seat No:\t\t\t' + randomRef1 + "\n")
    txt_receipt.insert(END, 'Flight No:\t\t\t' + randomRef2 + "\n")
    txt_receipt.insert(END, 'Date:\t\t\t' + cal.get_date() + "\n")
    txt_receipt.insert(END, 'Departure Time:\t\t\t' + menu_head5.get() + "\n")
    txt_receipt.insert(END, 'First Name:\t\t\t' + Firstname1.get() + "\n")
    txt_receipt.insert(END, 'Last Name:\t\t\t' + Lastname1.get() + "\n")
    txt_receipt.insert(END, 'Gender:\t\t\t' + menu_head.get() + "\n")
    txt_receipt.insert(END, 'Address:\t\t\t' + Address.get() + "\n")
    txt_receipt.insert(END, 'Pin code:\t\t\t' + Pin_code.get() + "\n")
    txt_receipt.insert(END, 'Mobile No:\t\t\t' + Mobile_no1.get() + "\n")
    txt_receipt.insert(END, 'Email Id:\t\t\t' + email_id1.get()+ "\n")
    txt_receipt.insert(END, 'Source:\t\t\t' + menu_head1.get() + "\n")
    txt_receipt.insert(END, 'Destination:\t\t\t' + menu_head2.get() + "\n")
    txt_receipt.insert(END, 'Flight type:\t\t\t' + menu_head3.get() + "\n")
    if (ac_1.get() == 1):
        txt_receipt.insert(END, 'Business class:\t\t\t' + ac.get() + "\n")
    elif (non_ac.get()==1):
        txt_receipt.insert(END, 'Economy class:\t\t\t' + nonac.get() + "\n")
    txt_receipt.insert(END, '==========================================',"\n")
    txt_receipt.insert(END, 'Ticket cost:\t\t\t' + ticketcost.get() + "\n")
    txt_receipt.insert(END, 'Gst cost:\t\t\t' + gstcost.get() + "\n")
    txt_receipt.insert(END, 'Total cost:\t\t\t' + totalcost.get() + "\n")
    txt_receipt.insert(END, '==========================================',"\n")



receipt_btn=Button(button_detail,font=("times new roman",18,"bold"),width=8,bd=5,text="RECEIPT",command=Receipt)
receipt_btn.place(x=245,y=0)


def exit():
    top6.destroy()

exit_btn=Button(button_detail,font=("times new roman",18,"bold"),command=exit,width=6,bd=5,text="EXIT")
exit_btn.place(x=375,y=0)




def submit():
    top9 = Toplevel()
    top9.title("PAYMENT IMAGE")
    top9.geometry("550x700+450+50")
    top9.configure(bg="white")
    top9.resizable(False, False)
    head = Label(top9, text="PAYMENT DETAIL", font=("times new roman", 20, "bold"), bg="white", fg="red")
    head.place(x=160, y=5)
    top9.bg = ImageTk.PhotoImage(file="pay4.jpg")
    top9.bg_image = Label(top9, image=top9.bg, bg="white").place(x=140, y=70)
    final_amt = Text(top9, width=20, height=1, font=("times new roman", 15, "bold"))
    final_amt.place(x=180, y=400)
    final_amt.delete("1.0", END)
    final_amt.insert(END, 'Amount to pay:\t' + totalcost.get() + "\n")
    otp_veri1 = Label(top9, text="OTP VERIFICATION", font=("times new roman", 18, "bold"), bg="white", fg="red")
    otp_veri1.place(x=180, y=440)
    otp_veri2 = Entry(top9, font=("times new roman", 18, "bold"), textvariable=otp_veri, bd=5, width=10,relief=RIDGE)
    otp_veri2.place(x=225, y=480)

    def getotp():
        user_email = "agtravels2021@gmail.com"
        receiver_email = email_id.get()
        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(user_email, "ganushinde3")

        subject = "Regarding your ticket"
        body = ("Yours OTP:")

        message = "Subject:{}\n\n{}\n{}".format(subject, body, otp)

        server.sendmail(user_email, receiver_email, message)

        server.quit()

    get_otp = Button(top9, font=("times new roman", 18, "bold"), command=getotp, width=12, bd=3, text="GET OTP",bg="white")
    get_otp.place(x=100, y=530)

    def resendotp():
        user_email = "agtravels2021@gmail.com"
        receiver_email = email_id.get()
        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(user_email, "ganushinde3")

        subject = "Regarding your ticket"
        body = ("Yours OTP:")

        message = "Subject:{}\n\n{}\n{}".format(subject, body, otp)

        server.sendmail(user_email, receiver_email, message)

        server.quit()

    verify_otp = Button(top9, font=("times new roman", 18, "bold"), width=12, bd=3, command=resendotp,text="RESEND OTP", bg="white")
    verify_otp.place(x=300, y=530)

    def submit1():
        if (otp_veri.get() == str(otp)):
            messagebox.showinfo("Welcome", "Otp verify", parent=top9)
            user_email = "agtravels2021@gmail.com"
            receiver_email = email_id.get()
            server = smtplib.SMTP("smtp.gmail.com", 587)

            server.starttls()

            server.login(user_email, "ganushinde3")

            subject = "Regarding your ticket"
            body = ("YOUR TICKET BOOK SUCCESSFULLY")

            message = "Subject:{}\n\n{}".format(subject, body)

            server.sendmail(user_email, receiver_email, message)

            server.quit()


        else:
            print("Invalid")
            messagebox.showerror("Error", "Invalid otp", parent=top9)

    submit_btn = Button(top9, font=("times new roman", 18, "bold"), bg="lightgreen", command=submit1, width=10, bd=5,text="SUBMIT")
    submit_btn.place(x=215, y=600)


submit_btn=Button(button_detail,font=("times new roman",18,"bold"),bg="lightgreen",command=submit,width=10,bd=5,text="SUBMIT")
submit_btn.place(x=160,y=60)

#--------------------------------------------------Cost Frame------------------------------------------------------------------------------
tc_lable=Label(cost_detail,font=("times new roman",18),text="Ticket Cost",fg="black",bg="white")
tc_lable.place(x=0,y=5)
tc_entry=Entry(cost_detail,font=("times new roman",18,"bold"),bd=5,width=20,textvariable=ticketcost,relief=RIDGE,justify=RIGHT)
tc_entry.place(x=150,y=5)

gst_lable=Label(cost_detail,font=("times new roman",18),text="GST Cost",fg="black",bg="white")
gst_lable.place(x=0,y=50)
gst_entry=Entry(cost_detail,font=("times new roman",18,"bold"),bd=5,width=20,textvariable=gstcost,relief=RIDGE,justify=RIGHT)
gst_entry.place(x=150,y=50)

total_lable=Label(cost_detail,font=("times new roman",18),text="Total Cost",fg="black",bg="white")
total_lable.place(x=0,y=95)
total_entry=Entry(cost_detail,font=("times new roman",18,"bold"),bd=5,width=20,textvariable=totalcost,relief=RIDGE,justify=RIGHT)
total_entry.place(x=150,y=95)

#top6.mainloop()

