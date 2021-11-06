guest_list=['a','b','c','d']
#del a[0]
#print(a)

#guest list
message='invite you to dinner'
print(f'{message} {guest_list[0]}')
print(f'{message} {guest_list[1]}')
print(f'{message} {guest_list[2]}')
print(f'{message} {guest_list[3]}')

#changing guest list
print("the b can't come")
guest_list[1]='e'
print(f'{message} {guest_list[0]}')
print(f'{message} {guest_list[1]}')
print(f'{message} {guest_list[2]}')
print(f'{message} {guest_list[3]}')

#more quests
print('I found a bigger dinning table')
guest_list.insert(0,'f')
guest_list.insert(3,'j')
guest_list.insert(6,'k')
for i in guest_list:
    print(message,i)

#shrinking guest list
print('I can invite only two people for dinner')
message2="I can't invite you"
message3='youre still invited'
print(message2,guest_list.pop(0))
print(message2,guest_list.pop(0))
print(message2,guest_list.pop(0))
print(message2,guest_list.pop(0))
print(message2,guest_list.pop(0))
print(message3,guest_list)
del guest_list[0]
del guest_list[0]
print(guest_list)
