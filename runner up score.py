n = int(input('enter the number of participants: '))
arr = list(set(map(int, input('enter numbers with spaces: ').split())))
arr.sort()

print(f'the runner up score is {arr[-2]}')
