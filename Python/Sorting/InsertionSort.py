def sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and arr[j]>key:
            p = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = p
            j-=1
    return arr
arr = [2,5,9,0,5,6,8,85,12,8,10]
print(arr)
arr = sort(arr)
print(arr)