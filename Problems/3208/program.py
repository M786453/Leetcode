"""
3208. Alternating Groups II
Author: Ahtesham Sarwar
"""

def numberOfAlternatingGroups(colors, k):

    length = len(colors)

    colors += colors

    alternating_groups_counter = 0

    for start in range(length):
        end = start + k
        if (colors[start] == colors[start-1] and colors[start] == colors[start+1]) \
            or (colors[end] == colors[end-1] and colors[end] == colors[end+1]):
            alternating_groups_counter += 1

    return alternating_groups_counter

print("Answer:",numberOfAlternatingGroups(colors = [0,1,0,1,0], k = 3))