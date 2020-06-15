def insertion_sort(buckets):
    for k in range(len(buckets)):
        anchor=k
        while anchor > 0 and buckets[anchor-1] > buckets[k]:
            temp=buckets[k]
            buckets[k]=buckets[anchor-1]
            buckets[anchor-1]=temp
            k=anchor-1
            anchor-=1
    return buckets


def bucket_sort(arr,buckets):
    for i in range(len(arr)):
        if len(buckets[int(arr[i]*len(arr))])==0:
            buckets[int(arr[i]*len(arr))].append(arr[i])
        else:
            buckets[int(arr[i] * len(arr))].append(arr[i])


if __name__ == '__main__':
    arr=[0.25,0.36,0.58,0.41,0.29,0.22,0.45,0.79,0.01,0.69]
    buckets = [[] for i in range(len(arr))]
    print('before sorting:',arr)
    bucket_sort(arr,buckets)
    j=0
    for i in range(len(buckets)):
        if len(buckets[i])>1:
            res=insertion_sort(buckets[i])
            for element in res:
                arr[j]=element
                j+=1
        elif len(buckets[i])==1:
            arr[j]=buckets[i].pop()
            j+=1
    print('Sorted array: ',arr)