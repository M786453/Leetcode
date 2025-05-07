# 1456. Maximum number of vowels in a substring of given length
class Solution:
    
    def maxVowels(self, s, k):
        
        max_vow = 0
        
        vow_map = {
            "a": 1,
            "e": 1,
            "i": 1,
            "o":1,
            "u":1
        }
        
        for c in s[:k]:
            
            max_vow += vow_map.get(c,0)
            
        curr = max_vow
            
        for i in range(k, len(s)):
            
            curr = curr + vow_map.get(s[i],0) - vow_map.get(s[i-k],0)
          
            max_vow = max(curr, max_vow)
            
        return max_vow
       
       
print("Answer:", Solution().maxVowels(s = "leetcode", k = 3))
            
            
            
            
            
            