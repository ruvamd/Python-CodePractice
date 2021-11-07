import json

def get_stored_username():#get stored username if available
    filename='UW/python crash cource/chapter 10/username.json'
    try:   
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():#greet the user
    username=get_stored_username()
    if username:
        print(f'welcome back {username},does it your name?')
        choose=input('y or n:')
        if choose=='y':
            print(f'welcome back {username}')
        elif choose=='n':
            username=get_new_username()
            print(f"w'll remember when you come back {username}")
    
def get_new_username():
    username=input("what's your name?:")
    filename='UW/python crash cource/chapter 10/username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

greet_user()