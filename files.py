myFile=open('scores.txt','w')

print('name '+myFile.name)
print('mode '+myFile.mode) 
myFile.write('abc')
myFile.close()
myFile=open('scores.txt','r')
print('my one line: '+myFile.readline())
myFile.seek(0)
for line in myFile:
    newHighScore=line.replace('abc','cba')
    print(newHighScore)
print('reading... '+myFile.read())
