#include<iostream>
#include<string>

bool palindrome(std::string s, int a, int b);

int main()
{
    std::string s;
    std::cin>>s;
    std::cout<<palindrome(s,0, s.length()-1)<<std::endl;
    return 0;
}
bool palindrome(std::string s,int a, int b)
{
    if(a>=b) return true;
    return s[a]==s[b] && palindrome(s,a+1,b-1);
}