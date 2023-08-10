import itertools

election={1:'barb',2:'karen',3:'erin'}
for p in itertools.permutations(election.values()): 
    print(p)
print()

colors=['red','blue','purple','orange','yellow','pink']
for c in itertools.combinations(colors,3):
    print(c)