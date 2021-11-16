import json
import csv

with open('UW/assignment_6/data.csv') as f:
    reader=csv.DictReader(f)
    a=list(reader)
    print(a)
with open('UW/assignment_6/load_data.csv','w') as f:
    f.write(str(a))
    
    # data=f.read()
    # print(data)
    # data_load=json.loads(data)
    # print(data_load)