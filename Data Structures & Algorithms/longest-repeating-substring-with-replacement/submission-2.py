class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        #alphabets
        counts = [0] * 26
        #replacement = current substring - freq
        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            #window invalid
            while (r-l+1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        
        return longest

        #time O(n) space

        
        


        