#test
# food='pizza'
# car='Subaru'
# home='mantion'
# city='seattle'
# country='new zeland'

# print("is food == 'pizza'?I predict True")
# print(food=='pizza')
# print("is food == 'soup'?I predict False")
# print(food=='soup')

# print(car=='subaru')
# print(car=='bmw')
# print(home=='mantion')
# print(home=='tiny')
# print(city=='seattle')
# print(city=='denver')
# print(country=='new zeland')
# print(country=='australia')
# if 'subaru' in car:
#     print('the car is correct')
# else:print('the car is incorrect')
# print(car.lower()=='subaru')

# a=12
# b=24
# print(a>b and a<b,a<b or b<a)

# l=('a','b')
# if 'a' in l:
#     print('the a in l')
# else:print('a is not in the l')
# if 'c' not in l:
#     print('the c not in l')

#aliens colors
#alien_color='red'
# if 'red' in alien_color:
#     print('no it is not')
# if 'green' in alien_color:
#     print('you earned 5 points')

# if 'yellow' in alien_color:
#     color='yellow'
# elif 'green' in alien_color:
#     color='green'
# else:color='red'

# print(f'your color is {color}')

#stage of life
# age=66
# if age<2:
#     print('the person is a baby')
# elif age>=2 and age<4:
#     print('the person is a toddler')
# elif age>=4 and age<13:
#     print('the person is a kid')
# elif age>=13 and age<20:
#     print('the person is a teenager')
# elif age>=20 and age<65:
#     print('the person is an adult')
# else:print('the person is an elder')

#favorite fruit
# favorite_fruit=['mango','kiwi','bread']
# if 'mango' in favorite_fruit:
#     print('yes')
# if 'pepper' in favorite_fruit:
#     print('no')

#hello admin
# admin_list=['admin','b','c','d']
# for admin in admin_list:
#     if admin=='admin':
#         print('hello admin,would you like to see report?')
#     else:print(f'hello {admin} thanks for logging in')

#no users
# admin_list=[]
# if admin_list:
#     for admin in admin_list:
#         if admin=='admin':
#             print('hello admin,would you like to see report?')
#         else:print(f'hello {admin} thanks for logging in')
# else:print('we need to find some more people')

#cheking usernames
# current_user=['a','B','c','d','f']
# new_usernames=['e','d','n','h','b']

# for user in new_usernames:
#     if user in current_user:
#         if user==user.lower():
#             print('no capitol letters allowed')
#         print(f'the {user} is old,need to enter the new username')

#     else:print(f'the new user {user} is available') 

#ordinal numbers
numb_list=[1,2,3,4,5,6,7,8,9]
# ordinal=lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
# print([ordinal(n) for n in numb_list])
for n in numb_list:
    if n<10:
        if n==1:
            suffics='st'
        elif n==2:
            suffics='nd'
        elif n==3:
            suffics='rd'
        else:suffics='th'
        print(str(n)+suffics)


    