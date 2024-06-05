import heapq

def mergeKSorted(lists:list[list[int]])->list[int]:
    minHeap = []
    
    '''
    Time Complexity of code below is O(k)
    '''
    for i in range(len(lists)):
        if len(lists[i])>0:
            heapq.heappush(minHeap,(lists[i][0],i,0))
    
    merged=[]
    
    '''
    Time Complexity of code below is O(n*logk)
    n is for the while loop which runs untill whole heap is not empty thus running for n  times
    after each removal of element there is at max one insertion in the heap this process takes logk time
    '''
    while len(minHeap)>0:
        element,listIndex,elementIndex = heapq.heappop(minHeap)
        merged.append(element)
        if elementIndex<len(lists[listIndex])-1:
            elementIndex+=1
            heapq.heappush(minHeap,(lists[listIndex][elementIndex],listIndex,elementIndex))
    
    return merged

lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(mergeKSorted(lists))