import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

user_email = "agtravels2021@gmail.com"
receiver_email = "abhishekjadhav364@gmail.com"
subject = 'Regarding your ticket'
msg=MIMEMultipart()
msg['From'] = user_email
msg['To'] = receiver_email
msg['Subject'] = subject

body = 'YOUR TICKET BOOK SUCCESSFULLY'
msg.attach(MIMEText(body,'plain'))

filename='1.pdf'
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)

text=msg.as_string()
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user_email, "ganushinde3")


server.sendmail(user_email,receiver_email,text)

server.quit()

print("done")
