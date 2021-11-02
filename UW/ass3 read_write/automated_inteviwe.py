import csv

with open('UW/ass3 read_write/questions.csv','r') as questions_file:
    csv_reader=csv.reader(questions_file,delimiter='\t')
    # csv_reader=csv.DictReader(questions_file)
    # with open('UW/ass3 read_write/copy.csv','w') as copy:
    #     csv_writer=csv.writer(copy,delimiter='\t')
    field_name=[name,question,answer]
    for question in csv_reader:
        print(question)
        # csv_writer.writerow(question)
def answers(a):
    a=input()
    return a

    with open('UW/ass3 read_write/answers.csv','w') as answers_file:
        for q in csv_reader:
            print(q,answers())
            answers_file.write(answers)
