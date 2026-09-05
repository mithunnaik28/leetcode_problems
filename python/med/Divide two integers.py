class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        count = 0
        while dividend >= divisor:
            temp = divisor
            current = 1

            while dividend >= temp + temp:
                temp = temp + temp
                current = current + current

            dividend = dividend - temp
            count = count + current

        if negative:
            count = -count

        if count > 2147483647:
            count = 2147483647

        return count
