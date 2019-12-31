import platform

def main():
    message()
#print('hello,world.')
def message():
    print('this is python version {}'.format(platform.python_version()))
    print('line 2')
    if False:
        print('line 3')
    else:
        print('not true')
main()