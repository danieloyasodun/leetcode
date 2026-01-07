import collections

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        string_builder = collections.deque()
        i = 0

        while i < len(s):
            if s[i] != " ":
                start = i
                # move i to the end of the word
                while i < len(s) and s[i] != " ":
                    i += 1
                string_builder.appendleft(s[start:i])
            i += 1

        return " ".join(string_builder)
