# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("can't devide by zero")

print('enter the two numbers')
print('enter q to quit')
while True:
    fn=input()
    if fn=='q':
        break
    sn=input()
    if sn =='q':
        break
    try: 
        answer=int(fn)/int(sn)
    except ZeroDivisionError:
        print("can't devide by zero")
    except ValueError:
        print("enter numbers only")
    else:print(answer)

# file='UW/python crash cource/chapter 10/alice.txt'
# try:
#     with open(file) as f:
#         data=f.read()
# except FileNotFoundError:
#     print(f'the file {file} does not exist')
# else:
#     words=data.split()
#     number_of_words=len(words)
#     print(f'the {file} has {number_of_words} number of words {words}')