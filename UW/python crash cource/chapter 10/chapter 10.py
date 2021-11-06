# file='UW/python crash cource/chapter 10/pi_digits.txt'
# file_million='UW/python crash cource/chapter 10/pi_million_digits.txt'
# with open(file_million) as file_object:
#     lines=file_object.readlines()

# store=''

# for line in lines:
#     store+=line.strip()
# bd=input()
# if bd in store:
#     print('yes')
# else:print('no')
# print(store)
# print(store[:51])
# print(len(store))

with open('UW/python crash cource/chapter 10/learn.txt') as f:
#     data=f.readlines()
    data=f.read()
    # data=f.readline()
# store=''
# data=str(data)
rd=data.replace('one','six')
# print(data)
print(rd)
# for line in data:
#     mult=line.strip()
#     print(mult*3)
    # store+=line.strip()
# print(store*3)
