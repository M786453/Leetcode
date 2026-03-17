class Solution(object):
    def searchInsert(self, nums, target):
        # O(n) solution
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(len(nums)):

            if nums[i] == target:
                return i
            elif i == len(nums)-1 and target > nums[i]:
                return i+1
            elif target > nums[i] and  target < nums[i+1]:
                return i+1

s = Solution()

print("Answer:", s.searchInsert(nums = [1,3,5,6], target = 7))

    