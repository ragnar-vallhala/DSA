class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count=0
        for i in nums:
            if i%3==0:
                count+=1
        return len(nums)-count