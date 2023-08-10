def main():
    f=open('lines.txt')
    for line in f:  
        print(line.rstrip())
main()