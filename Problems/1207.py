# Problem#1207: Unique number of occurrences

class Solution:
    
    def uniqueOccurrences(self, arr):
        
        occur_map = {}
        
        for n in arr:
            
            if n in occur_map:
                occur_map[n] += 1
            else:
                occur_map[n] = 1
        
        occur_list = occur_map.values()
        
        return len(occur_list) == len(set(occur_list))
        
        
        
print("Answer:", Solution().uniqueOccurrences(arr = [1,2]))