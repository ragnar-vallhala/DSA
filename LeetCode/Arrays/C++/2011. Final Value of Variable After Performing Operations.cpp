#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int ans{};
        for(int i{};i<operations.size();i++)
        {
            if(operations[i][0]=='-' || operations[i][2]=='-') ans--;
            else ans++;
        }
        return ans;
    }
};