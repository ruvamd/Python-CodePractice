class Employee:
    def __init__(self,first_name,last_name,annual_salary=5000):
        self.first_name=first_name
        self.last_name=last_name
        self.annual_salary=annual_salary

    def annual_salary():
        ask=input('if you want to rise annual salary,choose r,else n:')
        if 'r' in ask:
            how_much=input('how much to raise?:')
            sum=annual_salary+how_much
            print(f'the sum is {sum}')
        elif 'n' in ask:
            print(f'the annual summary remains {annual_salary}')
    
    def f_name():
        first_name=input('enter the first name:')
        return print(f'{first_name}')
    def l_name():
        last_name=input('enter the last name:')
        return print(last_name)


employee=Employee
employee.f_name()
employee.l_name()
employee.give_raise(50)


