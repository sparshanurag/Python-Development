from email.message import EmailMessage
from cred import password
import ssl 
import smtplib

email_sender = "upes.sparshanurag@gmail.com"
email_password = password

email_receiver = 'sparshanurag@gmail.com'

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
    smtp.sendmail(email_sender, email_receiver, em.as_string())