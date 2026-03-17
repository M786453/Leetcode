class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """

        counter = 0

        for wrd in text.split():

            is_valid = True

            for c in wrd:
                
                if c in brokenLetters:
                    is_valid = False
                    break

            if is_valid:
                counter += 1

        return counter
