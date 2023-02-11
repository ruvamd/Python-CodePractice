def sum(values):
    if not values: # base case for an empty list
        return 0
    return values[0] + sum(values[1:]) # recursive case for a non-empty list

print(sum([1, 2, 3, 4, 5]))

