def sim_global():
    return {"size": "small", "length": 10}


b = sim_global()["size"]
assert b == "small"


def tryit(globals):
    a = globals()
    return "in try", a["size"]


assert tryit(sim_global) == ("in try", "small")
