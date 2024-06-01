#include <bits/stdc++.h>
using namespace std;

void insert(vector<int> &heap, int value)
{
    heap.push_back(value);
    int i = heap.size() - 1;
    while( i>0)
    {
        int parent = (i-1)/2;
        if(heap[parent]<heap[i])
        {
            int temp = heap[i];
            heap[i] = heap[parent];
            heap[parent] = temp;
            i = parent;
        }
        else
        {
            break;
        }
    }

}

vector<int> makeHeap(int arr[], int n)
{
    vector<int> heap{};
    for(int i=0;i<n;i++)
    {
        insert(heap,arr[i]);
    }
    return heap;
} 

void heapify(vector<int> &heap, int size, int i)
{
    if(i>size)
        return;
    
    while(i<size)
    {
        int left = 2*i+1;
        int right = 2*i+2;
        int largest = i;
        if(left<size && heap[largest]<=heap[left])
            largest=left;
        if(right<size && heap[largest]<=heap[right])
            largest=right;
        if (largest!=i)
        {
            int temp = heap[i];
            heap[i] = heap[largest];
            heap[largest] = temp;
            i = largest;
        }
        else
            break;
    }
}

void del(vector<int> &heap, int index)
{
    if(index>=heap.size())
    {
        return;
    }

    heap[index] = heap[heap.size()-1];
    heap.pop_back();
    heapify(heap,heap.size(),index);

}

void print(vector<int>& heap)
{
    for(int i=0;i<heap.size();i++)
    {
        cout<<heap[i]<<" ";
    }
    cout<<endl;
}

void heapSort(vector<int> &heap)
{
    for(int i=heap.size()-1;i>0;i--)
    {
        int temp = heap[0];
        heap[0] = heap[i];
        heap[i] = temp;
        heapify(heap,i,0);
    }
}
int main()
{
    int arr[] = {1,1,-5,8,20,35,13,-11,3,4};
    vector<int> heap = makeHeap(arr,10);
    print(heap);
    heapSort(heap);
    print(heap);
}