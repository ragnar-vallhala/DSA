#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans;
        for(int i{};i<n;i++)
        {
            ans.push_back(nums[i]);
            ans.push_back(nums[i+n]);
        }
        return ans;
    }
};