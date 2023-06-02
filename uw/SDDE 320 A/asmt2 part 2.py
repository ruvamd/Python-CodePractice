from typing import Tuple

def two_sum(twoSumSource, target) -> Tuple[int, int]:
    # create a dictionary to store the complements of each number
    complements = {}
    
    # iterate over all numbers in the input array
    for i in range(len(twoSumSource)):
        # check if the complement of the current number is already in the dictionary
        if twoSumSource[i] in complements:
            # if yes, we've found a pair of numbers that add up to the target sum, so return their indices
            return (complements[twoSumSource[i]], i)
        else:
            # if no, add the complement of the current number to the dictionary
            complements[target - twoSumSource[i]] = i
    
    # if we've iterated over the entire array without finding a pair of numbers that add up to the target sum, return (-1, -1)
    return (-1, -1)

# example input array and target sum
twoSumSource = [2, 7, 11, 15]
target = 9

# call two_sum() function
result = two_sum(twoSumSource, target)

# print result
print(result)
