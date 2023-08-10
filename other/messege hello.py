import platform

def main():
    message()
print('hello,world.\n')

def message():
    print(f'this is python version {platform.python_version()}\n')
    print('line 2')
    if False:
        print('line 3')
    else:
        print('not true\n')
main()