import json

numbers=[1,2,3,4,5,6]
filename='UW/python crash cource/chapter 10/numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)
