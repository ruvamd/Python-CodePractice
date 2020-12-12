#google en-route-salute
def solution(s):
    ans=count=0
    for simbol in s:
        if simbol=='<':
            ans+=count #start counting from 0
        elif simbol=='>':
            count+=1
    return ans*2

print(solution(">----<"))
print(solution("<<>><"))
print(solution('--->-><-><-->-'))

#alternative code
# def answer(s):
#     ans = cnt = 0
#     for i in s:
#         if i == '<':
#             ans += cnt;
#         elif i == '>':
#             cnt += 1
#     return ans << 1

# print(answer('--->-><-><-->-'))