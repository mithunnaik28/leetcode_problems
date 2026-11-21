class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority,num = 0,0
        for i in set(nums):
            count = nums.count(i)
            if count >= majority:
                majority = count
                num = i
        return num
