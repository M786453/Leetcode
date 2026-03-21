class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        fast = slow = 0

        while fast < len(nums)-1:

            if nums[fast] != nums[fast+1]:
                slow += 1
                nums[slow] = nums[fast+1]

            fast += 1
        
        return slow+1
    
s = Solution()

print("Answer:", s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))

