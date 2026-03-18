class Solution(object):
    def searchInsert(self, nums, target):
        # O(n) solution
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start, end = 0, len(nums) - 1

        while start <= end:

            mid = (start + end)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

            mid = start + (end - start)//2

        return start
            

s = Solution()

print("Answer:", s.searchInsert(nums = [1,3], target = 2))

    