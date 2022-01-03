import smtplib
import getpass

mail_server=smtplib.SMTP_SSL('smtp.google.com')
mail_server.set_debuglevel(1)
mail_pass=getpass.getpass('Password? ')
mail_server.login(sender,mail_pass)

print(mail_pass)