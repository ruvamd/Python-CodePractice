rolodex={'a':12343,
         'b':45435,
         'c':89786,}
def callerId(lookupNumber):
    for name,num in rolodex.items():
        if num==lookupNumber:
            return name