class Solution:
    def reverse(self, x: int) -> int:
        reverse1 = int(str(abs(x))[::-1])
        if x < 0:
            reverse1 = -reverse1
        if reverse1 < -2**31 or reverse1 > 2**31 - 1:
            return 0
        return reverse1
