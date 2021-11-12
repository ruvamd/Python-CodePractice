messages=['a','b','c']
sent_messages=[]
def show_messages(messages,sent_messages):
    while messages:
        message=messages.pop()
        print(f'the current message is {message}')
        sent_messages.append(message)

def send_messages(sent_messages):
    for message in sent_messages:
        print(f'the message was sent {message}')

show_messages(messages[:],sent_messages)
send_messages(sent_messages)
print(messages)
