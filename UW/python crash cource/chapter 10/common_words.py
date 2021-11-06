def count_words(filename):
    with open(filename) as f:
        data=f.read()
        words=data.split()
        number_of_words=words.count('at')
        print(f"the file {filename} has {number_of_words} 'at' words")

filenames=['UW/python crash cource/chapter 10/moby_dick.txt',
           'UW/python crash cource/chapter 10/little_women.txt']
for name in filenames:
    count_words(name)