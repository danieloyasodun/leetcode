class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) %2 != 0: return False

        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in '({[':
                stack.append(c)
            elif not stack or stack.pop() != mapping[c]:
                return False
        return not stack
