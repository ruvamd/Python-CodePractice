def left2(str):
  f=str[:2]
  l=str[2:]
  return l+f
  #or return str[2:]+str[:2]
print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))