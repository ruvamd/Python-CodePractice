def mixAndCook():
    print('take eggs')
    print('broke eggs and put in stove')
    print('put papper')
    print('cover with cup')
    print('wait five minutes')
    print('turn off the stove')
def makeOmelette(ingredient):
    mixAndCook()
    omelette='a {} omelette'.format(ingredient)
    return omelette
def makePancake():
    mixAndCook()
    pancake='a delicious pancake'
    return pancake
def fancyOmelette(*ingredients):
    mixAndCook()
    omelette='a fency omelette with {} ingredients'.format(len(ingredients))
    return omelette
