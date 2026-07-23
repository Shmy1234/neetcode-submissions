class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        char = ""
        l = len(strs)
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) -1 < i:
                    if not char == strs[j][i]:
                        return longest
            longest += char
        
        return longest

