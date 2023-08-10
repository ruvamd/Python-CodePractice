class circuitBreaker:
    def __init__(self,maxAmps):
        self.capacity=maxAmps
        self.load=0
    def connect(self,amps):
        if self.load+amps>self.capacity:
            raise Exception('connect will exceed capacity')
        elif self.load+amps<0:
            raise Exception('connect will cause negative load')
        else: 
            self.load+=amps
cb=circuitBreaker(20)