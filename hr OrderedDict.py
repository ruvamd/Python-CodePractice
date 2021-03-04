from collections import OrderedDict

# dict={}
# count=0
# dict=od()
# numberOfItems=int(input())
# dict[input()]=input().split()

# if numberOfItems and dict>=100 or numberOfItems and dict<0:
#     print('enter in range 0-100')

# for numberOfItems in dict:
#     count+=1
#     print(numberOfItems)

#---alt code---
# d = OrderedDict()
# for _ in range(int(input())):
#     item, space, quantity = input().rpartition(' ')
#     d[item] = d.get(item, 0) + int(quantity)
# for item, quantity in d.items():
#     print(item, quantity)

#---alt code---
# from collections import Counter
# d = Counter()
# for i in range(int(input())):
#     name,blank,price = input().rpartition(" ") 
#     d[name]= d[name]+int(price)
# for i in d.items():
#     print(*i)

#---alt code---
ordered_dictionary = OrderedDict()
for _ in range(int(input())):
    item, price = input().rsplit(' ', 1)
    ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(price)
[print(item, ordered_dictionary[item]) for item in ordered_dictionary]

    
