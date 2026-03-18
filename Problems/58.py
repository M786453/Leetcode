class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        current_word_length = 0

        for c in s[::-1]:

            if c == " ":
                if current_word_length > 0:
                    return current_word_length

                continue

            current_word_length += 1

        return current_word_length
    
s = Solution()

# print("Answer:", s.lengthOfLastWord(s = "Hello World"))
# print("Answer:", s.lengthOfLastWord("   fly me   to   the moon  "))
print("Answer:", s.lengthOfLastWord("a"))