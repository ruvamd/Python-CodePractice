def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args,**kwds):
            return multiplier*old_function(*args,**kwds)    
        return new_function
    return multiply_generator
@multiply(3)
def return_num(num):
    return_num
return_num(5)