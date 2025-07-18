
def maxFrequencyElements(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_freq = -1
    counter = 0
    unique_nums = set(nums)

    for n in unique_nums:
        frequency = nums.count(n)
        if max_freq < frequency:
            max_freq = frequency
            counter = 1
        elif max_freq == frequency:
            counter +=1 
    
    return max_freq*counter 
    
# print(maxFrequencyElements([1,2,3,4,5]))