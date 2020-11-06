import re

#alternative code1
# def count_code(str):
#   count = 0
#   i=0
#   while "co" in str[i:]:
#     if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
#       count += 1
#     i+=str[i:].index("co")+3
#   return count

#alternative code2
# def count_code(str):
#     exp = '^co[a-z|A-Z]e$'
#     count = 0
#     for i in range(len(str) - 1):
#         if re.match(exp, str[i:i + 4]):
#             count+=1
#     return count

def count_code(str):
  count=0
  for i in range(97,123): 
     count+= str.count('co'+chr(i)+'e')
  return count

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))