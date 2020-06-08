def swap(arr,k,i):
    temp = arr[k]
    arr[k] = arr[i]
    arr[i] = temp

def partition(arr,low,high):
    pivot=arr[high]
    #pivot_index= high
    i=low-1

    for k in range(low,len(arr)-1):
        if arr[k]<pivot :
            i+=1
            temp=arr[k]
            arr[k]=arr[i]
            arr[i]=temp

    temp = arr[high]
    arr[high] = arr[i + 1]
    arr[i + 1] = temp

    return (i+1)

def quickSort(arr,low,high):

    if low<high :
        pi=partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

if __name__ == '__main__':
    arr=input('Enter numbers to sort separated by comma:').split(',')
    arr=list(map(lambda x:int(x),arr))
    print(arr)
    quickSort(arr,0,len(arr)-1)
    print(arr)