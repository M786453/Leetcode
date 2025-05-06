#1679. Max number of K-sum pairs

class Solution:
        
    def maxOperations(self, nums, k):
       
        nums.sort()
        
        left = 0
        right = len(nums)-1
        
        count = 0
        
        while left < right:
                
                if nums[left] + nums[right] == k:
                    count += 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > k:
                    right -= 1
                else:
                    left += 1
                    
        return count
                
                
print("Answer:",Solution().maxOperations(nums = [1,2,3,4], k = 5))
 
            
            
            
            

