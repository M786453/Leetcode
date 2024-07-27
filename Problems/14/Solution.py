# Problem#14: Longest Common Prefix
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        target = strs[0]

        target_length = len(target)

        common_prefix = ""

        if target_length == 0:
            return common_prefix
        
        for i in range(target_length):

            if all(i < len(s) and s[i] == target[i] for s in strs):
                common_prefix += target[i]
            else:
                break

        return common_prefix


