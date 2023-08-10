'''
Given a string, return a new string made of every other 
char starting with the first, so "Hello" yields "Hlo".
'''
def string_bits(str):
  return str[::2]

print(string_bits('Hello')) #→ 'Hlo'
print(string_bits('Hi')) #→ 'H'
print(string_bits('Heeololeo')) #→ 'Hello'