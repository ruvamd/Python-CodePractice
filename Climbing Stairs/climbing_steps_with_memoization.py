def step_ways(steps, memo={}):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    elif steps in memo:
        return memo[steps]
    else:
        memo[steps] = step_ways(steps - 1, memo) + step_ways(steps - 2, memo) + step_ways(steps - 3, memo)
        return memo[steps]

print(step_ways(4))
