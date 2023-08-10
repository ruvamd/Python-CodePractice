import tempfile

tempFile=tempfile.TemporaryFile()
tempFile.write(b'save:5758698')
tempFile.seek(0)
print(tempFile.read())
tempFile.close()