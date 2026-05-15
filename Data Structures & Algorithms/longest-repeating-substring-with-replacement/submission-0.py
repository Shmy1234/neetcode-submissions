class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = {}
        i, j = 0, 0
        m, longest = 0, 0
        while i <= j <= len(s) - 1:
            if s[j] in tracker:
                tracker[s[j]] += 1
            else: 
                tracker[s[j]] = 1
            
            m = max(m, tracker[s[j]]) #max character

            while j+1-i- m > k:
                tracker[s[i]] -= 1
                i+=1
            longest = max(longest, j+1-i)
            j+=1

        return longest


