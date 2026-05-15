class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        char = ""
        l = len(strs)
        for i in range(len(min(strs))):
            char = min(strs)[i]
            for j in range(len(strs)):
                if not char == strs[j][i]:
                    return longest
            longest += char
        
        return longest

