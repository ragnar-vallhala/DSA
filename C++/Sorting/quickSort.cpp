#include <bits/stdc++.h>
using namespace std;

template <typename T>
int partition(vector<T> &arr, int l, int h)
{
    int i = l;
    int j = h;
    while(i<j)
    {
        int key = arr[i];
        while(arr[i]<=key)i++;
        while(arr[j]>key)j--;
        if(i<j)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[l];
    arr[l] = arr[j];
    arr[j] = temp;
    return j;
}

template <typename T>
void printVector(vector<T> &arr)
{
    for(int i{};i<arr.size();i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

template <typename T>
void quickSort(vector<T> &arr, int l, int h)
{
    if(arr.size()<=1)
        return;
    
    int key = partition(arr,l,h);
    if(l<key-1)
        quickSort(arr,l,key-1);
    if(h>key+1)
        quickSort(arr,key+1,h);
}

int main()
{
    vector<int> arr = {2,5,9,0,5,6,8,85,12,8,10};
    printVector(arr);
    quickSort(arr,0,arr.size());
    printVector(arr);
   
}