class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed_external = ""
        for i in s:
            if i.isalnum():
                removed_external += i.lower()
        if removed_external == removed_external[::-1]:
            return True
        else:
            return False
