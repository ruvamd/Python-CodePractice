from collections import OrderedDict
od=OrderedDict()
for _ in range(int(input())):
    name,_,price=input().rpartition(' ')
    od[name]=od.get(name,0)+int(price)
for name,price in od.items():
    print(name,price)

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


