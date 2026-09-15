class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        int_in_list = list(str(n))
        total = 0
        for i in set(int_in_list):
            count_numbers = int_in_list.count(i)
            total += int(count_numbers)*int(i)
        return total
