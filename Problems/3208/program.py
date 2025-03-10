"""
3208. Alternating Groups II
Author: Ahtesham Sarwar
"""

def numberOfAlternatingGroups(colors, k):

    length = len(colors)

    ag_counter = 0

    # Total Time Complexity: n*k
    for start in range(length): # Time complexity: n

        
        if start+k > length:
            end = (start+k) - length
            ag = colors[start:] + colors[:end]
        else:
            end = start+k
            ag = colors[start:end]
        
        is_ag = True
        for i in range(k-1): # Time complexity: k
            if ag[i] == ag[i+1]:
                is_ag = False
                break
        
        if is_ag:
            ag_counter += 1

    return ag_counter

print("Answer:",numberOfAlternatingGroups( colors = [1,1,0,1], k = 4))