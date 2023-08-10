'''
Given a non-negative number "num", return True if num is within 2 of a 
multiple of 10. Note: (a % b) is the remainder of dividing a by b, 
so (7 % 5) is 2.
'''
def near_ten(num):
    a = num % 10
    if  (10 - (10-a)) <= 2 or (10 - a) <= 2:
        return True
    else:
        return False

#alternative code 1
#     a = num % 10
#     return 8 <= a or 2 >= a

#alternative code 2 
#     return not(2 < (num % 10) < 8)

#alternative code 3
#     return abs(5 - num % 10) >= 3

#alternative code 4
# def near_ten(num_list):
#     a = np.mod(num_list, 10)
#     return np.logical_or(2 >= a, 8 <= a)  

#not showing False output,only in cb.
    # within = num - (num+2)/10*10
    # return within in range(-2,3)
    
    # within = num%((num/10)*10) if num >= 10 else num
    # return within in [8,9,0,1,2]  

print(near_ten(12)) #→ True
print(near_ten(17)) #→ False
print(near_ten(19)) #→ True
