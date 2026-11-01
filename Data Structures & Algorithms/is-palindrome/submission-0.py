class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        lo, hi = 0, len(newStr) - 1

        while lo <= hi:
            if newStr[lo] != newStr[hi]:
                return False
            lo += 1
            hi -= 1
        
        return True