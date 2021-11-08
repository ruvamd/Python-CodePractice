def full_name(first,last,middle=''):
    # first_name=input('enter the first name:')
    # last_name=input('inter the last name:')
    # print(f'{first_name} {last_name}')
    if middle:
        full_name=(f'{first} {middle} {last}')
    else:
        full_name=(f'{first} {last}')
    return full_name.title()
# print(full_name('vadim','rusu'))
