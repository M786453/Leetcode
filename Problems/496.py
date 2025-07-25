class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        greater_element_map = {}

        for i in range(len(nums2)-1):

            if nums2[i+1] > nums2[i]:
                greater_element_map[nums2[i]] = nums2[i+1]
            else:
                greater_element_map[nums2[i]] = -1
            
        greater_element_map[nums2[-1]] = -1 # Always -1 for last element

        return [greater_element_map[n] for n in nums1]

ss = Solution()

print("Answer:",ss.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))