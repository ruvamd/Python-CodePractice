def main():
    game=['scissors','rock','paper']
    del game[1:5]
    #x=game.pop()
    printList(game)
def printList(o):
    for i in o:
        print(i,end=' ',flush=True)
    print()
if __name__=='__main__':main()
