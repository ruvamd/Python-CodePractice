actor={'name':'john cleese','rank':'awesome'}
def get_last_name():
    return actor['name'].split()[1]
get_last_name()
print('all exceptions caught!Good job!')
print('the actor`s last name is %s'%get_last_name())