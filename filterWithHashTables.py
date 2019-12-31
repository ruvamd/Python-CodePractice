items=['apple','pear','orange','banana','kiwi',
       'apple','pear','orange','banana','kiwi',
       'apple','pear','orange','banana','kiwi']
filter=dict()
for key in items:
    filter[key]=0
result=set(filter.keys())
print(result)