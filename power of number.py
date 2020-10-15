def is_power_of(number,base):
  if number%base or base==1: 
      return False 
  i=1
  while i<number:
    i*=base
    if i==number: 
        return True
  return False

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False