n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

s=0
for i in student_marks[query_name]:
    s+=i/3
print(f'{s:.2f}')    
