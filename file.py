import sqlite3
from tkinter import*
try:
    con = sqlite3.connect("user_registration")
    cur = con.cursor()
    cur.execute('Select * from user_bus_detail where email_id=?',('gs8783007@gmail.com',))
    row = cur.fetchall()
    con.commit()
    con.close()
    for a in row:
        bill=a[0]
        seat=a[1]
        busno=a[2]
        date=a[3]
        time=a[4]
        fname=a[5]
        lname=a[6]
        mob=a[10]
        source=a[12]
        destinaton=a[13]
        type=a[14]
        total=a[15]

    f = open("3.txt", "w+")
    f.write("=====================================================\n")
    f.write('Reciept no:'+str(bill))
    f.write('\nSeat No: '+str(seat))
    f.write('\nBus No: '+str(busno))
    f.write('\nTravel Date: '+str(date))
    f.write('\nTravel Time: '+str(time))
    f.write('\nName: '+str(fname)+" "+str(lname))
    f.write('\nMobile No: '+str(mob))
    f.write('\nSource: '+str(source))
    f.write('\nDestination: '+str(destinaton))
    f.write('\nBus Type: '+str(type))
    f.write('\nTotal Paid Amount: '+str(total))
    f.write("\n=====================================================")
    f.close()
except Exception as e:
    print(e)

