def separateNames(names):
    for fullName in names:
        for name in fullName.split(''):
            yield name
def getLongest(namelist):
    fullNames=(name.strip() for name in open(namelist))
    names=separateNames(fullNames)
    lengths=((name,len(name)) for name in names)
    return max(lengths,key=lambda x:x[1])
    