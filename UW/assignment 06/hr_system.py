#record: name,address,ssn,date of birth,job title,start date,end date
#store: csv file
#load: csv file
#record data validation: check for missing fields,invalid values,error handling with message

#produse: a list of current employees and employees who left last month.Sort two list by emp.ID
#reminder: schedule reminder three month before annual review and show. 
#pytest

import re
import csv

stored_data=[]
current_employees=[]
employee_left=[]

match_string='^[A-Za-z]*$'
match_str_num='^[A-Za-z0-9]*$'
match_address='[a-zA-Z0-9],*'
match_ssn='^\d{3}-\d{2}-\d{4}$'
match_date_of_birth='^\d{2}/\d{2}/\d{4}$'
match_start_end_date='^\d{2}/\d{2}/\d{4}$' 
    
def first_last_name():
    
    while True:
        first_name=input('enter the first name:')
        first_name_match=re.match(match_string,first_name)
        if not first_name_match:
            print('enter letters only')
            continue
        else: 
            while True:
                
                stored_data.append(first_name)
                last_name=input('enter the last name:')
                last_name_match=re.match(match_string,last_name)
                if not last_name_match:
                    print('enter letters only')
                    continue
                else:
                    stored_data.append(last_name)
                break
        break 

def address_record():
    while True:
        address=input('enter the address(street,city,state):')
        address_match=re.match(match_address,address)
        if not address_match:
            print('enter letters and numbers only')
            continue
        else:
            stored_data.append(address)
            break

def ssn_record():
    while True:
        ssn=input('enter your ssn(000-00-0000):')
        ssn_match=re.match(match_ssn,ssn)
        if not ssn_match:
            print('enter numbers and dashes only')
            continue
        else:
            stored_data.append(ssn)
            break

def date_of_birth_record():
    while True:
        date_of_birth=input('enter your date of birth(mm/dd/yyyy):')
        date_of_birth_match=re.match(match_date_of_birth,date_of_birth)
        if not date_of_birth_match:
            print('enter numbers and slash only')
            continue
        else:
            stored_data.append(date_of_birth)
            break

def title_record():
    while True:
        job_title=input('enter your job title:')
        job_title_match=re.match(match_string,job_title)
        if not job_title_match:
            print('enter letters only')
            continue
        else:
            stored_data.append(job_title)
            break

def start_end_date():
    while True:
        start_date=input('enter the start date(mm/dd/yyyy):')
        start_date_match=re.match(match_start_end_date,start_date)
        if not start_date_match:
            print('enter number and splash only')
            continue
        stored_data.append(start_date)
        break
    while True:
        ask_if_left=input('does employee left?(y or n):')
        if 'y' in ask_if_left:
            end_date=input('enter the end date(mm/dd/yyyy):')
            end_date_match=re.match(match_start_end_date,end_date)
            if not end_date_match:
                print('enter number and splash only')
                continue
            stored_data.append(end_date)
            break
        elif 'n' in ask_if_left:
            present='present'
            stored_data.append(present)
            break

def currrent_left_employee_sort():
        if stored_data[-1]=='present':
            current_employees.append(stored_data)
        else:
            employee_left.append(stored_data)

def write_in_csv():
    with open('src/assignment06/HR_System_profect/src/hr_system/store.csv','a') as store:
        format_store_csv=','.join(stored_data)
        store.writelines(format_store_csv)

def load_from_csv():
    with open('src/assignment06/HR_System_profect/src/hr_system/store.csv') as load:
        read_stored=csv.reader(load)
        for i in read_stored:
            print(i)

def record_data():
        employee_id=0
        while True:
            employee_id+=1
            stored_data.append(f'\n{str(employee_id)}')
            first_last_name()
            address_record()
            ssn_record()
            date_of_birth_record()
            title_record()
            start_end_date()
            currrent_left_employee_sort()
            record=input('enter more?(y or n)')
            if 'y' in record:
                continue
            else:
                break
record_data()

write_in_csv()
load_from_csv()
