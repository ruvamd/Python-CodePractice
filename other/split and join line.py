string='this is a string'

def split_and_join(line):
    # line=string.split(' ')
    # line='-'.join(line)
    # return line

#alternative code
    return '-'.join(line.split())

print(split_and_join(string))