class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        p1=max(x,z)-min(x,z)
        p2=max(y,z)-min(y,z)
        if p1 < p2:
            return 1
        elif p1 > p2:
            return 2
        elif p1 == p2:
            return 0
