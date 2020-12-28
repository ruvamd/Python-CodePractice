# N = int(input())
# list=['1.insert','2.print','3.remove','4.append','5.sort','6.sort','7.reverse']
# arr=[]
# print(list)

def handler(result):
    inp = input().split()
    
    command = inp[0]
    values = inp[1:]
    
    if command == 'print':
        print(result)
    else:
        execute='result.'+command+"("+",".join(values)+")"
        eval(execute)

result = []
for i in range(int(input())):
    handler(result)