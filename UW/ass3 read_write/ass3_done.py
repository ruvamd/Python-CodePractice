Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import csv
import operator
import json

questions = []
question_id = 0
sequence_number = 0
prompt='enter a questions,q when done:'

#questions
while True:
    question=input(prompt)
    if question=='q':
        break
    question_id += 1
    sequence_number += 1
    questions.append(f"{str(question_id)},{str(sequence_number)},{question},{False}\n")

with open('src/assignment04/create_questions.csv','w') as f:
    f.writelines(questions)
# with open('src/assignment04/load_questions.csv','w') as f:
#     json.dump(questions,f)
loaded_questions = csv.reader(open('src/assignment04/create_questions.csv'), delimiter=',')
questions_to_sort = []
for question in loaded_questions:
    if question[3] == 'False':
        questions_to_sort.append(question)
sorted_questions = sorted(questions_to_sort, key=operator.itemgetter(1))
print(sorted_questions)   

#answers
answers = []
name = input("Your name?: ")
for question in sorted_questions:
    answer = input(question[2] + ": ")
    answers.append(f"{question[0]}, {name}, {answer}\n")
with open('src/assignment04/answers.csv','w') as f:
    f.writelines(answers)

loaded_answers = list(csv.reader(open('src/assignment04/answers.csv'), delimiter=','))
print(f"Answers for {name}")
counter = 0
for question in sorted_questions:
    print(f"{question[2]} -> {loaded_answers[counter][2]}")
    counter += 1
