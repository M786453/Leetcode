class Solution(object):
    def searchInsert(self, nums, target):
        # O(n) solution
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0

        end = len(nums)

        mid = end // 2

        while start < end:

            print("Start:", start)
            print("End:", end)
            print("Mid:", mid)

            if nums[mid] == target:
                return mid
            elif target > nums[mid] and mid+1 < len(nums) and target < nums[mid+1]:
                return mid + 1
            
            if target > nums[mid]:
                start = mid
            else:
                end = mid

            mid = start + (end - start)//2

            # break
            

s = Solution()

print("Answer:", s.searchInsert(nums = [1,3,5,6], target = 7))

    