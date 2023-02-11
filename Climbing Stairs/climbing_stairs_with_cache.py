def step_ways_cached(steps):
    cache = {}
    def step_ways(steps):
        if steps < 0:
            return 0
        elif steps == 0:
            return 1
        elif steps in cache:
            return cache[steps]
        else:
            cache[steps] = step_ways(steps - 1) + step_ways(steps - 2) + step_ways(steps - 3)
            return cache[steps]
    return step_ways(steps)

print(step_ways_cached(4))


