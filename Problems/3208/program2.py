"""
3208. Alternating Groups II
Author: Ahtesham Sarwar
"""

def numberOfAlternatingGroups(colors, k):

    for i in range(k-1):

        colors.append(colors[i])
    
    length = len(colors)

    result = 0

    # Bounds of sliding window
    left = 0
    right = 1

    while right < length:

        # Pattern breaks when both current and previous tiles are same
        if colors[right] == colors[right-1]:
            left = right
            right += 1
            continue

        # Extend the window
        right += 1
        
        # Skip counting sequence if it's lenght is smaller than k
        if right - left < k:
            continue

        # Record a valid sequence and shrink window from the left to search for more
        result += 1
        left += 1

    return result

print("Answer:",numberOfAlternatingGroups( colors = [0,1,0,1,0], k = 3))