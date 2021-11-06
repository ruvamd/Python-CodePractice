def count_words(filename):
    #count the approximate words in the file
    try:
        with open(filename) as f:
            data=f.read()
    except FileNotFoundError:
        print(f'the file {filename} does not exist')
        # pass
    else:
        words=data.split()
        number_of_words=len(words)
        print(f'the {filename} has {number_of_words} number of words')

# filenames='UW/python crash cource/chapter 10/alice.txt'
filenames=['UW/python crash cource/chapter 10/alice.txt',
           'siddhartha.txt',
           'UW/python crash cource/chapter 10/moby_dick.txt',
           'UW/python crash cource/chapter 10/little_women.txt']
for filename in filenames:
    count_words(filename)
    