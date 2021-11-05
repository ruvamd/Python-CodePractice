# prompt='hey'
# prompt+='\nlalaley '

# name=input(prompt)
# print(f'this is your {name}')

#rental car
# car=input('what type of car do you want?:')
# print(f'let me see the {car} that you want')

# restaurant seating
# seats=int(input('how many seats do you want for your group?:'))
# if seats>8:
#     print('you need to wait for the table')
# else:print('your table is ready')

#multiple number
# number=int(input('enter the number:'))
# if number%10==0:
#     print(f'the {number} is mustiple by 10')
# else:print(f'the {number} is not multiple by 10')

#pizza toppings
# top_mes='toping added:'
# enter_mess='enter the toppings:'
# while True:
#     ent_top=(input(enter_mess))
#     if ent_top=='q':
#         break
#     else:print(top_mes)

#movie theater
# while True:
#     age=int(input('enter your age:'))
#     if age<3:
#         print('the ticket is free')
#     elif age>=3 and age<=12:
#         print('the ticket cost 10$')
#     else:print('the ticket is 15$')
#     break

#three exits
# x=0
# while x<12:
#     x+=1
#     print(x)
#     if x==8:
#         break

# active=True
# count=0
# while active:
#     count+=1
#     print(count)
#     if count==24:
#         active=False

#deli
# sandwich_orders=['chicken sandwich','seafood sandwich','grilled sandwich','egg sandwich']
# finished_sandwiches=[]
# while sandwich_orders:
#     sandwich=sandwich_orders.pop()
#     print(f"I've made your {sandwich}")
#     finished_sandwiches.append(sandwich)
# print('this sandwiches was made:')
# for i in finished_sandwiches:
#     print('\t',i)

#no pastrami

# sandwich_orders=['chicken sandwich','pastrami','seafood sandwich',
#                  'pastrami','grilled sandwich','pastrami','egg sandwich']
# finished_sandwiches=[]

# print('the deli has run out of pastrami')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#     sandwich=sandwich_orders.pop()
#     add=finished_sandwiches.append(sandwich)
# print(finished_sandwiches)

#dream vacation
# active_poll=True
# store_answ=[]

# while active_poll:
#     response=input('what place would you like to visit?:')
#     answers=(f'you would like to visit {response}')
#     store_answ.append(answers)
#     if len(store_answ)==3:
#         active_poll=False
# print(store_answ)

# active_poll=True
# store_poll={}
# while active_poll:
#     name=input("what's your name?:")
#     place=input('what place do you want to visit?:')
#     store_poll[name]=place
#     other_places=input('any other places that you want to visit?(y or n):')
#     if 'n' in other_places:
#         active_poll=False
# print(store_poll)