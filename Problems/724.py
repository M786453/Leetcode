# Problem#724: Find Pivot Index

class Solution:
    
    def pivotIndex(self, nums):
        
        total_sum = sum(nums)
        
        pre_sum = 0
        
        for i in range(len(nums)):
            
            post_sum = total_sum - nums[i] - pre_sum
            
            if pre_sum == post_sum:
                
                return i
            
            pre_sum += nums[i]
                
        return -1
         
print("Answer:", Solution().pivotIndex(nums = [2,1,-1]))