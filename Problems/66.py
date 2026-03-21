class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        i = len(digits) - 1

        while i >= 0:

            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:

                digits[i] = 0

                if i == 0 and digits[i] == 0:
                    digits = [1] + digits

            i -= 1

        return digits

s = Solution()

print("Answer:", s.plusOne([9]))