class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sTable = {}
        tTable = {}
        for i in s:
            if i in sTable:
                sTable[i] += 1
            else:
                sTable[i] = 1
        for i in t:
            if i in tTable:
                tTable[i] += 1
            else:
                tTable[i] = 1
        return sTable == tTable
