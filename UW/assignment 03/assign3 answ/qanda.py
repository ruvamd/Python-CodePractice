# part 1
questions = []
question_id = 0
sequence_number = 0
while True:
    question = input("Enter a questions, 999 when done: ")
    if question == "999":
        break
    question_id += 1
    sequence_number += 1
    questions.append(f"{str(question_id)},{str(sequence_number)},{question},{False}\n")

f = open("questions-create.csv", "w")
f.writelines(questions)
f.close()

# part 2 - uses a hand created file, not the one above
import csv
import operator

loaded_questions = csv.reader(open('questions-load.csv'), delimiter=',')
questions_to_sort = []
for question in loaded_questions:
    if question[3] == 'False':
        questions_to_sort.append(question)
sorted_questions = sorted(questions_to_sort, key=operator.itemgetter(1))
print(sorted_questions)

#part 3
answers = []
name = input("Your name?: ")
for question in sorted_questions:
    answer = input(question[2] + ": ")
    answers.append(f"{question[0]}, {name}, {answer}\n")

f = open("answers.csv", "w")
f.writelines(answers)
f.close()

#part 4 (separate file - would need to repeat part 2 above at start
loaded_answers = list(csv.reader(open('answers.csv'), delimiter=','))
print(f"Answers for {name}")
counter = 0
for question in sorted_questions:
    print(f"{question[2]} -> {loaded_answers[counter][2]}")
    counter += 1
