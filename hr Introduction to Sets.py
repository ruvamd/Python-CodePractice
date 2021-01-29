#---alt code---
#sdh=set([154,161,167,170,171,174,176,182])
# sdhsum=sum(sdh)
# tndh=len(sdh)
# avr=sdhsum/tndh
# print(avr)

sdh=[154,161,167,170,171,174,176,182]

def average(arrray):
    return sum(set(arrray))/len(set(arrray))

print(average(sdh))