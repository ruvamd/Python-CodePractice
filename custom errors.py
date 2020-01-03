class electricError(Exception):
    def __init__(self,device,problem):
        self.device=device
        self.problem=problem
    def __str__(self):
        return f'the {self.device} is {self.problem}!'
class plumbingError(Exception):
    def __init__(self,device,problem):
        self.device=device
        self.problem=problem
    def __str__(self):
        return f'the {self.device} is {self.problem}!'
def causeError(errorType):
    if errorType=='electrical':
        raise electricError('circuit breaker','overloaded')
    elif errorType=='plumbing':
        raise plumbingError('dishwasher','spraing water')
try:
    causeError('electrical')
except electricError as e:
    print(e)
    print('fix it myself')
except plumbingError as e:
    print(e)
    print('call the plumber')
    