from email.mime.text import MIMEText
from email.mime.text import MIMEText
import smtplib

host="smtp.gmail.com"
port=587
username="ruvamd@gmail.com"
password="na244311571naga"
from_email=username
to_list=["ruvamd@gmail.com"]

email_conn=smtplib.SMTP(host,port)
email_conn.echo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(from_email,to_list,"<b>hello</b><br/>there this is an email message")
email_conn.quit()

the_msg=MIMEMultipart("alternative")
the_msg['Subject']="Hello there!"
the_msg["From"]=from_email
the_msg["to"]=to_list

plain_text="Testing the message"
html_txt=""
<html>
    <head>some</head>
    <body>
        <p>hey!<br>
            testing this email <b>message</b>,made by <a href='fff'>
        </p>
    </body>
</html>

part_1=MIMEText(plain_txt,'pain')
part_2=MIMEText(html_txt,"html")

the_msg.attach(part_1)
the_msg.attach(part_1)

print(the_msg.as_string())
