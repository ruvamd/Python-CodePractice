def listBenefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def buildSentence(benefit):
    return f'{benefit} is a benefit of functions!'

def nameTheBenefitsOfFunctions():
    for benefit in listBenefits():
        print(buildSentence(benefit))

nameTheBenefitsOfFunctions()