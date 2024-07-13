# def maximum(arr:list, start:int, end:int)->int:
#     if end>len(arr) or  start>end:
#         return 0
#     elif start==end:
#         return arr[start]
#     else:
#         return max(sum(arr[start:end]),max(maximum(arr,start+1,end), maximum(arr,start,end-1)))

# arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

# print(maximum(arr,0,len(arr)-1))




def maximum(arr:list, start:int, end:int)->tuple[int,int,int]:
    if end<0 or  start>end or start>=len(arr):
        return (0,-1,-1)
    elif start==end:
        return (arr[start],start,start)
    else:
        s1 = sum(arr[start:end])
        s2,a2,b2 = maximum(arr,start+1,end)
        s3,a3,b3 = maximum(arr,start,end-1)
        if s1>s2 and s1>s3:
            return (s1,start,end-1)
        elif s2>s1 and s2>s3:
            return (s2,a2,b2)
        else:
            return (s3,a3,b3)
        


def kadane(arr):
    if not arr:
        return (0, -1, -1)

    max_sum = current_sum = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

    return (max_sum, start, end)




arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

print(maximum(arr,0,len(arr)-1))
print(kadane(arr))