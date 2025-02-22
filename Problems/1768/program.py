
def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    if len(word1) < len(word2):
        return "".join([word1[i]+word2[i] for i in range(len(word1))]) + word2[len(word1):]
    else:
        return "".join([word1[i]+word2[i] for i in range(len(word2))]) + word1[len(word2):]
    
print(mergeAlternately("abcd", "pq"))
