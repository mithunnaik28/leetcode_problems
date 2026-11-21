class Solution:
    def fib(self, n: int) -> int:
        fib = 0
        f_1 = 1
        for i in range(n):
            fib,f_1 = f_1, fib + f_1
        return fib
        
