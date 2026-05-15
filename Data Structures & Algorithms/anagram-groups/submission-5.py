class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # // create a hasmap 
        # // store the tuple of all 
        # // key example: a b b (2, 0, 0)
        # // values: []
        
        groups = {}
        for s in strs:
            key = [0]*26
            for c in s: 
                key[ord(c.lower()) - ord("a")] += 1
            
            if tuple(key) in groups:
                groups[tuple(key)].append(s)
            else:
                groups[tuple(key)] = [s]
        
        return list(groups.values())
