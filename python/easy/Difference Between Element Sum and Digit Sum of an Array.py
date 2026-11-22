class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        digitSum = 0
        for i in nums:
            if i >= 10:
                j = i
                while j>=1: 
                    digitSum += j%10
                    j //=10
            else:
                digitSum += i
        return abs(sum(nums)-digitSum)
