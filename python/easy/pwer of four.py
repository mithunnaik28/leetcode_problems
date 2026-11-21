class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(n):
            if n == **i:
                return True 
            elif n < 4**i:
                return False
