chris={}
chris['first']='chris'
chris['last']='helen'

sahra={'first':'sahra','last':'ingvar'}

people=[chris,sahra]
people.append({'first':'bill','last':'gates'})
presenters=people[0:2]

print(people)
print(presenters)
print(len(presenters))