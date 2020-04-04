def main():
    list=[3,45,23,7,8,90,4,55]
    bubbleSort(list)
    print('Result:',list)

def bubbleSort(dataset):
    n=len(dataset)
    for i in range(n):
        for j in range(0,n-i-1):
            if dataset[j]>dataset[j+1]:                
                dataset[j],dataset[j+1]=dataset[j+1],dataset[j]
        print('Current state:',dataset)

if __name__=='__main__':
    main()