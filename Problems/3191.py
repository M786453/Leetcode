"""
3191. Minimum Operations to Make Binary Array Elements to One 1
"""

def minOperations(nums):

    operations = 0

    i = 0

    while i < (len(nums) - 2):

        if nums[i] == 1:
            i += 1
            continue 

        nums[i] = int(bool(nums[i] == 0))

        nums[i+1] = int(bool(nums[i+1] == 0))

        nums[i+2] = int(bool(nums[i+2] == 0))

        operations += 1

        i += 1

    if nums[len(nums)-2] == 0 or nums[len(nums)-1] == 0:
        return -1
    else:
        return operations
    
print("Answer:", minOperations(nums = [0,1,1,1,0,0]))

print("Answer:", minOperations(nums = [0,1,1,1]))