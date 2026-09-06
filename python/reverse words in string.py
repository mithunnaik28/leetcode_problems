class Solution:
    def reverseWords(self, s: str) -> str:
        out_put = ""
        for i in s.split():
            out_put += i[::-1] + " "
        return out_put.strip()
