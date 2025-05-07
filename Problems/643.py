# 643. Maximum Average Subarray I

class Solution:
    
    def findMaxAverage(self, nums, k):
        
        curr = res = sum(nums[:k])
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            res = max(curr,res)
                            
        return res/k         
            
print("Answer:", Solution().findMaxAverage(nums = [-1], k = 1))