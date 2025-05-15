# Problem#2215: Find the difference of two arrays

class Solution:
    
    def findDifference(self, nums1, nums2):
       
        s1 = set(nums1)
        s2 = set(nums2)
        
        return [list(s1-s2), list(s2-s1)]
        
print("Answer:", Solution().findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))