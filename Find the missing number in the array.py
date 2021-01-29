#n=[3,7,1,2,8,4,5]

#---alt code---
# def missNum(n):
#     sumOfElements=sum(n)
#     n=len(n)+1
#     actualSum=(n*(n+1))/2
#     return actualSum-sumOfElements
# print(missNum(n))

n=sorted([3,7,1,2,8,4,5])
n1=len(sorted(range(n[0],n[-1])))
def find_missing(lst): 
    #return [x for x in range(lst[0], lst[-1]+1) if x not in lst]  
    #return sorted(set(range(lst[0],lst[-1]))-set(lst))       
    return sorted(set(range(lst[0],lst[-1] + 1)).difference(lst))
print(find_missing(n))