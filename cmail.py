import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('narinisumanth@gmail.com','qlyy fujn hoys gpfw')
    msg=EmailMessage()
    msg['FROM']='narinisumanth@gmail.com'
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

