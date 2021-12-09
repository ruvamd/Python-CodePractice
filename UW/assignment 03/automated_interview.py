'''1.questions are stored in the file
  1.1 loaded from the file when app starts
  2.code that promt questions from file
  2.1 store question_id, sequence_number, question,deleted_flag
  3.load the questions from the question file
  4.store the answers to the questions, and then write a new program print them
  question_id,name_of_person_interviewed,answer
  5.write in report.py report '''
import csv
#capture the questions
store_answers=[]
store_questions=[]
with open('src/assignment03/questions.csv','r') as read_questions:
    # print(read_questions.read())
    # csv.reader(read_questions)
    # line=read_questions.readlines()
    for l in read_questions:
      print(l,end='')
      answer=input('enter the answer: ')
      store_answers.append(answer)
      store_questions.append(l)
    with open('src/assignment03/stored_questions.csv','w') as stor_qst:
      stor_qst.write(f'{store_answers[1]},1,{store_questions[1]},False')
      
    with open('src/assignment03/report.csv','w') as report:
      report.write(f'{store_answers[1]},')
      report.write(f'{store_answers[0]},')
      report.write(store_answers[3])
    

