class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            #s[i] = is the character
            # this for loop counts how many the character appears ex: racecar r
            #appears 2 times so r --> 2
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        #making sure the counting in the hashmaps are the same
        