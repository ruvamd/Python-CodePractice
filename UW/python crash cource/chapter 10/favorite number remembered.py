import json

filename='UW/python crash cource/chapter 10/store_fn.json'
try:    
    with open(filename) as f:
        store=json.load(f)
        print(store)
except FileNotFoundError:
        fn=input('enter your favorite number:')
        with open(filename,'w') as f:
            store=json.dump(fn,f)




    


