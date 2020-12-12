#Assignment: please pass the coded messages
#not done
# def solution(list):
#     list.sort(reverse=True)
#     for i in len(list)+1:
#         if sum(i)%3==0:
#             return int(i)
#     return 0


#alternative code
from itertools import combinations
 
def solution(l):
	l.sort(reverse = True)
	for i in reversed(range(1, len(l) + 1)):
		for tuple in combinations(l, i):
			if sum(tuple) % 3 == 0: return int(''.join(map(str, tuple)))
	return 0

print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))
