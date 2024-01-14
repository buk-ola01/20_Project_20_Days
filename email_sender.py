from email.message import EmailMessage
from app_passwrod import password
import pandas as pd
import ssl
import smtplib

email_sender = 'jimohsamad2005@gmail.com'
email_password = password

email_receiver = 'jimohab.22@student.funaab.edu.ng'

subject = "200L First Semester Courses"

pd_body = {
    "COURSE CODE" : ["ABE 201", "CVE 201", "ELE 201", "ELE 203", "ELE 291", "MCE 201", "MCE 203", "MCE 205", "MTS 201", "CSC 201", "GNS 201"],
    "COURSE TITLE" : ["Engineering Drawing I", "Engineer in Society", "Applied Electricity I", "Fundamentals of ICT", "Applied Electricity Laboratory I", "Engineeirng Mechanics I", "Engineering Materials", "Fluid Mechanics I", "Mathematical Equations", "Introduction to Computer Science", "Writing and Literary Appreciation"],
    "U" : ["2", "1", "2", "2", "1", "2", "3", "3", "3", "3", "1"],
    "L" : ["1", "1", "2", "1", "-", "2", "2", "2", "2", "2", "1"],
    "T" : ["-", "-", "-", "-", "-", "-", "-", "-", "1", "-", "-"],
    "P" : ["1", "-", "-", "1", "1", "-", "1", "1", "-", "1", "-"]
}
df_body = pd.DataFrame(pd_body)
pd.set_option('display.max_columns', None)
body = str(df_body)


#Create EmailMessage Object
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

#Create a secure connection using SSL
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
