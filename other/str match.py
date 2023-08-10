'''
Given 2 strings, a and b, return the number of the positions 
where they contain the same length 2 substring. So "xxcaazz" 
and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings 
appear in the same place in both strings.
'''
def string_match(a, b):

    count = 0
    for i in range(min(len(a), len(b)) - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1                  
    return count

#alternative code 2    
    # def splitter(str,n):
    #     result = []
    #     for i in range(0,len(str)-n+1):
    #         result.append(str[i:i+n])
    #     return result
    # count = 0
    # b_splitted = splitter(b,2)
    # for pair in splitter(a,2):
    #     if pair in splitter(b,2):
    #         count += 1
    # return count

#alternative code 1
#   # Figure which string is shorter.
#   shorter = min(len(a), len(b))
#   count = 0
#   # Loop i over every substring starting spot.
#   # Use length-1 here, so can use char str[i+1] in the loop
#   for i in range(shorter-1):
#     a_sub = a[i:i+2]
#     b_sub = b[i:i+2]
#     if a_sub == b_sub:
#       count += 1
#   return count
    count=0
    for n in int(range(len(a),len(b))):
        a=a[n:n+2]
        b=b[n:n+2]
        if a==b:
            count+=1
    return count

print(string_match('xxcaazz', 'xxbaaz')) #→ 3
print(string_match('abc', 'abc')) #→ 2
print(string_match('abc', 'axc')) #→ 0