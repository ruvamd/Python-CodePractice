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
    omelette='a {} omelette'.format(cheese)
    return omelette
def makePancake():
    mixAndCook()
    pancake='a {} pancake'.format(cheese)
    return pancake
def fancyOmelette(*ingredients):
    mixAndCook()
    omelette='a fency omelette with {} ingredients'.format(len(ingredients))
    return omelette
