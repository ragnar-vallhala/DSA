function insert(heap,num)
{
    heap.push(num);
    let i = heap.length - 1;
    while(i>0)
    {
        let parent = Math.floor((i-1)/2);
        if(heap[parent] < heap[i]){
            let temp = heap[parent];
            heap[parent] = heap[i];
            heap[i] = temp;
            i = parent;
        }
        else{
            break;
        }
    }
    return heap;
}

function makeHeap(arr){
    let heap = [];
    for(let i = 0; i < arr.length; i++){
        heap = insert(heap,arr[i]);
    }
    return heap;
}

function heapfy(heap,index,size){
    
    if (index > size){
        return heap;
    }

    while(index < size){
        let left = 2 * index + 1;
        let right = 2 * index + 2;
        let largest = index;

        if(left<size && heap[largest]<heap[left]){
            largest = left;
        }
        if(right<size && heap[largest]<heap[right]){
            largest = right;
        }
        if(largest!=index){
            let temp = heap[largest]
            heap[largest] = heap[index]
            heap[index] = temp
            index = largest
        }
        else{
            break;
        }
    }
    return heap;
}

function heapSort(arr)
{
    let heap = makeHeap(arr);

    for(let i = heap.length-1;i > 0; i--)
    {
        let temp = heap[i];
        heap[i] = heap[0];
        heap[0] = temp;
        heap = heapfy(heap,0,i);
    }
    return heap;
}

let arr = [2,3,2,0,6,-3,45,-65]
console.log(arr)
let arr2 = heapSort(arr)
console.log(arr2)
