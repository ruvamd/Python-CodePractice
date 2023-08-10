cheese='cheddar'
def mixAndCook():
    print('take eggs')
    print('broke eggs and put in stove')
    print('put papper')
    print('cover with cup')
    print('wait five minutes')
    print('turn off the stove')
def makeOmelette():
    global cheese
    cheese='swiss'
    mixAndCook()
    omelette=f'a {cheese} omelette'
    return omelette
def makePancake():
    mixAndCook()
    pancake=f'a {cheese} pancake'
    return pancake
def fancyOmelette(*ingredients):
    mixAndCook()
    omelette=f'a fency omelette with {len(ingredients)} ingredients'
    return omelette
