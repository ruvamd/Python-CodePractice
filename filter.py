scores=[66,90,68,99,76,60,88,74,81,65]

def isAstudent(score):
    return score>75
over75=list(filter(isAstudent,scores))
print(over75)