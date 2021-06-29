#-----alternative not finished code-------
# numberOfS=int(input('enter the number of students: '))
# #numberOfS>=2 and numberOfS<=5
# NameGrade={}
# for _ in range(numberOfS):
#     name=input('enter the student name: ')
#     grade=input('enter the student grade: ')
# val=NameGrade[name]=grade
# #students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# second=sorted(list(set(val)))[1]
# second_low=[]
# for key,value in NameGrade.items():
#     if value==second:
#         second_low.append(key)
# second_low.sort()
# for name in second_low:
#     print(name)

#----------alternative code------------#
# def secondLowestGrade(classList):
#     secondLowestScore = sorted(set(_[1] for _ in classList))[1]
#     result = sorted([_[0] for _ in classList if _[1] == secondLowestScore])
#     return result

# numberOfStudents = int(input())
# classList = []
# for i in range(numberOfStudents):
#     classList.append([str(input()), float(input())])
# print('\n'.join(secondLowestGrade(classList)))