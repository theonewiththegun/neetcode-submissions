class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = ''.join(x.lower() for x in s if x.isalnum())
        l, r = 0, len(_s) - 1
        while l < r:
            if _s[l] != _s[r]:
                return False
            l += 1
            r -= 1

        return True     
        