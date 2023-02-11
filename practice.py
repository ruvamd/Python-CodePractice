def SayHiNTimes(n):
    x = 0
    while x < n:
        x += 1
        print("hi")
        
SayHiNTimes(5)

def Sort(numbers):
    for x in range(len(numbers)):
        for y in range(len(numbers)):
            if numbers[x] < numbers[y]:
                temp = numbers[x]
                numbers[x] = numbers[y]
                numbers[y] = temp

def Display(myList):
  for num in myList:
   print(num)

num_list = [5, 1, 8, 2]

Display(num_list)

Sort(num_list)

Display(num_list)

def PrintFirstItemThenFirstHalfThenSayHi100Times(int_list):
  print(int_list[0])

  middleIndex = len(int_list)/2
  index = 0

  while index < middleIndex:
      print(int_list[index])
      index += 1

  x = 0
  while x < 100:
      x += 1
      print("hi")
      
PrintFirstItemThenFirstHalfThenSayHi100Times(num_list)