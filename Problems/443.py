class Solution:
    
    def compress(self, chars: List[str]) -> int:
    
        cmprsd_index = 0
        length = len(chars)
        i = 0
    
        while i < length:
       
           # Calculate group length of same consecutive elements
           grp_len = 0
       
           while i+grp_len+1 < length and chars[i] == chars[i+grp_len+1]:
            
                grp_len += 1
       
           grp_len += 1
       
           # Update input array with compressed elements
           cmprsd_grp_str = f'{chars[i]}{grp_len}' if grp_len > 1 else chars[i]
       
           chars[cmprsd_index:cmprsd_index+len(cmprsd_grp_str)] = cmprsd_grp_str
       
           cmprsd_index += len(cmprsd_grp_str)
      
           i += grp_len
      
        return cmprsd_index