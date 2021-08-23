import numpy

''' 
input row 2 and column 2
2 2
1 2
3 4
'''
# my_array = numpy.array([[1,2,3],[4,5,6]])
# print(numpy.transpose(my_array))
# print(my_array.flatten())

array=numpy.array([input().split() for y in range(int(input().split()[0]))], int)
print(numpy.transpose(array),array.flatten(), sep="\n")

