/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let ans=0;
    nums.sort();
    let last=0;
    for(let i=0;i<nums.length-1;i++)
    {
        if(nums[i]==nums[i+1]) last++;
        else{
            ans+=last*(last+1)/2;
            last=0;
        }
    }
    ans+=last*(last+1)/2;
    return ans;
};