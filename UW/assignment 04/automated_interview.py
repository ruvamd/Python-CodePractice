import csv
import operator
import json
import re

questions = []
question_id = 0
sequence_number = 0
prompt='enter a questions,q when done:'
#questions
while True:
    question=input(prompt)
    if question=='q':
        break
    ask=input(f"Does the question '{question}' correct? choose y or n:")
    if ask=='y':
        if len(question)>=10 or len(question)>=30:
            pass
        else:
            print('question range shoud be from 10 to 30 charachters.reenter question')
            questions.pop()
    elif ask=='n':
        ask_to_correct=input('do you want to delete and correct the question? y or n:') 
        # questions.pop()
        if ask_to_correct=='y' or 'n':
            pass
        
    question_id += 1
    sequence_number += 1
    questions.append(f"{str(question_id)},{str(sequence_number)},{question},{False}\n")

with open('src/assignment04/create_questions.csv','w') as f:
    f.writelines(questions)

loaded_questions = csv.reader(open('src/assignment04/create_questions.csv'), delimiter=',')
questions_to_sort = []
for question in loaded_questions:
    if question[3] == 'False':
        questions_to_sort.append(question)
sorted_questions = sorted(questions_to_sort, key=operator.itemgetter(1))
print(sorted_questions)   

#answers
answers = []

name = input("your name?: ")
for question in sorted_questions:
    answer = input(question[2] + ": ")
    if question[2]=='What is your email address?':
        if re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',answer):
            pass
        else: 
            print(f"invalid email '{answer}' format,enter again:")
            answer=input(question[2] + ": ")
    elif len(answer)==0:
        print('the answer is empty,enter again:')
        answer = input(question[2] + ": ")  
    answers.append(f"{question[0]}, {name}, {answer}\n")
with open('src/assignment04/answers.csv','w') as f:
    f.writelines(answers)

loaded_answers = list(csv.reader(open('src/assignment04/answers.csv'), delimiter=','))
print(f"Answers for {name}")
counter = 0
for question in sorted_questions:
    print(f"{question[2]}: {loaded_answers[counter][2]}")
    counter += 1
