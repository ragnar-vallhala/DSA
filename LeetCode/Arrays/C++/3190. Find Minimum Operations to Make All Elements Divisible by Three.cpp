#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int num{};
        for(auto i:nums)
        {
            if(i%3==0) num++;
        }
        return nums.size()-num;
    }
};