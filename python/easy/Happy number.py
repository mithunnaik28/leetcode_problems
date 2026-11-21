class Solution:
    def isHappy(self, n: int) -> bool:
        check = n
        while check > 9:
            x = 0
            for i in str(check):
                x += int(i)**2
            check = x
            if check == n:
                break
        if check == 1 or check == 7:
            return True
        else:
            return False
