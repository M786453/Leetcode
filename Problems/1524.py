"""
1524. Number of Sub-arrays with Odd Sum
"""

def totalOddSubArrays(arr):

    # time complexity: n * (n-1) => n^2 - n =>  n^2

    total_odd_sub_arrays = 0

    for i in range(len(arr)):

        for j in range(i+1,len(arr)+1):

            if sum(arr[i:j]) % 2 != 0:
                total_odd_sub_arrays += 1
    
    return total_odd_sub_arrays

print(totalOddSubArrays([1,2,3,4,5,6,7]))