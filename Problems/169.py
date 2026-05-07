class Solution(object):

    def majorityElement(self, nums):

        counter = {}

        for n in nums:

            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 0
        
        majority_element = -1
        max_count = -1

        for k in counter:

            if counter[k] > max_count:
                majority_element = k
                max_count = counter[k]
        
        return majority_element

s = Solution()
# print("Answer:", s.majorityElement(nums = [3,2,3]))
# print("Answer:", s.majorityElement(nums = [2,2,1,1,1,2,2]))
print("Answer:", s.majorityElement([3,3,4]))