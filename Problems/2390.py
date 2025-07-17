class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_stack = []

        for chr in s:

            if chr == "*":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(chr)

        return "".join(s_stack)
