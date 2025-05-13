# Problem#1496: Longest subarray of ones after deleting one element
class Solution:
    def longestSubarray(self, nums):
    
        k = 1
    
        l=r=0
    
        for r in range(len(nums)):
        
            if nums[r] == 0:
            
                k -= 1
        
            if k < 0:
            
                if nums[l] == 0:
                    k += 1
            
                l += 1
     
        return r-l
     

print("Answer:", longestSubarray(nums = [1,1,1]))