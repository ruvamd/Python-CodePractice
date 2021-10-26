questions=('1.What is your name? ',
           '2.What is your conference ID? ',
           '3.Which organization do you represent? ',
           '4.What is your email address? ',
           '5.State any food preferences? ')
answers=('your name is',
         'your conference ID is',
         'your organisation is',
         'your email is',
         'your food preference is')

select='Select which of the following sessions you wish to attend – enter y or n'
sessions=('Python for beginners', 
          'Database development with Python', 
          'Python for data science', 
          'Advanced Python for application developers')
#q&a
q_1=input(questions[0])
print(answers[0],q_1)
q_2=input(questions[1])
print(answers[1],q_2)
q_3=input(questions[2])
print(answers[2],q_3)
q_4=input(questions[3])
print(answers[3],q_4)
q_5=input(questions[4])
print(answers[4],q_5,'\n')  

#session selection
print(select)
for session in sessions:
    input(f'{session}:')






