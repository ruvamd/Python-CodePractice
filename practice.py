import os,glob

os.chdir('/Users/vadim/Documents/python\ lynda\ files/my\ practice\ files')
for file in glob.glob('*.PNG'):
    print(file)
