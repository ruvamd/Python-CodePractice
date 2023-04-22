import time
import random
from typing import List

class QuickSort:
    @staticmethod
    def pick_pivot_first(start:int, end:int):
        return start

    @staticmethod
    def pick_pivot_middle(start:int, end:int):
        return (start + end) // 2

    @staticmethod
    def quick_sort(A:List[int], start:int, end:int, pick_pivot_func):
        if start >= end:
            return
        pivot_index = pick_pivot_func(start, end)
        pivot_final_index = QuickSort.partition(A, start, end, pivot_index)

        QuickSort.quick_sort(A, start, pivot_final_index-1, pick_pivot_func)
        QuickSort.quick_sort(A, pivot_final_index+1, end, pick_pivot_func)

    @staticmethod
    def partition(A:List[int], start:int, end:int, pivot_index:int):
        pivot_value = A[pivot_index]
        A[start], A[pivot_index] = A[pivot_index], A[start]

        left_most_bigger_index = start + 1
        for i in range(start+1, end+1):
            if A[i] < pivot_value:
                A[i], A[left_most_bigger_index] = A[left_most_bigger_index], A[i]
                left_most_bigger_index += 1
        pivot_final_index = left_most_bigger_index - 1
        A[start], A[pivot_final_index] = A[pivot_final_index], A[start]

        return pivot_final_index


# Create a sorted array of 10,000 elements
sorted_arr = list(range(10000))

# Create an unsorted array of 10,000 elements
unsorted_arr = list(range(10000))
random.shuffle(unsorted_arr)

# Time quicksort with pick_pivot_first function
start = time.time()
QuickSort.quick_sort(unsorted_arr, 0, len(unsorted_arr)-1, QuickSort.pick_pivot_first)
end = time.time()
print(f"Time taken for quicksort with pick_pivot_first function: {(end-start) * 1000} ms")

# Time quicksort with pick_pivot_middle function
start = time.time()
QuickSort.quick_sort(unsorted_arr, 0, len(unsorted_arr)-1, QuickSort.pick_pivot_middle)
end = time.time()
print(f"Time taken for quicksort with pick_pivot_middle function: {(end-start) * 1000} ms")
