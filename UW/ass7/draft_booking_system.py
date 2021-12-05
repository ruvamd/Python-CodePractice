#capture
'''
Name of the customer.
Package description.
Are the contents dangerous? [Y/N]
Weight (kgs).
Volume (cubic meters).
Required delivery date (month/date/year).
International destination? [Y/N]
'''
#route the package (air / ground / ocean)
#shipping options print and append to booking_quotes.csv
#urgent:1.less than three business days
       #2.via air
# heavy(9kg) or large124: not urgent-truck,ocean(international)
import re
import csv
import datetime as dt
from datetime import time,date
from datetime import datetime as dts

date_format='^\d{2}/\d{2}/\d{4}$'
data=[]
air_kg_cost=10 
air_cubic_cost=20 #per cubic meter
truck_flat_cost=25
truck_urgent_cost=45
ocean_flat_cost=30
heavy_package=9
large_package=124

def menu():
    menu_description=(['Hi.This information will be gathered:','-name','-package description','-content dangerous','-weight','-volume','-delivery date','-destination'])
    for i in menu_description:
        print(i)

def first_last_name():
    while True:
        first_name=input('enter the first name:')
        if not first_name.isalpha():
            print('enter letters only')
            continue
        data.append(first_name)
        break
    while True:
        last_name=input('enter the last name:')
        if not last_name.isalpha():
            print('enter letters only')
            continue
        data.append(last_name)
        break

def danger():
    while True:    
        ask_danger=input('Does the content dangerous?(y/n):')
        if 'y' in ask_danger:
            print('it cannot be routed via air')
            data.append(ask_danger)
        elif 'n' in ask_danger:
            data.append(ask_danger)
            break
        else:
            print('enter y or n only')
            continue
        break

def international():
    while True:
        ask_international=input('international destination?(y/n):')
        if 'y' in ask_international:
            data.append(f'{ask_international}')
        elif 'n' in ask_international:
            data.append(f'{ask_international}')
            break
        else:
            print('enter y or n only')
            continue
        break

def package_description():
    pack_descr=input('enter the package description:')
    data.append(pack_descr)

def check_urgent():
     

def weight():
    weight_restricted=10  
    while True:
        try:
            enter_weight=int(input('enter the package weight(kg):'))
            if enter_weight==heavy_package:
                print('The package is heavy.Will be routed via truck or ocean.')
                data.append('heavy') 
            elif enter_weight<weight_restricted and enter_weight>0:
                data.append(enter_weight)       
            else:
                print('to be shipped,the weight should be less then 10 kg')
                re_ask=input('Do you want to enter another package?(y/n):')
                if 'y' in re_ask:
                    continue
                else:
                    return 'n'
        except ValueError:    
            print('enter the numbers only')
            continue
        break

def volume():
    size_restricted=5**3
    while True:    
        try:
            enter_volume=int(input('enter the package volume(exp:5x5x5=125 cubic meters):'))
            if enter_volume==large_package:
                print('The package is large.It will be delivered by truck or ocean(for international)')
                data.append('large')
            elif enter_volume<size_restricted and enter_volume>0:
                data.append(enter_volume)
            else:
                print('the volume should be smaller then 5x5x5 meters (125 cubic meters)')
                re_ask=input('Do you want to enter another package volume?(y/n):')
                if 'y' in re_ask:
                    continue
                else:
                    return 'n'
        except ValueError:
            print('enter the numbers only')
            continue
        break

def delivery_date():
    today=date.today()
    # today_day=today.day
    # today_format=today.strftime('%m/%d/%Y')
    
    delta=dt.timedelta(days=3)

    limit=today+delta
    limit_day=limit.day

    while True:    
        enter_date=input('enter the delivery date(mm/dd/yyyy):')
        enter_date_match=re.match(date_format,enter_date)
        if not enter_date_match:
            print('enter the correct format')
            continue
        format_ent_date=dts.strptime(enter_date,'%m/%d/%Y')
        ent_day=format_ent_date.day
        if ent_day<limit_day:
            data.append('urgent')
            print('urgent.Will be delivered in less then three days by Air if possible.')
        else:
            data.append('not urgent')
            print('will be delivered by truck or ocean')
        data.append(enter_date)
        break

def write_to_csv():
    with open('src/assignment07/booking_system/src/booking_system/booking_quotes.csv','w') as store_bq:
        format_bq_csv=','.join(map(str,data))
        store_bq.writelines(format_bq_csv)
        
def load_from_csv():
    with open('src/assignment07/booking_system/src/booking_system/booking_quotes.csv') as load_bq:
        read_stored_bq=csv.reader(load_bq)
        for i in read_stored_bq:
            print(i)

def record():
    id=0
    while True:
        # menu()
        id+=1
        data.append(f'\n{id}') #fix new line
        # first_last_name()
        # package_description()
        # danger()
        # if weight()!='n':
        #     pass
        # else:
        #     break  
        if volume()!='n':
            pass
        else:
            break
        # delivery_date()
        # international()
        
        write_to_csv()
        load_from_csv()
        more=input('enter more?(y or n)')
        if 'y' in more:
            continue
        elif 'n' in more:
            break
        else:
            print('enter y or n only')
            continue
    # print(data)

record()
        
     