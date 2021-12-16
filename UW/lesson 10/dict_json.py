import json

dictionary_variable = {'k': 'value'}

with open('file.json', 'w+') as f:
     json.dump(dictionary_variable, f)


# Load the file all in one go
dictionary_variable = json.loads(open('file.json').read())
print(dictionary_variable)
