import json

file='/Users/vadim/Documents/Programming languages/Python/Python code/UW/python crash cource/chapter 16(downloading data)/data/eq_data_1_day_m1.json'
with open(file) as f:
    load_json=json.load(f)
    # print(load_json)

wr_json_file='/Users/vadim/Documents/Programming languages/Python/Python code/UW/python crash cource/chapter 16(downloading data)/data/eq_data_wr.json'
with open(wr_json_file,'w') as wr_f:
    json.dump(load_json,wr_f,indent=4)
