def main():
    x=0
    while (x<5):
        print(x)
        x=x+1
    for x in range(5,10):
        print(x)
    days=['mon','tue','wed','thu','fri','sat','sun']
    for d in days:
        print(d)   
    for x in range(5,10):
        #if (x==7):break
        #print(x)   
        if (x%2==0):continue
        print(x)  
main()