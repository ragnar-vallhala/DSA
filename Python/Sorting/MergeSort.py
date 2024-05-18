def merge(arr1:list[int],arr2:list[int])->list[int]:
    arr=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
            
    while i<len(arr1):
        arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr.append(arr2[j])
        j+=1
    
    
    return arr


def sort(arr):
    
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        sortedArray = merge(left, right)
        return sortedArray

arr = [2,5,9,0,5,6,8,85,12,8,10]
print(arr)
arr = sort(arr)
print(arr)
            
     
    