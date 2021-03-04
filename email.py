from email.message import EmailMessage
message=EmailMessage()

sender='ruvamd@gmail.com'
recipient='ruvamd@gmail.com'

message['From']=sender
message['To']=recipient
message['Subject']=f'greetings from {sender} to {recipient}'
body="hey,I'm learning to send emails"
message.set_content(body)
print(message)