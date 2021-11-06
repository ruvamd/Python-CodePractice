prompt='enter your name:'
prompt+='(enter the q for quit)'
message=""
with open('UW/python crash cource/chapter 10/guest_book.txt','w') as f:
        while message!='q':
                message=input(prompt)
                print(f"greetings {message},the data was recording in the file quest_book")
                f.write(f'{message}\n')
               

# prompt='enter your name:'
# prompt+='(enter the q for quit)'
# message=''
# while message!='q':
#         message=input(prompt)
#         print(message)