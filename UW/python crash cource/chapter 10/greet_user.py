import json

filename='UW/python crash cource/chapter 10/username.json'
with open(filename) as f:
    username=json.load(f)
    print(f'welcome back {username}')