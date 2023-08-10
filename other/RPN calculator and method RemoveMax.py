# 1. Create a Reverse Polish Notation calculator
class RPN:
  def __init__(self):
    self.stack = []

  def process(self, value):
    if value == "+":
      num2 = self.stack.pop()
      num1 = self.stack.pop()
      self.stack.append(num1 + num2)
    elif value == "-":
      num2 = self.stack.pop()
      num1 = self.stack.pop()
      self.stack.append(num1 - num2)
    elif value == "*":
      num2 = self.stack.pop()
      num1 = self.stack.pop()
      self.stack.append(num1 * num2)
    elif value == "/":
      num2 = self.stack.pop()
      num1 = self.stack.pop()
      self.stack.append(num1 / num2)
    else:
      self.stack.append(float(value))

  def result(self):
    return self.stack[-1]

rpn = RPN()
rpn.process("5")
rpn.process("4")
rpn.process("+")
rpn.process("3")
rpn.process("-")
print('-----fist result------')
print(rpn.result())  # prints 6.0
print('-----second result------')

# 2. Write a method that removes the maximum value from a stack
def remove_max(values):
    if not values:
        return None
    
    # Use a queue as auxiliary storage
    queue = []
    max_val = values[-1]
    
    # Remove all instances of the maximum value from the stack
    while values:
        val = values.pop()
        if val > max_val:
            max_val = val
        queue.append(val)
    
    # Put all non-maximum values back onto the stack
    while queue:
        val = queue.pop(0)
        if val != max_val:
            values.append(val)
    
    return max_val

values = [7, 77, 88, 2, 97, 5, 117, 107, 61, 107, 52]
max_value = remove_max(values)
print(max_value)  # prints 117
print(values)  # prints [7, 77, 88, 2, 97, 5, 107, 61, 107, 52]

max_value = remove_max(values)
print(max_value)  # prints 107
print(values)  # prints [7, 77, 88, 2, 97, 5, 61, 52]

