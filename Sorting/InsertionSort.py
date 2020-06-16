def insertionSort(ar):
    for i in range(len(ar)):
        check=i
        while check > 0 and ar[check-1] > ar[i]:
            temp=ar[i]
            ar[i]=ar[check-1]
            ar[check-1]=temp
            i=check-1
            check-=1

if __name__ == '__main__':
    arr=input('Enter numbers to sort separated by space: ').split(' ')
    arr=list(map(lambda x:int(x),arr))
    insertionSort(arr)
    print(arr)