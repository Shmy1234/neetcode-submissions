class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            lst = [0]*26
            for char in s:
                lst[ord(char)-ord('a')] += 1
            d[tuple(lst)] = [s] + d.get(tuple(lst), [])
        return list(d.values())
        