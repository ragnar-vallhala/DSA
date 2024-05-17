#include <bits/stdc++.h>
using namespace std;


void printArray(int arr[], int n)
{
    for(int i{};i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}


int* sort(int arr[], int n)
{
    for(int i{1};i<n;i++)
    {
        int key = arr[i];
        int j = i-1;
        while(j>=0 && arr[j]>key)
        {
            int k = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = k;
            j--;
        }
    }
    return arr;
} 


int main()
{
    int arr[] = {2,5,9,0,5,6,8,85,12,8,10};
    int n = 11;
    printArray(arr,n);
    int* sortedArray = sort(arr,n);
    printArray(arr,n);
    return 0;
}