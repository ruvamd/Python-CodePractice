# first_name=input()
# last_name=input()
# print(f'Hello {first_name} {last_name}!You just delved into python.')

#----alt code---
# def print_full_name(fn,ln):
#     first_name=input()
#     last_name=input()
#     print(f'Hello {first_name} {last_name}! You just delved into python.')

# print_full_name('','')

#-----alt code----
# def print_full_name(fn,ln):
#     print('Hello',fn,ln+'! You just delved into python.')
# print_full_name('vadim','rusu')

#-----alt code-----
# def print_full_name(first_name, last_name):
#     print(f'Hello {first_name} {last_name}! You just delved into python.')
# print_full_name('vadim','rusu')

#-----alt code-----
def first_last_name():
    first_name=input('first name: ')
    last_name=input('last name: ')
    if any(char.isdigit() for char in first_name or last_name):
        print('enter only letters')
    else: print(f'Hello {first_name} {last_name}!You just delved into python.')
    
first_last_name()


#'Hello'
#'! You just delved into python.'