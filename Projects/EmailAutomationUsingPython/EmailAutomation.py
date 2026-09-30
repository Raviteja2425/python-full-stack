#Email Automation using Python
'''
import smtplib
#First we need to connect to gmail server...
server=smtplib.SMTP('smtp.gmail.com',587)
print(server)
server.starttls()
server.login('doddiraviteja79@gmail.com','ekva qigz zyts zwer')
message = "Hello"
server.sendmail('doddiraviteja79@gmail.com',"vanaranjith4@gmail.com",message)
server.quit()
print('mail sent...')


import email
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = MIMEMultipart()
print(msg)
otp=random.randint(1111,9999)
From = "doddiraviteja79@gmail.com"
To="vanaranjith4@gmail.com"
Subject="Email Automation project Using Python"
msg['From']=From
msg['To']=To
msg['Subject']=Subject
body = (f'Prepare well and make sure to present well And Your otp is {otp}')
msg.attach(MIMEText(body))
#Finally we will convert above as string
text = msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('doddiraviteja79@gmail.com','ekva qigz zyts zwer')
server.sendmail(From,To,text)
server.quit()
print('mail sent...')
'''

#Now to extend this we can also send random OTP to users
import email
import smtplib
#MIME--> Multipurpose mail extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import math, random
#as we want to generate random number
msg = MIMEMultipart()
digits = "0123456789"
OTP =""
for i in range(4):
    OTP+=digits[math.floor(random.random()*10)]
    #print(OTP)
From = "doddiraviteja79@gmail.com"
To="vanaranjith4@gmail.com"
Subject="Gmails Two-Step Verfication Code"
msg['From']=From
msg['To']=To
msg['Subject']=Subject
body = (f'Your otp is {OTP}')
msg.attach(MIMEText(body))
#Finally we will convert above as string
text = msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('doddiraviteja79@gmail.com','ekva qigz zyts zwer')
server.sendmail(From,To,text)
user =input("Enter the OTP:")
if user == OTP:
    print("Authorization Success")
else:
    print("Check the OTP again")

