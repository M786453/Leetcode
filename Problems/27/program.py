class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0

        while i < len(nums):

            if nums[i] == val:
                del nums[i]
                continue

            i += 1
        
        return len(nums)

print(Solution().removeElement(nums = [3,2,2,3], val = 3))
# [0,1,2,3]
# [3,2,2,3] => size => 4
# val = 2
# index=1 -> list val -> 2
# [3,2,3] => size => 3
# [3,3] => 2
