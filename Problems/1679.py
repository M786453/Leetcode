#1679. Max number of K-sum pairs

class Solution:
    
    def maxOperations(self, nums, k):
        
        left = 0
        right = len(nums)-1
        ops = 0
        
        while left < right:
            print(nums)
            print(left,right)
            if nums[left]+nums[right] == k:
                del nums[left]
                right -= 1
                del nums[right]
                right -= 1
                ops += 1
            else:
                if nums[left+1] < nums[right-1]:
                    left += 1
                else:
                    right -= 1
             
        print(nums)
        return ops
        
    def sol2(self, nums, k):
       
        nums_dict = {}
       
        i = 0
       
        ops = 0
       
        while i < len(nums):
                
                print("i", i)
                
                print(nums)
                
                rem = abs(k-nums[i])
                
                print("rem", rem)
                
                print(nums_dict)
                
                if rem in nums_dict:
                    
                    del nums[i]
                    del nums[nums_dict[rem][0] if nums_dict[rem][0] < i else nums_dict[rem][0]-1]
                    
                    del nums_dict[rem][0]
                    
                    if len(nums_dict[rem]) == 0:
                        del nums_dict[rem]
                        
                    ops += 1
                    
                    i -= 1
                    
                    continue
                    
                else:
                    
                    if nums[i] in nums_dict:
                        nums_dict[nums[i]].append(i)
                    else:
                        nums_dict[nums[i]] = [i]
                i += 1
        
        print(nums)
        
        print(nums_dict)  
                
        return ops
                
                
print("Answer:",Solution().sol2(nums = [3,3,3,1,3,4,3], k = 6))
 
            
            
            
            

