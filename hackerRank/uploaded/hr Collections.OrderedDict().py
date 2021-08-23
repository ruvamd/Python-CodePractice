'''
enter:
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
'''
from collections import OrderedDict
od=OrderedDict()
for _ in range(int(input())):
    name,_,price=input().rpartition(' ')
    od[name]=od.get(name,0)+int(price)
for name,price in od.items():
    print(name,price)
'''
output:
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''

#---test---
# if NItm<0 and NItm>=100:
#     print('the range is 0-100')
# if NnamePrice<0 and NnamePrice>=100:
#     print('the range is 0-100')

#---alt code---
# store_item = dict()
# for _ in range(int(input())):
#     key,_,value = input().rpartition(" ")
#     store_item[key] = store_item.get(key,0) + int(value)
# for k,v in store_item.items():
#     print(k,v)


