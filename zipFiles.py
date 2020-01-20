import zipfile
zip=zipfile.ZipFile('Archive.zip','r')
print(zip.namelist())
for meta in zip.infolist():
    print(meta)
print(zip.read('scores.txt'))
zip.extract('scores.txt')