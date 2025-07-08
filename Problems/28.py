class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        needle_length = len(needle)

        for i in range(len(haystack)):

            if haystack[i] == needle[0] and haystack[i:i+needle_length] == needle:

                return i

        return -1