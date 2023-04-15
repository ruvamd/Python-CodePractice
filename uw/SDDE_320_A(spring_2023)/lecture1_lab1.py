import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = []
    right = []
    middle = []
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            middle.append(element)
    return quicksort(left) + middle + quicksort(right)

arr = [3, 5, 2, 8, 1, 9, 4, 7, 6]
sorted_arr = quicksort(arr)
print(sorted_arr)
