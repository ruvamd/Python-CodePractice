# for i in range(10):
#     print(i)

# print([i for i in range(10)])

# def add_one(x):
#     return x+1
#print(list(map(add_one,range(10))))

#print([add_one(x) for x in range(10)])
# for x in range(10):
#     if x%2:
#         print(x)
# print([x for x in range(10) if x%2])

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# print(l[::-1],l[::2])


# print(l[13:],l[:3],l[7:10])
# def last_first(x):
#     return x[::-15]

# def mid_odd(x):
#     return x[4:-4:2]

# print('the middle odd numb. from list l',mid_odd(l))
# print(last_first(l))

# for i in range(101):
#     print(i)
#     if i > 50:
#         break

for i in range(101):
   if i > 50:
       break
   if i < 25:
       continue
   print(i)