from name_function import full_name

print('enter q to quit')
while True:
    first=input('enter first name:')
    if first=='q':
        break
    last=input('enter last name:')
    if last=='q':
        break
    formatted_full_name=full_name(first,last)
    print(f'your formatted full name is {formatted_full_name}')
