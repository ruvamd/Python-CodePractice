from typing import Tuple

# 1
def find_intersection(array_one, array_two) -> list:
    # initialize empty list to store shared values
    shared_values = []
    
    # iterate over all elements in array one
    for i in range(len(array_one)):
        # check if current element is in array two
        if array_one[i] in array_two:
            # if yes, add to shared values list and remove from array two
            shared_values.append(array_one[i])
            array_two.remove(array_one[i])
    
    # return shared values list
    return shared_values

# example input arrays
array_one = [3, 4, 5, 1, 2]
array_two = [5, 4, 3, 7, 6]

# call find_intersection() function
shared_values = find_intersection(array_one, array_two)

# print shared values list
print(shared_values)

