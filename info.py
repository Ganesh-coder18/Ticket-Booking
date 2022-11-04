from tkinter import*
import random
from tkcalendar import *
import smtplib
from PIL import ImageTk
from tkinter import messagebox


top5 = Toplevel()
top5.title("INFO PAGE")
top5.geometry("1472x800+25+0")
top5.resizable(False, False)
top5.configure(bg="white")
main_name = Label(top5, text="BEST PLACES TO VISIT", fg="BLACK", bg="white", font=("Times new roman", 28, "bold"))
main_name.place(x=525, y=0)

top5.bg = ImageTk.PhotoImage(file="26.jpg")
top5.bg_image = Label(top5, image=top5.bg).place(x=5, y=50)
fst_img = Label(top5, text="AGRA", fg="BLACK", bg="white", font=("Times new roman", 20))
fst_img.place(x=95, y=235)

top5.bg1 = ImageTk.PhotoImage(file="27.jpg")
top5.bg_image = Label(top5, image=top5.bg1).place(x=300, y=50)
snd_img = Label(top5, text="LADAKH", fg="BLACK", bg="white", font=("Times new roman", 20))
snd_img.place(x=375, y=235)

top5.bg2 = ImageTk.PhotoImage(file="28.jpg")
top5.bg_image = Label(top5, image=top5.bg2).place(x=595, y=50)
thd_img = Label(top5, text="GOA", fg="BLACK", bg="white", font=("Times new roman", 20))
thd_img.place(x=690, y=235)

top5.bg3 = ImageTk.PhotoImage(file="29.jpg")
top5.bg_image = Label(top5, image=top5.bg3).place(x=890, y=50)
fth_img = Label(top5, text="KERALA", fg="BLACK", bg="white", font=("Times new roman", 20))
fth_img.place(x=980, y=235)

top5.bg4 = ImageTk.PhotoImage(file="30.jpg")
top5.bg_image = Label(top5, image=top5.bg4).place(x=1185, y=50)
ffth_img = Label(top5, text="KASHMIR", fg="BLACK", bg="white", font=("Times new roman", 20))
ffth_img.place(x=1260, y=235)

top5.bg5 = ImageTk.PhotoImage(file="31.jpg")
top5.bg_image = Label(top5, image=top5.bg5).place(x=5, y=275)
sxt_img = Label(top5, text="MAHABALESHWAR", fg="BLACK", bg="white", font=("Times new roman", 20))
sxt_img.place(x=20, y=465)

top5.bg6 = ImageTk.PhotoImage(file="32.jpg")
top5.bg_image = Label(top5, image=top5.bg6).place(x=300, y=275)
svnth_img = Label(top5, text="ITALY", fg="BLACK", bg="white", font=("Times new roman", 20))
svnth_img.place(x=390, y=465)

top5.bg7 = ImageTk.PhotoImage(file="33.jpg")
top5.bg_image = Label(top5, image=top5.bg7).place(x=595, y=275)
eith_img = Label(top5, text="LONDON", fg="BLACK", bg="white", font=("Times new roman", 20))
eith_img.place(x=670, y=465)

top5.bg8 = ImageTk.PhotoImage(file="34.jpg")
top5.bg_image = Label(top5, image=top5.bg8).place(x=890, y=275)
ninth_img = Label(top5, text="NEW YORK", fg="BLACK", bg="white", font=("Times new roman", 20))
ninth_img.place(x=955, y=465)

top5.bg9 = ImageTk.PhotoImage(file="35.jpg")
top5.bg_image = Label(top5, image=top5.bg9).place(x=1185, y=275)
tnth_img = Label(top5, text="PARIS", fg="BLACK", bg="white", font=("Times new roman", 20))
tnth_img.place(x=1285, y=465)

top5.bg10 = ImageTk.PhotoImage(file="36.jpg")
top5.bg_image = Label(top5, image=top5.bg10).place(x=5, y=505)
eleth_img = Label(top5, text="TURKEY", fg="BLACK", bg="white", font=("Times new roman", 20))
eleth_img.place(x=75, y=695)

top5.bg11 = ImageTk.PhotoImage(file="37.jpg")
top5.bg_image = Label(top5, image=top5.bg11).place(x=300, y=505)
tweth_img = Label(top5, text="MALDIVES", fg="BLACK", bg="white", font=("Times new roman", 20))
tweth_img.place(x=365, y=695)

top5.bg12 = ImageTk.PhotoImage(file="38.jpg")
top5.bg_image = Label(top5, image=top5.bg12).place(x=595, y=505)
thrteen_img = Label(top5, text="SINGAPORE", fg="BLACK", bg="white", font=("Times new roman", 20))
thrteen_img.place(x=650, y=695)

top5.bg13 = ImageTk.PhotoImage(file="39.jpg")
top5.bg_image = Label(top5, image=top5.bg13).place(x=890, y=505)
frteen_img = Label(top5, text="MAURITIUS", fg="BLACK", bg="white", font=("Times new roman", 20))
frteen_img.place(x=950, y=695)

top5.bg14 = ImageTk.PhotoImage(file="40.jpg")
top5.bg_image = Label(top5, image=top5.bg14).place(x=1185, y=505)
tweth_img = Label(top5, text="EUROPE", fg="BLACK", bg="white", font=("Times new roman", 20))
tweth_img.place(x=1260, y=695)
