class Solution:
    def mirrorDistance(self, n: int) -> int:
        if 1<=n:
            list1=[int(str(n)[::-1]),n] 
            mr_distance= max(list1)-min(list1)
            return mr_distance
