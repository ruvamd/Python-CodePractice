# def solution(x, y):
#     if (x,y)==(1,1):
#         return 'impossible'
#     elif x>y:
#         x-y(x/y)
#         return str(x)
#     elif y>x:
#         y-x(y/x)
#         return str(x)


def solution(x,y):
    g=(int(x),int(y))
    x,y=g
    count=0
    while x!=y:
        if x > y:
            num_subs = (x-y)//y + ((x-y) % y > 0)
            count+= num_subs
            x, y = x - num_subs * y, y
        elif y > x:
            num_subs = (y-x)//x + ((y-x) % x > 0)
            count+= num_subs
            x, y = x, y - num_subs * x
        
    return str(count) if (x, y)==(1, 1) else 'impossible'

print(solution('4', '7'))
print(solution('2', '1'))