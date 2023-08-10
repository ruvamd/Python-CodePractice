"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
  result = ""
  for i in range(1,len(str)+1):
    result+=str[:i]
  return result

#alternative solution
#   s=''
#   for x in range(len(str)):
#     for y in range(x):
#       s+=str[y]
#     s+=str[x]
#   return s

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))