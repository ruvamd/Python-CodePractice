import json

filename='UW/python crash cource/chapter 10/username.json'
try:   
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("what's your name?:")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"w'll remember when you come back {username}")
else:
    print(f'welcome back {username}')