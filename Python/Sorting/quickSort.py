def partition(arr,l,h):
    if h<l:
        raise IndexError
    
    i=l
    j=h
    while i < j:
        key = arr[i]
        
        while arr[i]<=key:
            i+=1

        while arr[j]>key:
            j-=1
        
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[l], arr[j] = arr[j], arr[l]
    return (arr,j)


def quickSort(arr,l,h):
    if len(arr)<=1:
        return arr
    
    arr,key = partition(arr,l,h)
    if key-1>l:
        arr = quickSort(arr,l,key-1)
    if key+1<h:
        arr = quickSort(arr,key+1,h)
    return arr 

arr = [2,5,9,0,5,6,8,85,12,8,10]

print(quickSort(arr,0,len(arr)-1))
                
    
    