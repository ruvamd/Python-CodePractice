def step_ways(steps):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    else:
        return step_ways(steps - 1) + step_ways(steps - 2) + step_ways(steps - 3)

print(step_ways(4))
