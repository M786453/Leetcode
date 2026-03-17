class Solution:
    
    def spellchecker(self, wordlist, queries):

        def devowel(wrd):

            return "".join("*" if c in "aeiou" else c for c in wrd)
        
        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for wrd in wordlist:

            wrdL = wrd.lower()
            words_cap.setdefault(wrdL, wrd)
            words_vow.setdefault(devowel(wrdL), wrd)

        def solve(qry):

            

            if qry in words_perfect:
                return qry
            
            qryL = qry.lower()
            if qryL in words_cap:
                return words_cap[qryL]
            
            qryLV = devowel(qryL)
            if qryLV in words_vow:
                return words_vow[qryLV]
            
            return ""
            
        return map(solve, queries)
