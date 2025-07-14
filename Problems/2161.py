"""
2161. Partition array according to given pivot
Author: Ahtesham
"""

def pivotArray(nums, pivot):

    left = []
    right = []
    center = []

    for n in nums:

        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            center.append(n)
    
    return left + center + right

print(pivotArray([-3,4,3,2], 2))