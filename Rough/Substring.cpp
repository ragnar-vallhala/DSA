#include<bits/stdc++.h>
using namespace std;


void substring(string &s, int &count, int i = 0, string sub = "");

int main()
{
    string s;
    cin>>s;
    int n = 0;
    substring(s,n);
    cout<<"number of substrings "<<n<<endl;  
    return 0;
}


void substring(string &s, int &count,  int i, string sub)
{
    if(i>=s.length())
    {
        cout<<sub<<endl;
        count++;
        return;
    }

    substring(s,count, i+1,sub);
    substring(s,count, i+1,sub+s[i]);
}