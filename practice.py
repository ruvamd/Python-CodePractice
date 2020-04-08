vfile=open('vf.txt','w')

print('name '+vfile.name)
print('mode '+vfile.mode)

vfile.write('vadim')
vfile.close()
vfile=open('vf.txt','r')
print('one line '+vfile.readline())
vfile.seek(0)

for line in vfile:
    newName=line.replace('vadim','midav')
    print(newName)
print('reading...'+vfile.read())


