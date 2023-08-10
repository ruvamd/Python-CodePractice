#combines long ch with sh ch on start and end string
def combo_string(a, b):
  if len(a)>len(b):
    return b+a+b
  elif len(b)>len(a):
    return a+b+a
print(combo_string('Hello', 'hi'))
print(combo_string('hi', '2345'))
print(combo_string('aaa', 'b'))