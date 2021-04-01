# for i in range(int(input())):
#     try:
#         a,b=map(int,(input().split()))
#         print(a//b)
#     except BaseException as e:
#         print('error code:',e)

# for test in range(int(input())):
#     try:
#         a,b = map(int,input().split()) 
#         division_result = a // b
#         print(division_result)
#     except ZeroDivisionError as e:
#         print("Error Code:", e)
#     except ValueError as e:
#         print("Error Code:", e)

for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)

