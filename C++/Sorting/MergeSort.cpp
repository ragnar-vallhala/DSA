#include <bits/stdc++.h>
using namespace std;

vector<int> merge(vector<int> arr1,  vector<int> arr2)
{
    vector<int> arr3{};
    int i{},j{};
    while(i<arr1.size() && j<arr2.size())
    {
        if(arr1[i]<arr2[j])
        {
            arr3.push_back(arr1[i]);
            i++;
        }
        else
        {
            arr3.push_back(arr2[j]);
            j++;
        }
    }

    while(i<arr1.size())
    {
        arr3.push_back(arr1[i]);
        i++;
    }
    while(j<arr2.size())
    {
        arr3.push_back(arr2[j]);
        j++;
    }

    return arr3;
}

void print(vector<int> arr)
{
    for(int i{};i<arr.size();i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
vector<int> sort(vector<int> arr)
{
    if(arr.size()<=1)
    {
        return arr;
    }
    else
    {
        int mid = arr.size()/2;
        vector<int> left = sort(vector<int>(arr.begin(),arr.begin()+mid));
        vector<int> right = sort(vector<int>(arr.begin()+mid,arr.end()));
        return merge(left, right);
    }
}
int main()
{
    vector<int> a{2,5,1,0,9,10};    
    vector<int> c = sort(a);
    print(a);
    print(c);
}