def sum(values, memo={}):
    if not values: # base case for an empty list
        return 0
    if values in memo: # check if we have seen this list before
        return memo[values]
    result = values[0] + sum(values[1:], memo) # recursive case for a non-empty list
    memo[values] = result # memoize the result for future calls
    return result

print(sum(tuple([1, 2, 3, 4, 5])))