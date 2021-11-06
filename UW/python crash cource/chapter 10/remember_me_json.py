import json

username=input("what's your name?:")
filename=('UW/python crash cource/chapter 10/username.json')
with open(filename,'w') as f:
    json.dump(username,f)
    print(f"w'll remember when you come back {username}")
