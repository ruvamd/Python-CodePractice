items=['apple','pear','orange','banana','kiwi',
       'apple','pear','orange','banana','kiwi',
       'apple','pear','orange','banana','kiwi']
counter=dict()
for item in items:
    if (item in counter.keys()):
        counter[item]+=1
    else:
        counter[item]=1
print(counter)