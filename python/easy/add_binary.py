class Solution(object):
    def addBinary(self, a, b):
        r_a = a[::-1]
        r_b = b[::-1]

        b_sum = ""
        carry = 0

        for i in range(max(len(a), len(b))):
            x = int(r_a[i]) if i < len(r_a) else 0
            y = int(r_b[i]) if i < len(r_b) else 0

            total = x + y + carry

            b_sum += str(total % 2)
            carry = total // 2

        if carry:
            b_sum += str(carry)

        return b_sum[::-1]
