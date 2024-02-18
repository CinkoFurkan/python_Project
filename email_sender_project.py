""""from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'furkancinko2312@gmail.com'
email_password = 'myBcep-pebtu1-rirzud'
email_receiver = 'yexid16080@newnime.com'

subject = "Don't forget to subscribe"  
body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject  
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_bytes())"""""


height = input("what is your height? ")
weight = input("What is your weight? ")

