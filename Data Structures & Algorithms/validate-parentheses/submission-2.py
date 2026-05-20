class Solution:
    def isValid(self, s: str) -> bool:
        corr = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in corr:
                stack.append(c)
            else:
                if not stack or corr[stack.pop()] != c:
                    return False
        return not stack
        