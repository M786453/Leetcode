"""
3191. Minimum Operations to Make Binary Array Elements to One 1
"""

def minOperations(nums):

    operations = 0

    i = 0

    are_all_one = True

    while i < (len(nums) - 2):

        if nums[i] == 1:
            i += 1
            if nums[i] == 1:
                i +=1
                if nums[i] == 1:
                    i += 1
            continue # Skip next executions

        nums[i] = int(bool(nums[i] == 0))

        nums[i+1] = int(bool(nums[i+1] == 0))

        nums[i+2] = int(bool(nums[i+2] == 0))

        if nums[i] == 0:
            are_all_one = False

        operations += 1

    if are_all_one:
        if nums[len(nums)-2] == 0 or nums[len(nums)-1] == 0:
            are_all_one = False

    if are_all_one:
        return operations
    else:
        return -1