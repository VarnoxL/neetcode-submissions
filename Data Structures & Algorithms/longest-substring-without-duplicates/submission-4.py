class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, n = 0, len(s)
        longest = 0
        seen = set()
        
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            w = (r - l) + 1
            longest = max(longest, w)
            seen.add(s[r])
        
        return longest
        #O(n) time
        #O(1) space


        

        