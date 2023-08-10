#!/usr/bin/env python3
class animal:
    def __init__(self,**kwargs):
        self._type=kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name=kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound=kwargs['sound'] if 'sound' in kwargs else 'rawr'
def type(self):
    return self._type
def type(self):
    return self._name
def type(self):
    return self._sound
def printAnimal(o):
    if not isinstance(o,animal):
        raise TypeError('printAnimal():requires an animal')
    print('the {} is named "{}" and says "{}".'.format(o.type(),o.name(),o.sound()))

def main():
    a0=animal(type='kitten',name='fluffy',sound='rwar')
    a1=animal(type='duck',name='donald',sound='quack')
    printAnimal(a0)
    printAnimal(a1)
    printAnimal(animal(type='velociraptor',name='veronica',sound='hello'))
    printAnimal(animal())
main()