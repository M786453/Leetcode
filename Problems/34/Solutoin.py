from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]

        lowerbound = 0

        upperbound = len(nums)

        while upperbound > lowerbound:

            print("Upperbound:", upperbound)

            print("Lowerbound:", lowerbound)

            mid = (lowerbound + (upperbound - lowerbound)) // 2

            if nums[mid] > target:
                upperbound = mid - 1
            elif nums[mid] < target:
                lowerbound = mid + 1
            else:
                # Target found
                first_pos = mid

                last_pos = mid

                while nums[last_pos] == target:

                    last_pos += 1

                return [first_pos, last_pos-1]
        
        return [-1, -1]

print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 11))



