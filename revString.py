def strReverse(aString):
    revString=''
    for ch in aString:
        revString=ch+revString
    print(revString)
strReverse('hello')