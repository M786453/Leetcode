def sol(nums):
    
    length = len(nums)
    start = length-1
    
    for end in range(length-1, -1, -1):
        if nums[end] == 0:
            nums[end:start] = nums[end+1:start+1]
            nums[start] = 0
            start -= 1
            
    return nums