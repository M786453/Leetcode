# Problem#1732: Find the highest altitude

class Solution:
    
    def largestAltitude(self, gain):
        
        max_alt = 0
        sum_alt = 0
        
        for net_alt in gain:
            
            sum_alt += net_alt
            
            if sum_alt > max_alt:
                max_alt = sum_alt
                
        return max_alt
        
print("Answer:",Solution().largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))
                