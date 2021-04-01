import re

for _ in range(int(input())):
    try:
        i=bool(re.compile(input()))  
    except re.error:
        print(i)
        print('False')
        

# for _ in range(int(input())):
#     try:
#         print(bool(re.compile(input())))
#     except re.error:
#         print('False')