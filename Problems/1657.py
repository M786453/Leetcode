from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if set(word1) != set(word2):
            return False

        first_word_counter = Counter(word1)
        second_word_counter = Counter(word2)

        return sorted(first_word_counter.values()) == sorted(
            second_word_counter.values()
        )
