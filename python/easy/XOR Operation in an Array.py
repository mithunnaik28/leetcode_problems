class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = start
        for i in range(start+2,start+(n*2),2):
            xor ^= i
        return xor
