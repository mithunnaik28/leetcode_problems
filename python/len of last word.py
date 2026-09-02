class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list1 = [i for i in s.split()]
        return len(list1[-1])
