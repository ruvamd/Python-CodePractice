def mixAndCook():
    print('take eggs')
    print('broke eggs and put in stove')
    print('put papper')
    print('cover with cup')
    print('wait five minutes')
    print('turn off the stove')
def makeOmelette(ingredient):
    mixAndCook()
    omelette=f'a {ingredient} omelette'
    return omelette
def makePancake():
    mixAndCook()
    pancake='a delicious pancake'
    return pancake
def fancyOmelette(*ingredients):
    mixAndCook()
    omelette=f'a fency omelette with {len(ingredients)} ingredients'
    return omelette
