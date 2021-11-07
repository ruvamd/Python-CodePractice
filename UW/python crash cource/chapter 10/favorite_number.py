import json

store_fn_json='UW/python crash cource/chapter 10/store_fn.json'

def write_fn():
    fn=input('enter your favorite number:')
    with open(store_fn_json,'w') as f:
        store=json.dump(fn,f)

def read_fn():
    with open(store_fn_json) as f:
        store=json.load(f)
    return store

print(f'your favorite number is {read_fn()}')