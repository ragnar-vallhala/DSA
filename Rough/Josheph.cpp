#include<iostream>

int Josheph(int n,int k);

int main()
{
    int n,k;
    std::cin>>n>>k;
    std::cout<<Josheph(n,k)<<std::endl;
    return 0;
}


int Josheph(int n,int k)
{
    if(n==1) return 0;
    else return (Josheph(n-1,k)+k)%n;
}