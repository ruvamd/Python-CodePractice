import json

filename='UW/python crash cource/chapter 10/numbers.json'
with open(filename) as f:
    data=json.load(f)
print(data)