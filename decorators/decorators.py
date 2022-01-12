def repeater(old_function):
    def new_function(*args,**kwds):
        old_function(*args,**kwds)
        old_function(*args,**kwds)
    return new_function