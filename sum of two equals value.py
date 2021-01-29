val=[5,7,1,2,8,4,3]

# def value(v,n):
#     fv=set() 
#     for i in n:
#         if v-i in fv:
#             return True
#         fv.add(i)
#     return False
# print(value(10,val))

arr=[5,7,1,2,8,4,3]
n=len(arr)
sum=10
def find_sum_of_two(arr,n,sum):
    count=0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==sum:
                return True
    False

print(find_sum_of_two(arr,n,sum))