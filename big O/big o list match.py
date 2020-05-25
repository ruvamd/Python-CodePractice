list=[1,2,3,4,5,6]

def matcher(list,match):
    for item in list:
        if item==match:
            return True
    return False
    
matcher(list,1)
