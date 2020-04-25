def main():
    seq1=range(11)
    seq2=[x for x in seq1 if x % 3 !=0]
    
    printList(seq1)
    printList(seq2)

def printList(o):
    for x in o:
        print(x,end='')
    print()
main()