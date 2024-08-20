# max heap
def insert(heap:list, num:int)->list:
    heap.append(num)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent]<heap[i]:
            temp = heap[i]
            heap[i] = heap[parent]
            heap[parent] = temp
            i=parent
        else:
            break
    return heap

def heapify(arr:list)->list:
    heap = []
    for i in range(len(arr)):
        heap = insert(heap, arr[i])
    return heap


def delete(heap:list, value:int)->list:
    index=-1
    for i in range(len(heap)):
        if heap[i]==value:
            index=i
    if index==-1:
        raise f"Value {value} not found in the heap."
    
    heap[index] = heap[len(heap)-1]
    del heap[len(heap)-1]
    
    while index<len(heap)-1:    
        child = 2*index + 1
        
        if heap[child]>heap[index]:
            temp = heap[child]
            heap[child] = heap[index]
            heap[index] = temp
    
    return heap

def makeHeap(heap: list, i: int, n:int) -> list:
    if i >= n:
        return heap

    while i < n:
        child1 = 2 * i + 1
        child2 = 2 * i + 2
        largest = i

        if child1 < n and heap[child1] > heap[largest]:
            largest = child1
        if child2 < n and heap[child2] > heap[largest]:
            largest = child2

        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest
        else:
            break

    return heap


def heapSort(heap:list)->list:
    heap = makeHeap(heap, len(heap)-1, len(heap))
    for i in range(len(heap)-1, 0, -1):
        temp = heap[0]
        heap[0] = heap[i]
        heap[i] = temp
        heap = makeHeap(heap, 0, i)

    return heap





heap=[]
arr = [1,2,3,4,5,6,7,8]
print("Array: ",arr)
heap = heapify(arr)
print("Heap:  ",heap)
heap = heapSort(heap)
print("Sorted:",heap)
