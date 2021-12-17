#converts year salary to month,week,day,hour

def enter_num():
    salary=[]
    range=['month','week','day','hour']
    while True:
        try: 
            ent_year=int(input())
        except ValueError:
            print('enter the numbers only')
            continue
        else: break

    month=ent_year/12
    week=(ent_year/12)/4
    day=((ent_year/12)/4)/5 
    hour=(((ent_year/12)/4)/5)/8 

    salary.append(round(month,2))
    salary.append(round(week,2))
    salary.append(round(day,2))
    salary.append(round(hour,2))

    x=dict(zip(range,salary))

    for k,v in x.items():
        print(k,v)
        
enter_num()
