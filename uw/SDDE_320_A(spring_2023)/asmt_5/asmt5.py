'''
Rod Cutting
You are given a rod of length 8. It has a price array [ 0, 1, 6, 2, 4, 3, 3, 2, 8 ]
Write the following class with these functions:
	class RodLengthCalculator:
  		def __init__(self, rod_length, price_array):
		
		def find_max_value_top_down_memoization(self) -> Tuple[int, List[int]]:
 		
		def find_max_value_bottom_up(self) -> Tuple[int, List[int]]:

The functions should return:
* Maximum value for selling a rod of length rodLength.
* The size(s) of the rod that fetch the maximum value you found above.
* For returning the sizes, your function should return an array of the cut rod sizes as the out parameter sizes, starting at index 0
Example:
* If you determine the best choice is to sell the rod of length 8 (no cuts), the sizes array will have 8 at index 0.
* If lengths are 4 and 4, the sizes array will have 4 at index 0, and 4 at index 1.
'''

from typing import Tuple, List

class RodLengthCalculator:
    def __init__(self, rod_length: int, price_array: List[int]):
        self.rod_length = rod_length
        self.price_array = price_array
        self.memo = [-1] * (rod_length + 1)
        self.sizes = [-1] * rod_length

    def find_max_value_top_down_memoization(self) -> Tuple[int, List[int]]:
        max_value = self._find_max_value_top_down_memoization(self.rod_length)
        return max_value, self.sizes[:max_value]

    def _find_max_value_top_down_memoization(self, rod_length: int) -> int:
        if rod_length == 0:
            return 0
        if self.memo[rod_length] != -1:
            return self.memo[rod_length]

        max_value = -1
        for i in range(1, rod_length+1):
            value = self.price_array[i] + self._find_max_value_top_down_memoization(rod_length - i)
            if value > max_value:
                max_value = value
                self.sizes[rod_length-1] = i
        self.memo[rod_length] = max_value
        return max_value

    def find_max_value_bottom_up(self) -> Tuple[int, List[int]]:
        max_values = [0] * (self.rod_length + 1)
        for i in range(1, self.rod_length+1):
            max_value = -1
            for j in range(1, i+1):
                value = self.price_array[j] + max_values[i-j]
                if value > max_value:
                    max_value = value
                    self.sizes[i-1] = j
            max_values[i] = max_value
        return max_values[self.rod_length], self.sizes

rod_length = 8
price_array = [0, 1, 6, 2, 4, 3, 3, 2, 8]

r = RodLengthCalculator(rod_length, price_array)

# Find max value using top-down dynamic programming with memoization
max_value, sizes = r.find_max_value_top_down_memoization()
print("Max value using top-down dynamic programming with memoization:", max_value)
print("Sizes of the cut rods:", sizes)

# Find max value using bottom-up dynamic programming
max_value, sizes = r.find_max_value_bottom_up()
print("Max value using bottom-up dynamic programming:", max_value)
print("Sizes of the cut rods:", sizes)
