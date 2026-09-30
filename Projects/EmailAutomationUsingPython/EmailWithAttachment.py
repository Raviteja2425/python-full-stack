"""
import email
import smtplib
#MIME--> Multipurpose mail extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Now to add attachment
from email.mime.base import MIMEBase
from email import encoders
attach = "5th WEEK Report - WORISGO_ BE WB Internship.pdf"
msg = MIMEMultipart()
From = "doddiraviteja79@gmail.com"
To="vanaranjith4@gmail.com"
Subject="WEEK-5 Attachment"
msg['From']=From
msg['To']=To
msg['Subject']=Subject
body = ("This is my Week 5 Report of my Internship")
msg.attach(MIMEText(body))
#Finally we will convert above as string
text = msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('doddiraviteja79@gmail.com','ekva qigz zyts zwer')
server.sendmail(From,To,text)
server.quit()
print('mail sent.....')
"""

import email
import smtplib

# MIME --> Multipurpose Internet Mail Extensions
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# For attachment
from email.mime.base import MIMEBase
from email import encoders

# PDF file path
attach = "5th WEEK Report - WORISGO_ BE WB Internship.pdf"

# Create email
msg = MIMEMultipart()

From = "doddiraviteja79@gmail.com"
To = "vanaranjith4@gmail.com"
Subject = "WEEK-5 Attachment"

msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject

# Email body
body = "This is my Week 5 Report of my Internship"

msg.attach(MIMEText(body, 'plain'))

with open(attach, "rb") as file:

    attachment = MIMEBase("application", "pdf")

    attachment.set_payload(file.read())

# Encode the attachment
encoders.encode_base64(attachment)

# Add attachment filename
attachment.add_header(
    "Content-Disposition",
    f"attachment; filename=\"{attach}\""
)

# Attach PDF to email
msg.attach(attachment)

# Convert email to string
text = msg.as_string()

# Connect to Gmail
server = smtplib.SMTP("smtp.gmail.com", 587)

# Secure connection
server.starttls()

# Login
server.login(
    "doddiraviteja79@gmail.com",
    "ekva qigz zyts zwer"
)

# Send email
server.sendmail(From, To, text)

# Close connection
server.quit()

print("Mail sent successfully with attachment.....")
