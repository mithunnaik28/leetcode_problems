class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 1
        value = 1
        while value < n:
            value = 2**power
            power += 1
        if value == n:
            return True
        else:
            return False
