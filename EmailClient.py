from socket import *
from smtplib import SMTP_SSL
from dotenv import load_dotenv
import os
load_dotenv()
mailserver= "smtp.gmail.com" #server host we will be using
serverPort=465 #port the socket uses (think of localhost:5000 when deploying a webapp)
username='acmbyte.ccny@gmail.com' 
password= os.getenv('app_password')#this is the app password, you will have to go to your google account -> security ->2fa -> app passwords to set this up
message_body=input('Enter message:\n')
header= 'Subject: ' + input('Enter subject:\n')
message=f"{header}\n\n{message_body}"
recipient=input('Enter a recipient: \n')
with SMTP_SSL(mailserver, serverPort) as server: #at this point, TCP has been established.
    try:
        server.ehlo() #identifier to esmtp server
        #print(server.verify(mailserver))   
        server.login(username,password) #login handler
        server.sendmail(username,recipient,message)
        server.quit() #close tcp
        print("inshallah we send")
    except:
        print("womp womp")