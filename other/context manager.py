from contextlib import contextmanager
@contextmanager
def simpleContextManager(obj):
    try:
        obj.someProperty +=1
        yield
    finally:
        obj.someProperty -=1
class someObj(object):
    def __init__(self,arg):
        self.someProperty=arg 
        