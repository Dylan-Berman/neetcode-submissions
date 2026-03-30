class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadict = {}
        for word in strs:
            alphabet = [0] * 26
            for letter in word:
                index = ord(letter) - ord ('a')
                alphabet[index] += 1
            alphabet = tuple(alphabet)
            anadict[alphabet] = anadict.get(alphabet, []) + [word] 
        return list(anadict.values())