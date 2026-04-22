from collections import deque
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nidx = n - 1
        midx = m - 1
        right = m + n - 1

        while nidx >= 0:

            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1
            
            right -= 1

s = Solution()

print("Answer:", s.merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2], n = 3))