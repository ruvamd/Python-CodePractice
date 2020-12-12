from itertools import combinations

def solution(num_buns, num_required):
    buns=[[] for i in range(num_buns)]
    if num_required==0:
        return buns
    startLock=0
    for copie in combinations(buns,num_buns - num_required + 1):
        for item in copie:
            item.append(startLock)
        startLock+=1
    return buns

print(solution(2,1))