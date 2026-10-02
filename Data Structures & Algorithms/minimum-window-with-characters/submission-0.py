class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        #must use counter and dict, match character to num
        t_count = Counter(t)
        s_count = defaultdict(int)
        formed = 0
        #since dict, automatically distinct 
        required = len(t_count)
        min_len = float('inf')
        result_start = 0

        for r in range(len(s)):
            char = s[r]
            s_count[char] += 1
            if s_count[char] == t_count[char]:
                formed += 1
            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    result_start = l
                if s_count[s[l]] == t_count[s[l]]:
                    formed -= 1
                s_count[s[l]] -= 1
                l += 1
        if min_len == float('inf'):
            return ""
        return s[result_start: result_start + min_len]
        



                
                
            

            


        