import json
def add_employee(salaries_json,name,salary):
     salaries=json.loads(salaries_json)
     salaries[name]=salary
     return json.dumps(salaries)
salaries="{'alfred':300,'jane':400}"
new_salaries=add_employee(salaries,'me',800)
decoded_salaries=json.loads(new_salaries)
print(decoded_salaries['alfred'])
print(decoded_salaries['jane'])
print(decoded_salaries['me'])