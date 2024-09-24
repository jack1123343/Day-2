import yagmail
import os
from dotenv import load

load()

sender = "nadexvenomplays@gmail.com"
receiver = "m0bujuj1pyw3@10mail.xyz"
subject = 'Test Mail Using Python'
contents = 'Test Mailsufhdsfskjh'

yag = yagmail.SMTP(user = sender, password = os.getenv('PASSWORD'))
yag.send(to = receiver, subject = subject, contents = contents)
print("Email Sent")