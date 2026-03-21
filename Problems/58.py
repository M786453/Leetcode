class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        current_word_length = 0
        i = len(s)-1

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            current_word_length += 1
            i -= 1
        
        return current_word_length
    
s = Solution()

print("Answer:", s.lengthOfLastWord(s = "Hello World"))
# print("Answer:", s.lengthOfLastWord("   fly me   to   the moon  "))
# print("Answer:", s.lengthOfLastWord("a"))