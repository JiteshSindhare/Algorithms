
def mergeSort(arr,low,high):
    mid=int((len(arr))/2)
    L=arr[:mid]
    R=arr[mid:]
    #print(len(L)*' ','/',len(R)*' ',"\ ")
    #vis.append((L,R))
    #visualize(vis)
    if len(arr)>1:
        mergeSort(L,low,mid)
        mergeSort(R,mid,high)

        i,j,k=0,0,0

        # Merging
        while i<len(L) and j<len(R):
            if L[i]>R[j]:
                arr[k]=R[j]
                j+=1
                k+=1
            else:
                arr[k] = L[i]
                i += 1
                k += 1

        while i<len(L):
            arr[k]=L[i]
            k+=1
            i+=1
        while j<len(R):
            arr[k]=R[j]
            k+=1
            j+=1


if __name__ == '__main__':
    arr=input("Enter numbers separated by comma: ").split(',')
    arr=list(map(lambda x:int(x),arr))
    print(arr)
    mergeSort(arr,0,len(arr))
    print(arr)