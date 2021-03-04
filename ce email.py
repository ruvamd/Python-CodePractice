from email.message import EmailMessage
message=EmailMessage()

sender='ruvamd@gmail.com'
recipient='ruvamd@gmail.com'

message['From']=sender
message['To']=recipient
message['Subject']=f'greetings from {sender} to {recipient}'
body="hey,I'm learning to send emails"
message.set_content(body)
#attachment
import os.path 
attachment_path='/Users/vadim/Documents/Programming languages/Python/ca.png'
attachment_filename=os.path.basename(attachment_path)
import mimetypes
mime_type,_=mimetypes.guess_type(attachment_path)
mime_type,mime_subtype=mime_type.split('/',1)

print(mime_type)
print(mime_subtype)

with open(attachment_path,'rb') as ap:
    message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
#send throught smtp
import smtplib
import getpass

mail_server=smtplib.SMTP_SSL('smtp.google.com')
mail_server.set_debuglevel(1)
mail_pass=getpass.getpass('Password? ')
mail_server.login(sender,mail_pass)
mail_server.send_message(message)
{}
mail_server.quit()
print(message)