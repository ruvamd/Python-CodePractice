def main():
    seq=range(11)
    #seq2=[x*2 for x in seq]
    seq2=[x for x in seq if x % 3 !=0]
    printList(seq)
    printList(seq2)
def printList(o):
    for x in o:print(x,end='')
    print()
main()